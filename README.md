## TAGMA version 1.0 ##
## Metagenomic strain profiling based on toxin-antitoxin gene systems ##


TAGMA makes strain level profiling of metagenome. Initially it is developed for analysis of Bifidabacterium and Lactobacillus strains and use of toxin-antitoxin genes as genetic markers. But algorithm can be used for other strains and genes since they are provided properly in input file.

#### Dependencies: ####

- Python 2.7.11(last version of python can be downloaded from https://www.python.org/downloads/ )
- Biopython 1.66(can be downloaded from https://biopython.org/wiki/Download)
- BLAST Command Lines Applications 2.4.0(can be downloaded from ftp://ftp.ncbi.nih.gov/blast/executables/igblast/release/LATEST)
- bowtie2 2.2.9 (can be downloaded from http://bowtie-bio.sourceforge.net/bowtie2/index.shtml)

#### USAGE: ####
program requires installation of Biopython extension for python and presence of BLAST Command Lines Applications and bowtie2 in system PATH.

Help information about program can be obtained in commandline by typing
```
python toximet.py --help
```
Arguments of the commandline:
```
toximet.py [-h] [-marf MARKERS_FILE] [-metaf METAGENOME_FILE]
                  [-out_fol OUTPUT_FOLDER] [--nproc N]
                  [--bt2_ps BowTie2_presets] [--evalue E-value]
                  [-max_err Maximum_errors]
                  [-val_pos_mismatch vpm_mismatch_number]
                  [-gene_cov gene_coverage]

main arguments:
-marf – specifies fasta file with markers
-metaf – specifies fastq file with metagenomic reads
-out_fol – output folder to create and store all output files

additional arguments:
--nproc – number of threads for parallel computation to use while mapping metagenomic reads (default value is 1).
--bt2_ps – bowtie2 presets for mapping metagenomic reads (default value is very-sensitive-local)
--evalue – E-value threshold for all-over-all blast allingment on the step of analysis of genetic markers dintinguishability (default value is 10^(-30)).
-max_err – mismatch threshold for mapping metagenomic reads. Algorithm track all alignments of reads and filters out alignments that exceed specified number of mismatches (default value is 4).
-val_pos_mismatch – mismatch threshold for valuable positions. Valuable positions are such positions in sequence of genetic marker, that distinguish homogenious sequences (default value is 0).
-gene_cov – threshold for coverage of genetic markers by metagenomic reads. If genetic marker has less number of positions covered by metagenomic reads, it is not reported as detected sequence in metagenomic sample (default value is 20).
```

##### Input files and their format: #####

fasta file with genetic markers. Identifier of each sequence should be provided in special format. It should contain information about strain to which it is assigned. Identifiers should not contain spaces.
Format of the file is the following:
```
>[identifier of strain]~[identifier of marker]
[sequence of marker] 
```
fastq file with reads of 
metagenomic sample, both single end and paired end reads can be used, configuration of mapping can be provided exactly in bowtie2 format.

##### Output files #####
All output of the program is stored in folder that is specified in command line arguments and created in current working directory.

**tree.txt** – file contains list of strains and list of genetic markers, that are assigned to each strain.This information is extracted from .fasta file, that is provided by user (see description of fasta file). Format of the file is the following:
```
		[identifier of the strain]: [genenetic marker id 1],[genenetic marker id 2]...
```
**markers.fasta** – fasta file with genetic markers. Does not contain identifiers of strains (unlike fasta file that is provided by user) in identifier line. Used for following analyses in all-over-all blast and mapping of metagenomic reads;

**blast folder** – contains results of all over all blast alignment. 

**blast/db** – supplementary data for alignment, indexing of sequences that is made with dustmasker program – part of BLAST Command Line Tools;

**blast/all_to_all.txt,  blast/all_to_all.xml** – results of all-over-all blast alignment, .xml file is used by algorithm of derive differences between genetic markers, .txt file is supplemental and is created for visualization of results and can be used for additional control of results by user; evalue threshold for alignment is specified by user as one of the command line arguments (default value is 10-30);

**genes_vs_genes_differences.txt** – summary from all-over-all blast, contains differences of genetic markers, if aligned parts of the sequences are identical, nothing is reported. Format of the file is the following:
```
		[ID of query from blast output]
		 [ID of subject from blast output]
		  snps:
		[position of mismatch in genetic marker] [letter in query]->[letter in subject]
		  insertions:
		[position of insertion in query] [letter that was inserted]
		  deletions:
		[position of insertion in query] [letter that was deleted]
```
**genes_snp_ins_positions.txt** – summary of all-over-all blast, contains information about positions of SNPs and insertions in genetic markers. This positions are significant for distinguishing of homogeneous markers. Format of the file is the following:
```
		[ID of genetic marker]: [list of positions of SNPs and insertions]
```	
**bowtie2_db folder** – contains supplementary files for mapping metagenomic reads, indexing 	of sequences with bowtie2-build program;

**bt2_filtered.sam** – SAM file containing results of mapping of metagenomic reads to genetic markers. All alignments that exceed threshold of mismatches along all alignment or threshold of mismatches in positions that distinguish genetic markers from each other (this positions are defined by all-over-all blast) are filtered out. Value of maximal 	mismatches along all alignment is specified by user as one of command line arguments (**-max_err**), default value is 4.  Value of maximal mismatches in positions that distinguish genetic markers from each other is specified by user as one of command line arguments (**-val_pos_mismatch**), default value is zero;

**gene_coverage.txt** – summary of mapping metagenomic reads to genetic markers. File contains information about coverage of genetic markers by metagenomic reads. Format of the file is the following:
```
		[identifier of genetic marker]
		[position]: [aligned letter] – [number of alignments]
```
**test_results.txt** – file contains summary of analysis: list of strains, that has at least one detected genetic marker, and information of mapping metagenomic reads to genetic markers. Format of the file is the following:
```
		[identifier of strain]
		[identifier of genetic marker] [number of positions in genetic marker that are covered by metagenomic reads]
		read name: [identifier of aligned read]
		position in marker: [position in genetic marker where read was mapped]
		CIGAR: [CIGAR representation of read mapping, that is extracted from .sam file]
		detected positions (valuable SNPs, deletions and insertions): [list of positions in genetic marker, that are essential for distinguishing it from other homogeneous genetic markers and are covered by metagenomic reads]
```
**test_results_short.txt** – shortened version of results of the analysis. Format of the file os the following:
```
		[identifier of strain]
		 [identifier of genetic marker] [number of positions in genetic marker that are covered by metagenomic reads]
		  number of reads: [number of reads that are mapped with genetic marker]
		  detected val. pos.: [list of positions in genetic marker, that are essential for distinguishing it from other homogeneous genetic markers and are covered by metagenomic reads]
```
**gene_matrix.txt** – file represent distinguishability of genetic markers based of their coverage by metagenomic reads. Distinguishability is written in form of matrix, where each column and each string represent one of detected genetic markers. If element a(i,j) is 1 then i’th genetic marker (in i’th string) is indistinguishable from j’th genetic marker (in j’th column), 0 means that it is distinguishable. Format of the file is the following:
```
		[list of genetic markers]
		[martix of distinguishability, columns are numerated from left to the right, strings are numerated from top the down]
```
**strain_matrix.txt** – file represents distinguishability of strains based on coverage of their genetic markers. As previously, distinguishability is written in form of matrix, where each column and each string represent one of detected strains. If element a(i,j) is 1 then i’th strain (in i’th string) is indistinguishable from j’th strain (in j’th column), 0 means that it is distinguishable. Format of the file is the following:
```
		[list of strains]
		[martix of distinguishability, columns are numerated from left to the right, strings are numerated from top the down]
```
**privilege.txt** – summary of distinguishability of strains. All strains are grouped in such a way, that every strain in a group is either distinguishable from all other and at least one more strain in the group is indistinguishable from the first one or this strain is indistinguishable from at least one strain in the group. So strains are grouped in a way that in every group distinguishable strains are linked with some strain, that can not be distinguished from the first once. Every strain is assigned with a number, that shows number of strains, from which that particular strain can not be destinguished. We call that number “privilege”. The best detected strains have 0 value of privilege. The file contains described above groups with values of privilege. Format of the file is the following: 
```
		[strain identifier]: [value of privelege]
		groups of strains are separated by new line symbol;
```
**summary.txt** – summary of analyses. File contains data of privilege values and additional information about number of detected genes and their coverage. Format of the file is the following:
```
		[description if the file]
		[strain identifier] [fraction of detected geenetic markers] [list, containing coverage of each genetic marker] [value if privilege]
```

TAGMA requires to run a computer with amd64 compatible processor and minimum 4 GB RAM. Software have tested only on Linux-based operating systems. 
