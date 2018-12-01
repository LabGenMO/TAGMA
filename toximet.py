import sys
import os
import subprocess
import shutil
import argparse as ap
from os import listdir
from os.path import isfile, join
from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastnCommandline

def read_params(args):
	p = ap.ArgumentParser(description = 'This program makes quantitative analysis of metagenome and analyses presence of lacto and bifidobacteries. BowTie2 is used for alignment. BowTie2 is required in the system path with read and execution permissions.\n'
		'Output:\n', formatter_class = ap.RawTextHelpFormatter)
	arg = p.add_argument
	arg('-marf', metavar = 'MARKERS', type = str, nargs = '?', default = None, help = 'Input file in fasta format (genetic markers).\nDescription line must contain the folowing information:\n > [strain name] ~ [marker name]')
	arg('-metaf', metavar = 'METAGENOME', type = str, nargs = '?', default = None, help = 'Input file in fastq format (metagenome)\n')
	arg('--nproc', metavar = 'N', type = int, default = 1, help = 'The number of CPUs to use for parallelizing the alignment\n[default is 1 i.e. no parallelizing]\n')
	bt2ps = ['sensitive','very-sensitive', 'sensitive-local', 'very-sensitive-local']
	arg('--bt2_ps', metavar = 'BowTie2 presets', default = 'very-sensitive-local', choices = bt2ps, help = 'Presets options for BowTie2\n - sensitive\n - very-sensitive\n - sensitive-local\n - very-sensitive-local\n[default very-sensitive-local]\n')
	arg('--evalue', metavar = 'E-value', type = float, default = 10**(-30), help = 'E-value for all-vs-all markers blast (for identification of snp, insertion and deletion positions)')
	arg('-max_err', metavar = 'Maximum errors', type = int, default = 4, help = 'Maximum errors per read alignment (equal to sum of snps, insertions and deletions)')
	arg('-val_pos_mismatch', metavar = 'Val. pos. mismatch',  type = int, default = 0, help = 'Maximum errors in valuable positions in markers (valuable positions are difined by all vs. all blast)')
	arg('-gene_cov', metavar = 'GENE_COVERAGE', type = float, default = 20, help = 'Gene coverage threshold. All genes, that are covered by reads on more than this value are reported in test results.')
	arg('-out_fol', metavar = 'OUTPUT_FOLDER', type = str, default = 'output', help = 'Folder for all output files.')

	return vars(p.parse_args())

def make_tree_file(mar_f, path):
	tree = {}
	print mar_f
	inp_f =  open(mar_f,'r')
	try:
		for line in inp_f.readlines():
			if '>' in line:
				name = line.strip().replace('>','').split('~')[0]
				gene = '_'.join(line.strip().replace('>','').split('~')[1::])
				if name not in tree.keys():
					tree[name] = []
				tree[name].append(gene)	
	finally:
		inp_f.close()
	tree_f = open(path + '/tree','w')
	try:
		for strain in tree:
			tree_f.write(strain + ': ' + ','.join(tree[strain]) + '\n')
	finally:
		tree_f.close()

def make_seq_file(seq, path):
	inp_f = open(seq,'r')
	outp_f = open(path + '/markers.fasta','w')
	try:
		for line in inp_f.readlines():
			if '>' in line:
				outp_f.write('>' + '_'.join(line.strip().replace('>','').split('~')[1::]) + '\n')
			else:
				outp_f.write(line)
	finally:
		inp_f.close()
		outp_f.close()

def read_fasta(fasta_f):
	seq_d = {}
	with open(fasta_f, 'r') as seq_f:
		for line in seq_f.readlines():
			if '>' in line:
				s_name = line.strip().replace('>','')
				seq_d[s_name] = ''
			else:
				seq_d[s_name] = seq_d[s_name] + line.strip()
	return seq_d

def read_cigar(c):
	cig = []
	n = ''
	while len(c) != 0:
		if not (c[0] >= '0' and c[0] <= '9'):
			ch = c[0]
			cig = cig + [[ch, int(n)]]
			c = c[1::]
			n = ''
		else:
			n = n + c[0]
			c = c[1::]
	return cig

def bt2_gene_coverage(bt2_data, markers_f):
	genes_d = read_fasta(markers_f)
	cov = {}
	names = []
	for l in bt2_data:
		name = l[2]
		if name not in names:
			names.append(name)
			cov[name] = {}
			cov[name]['pos'] = ()
			cov[name]['cov'] = 0
			for n in range(len(genes_d[name])):
				cov[name]['pos'] = cov[name]['pos'] + ({'A':0, 'C':0, 'G':0, 'T':0, 'a':0, 'c':0, 'g':0, 't':0, 'U':0, 'R':0, 'Y':0, 'K':0, 'M':0, 'S':0, 'W':0, 'B':0, 'X':0, 'D':0, 'H':0, 'V':0, 'N':0},)
	for l in bt2_data:
		cigar = read_cigar(l[5])
		i = 0
		name = l[2]
		marker_pos = int(l[3])
		read_pos = 0
		for el in cigar:
			if el[0] in ['M','X']:
				for j in range(el[1]):
					cov[name]['pos'][marker_pos + j - 1][l[9][read_pos + j]] += 1
			if el[0] in ['M','I','S','X','=']:
				read_pos += el[1]
			if el[0] in ['M','X','D','N','H','P','=']:
				marker_pos += el[1]
	for al in cov.keys():
		for p in range(len(cov[al]['pos'])):
			check = False
			for ch in ['A','C','G','T','a','c','g','t','U','R','Y','K','M','S','W','B','X','D','H','V','N']:
				if cov[al]['pos'][p][ch] != 0:
					check = True
			if check:
				cov[al]['cov'] += 1
	return cov

def write_g_cov(g_cov, genes_f, outp):
	genes_d = read_fasta(genes_f)
	with open(outp, 'w') as out:
		good_al = []
		for al in g_cov:
			check = False
			for n in g_cov[al]['pos']:
				for ch in ['A','C','G','T','a','c','g','t','U','R','Y','K','M','S','W','B','X','D','H','V','N']:
					if n[ch] != 0:
						check = True
						break
				if check:
					break
			if check:
				good_al.append(al)
		for al in good_al:
			out.write(al + '  ' + str(g_cov[al]['cov']) + '\n')
			for n in range(len(g_cov[al]['pos'])):
				out.write('\t' + str(n+1) + ': ' + '(' + genes_d[al][n] + ') ' + ''.join([ch + ' - ' + str(g_cov[al]['pos'][n][ch]) for ch in ['A','C','G','T','a','c','g','t','U','R','Y','K','M','S','W','B','X','D','H','V','N'] if g_cov[al]['pos'][n][ch] != 0]) + '\n')

def read_tree(tree_path):
	tree_file = open(tree_path,'r')
	tree = {}
	try:
		for line in tree_file.readlines():
			line = line.strip()
			strain = line.split(': ')[0].split('~')[0]
			if strain not in tree:
				tree[strain] = {}
			for gene in line.split(': ')[1].split(','):
				tree[strain][gene] = {}
				tree[strain][gene]['dic'] = []
				tree[strain][gene]['cov'] = 0
	finally:
		tree_file.close()
	return tree

def suppl_tree(tree, bt2_data, g_cov, cov_threshold):
	for strain in tree:
		for gene in tree[strain]:
			for l in bt2_data:
				if gene == l[2] and g_cov[gene]['cov'] > cov_threshold:
					length = 0
					for el in read_cigar(l[5]):
						if el[0] in ['M','X']:
							length += el[1]
					det_pos = []
					for pos in val_pos[gene]:
						if pos <= (int(l[3]) + length) and pos >= int(l[3]):
							det_pos.append(pos)
					dic = {'read_name': l[0],
						'pos': [l[3] + '..' + str(int(l[3]) + length)],
						'CIGAR': [l[5]],
						'det_pos': det_pos}
					tree[strain][gene]['dic'].append(dic)
					tree[strain][gene]['cov'] = g_cov[gene]['cov']
	return tree

def write_test_result(tree, outp):
	al_strs = []
	for s in tree:
		check = False
		for loc in tree[s]:
			if tree[s][loc]['dic'] != []:
				check = True
		if check:
			al_strs.append(s)
	with open(outp,'w') as out:
		for s in al_strs:
			out.write(s + '\n')
			for loc in tree[s]:
				out.write('\t\t' + loc + '  ' + str(tree[s][loc]['cov']) + '\n')
				for dic in tree[s][loc]['dic']:
					out.write('\t\t\tread name: ' + dic['read_name'] + '\n')
					out.write('\t\t\tposition in marker: ' + ' '.join(dic['pos']) + '\n')
					out.write('\t\t\tCIGAR: ' + ' '.join(dic['CIGAR']) + '\n')
					out.write('\t\t\tdetected positions (valuable SNPs, deletions and insertions): ' + ' '.join([ str(n) for n in dic['det_pos']]) + '\n\n')
			out.write('\n')

def write_test_result_short(tree, outp):
	al_strs = []
	for s in tree:
		check = False
		for loc in tree[s]:
			if tree[s][loc]['dic'] != []:
				check = True
		if check:
			al_strs.append(s)
	with open(outp,'w') as out:
		for s in al_strs:
			out.write(s + '\n')
			for loc in tree[s]:
				poss = []
				for dic in tree[s][loc]['dic']:
					for n in dic['det_pos']:
						if str(n) not in poss:
							poss.append(str(n))
				out.write('\t\t' + loc + '  ' + str(tree[s][loc]['cov']) + '\n\t\t\tnumber of reads: ' + str(len(tree[s][loc]['dic'])) + '\n\t\t\tdetected val. pos.: ' + ' '.join(poss) + '\n')
			out.write('\n')

def diff_in_genes(bln_xml, genes_f):
	genes_d = read_fasta(genes_f)
	blastn = {}
	result_handle = open(bln_xml,'r')
	blast_records = NCBIXML.parse(result_handle)
	for blast_record in blast_records:
		blastn[blast_record.query] = {}
		for alignment in blast_record.alignments:
			hsp_n = 1
			if ' No definition line' in alignment.title:
				al_title = alignment.title[0:alignment.title.find(' No definition line')]
			else:
				al_title = alignment.title
			blastn[blast_record.query][al_title] = {}
			for hsp in alignment.hsps:
				blastn[blast_record.query][al_title][str(hsp_n)] = {}
				complement = False
				if hsp.frame != ():
					if hsp.frame[0] < 0:
						complement = True
				seq = genes_d[blast_record.query][hsp.query_start-1:hsp.query_end]
				if complement:
					seq = compl(seq)
				blastn[blast_record.query][al_title][str(hsp_n)]['seq'] = seq
				blastn[blast_record.query][al_title][str(hsp_n)]['query_start'] = hsp.query_start
				blastn[blast_record.query][al_title][str(hsp_n)]['query_end'] = hsp.query_end
				blastn[blast_record.query][al_title][str(hsp_n)]['expect'] = hsp.expect
				blastn[blast_record.query][al_title][str(hsp_n)]['score'] = hsp.score
				blastn[blast_record.query][al_title][str(hsp_n)]['bits'] = hsp.bits
				blastn[blast_record.query][al_title][str(hsp_n)]['num_alignments'] = hsp.num_alignments
				blastn[blast_record.query][al_title][str(hsp_n)]['identities'] = hsp.identities
				blastn[blast_record.query][al_title][str(hsp_n)]['positives'] = hsp.positives
				blastn[blast_record.query][al_title][str(hsp_n)]['gaps'] = hsp.gaps
				blastn[blast_record.query][al_title][str(hsp_n)]['strand'] = hsp.strand
				blastn[blast_record.query][al_title][str(hsp_n)]['frame'] = hsp.frame
				blastn[blast_record.query][al_title][str(hsp_n)]['query'] = hsp.query
				blastn[blast_record.query][al_title][str(hsp_n)]['match'] = hsp.match
				blastn[blast_record.query][al_title][str(hsp_n)]['sbjct'] = hsp.sbjct
				blastn[blast_record.query][al_title][str(hsp_n)]['sbjct_start'] = hsp.sbjct_start
				blastn[blast_record.query][al_title][str(hsp_n)]['sbjct_end'] = hsp.sbjct_end
				hsp_n = hsp_n + 1
	diff_pos = {}
	for q in blastn.keys():
		diff_pos[q] = {}
		for al in blastn[q]:
			if al != q:
				diff_pos[q][al] = {}
				diff_pos[q][al]['snp'] = {}
				diff_pos[q][al]['ins'] = {}
				diff_pos[q][al]['del'] = {}
				for hsp in blastn[q][al]:
					n = 0 #number in match string
					delet_num = 0
					for ch in blastn[q][al][hsp]['match']:
						if ch == ' ':
							if blastn[q][al][hsp]['query'][n:n+1] != '-' and blastn[q][al][hsp]['sbjct'][n:n+1] != '-':
								diff_pos[q][al]['snp'][blastn[q][al][hsp]['query_start'] + n - delet_num] = blastn[q][al][hsp]['query'][n:n+1] + '->' + blastn[q][al][hsp]['sbjct'][n:n+1]
							if blastn[q][al][hsp]['query'][n:n+1] != '-' and blastn[q][al][hsp]['sbjct'][n:n+1] == '-':
								diff_pos[q][al]['ins'][blastn[q][al][hsp]['query_start'] + n - delet_num] = blastn[q][al][hsp]['query'][n:n+1]
							if blastn[q][al][hsp]['query'][n:n+1] == '-' and blastn[q][al][hsp]['sbjct'][n:n+1] != '-':
								if blastn[q][al][hsp]['query_start'] + n - delet_num - 1 not in diff_pos[q][al]['del']:
									diff_pos[q][al]['del'][blastn[q][al][hsp]['query_start'] + n - delet_num - 1] = ''
								diff_pos[q][al]['del'][blastn[q][al][hsp]['query_start'] + n - delet_num - 1] = diff_pos[q][al]['del'][blastn[q][al][hsp]['query_start'] + n - delet_num - 1] + blastn[q][al][hsp]['sbjct'][n:n+1]
								delet_num += 1
						n += 1
	return diff_pos


def write_diff_pos(diff_pos, outp):
	with open(outp, 'w') as out:
		for q in diff_pos:
			out.write(q + '\n')
			for al in diff_pos[q]:
				out.write('\t' + al + '\n')
				if diff_pos[q][al]['snp'] != {}:
					out.write('\n\t\tsnps:\n\t\t' + '\n\t\t'.join([str(k) + ' ' + diff_pos[q][al]['snp'][k] for k in sorted(diff_pos[q][al]['snp'])]) + '\n\n')
				if diff_pos[q][al]['ins'] != {}:
					out.write('\n\t\tinsertions:\n\t\t' + '\n\t\t'.join([str(k) + ' ' + diff_pos[q][al]['ins'][k] for k in sorted(diff_pos[q][al]['ins'])]) + '\n\n')
				if diff_pos[q][al]['del'] != {}:
					out.write('\n\t\tdeletions:\n\t\t' + '\n\t\t'.join([str(k) + ' ' + diff_pos[q][al]['del'][k] for k in sorted(diff_pos[q][al]['del'])]) + '\n\n')



def genes_snp_ins_positions(diff_pos):
	val_pos = {}
	for q in diff_pos:
		val_pos[q] = []
		for al in diff_pos[q]:
			for n in diff_pos[q][al]['snp'].keys() + diff_pos[q][al]['ins'].keys():
				if n not in val_pos[q]:
					val_pos[q].append(n)
		val_pos[q] = sorted(val_pos[q])
	return val_pos

def filter_maxerr(bt2_data, max_err, markers_f):
	genes_d = read_fasta(markers_f)
	bt2_filt_maxerr = []
	for l in bt2_data:
		name = l[2]
		marker_pos = int(l[3])
		cigar = read_cigar(l[5])
		read = l[9]
		read_pos = 0
		err = 0
		for el in cigar:
			if el[0] == 'I' or el[0] == 'D':
				err = err + el[1]
			if el[0] == 'M':
				for j in range(el[1]):
					if genes_d[name][marker_pos + j - 1] != read[read_pos + j]:
						err += 1
			if el[0] in ['M','I','S','X','=']:
				read_pos += el[1]
			if el[0] in ['M','X','D','N','H','P','=']:
				marker_pos += el[1]
		if err <= max_err:
			bt2_filt_maxerr.append(l)
	return bt2_filt_maxerr

def filter_valpos(bt2_data, val_pos, val_pos_mismatch, markers_f):
	genes_d = read_fasta(markers_f)
	bt2_filt_valpos = []
	for l in bt2_data:
		cigar = read_cigar(l[5])
		name = l[2]
		marker_pos = int(l[3])
		read = l[9]
		detected_val_pos = []
		mismatch_val_pos = []
		read_pos = 0
		for el in cigar:
			if el[0] == 'M':
				for j in range(el[1]):
					if marker_pos + j in val_pos[name]:
						if genes_d[name][marker_pos + j - 1] == read[read_pos + j]:
							detected_val_pos.append(marker_pos + j)
						else:
							mismatch_val_pos.append(marker_pos + j)
			if el[0] in ['M','I','S','X','=']:
				read_pos += el[1]
			if el[0] in ['M','X','D','N','H','P','=']:
				marker_pos += el[1]
		if len(mismatch_val_pos) <= val_pos_mismatch:
			bt2_filt_valpos.append(l)
	return bt2_filt_valpos


def write_summary(sum_path):
	with open(sum_path, 'w') as out:
		al_strs = []
		for s in tree:
			check = False
			for loc in tree[s]:
				if tree[s][loc]['dic'] != []:
					check = True
			if check:
				al_strs.append(s)
		out.write('good detected strains\n\n' + '\n'.join([s + ' (' + str(len([g for g in tree[s] if tree[s][g]['cov'] != 0])) + '/' + str(len(tree[s].keys())) + ')' for s in al_strs if s not in chimeras['chim_by_genes'] + chimeras['chim_by_snps'] + prob_strains]) + '\n\nprobable strains\n\n' + '\n'.join(s + ' (' + str(len([g for g in tree[s] if tree[s][g]['cov'] != 0])) + '/' + str(len(tree[s].keys())) + ')' for s in prob_strains) + '\n\nchimeras by genes\n\n' +  '\n'.join([s  + ' (' + str(len([g for g in tree[s] if tree[s][g]['cov'] != 0])) + '/' + str(len(tree[s].keys())) + ')' for s in chimeras['chim_by_genes']]) + '\n\nchimeras by snps\n\n' +  '\n'.join([s + ' (' + str(len([g for g in tree[s] if tree[s][g]['cov'] != 0])) + '/' + str(len(tree[s].keys())) + ')' for s in chimeras['chim_by_snps']]))

def make_gene_matrix(diff_pos, tree, outp):
	genes_pos = {}
	for st in tree:
		for g in tree[st]:
			if tree[st][g]['cov'] != 0:
				poss = []
				for dic in tree[st][g]['dic']:
					for n in dic['det_pos']:
						if n not in poss:
							poss.append(n)
				genes_pos[g] = poss
	g_mat = {g1:{g2:0 for g2 in genes_pos.keys()} for g1 in genes_pos.keys()}
	for g1 in genes_pos.keys():
		for g2 in genes_pos.keys():
			if g2 in diff_pos[g1].keys():
				t_pos = diff_pos[g1][g2]['snp'].keys() + diff_pos[g1][g2]['ins'].keys() + diff_pos[g1][g2]['del'].keys()
				check = False
				for p in t_pos:
					if p in genes_pos[g1]:
						check = True
				if not check:
					g_mat[g1][g2] = 1
			if g1 == g2:
				g_mat[g1][g2] = 1

	print '\n'.join(g_mat.keys())
	print '\n'.join(' '.join(str(n) for n in g_mat[l].values()) for l in g_mat.keys())
	with open(outp, 'w') as out:
		out.write('\n'.join(g_mat.keys()) + '\n\n')
		out.write('\n'.join(' '.join(str(n) for n in g_mat[l].values()) for l in g_mat.keys()))
	return g_mat

def make_strain_matrix(tree, g_mat, outp):
	st_detgene = {} #dictionary that contains strains and detected genes (only strains that have detected genes)
	for st in tree:
		check = False
		genes = []
		for g in tree[st]:
			if tree[st][g]['cov'] != 0:
				check = True
				genes.append(g)
		if check:
			st_detgene[st] = genes
	st_mat = {st1 : {st2 : 0 for st2 in st_detgene.keys()} for st1 in st_detgene.keys()}
	for st1 in st_detgene.keys():
		for st2 in st_detgene.keys():
			check_st = True #true if st1 can't be distinguished from st2
			for g1 in st_detgene[st1]:
				check_gene = False
				for g2 in st_detgene[st2]:
					if g_mat[g1][g2] == 1:
						check_gene = True
				if not check_gene:
					check_st = False
			if check_st and len(st_detgene[st2]) >= len(st_detgene[st1]):
				st_mat[st1][st2] = 1

	print '\n'.join(st_mat.keys())
	print '\n'.join(' '.join(str(n) for n in st_mat[l].values()) for l in st_mat.keys())
	with open(outp, 'w') as out:
		out.write('\n'.join(st_mat.keys()) + '\n\n')
		out.write('\n'.join(' '.join(str(n) for n in st_mat[l].values()) for l in st_mat.keys()))
	return st_mat

def sort_by_representation(st_mat):
	sts = st_mat.keys()
	groups = []
	while len(sts) != 0:
		gr = [sts[0]]
		sts.remove(sts[0])
		check = True
		while check:
			check = False
			gr1 = gr
			for st1 in gr:
				for st2 in [st for st in st_mat if st_mat[st1][st] == 1]:
					if st2 not in gr1:
						gr1.append(st2)
						sts.remove(st2)
						check = True
				for st2 in [st for st in st_mat if st_mat[st][st1] == 1]:
					if st2 not in gr1:
						gr1.append(st2)
						sts.remove(st2)
						check = True
			gr = gr1
		groups.append(gr)
	st_repr = [] #this list contains dictionaries, each dictionary contains strain:privilegy (0 - the best, higher - worse), privelegy = number of strains, from which this strain can't be destingiushed
	for g in groups:
		st_repr.append( {st:len([s for s in st_mat if st_mat[st][s] == 1]) - 1 for st in g} )
	return st_repr


def write_summary(st_repr, tree, genes_f, out_f):
	seqs = read_fasta(genes_f)
	with open(out_f, 'w') as out:
		out.write('[strain] [n1]/[n0] [cov_1, cov_2, ...] [p]\nn1 - number of detected genetic markers\nn0 - number of all genetic markers\ncov_i - coverage of genetic marker number i\np - privelegy, number of strain from which this strain can not be distinguished\n\n')
		for dic in st_repr:
			for st in dic.keys():
				n1 = str(len([g for g in tree[st].keys() if tree[st][g]['cov'] != 0]))
				n0 = str(len(tree[st].keys()))
				covs = ', '.join([str(tree[st][g]['cov']) + '/' + str(len(seqs[g])) for g in tree[st].keys() if tree[st][g]['cov'] != 0])
				out.write(st + ' ' + n1 + '/' + n0 + ' [' + covs + '] ' + str(dic[st]) + '\n')
			out.write('\n')


if __name__ == '__main__':
	pars = read_params(sys.argv)
	marker_f = pars['marf']
	fastq_f = pars['metaf']
	N = pars['nproc']
	preset = pars['bt2_ps']
	e_val = pars['evalue']
	max_err = pars['max_err']
	val_pos_mismatch = pars['val_pos_mismatch']
	gene_cov_threshold = pars['gene_cov']
	out_fol = pars['out_fol']

	mypath = os.getcwd()
	folders = [f for f in listdir(mypath) if not isfile(join(mypath,f))]
	if out_fol not in folders:
		os.mkdir(out_fol)
	else:
		shutil.rmtree(out_fol)
		os.mkdir(out_fol)
	make_tree_file(marker_f, out_fol)
	make_seq_file(marker_f, out_fol)
	os.mkdir(out_fol + '/blast')
	os.mkdir(out_fol + '/blast/db')
	subprocess.call(['dustmasker', '-in', out_fol + '/markers.fasta', '-infmt', 'fasta', '-parse_seqids', '-outfmt', 'maskinfo_asn1_bin', '-out', out_fol + '/blast/db/genes.asnb'])
	subprocess.call(['makeblastdb', '-in', out_fol + '/markers.fasta', '-input_type', 'fasta', '-dbtype', 'nucl', '-parse_seqids', '-mask_data', out_fol + '/blast/db/genes.asnb', '-out', out_fol + '/blast/db/genes', '-title', out_fol + '/blast/db/genes'])
	blastn_cline = NcbiblastnCommandline(query= out_fol + '/markers.fasta', out= out_fol + '/blast/all_to_all.txt', outfmt=0, num_threads = 4, db = out_fol + '/blast/db/genes', evalue = e_val)
	os.system(str(blastn_cline))
	blastn_cline = NcbiblastnCommandline(query= out_fol + '/markers.fasta', out= out_fol + '/blast/all_to_all.xml', outfmt=5, num_threads = 4, db = out_fol + '/blast/db/genes', evalue = e_val)
	os.system(str(blastn_cline))
	diff_pos = diff_in_genes(out_fol + '/blast/all_to_all.xml', out_fol + '/markers.fasta')
	write_diff_pos(diff_pos, out_fol + '/genes_vs_genes_differences.txt')
	val_pos = genes_snp_ins_positions(diff_pos)
	with open(out_fol + '/genes_snp_ins_positions.txt', 'w') as out:
		out.write('\n'.join([name + ': ' + ', '.join([str(i) for i in val_pos[name]]) for name in val_pos.keys()]))

	os.mkdir(out_fol + '/bowtie2_db')
	subprocess.call(['bowtie2-build', '-f', out_fol + '/markers.fasta', out_fol + '/bowtie2_db/bt2_db'])
	bowtie2_db = out_fol + '/bowtie2_db/bt2_db'
	subprocess.call(['bowtie2', '--quiet', '--sam-no-hd', '--sam-no-sq', '--' + preset, '-x', bowtie2_db, '-U', fastq_f,
			'-S', out_fol + '/bt2_output', '-p', str(N), '-a'])
	bt2_data = [l.strip().split('\t') for l in open(out_fol + '/bt2_output') if l.strip().split('\t')[2][-1] != '*']
	bt2_filt_maxerr = filter_maxerr(bt2_data, max_err, out_fol + '/markers.fasta')
	bt2_filt_valpos = filter_valpos(bt2_filt_maxerr, val_pos, val_pos_mismatch, out_fol + '/markers.fasta')
	with open(out_fol + '/bt2_filtered' + '.sam', 'w') as out:
		out.write('\n'.join(['\t'.join(l) for l in bt2_filt_valpos]))
	os.remove(out_fol + '/bt2_output')
	g_cov = bt2_gene_coverage(bt2_filt_valpos, out_fol + '/markers.fasta')
	write_g_cov(g_cov, out_fol + '/markers.fasta', out_fol + '/gene_coverage.txt')
	tree = read_tree(out_fol + '/tree')
	suppl_tree(tree, bt2_filt_valpos, g_cov, gene_cov_threshold)

	write_test_result(tree, out_fol + '/test_results.txt')
	write_test_result_short(tree, out_fol + '/test_results_short.txt')

	g_mat = make_gene_matrix(diff_pos, tree, out_fol + '/gene_matrix.txt') # matrix with gene vs gene differences
	#g_mat[g1][g2] = 1 means that g1 can not be distinguished from g2 (0 if can be distinduished)
	st_mat = make_strain_matrix(tree, g_mat, out_fol + '/strain_matrix.txt')
	st_repr = sort_by_representation(st_mat)
	write_summary(st_repr, tree, out_fol + '/markers.fasta', out_fol + '/summary.txt')
	with open(out_fol + '/privilegy.txt', 'w') as out:
		out.write('\n\n'.join('\n'.join(st + ': ' + str(dic[st]) for st in dic.keys()) for dic in st_repr))
