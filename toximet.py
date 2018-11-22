





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-lLo2nlsdl+bHLu6PGvC2j3wfP45RnK4wKQLiPnCDcuXfU38AiD+JCdMywnF3WbJC1jaxe3lAI6AM4uJuMFBLEw==" rel="stylesheet" href="https://assets-cdn.github.com/assets/frameworks-08fc49d3bd2694c870ea23d0906f3610.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-mv6mDRPrioZTM6DqvWmoRTqzLBRhHXVLHuh4NbZvbWLfjVpC7gqihEHCfY+IR3fRoQ3KD7FLLz422a7iH/HT/g==" rel="stylesheet" href="https://assets-cdn.github.com/assets/github-4d9ab9919c1f80062f9616df3655449f.css" />
  
  
  
  
  

  <meta name="viewport" content="width=device-width">
  
  <title>TAGMA/bt2_snp_11.py at master · LabGenMO/TAGMA</title>
    <meta name="description" content="TAGMA makes strain level profiling of metagenome. Initially it is developed for analysis of Bifidabacterium and Lactobacillus strains and use of toxin-antitoxin genes as genetic markers. But algorithm can be used for other strains and genes since they are provided properly in input file. - LabGenMO/TAGMA">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta property="og:image" content="https://avatars2.githubusercontent.com/u/20303460?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="LabGenMO/TAGMA" /><meta property="og:url" content="https://github.com/LabGenMO/TAGMA" /><meta property="og:description" content="TAGMA makes strain level profiling of metagenome. Initially it is developed for analysis of Bifidabacterium and Lactobacillus strains and use of toxin-antitoxin genes as genetic markers. But algori..." />

  <link rel="assets" href="https://assets-cdn.github.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6MzQzNzQ2MTI2OjI2NDg2ZTBkMGE0M2MwZWQ5ZTA2N2ZjMWZjMDQxMDNhMjU4NDJhN2E0M2NkN2RlYWEwN2I3OGE0MWFjYjFkZmM=--674e9e65dd19a721460f7460e258f0cce7a40ad5">
  <meta name="pjax-timeout" content="1000">
  <link rel="sudo-modal" href="/sessions/sudo_modal">
  <meta name="request-id" content="FF7E:6A0F:55B2B74:7BD09AE:5BF6F31E" data-pjax-transient>


  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

      <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="FF7E:6A0F:55B2B74:7BD09AE:5BF6F31E" /><meta name="octolytics-dimension-region_edge" content="ams" /><meta name="octolytics-dimension-region_render" content="iad" /><meta name="octolytics-actor-id" content="20303460" /><meta name="octolytics-actor-login" content="LabGenMO" /><meta name="octolytics-actor-hash" content="a6f53b2cb7ec41d0b2c0e099fc6e4a410bd3ae06faf103c27a0296616ee7c98d" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">

  <meta class="js-ga-set" name="userId" content="4f5321742bc6724ce61d7e1d0c039d81" %>

<meta class="js-ga-set" name="dimension1" content="Logged In">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="LabGenMO">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="YmQ0MGFmMWFlZTlhZmQwZTI1MzA1YmU5MTMzNjUxZWZjZjUzYjJjNWVjMDVkOTExZDAyMDQzYzdkZGU2ZGZmM3x7InJlbW90ZV9hZGRyZXNzIjoiNS4yMjguMTQxLjE5MiIsInJlcXVlc3RfaWQiOiJGRjdFOjZBMEY6NTVCMkI3NDo3QkQwOUFFOjVCRjZGMzFFIiwidGltZXN0YW1wIjoxNTQyOTEwNzU1LCJob3N0IjoiZ2l0aHViLmNvbSJ9">

    <meta name="enabled-features" content="DASHBOARD_V2_LAYOUT_OPT_IN,EXPLORE_DISCOVER_REPOSITORIES,UNIVERSE_BANNER,MARKETPLACE_PLAN_RESTRICTION_EDITOR,NOTIFY_ON_BLOCK,SAVED_THREADS,TIMELINE_COMMENT_UPDATES,SUGGESTED_CHANGES_UX_TEST,SUGGESTED_CHANGES_BATCH,RELATED_ISSUES,MARKETPLACE_INSIGHTS_V2">

  <meta name="html-safe-nonce" content="59a91e7349f39a073c3132c34dcc77ca885ef36e">

  <meta http-equiv="x-pjax-version" content="0db17447ccd5454c4cbcd5322594675a">
  

      <link href="https://github.com/LabGenMO/TAGMA/commits/master.atom" rel="alternate" title="Recent Commits to TAGMA:master" type="application/atom+xml">

  <meta name="go-import" content="github.com/LabGenMO/TAGMA git https://github.com/LabGenMO/TAGMA.git">

  <meta name="octolytics-dimension-user_id" content="20303460" /><meta name="octolytics-dimension-user_login" content="LabGenMO" /><meta name="octolytics-dimension-repository_id" content="62649656" /><meta name="octolytics-dimension-repository_nwo" content="LabGenMO/TAGMA" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="62649656" /><meta name="octolytics-dimension-repository_network_root_nwo" content="LabGenMO/TAGMA" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="true" />


    <link rel="canonical" href="https://github.com/LabGenMO/TAGMA/blob/master/bt2_snp_11.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">


  <meta name="u2f-support" content="true">

  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



        
<header class="Header  f5" role="banner">
  <div class="d-flex flex-justify-between px-3 ">
    <div class="d-flex flex-justify-between ">
      <div class="">
        <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg height="32" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>

      </div>

    </div>

    <div class="HeaderMenu d-flex flex-justify-between flex-auto">
      <nav class="d-flex" aria-label="Global">
            <div class="">
              <div class="header-search scoped-search site-scoped-search js-site-search position-relative js-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" data-scope-type="Repository" data-scope-id="62649656" data-scoped-search-url="/LabGenMO/TAGMA/search" data-unscoped-search-url="/search" action="/LabGenMO/TAGMA/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control header-search-wrapper header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search or jump to…"
          data-unscoped-placeholder="Search or jump to…"
          data-scoped-placeholder="Search or jump to…"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search or jump to…"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations#csrf-token=ONaG7ADFo77BodozCxQcuoUr+JVHXwqwXTyTd3FStkCve8ZcaDG02gEgpRlxRMJRUI0Zd8ftCBbDWpqWpPengQ=="
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://assets-cdn.github.com/images/search-shortcut-hint.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              <ul class="d-none js-jump-to-suggestions-template-container">
                <li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item" role="option">
                  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center p-2 jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open" href="">
                    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
                      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
                      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
                      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
                    </div>

                    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

                    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
                    </div>

                    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
                      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
                        In this repository
                      </span>
                      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
                        All GitHub
                      </span>
                      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
                    </div>

                    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
                      Jump to
                      <span class="d-inline-block ml-1 v-align-middle">↵</span>
                    </div>
                  </a>
                </li>
              </ul>
              <ul class="d-none js-jump-to-no-results-template-container">
                <li class="d-flex flex-justify-center flex-items-center p-3 f5 d-none">
                  <span class="text-gray">No suggested jump to results</span>
                </li>
              </ul>

              <ul id="jump-to-results" role="listbox" class="js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container" >
                <li class="d-flex flex-justify-center flex-items-center p-0 f5">
                  <img src="https://assets-cdn.github.com/images/spinners/octocat-spinner-128.gif" alt="Octocat Spinner Icon" class="m-2" width="28">
                </li>
              </ul>
            </div>
      </label>
</form>  </div>
</div>

            </div>

          <ul class="d-flex pl-2 flex-items-center text-bold list-style-none">
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="/pulls">
                Pull requests
</a>            </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="/issues">
                Issues
</a>            </li>
              <li class="position-relative">
                <a class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-octo-click="marketplace_click" data-octo-dimensions="location:nav_bar" data-selected-links=" /marketplace" href="/marketplace">
                   Marketplace
</a>                  
              </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
                Explore
</a>            </li>
          </ul>
      </nav>

      <div class="d-flex">
        
<ul class="user-nav d-flex flex-items-center list-style-none" id="user-links">
  <li class="dropdown">
    <span class="d-inline-block  px-2">
      
    <a aria-label="You have no unread notifications" class="notification-indicator tooltipped tooltipped-s  js-socket-channel js-notification-indicator" data-hotkey="g n" data-ga-click="Header, go to notifications, icon:read" data-channel="notification-changed:20303460" href="/notifications">
        <span class="mail-status "></span>
        <svg class="octicon octicon-bell" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 12v1H0v-1l.73-.58c.77-.77.81-2.55 1.19-4.42C2.69 3.23 6 2 6 2c0-.55.45-1 1-1s1 .45 1 1c0 0 3.39 1.23 4.16 5 .38 1.88.42 3.66 1.19 4.42l.66.58H14zm-7 4c1.11 0 2-.89 2-2H5c0 1.11.89 2 2 2z"/></svg>
</a>
    </span>
  </li>

  <li class="dropdown">
    <details class="details-overlay details-reset d-flex px-2 flex-items-center">
      <summary class="HeaderNavlink"
         aria-label="Create new…"
         data-ga-click="Header, create new, icon:add">
        <svg class="octicon octicon-plus float-left mr-1 mt-1" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5v2z"/></svg>
        <span class="dropdown-caret mt-1"></span>
      </summary>
      <details-menu class="dropdown-menu dropdown-menu-sw">
        
<a role="menuitem" class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a role="menuitem" class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a role="menuitem" class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a role="menuitem" class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>


  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="LabGenMO/TAGMA">This repository</span>
  </div>
    <a role="menuitem" class="dropdown-item" href="/LabGenMO/TAGMA/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>


      </details-menu>
    </details>
  </li>

  <li class="dropdown">

    <details class="details-overlay details-reset d-flex pl-2 flex-items-center">
      <summary class="HeaderNavlink name mt-1"
        aria-label="View profile and more"
        data-ga-click="Header, show menu, icon:avatar">
        <img alt="@LabGenMO" class="avatar float-left mr-1" src="https://avatars1.githubusercontent.com/u/20303460?s=40&amp;v=4" height="20" width="20">
        <span class="dropdown-caret"></span>
      </summary>
      <details-menu class="dropdown-menu dropdown-menu-sw">
        <ul>
          <li class="header-nav-current-user css-truncate"><a role="menuitem" class="no-underline user-profile-link px-3 pt-2 pb-2 mb-n2 mt-n1 d-block" href="/LabGenMO" data-ga-click="Header, go to profile, text:Signed in as">Signed in as <strong class="css-truncate-target">LabGenMO</strong></a></li>
          <li class="dropdown-divider"></li>
          <li><a role="menuitem" class="dropdown-item" href="/LabGenMO" data-ga-click="Header, go to profile, text:your profile">Your profile</a></li>
          <li><a role="menuitem" class="dropdown-item" href="/LabGenMO?tab=repositories" data-ga-click="Header, go to repositories, text:your repositories">Your repositories</a></li>


          <li><a role="menuitem" class="dropdown-item" href="/LabGenMO?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">Your stars</a></li>
            <li><a role="menuitem" class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, your gists, text:your gists">Your gists</a></li>
          <li class="dropdown-divider"></li>
          <li><a role="menuitem" class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a></li>
          <li><a role="menuitem" class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">Settings</a></li>
          <li>
            <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="logout-form" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="14QCFYR3zbqaXjyWEjhdpYizC/NJtj4DpAU1fzfsO5jKpISNk0WTuGkTZTwZjGn3aXsLfAwe1JNrjK7NqPfHzA==" />
              <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout" role="menuitem">
                Sign out
              </button>
</form>          </li>
        </ul>
      </details-menu>
    </details>
  </li>
</ul>



        <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="sr-only right-0" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="LVeRpHg3vI+4wtZiJRSOU8myrIfNox41EnguAbNe+nAwdxc8bwXijUuPj8guoLoBKHqsCIgL9KXd8bWzLEUGJA==" />
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </div>
</header>

      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">


</div>



  <div role="main" class="application-main " >
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <div id="js-repo-pjax-container" data-pjax-container >
      







  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav  ">
    <div class="repohead-details-container clearfix container">

      <ul class="pagehead-actions">
  <li>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-remote="true" class="js-social-form js-social-container" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="if3SUvA7GcNbZFAc0uANpsSPNdqb23RiOLcFvvAsC/02IvHg35Z5AjSB2gbQbvr6DuhE/IGg/sHIXZFhc3gs0g==" />      <input type="hidden" name="repository_id" id="repository_id" value="62649656" class="form-control" />

      <details class="details-reset details-overlay select-menu float-left">
        <summary class="btn btn-sm btn-with-count select-menu-button" data-ga-click="Repository, click Watch settings, action:blob#show">
          <span data-menu-button>
              <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
              Unwatch
          </span>
        </summary>
        <details-menu class="select-menu-modal position-absolute mt-5" style="z-index: 99;">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
          </div>
          <div class="select-menu-list">
            <button type="submit" name="do" value="included" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Not watching</span>
                <span class="description">Be notified only when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Watch
                </span>
              </div>
            </button>


            <button type="submit" name="do" value="subscribed" class="select-menu-item width-full" aria-checked="true" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Watching</span>
                <span class="description">Be notified of all conversations.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Unwatch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="ignore" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Ignoring</span>
                <span class="description">Never be notified.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-mute v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                  Stop ignoring
                </span>
              </div>
            </button>
          </div>
        </details-menu>
      </details>
      <a class="social-count js-social-count"
        href="/LabGenMO/TAGMA/watchers"
        aria-label="1 user is watching this repository">
        1
      </a>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="starred js-social-form" action="/LabGenMO/TAGMA/unstar" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="esRduTj94wsQ8zXmnzHXh16OHx3hYANeeKWJsCWmcsd2rIS/szuwvRFApErfLDmU0Qwt8JMYiZl+seGqnmdctw==" />
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar LabGenMO/TAGMA"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/LabGenMO/TAGMA/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="unstarred js-social-form" action="/LabGenMO/TAGMA/star" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="nTPLoJfg1FAVytiPc2pwsZvn2THFO0shfcFBRnwy9UKNug6QCOXQ5hN7n4VQ5NnA/SLiEvefVx48Fh1J88/mcg==" />
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star LabGenMO/TAGMA"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/LabGenMO/TAGMA/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>  </div>

  </li>

  <li>
        <span class="btn btn-sm btn-with-count disabled tooltipped tooltipped-sw" aria-label="Cannot fork because you own this repository and are not a member of any organizations.">
          <svg class="octicon octicon-repo-forked v-align-text-bottom" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
          Fork
</span>
    <a href="/LabGenMO/TAGMA/network/members" class="social-count"
       aria-label="1 user forked this repository">
      1
    </a>
  </li>
</ul>

      <h1 class="public ">
  <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=20303460" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/LabGenMO">LabGenMO</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/LabGenMO/TAGMA">TAGMA</a></strong>

</h1>

    </div>
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
    aria-label="Repository"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /LabGenMO/TAGMA" href="/LabGenMO/TAGMA">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /LabGenMO/TAGMA/issues" href="/LabGenMO/TAGMA/issues">
        <svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /LabGenMO/TAGMA/pulls" href="/LabGenMO/TAGMA/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>


    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /LabGenMO/TAGMA/projects" href="/LabGenMO/TAGMA/projects">
      <svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>

    <a class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /LabGenMO/TAGMA/wiki" href="/LabGenMO/TAGMA/wiki">
      <svg class="octicon octicon-book" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"/></svg>
      Wiki
</a>
  <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse alerts /LabGenMO/TAGMA/pulse" href="/LabGenMO/TAGMA/pulse">
    <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Insights
</a>
    <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_settings repo_branch_settings hooks integration_installations repo_keys_settings issue_template_editor /LabGenMO/TAGMA/settings" href="/LabGenMO/TAGMA/settings">
      <svg class="octicon octicon-gear" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 8.77v-1.6l-1.94-.64-.45-1.09.88-1.84-1.13-1.13-1.81.91-1.09-.45-.69-1.92h-1.6l-.63 1.94-1.11.45-1.84-.88-1.13 1.13.91 1.81-.45 1.09L0 7.23v1.59l1.94.64.45 1.09-.88 1.84 1.13 1.13 1.81-.91 1.09.45.69 1.92h1.59l.63-1.94 1.11-.45 1.84.88 1.13-1.13-.92-1.81.47-1.09L14 8.75v.02zM7 11c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3z"/></svg>
      Settings
</a>
</nav>


  </div>

<div class="container new-discussion-timeline experiment-repo-nav  ">
  <div class="repository-content ">

    

  
    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/LabGenMO/TAGMA/blob/37ba3a7237c9ea75b28603ada8a57891cbc2c27c/bt2_snp_11.py">Permalink</a>

    <!-- blob contrib key: blob_contributors:v21:923c6b396d6d9802b18577c7442e3856 -->

    

    <div class="file-navigation">
      
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg class="octicon octicon-x js-menu-close" role="img" aria-label="Close" viewBox="0 0 12 16" version="1.1" width="12" height="16"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs" role="tablist">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Find or create a branch…" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/LabGenMO/TAGMA/blob/master/bt2_snp_11.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
        </div>

          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="select-menu-new-item-form js-new-item-form" action="/LabGenMO/TAGMA/branches" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="cFI68di57cDP7z29yryJzB7PzDR4htHSzL5Yspb989X0T/giwR3nKTo4XhOhNIIi0xCM74k2swPuM3CDJv5A4w==" />
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master">
            <input type="hidden" name="path_binary" id="path_binary" value="YnQyX3NucF8xMS5weQ==">

            <button type="submit" class="width-full select-menu-item js-navigation-open js-navigation-item">
              <svg class="octicon octicon-git-branch select-menu-item-icon" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 5c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v.3c-.02.52-.23.98-.63 1.38-.4.4-.86.61-1.38.63-.83.02-1.48.16-2 .45V4.72a1.993 1.993 0 0 0-1-3.72C.88 1 0 1.89 0 3a2 2 0 0 0 1 1.72v6.56c-.59.35-1 .99-1 1.72 0 1.11.89 2 2 2 1.11 0 2-.89 2-2 0-.53-.2-1-.53-1.36.09-.06.48-.41.59-.47.25-.11.56-.17.94-.17 1.05-.05 1.95-.45 2.75-1.25S8.95 7.77 9 6.73h-.02C9.59 6.37 10 5.73 10 5zM2 1.8c.66 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2C1.35 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2zm0 12.41c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm6-8c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Create branch: <span class="js-new-item-name"></span></span>
                <span class="description">from ‘master’</span>
              </div>
            </button>
</form>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

      <div class="BtnGroup float-right">
        <a href="/LabGenMO/TAGMA/find/master"
              class="js-pjax-capture-input btn btn-sm BtnGroup-item"
              data-pjax
              data-hotkey="t">
          Find file
        </a>
        <clipboard-copy for="blob-path" class="btn btn-sm BtnGroup-item">
          Copy path
        </clipboard-copy>
      </div>
      <div id="blob-path" class="breadcrumb">
        <span class="repo-root js-repo-root"><span class="js-path-segment"><a data-pjax="true" href="/LabGenMO/TAGMA"><span>TAGMA</span></a></span></span><span class="separator">/</span><strong class="final-path">bt2_snp_11.py</strong>
      </div>
    </div>


    
  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/LabGenMO/TAGMA/commit/68bf133d97266a08006bc6fb728e7fd9bb82b086" data-pjax>
          68bf133
        </a>
        <relative-time datetime="2016-07-05T16:05:47Z">Jul 5, 2016</relative-time>
      </span>
      <div>
        <a rel="contributor" data-skip-pjax="true" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=4741452" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/ArtemKasianov"><img class="avatar" src="https://avatars3.githubusercontent.com/u/4741452?s=40&amp;v=4" width="20" height="20" alt="@ArtemKasianov" /></a>
        <a class="user-mention" rel="contributor" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=4741452" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/ArtemKasianov">ArtemKasianov</a>
          <a data-pjax="true" title="adding code" class="message" href="/LabGenMO/TAGMA/commit/68bf133d97266a08006bc6fb728e7fd9bb82b086">adding code</a>
      </div>

    <div class="commit-tease-contributors">
      
<details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark float-left mr-2" id="blob_contributors_box">
  <summary class="btn-link" aria-haspopup="dialog"  >
    
    <span><strong>1</strong> contributor</span>
  </summary>
  <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast " aria-label="Users who have contributed to this file">
    <div class="Box-header">
      <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <h3 class="Box-title">Users who have contributed to this file</h3>
    </div>
    
        <ul class="list-style-none overflow-auto">
            <li class="Box-row">
              <a class="link-gray-dark no-underline" href="/ArtemKasianov">
                <img class="avatar mr-2" alt="" src="https://avatars3.githubusercontent.com/u/4741452?s=40&amp;v=4" width="20" height="20" />
                ArtemKasianov
</a>            </li>
        </ul>

  </details-dialog>
</details>
      
    </div>
  </div>



    <div class="file ">
      <div class="file-header">
  <div class="file-actions">


    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/LabGenMO/TAGMA/raw/master/bt2_snp_11.py">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/LabGenMO/TAGMA/blame/master/bt2_snp_11.py">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/LabGenMO/TAGMA/commits/master/bt2_snp_11.py">History</a>
    </div>

        <a class="btn-octicon tooltipped tooltipped-nw"
           href="github-windows://openRepo/https://github.com/LabGenMO/TAGMA?branch=master&amp;filepath=bt2_snp_11.py"
           aria-label="Open this file in GitHub Desktop"
           data-ga-click="Repository, open with desktop, type:windows">
            <svg class="octicon octicon-device-desktop" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z"/></svg>
        </a>

          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form js-update-url-with-hash" action="/LabGenMO/TAGMA/edit/master/bt2_snp_11.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="zT/sSxQPAAQwq+CbzckHqL/Af3Yw1CVMSs9xRp+yhfund0Mr7H1qK8MDgQb2gOamxfb2rapA1/2q9v1/PE7M2A==" />
            <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
              aria-label="Edit this file" data-hotkey="e" data-disable-with>
              <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
            </button>
</form>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form" action="/LabGenMO/TAGMA/delete/master/bt2_snp_11.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="C+grpTyjYx0WCBqlG7ZgE8AmgwTGkc6HjbXweKpdXAT5tPfwtqghsVhJ1SWJ6g87gdpkM59gy6avV94Ucxyn8A==" />
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Delete this file" data-disable-with>
            <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
          </button>
</form>  </div>

  <div class="file-info">
      542 lines (506 sloc)
      <span class="file-info-divider"></span>
    21.8 KB
  </div>
</div>

      

  <div itemprop="text" class="blob-wrapper data type-python ">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> sys</td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> os</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> subprocess</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> shutil</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> argparse <span class="pl-k">as</span> ap</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> os <span class="pl-k">import</span> listdir</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> os.path <span class="pl-k">import</span> isfile, join</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> Bio.Blast <span class="pl-k">import</span> <span class="pl-c1">NCBIXML</span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> Bio.Blast.Applications <span class="pl-k">import</span> NcbiblastnCommandline</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">read_params</span>(<span class="pl-smi">args</span>):</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line">	p <span class="pl-k">=</span> ap.ArgumentParser(<span class="pl-v">description</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>This program makes quantitative analysis of metagenome and analyses presence of lacto and bifidobacteries. BowTie2 is used for alignment. BowTie2 is required in the system path with read and execution permissions.<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line">		<span class="pl-s"><span class="pl-pds">&#39;</span>Output:<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>, <span class="pl-v">formatter_class</span> <span class="pl-k">=</span> ap.RawTextHelpFormatter)</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">	arg <span class="pl-k">=</span> p.add_argument</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">	arg(<span class="pl-s"><span class="pl-pds">&#39;</span>-marf<span class="pl-pds">&#39;</span></span>, <span class="pl-v">metavar</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>MARKERS<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span> <span class="pl-k">=</span> <span class="pl-c1">str</span>, <span class="pl-v">nargs</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>?<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-v">help</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Input file in fasta format (genetic markers).<span class="pl-cce">\n</span>Description line must contain the folowing information:<span class="pl-cce">\n</span> &gt; [strain name] ~ [marker name]<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line">	arg(<span class="pl-s"><span class="pl-pds">&#39;</span>-metaf<span class="pl-pds">&#39;</span></span>, <span class="pl-v">metavar</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>METAGENOME<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span> <span class="pl-k">=</span> <span class="pl-c1">str</span>, <span class="pl-v">nargs</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>?<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-v">help</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Input file in fastq format (metagenome)<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">	arg(<span class="pl-s"><span class="pl-pds">&#39;</span>--nproc<span class="pl-pds">&#39;</span></span>, <span class="pl-v">metavar</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>N<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span> <span class="pl-k">=</span> <span class="pl-c1">int</span>, <span class="pl-v">default</span> <span class="pl-k">=</span> <span class="pl-c1">1</span>, <span class="pl-v">help</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>The number of CPUs to use for parallelizing the alignment<span class="pl-cce">\n</span>[default is 1 i.e. no parallelizing]<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">	bt2ps <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>sensitive<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>very-sensitive<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>sensitive-local<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>very-sensitive-local<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">	arg(<span class="pl-s"><span class="pl-pds">&#39;</span>--bt2_ps<span class="pl-pds">&#39;</span></span>, <span class="pl-v">metavar</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>BowTie2 presets<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>very-sensitive-local<span class="pl-pds">&#39;</span></span>, <span class="pl-v">choices</span> <span class="pl-k">=</span> bt2ps, <span class="pl-v">help</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Presets options for BowTie2<span class="pl-cce">\n</span> - sensitive<span class="pl-cce">\n</span> - very-sensitive<span class="pl-cce">\n</span> - sensitive-local<span class="pl-cce">\n</span> - very-sensitive-local<span class="pl-cce">\n</span>[default very-sensitive-local]<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">	arg(<span class="pl-s"><span class="pl-pds">&#39;</span>--evalue<span class="pl-pds">&#39;</span></span>, <span class="pl-v">metavar</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>E-value<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span> <span class="pl-k">=</span> <span class="pl-c1">float</span>, <span class="pl-v">default</span> <span class="pl-k">=</span> <span class="pl-c1">10</span><span class="pl-k">**</span>(<span class="pl-k">-</span><span class="pl-c1">30</span>), <span class="pl-v">help</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>E-value for all-vs-all markers blast (for identification of snp, insertion and deletion positions)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">	arg(<span class="pl-s"><span class="pl-pds">&#39;</span>-max_err<span class="pl-pds">&#39;</span></span>, <span class="pl-v">metavar</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Maximum errors<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span> <span class="pl-k">=</span> <span class="pl-c1">int</span>, <span class="pl-v">default</span> <span class="pl-k">=</span> <span class="pl-c1">4</span>, <span class="pl-v">help</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Maximum errors per read alignment (equal to sum of snps, insertions and deletions)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">	arg(<span class="pl-s"><span class="pl-pds">&#39;</span>-val_pos_mismatch<span class="pl-pds">&#39;</span></span>, <span class="pl-v">metavar</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Val. pos. mismatch<span class="pl-pds">&#39;</span></span>,  <span class="pl-v">type</span> <span class="pl-k">=</span> <span class="pl-c1">int</span>, <span class="pl-v">default</span> <span class="pl-k">=</span> <span class="pl-c1">0</span>, <span class="pl-v">help</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Maximum errors in valuable positions in markers (valuable positions are difined by all vs. all blast)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">	arg(<span class="pl-s"><span class="pl-pds">&#39;</span>-gene_cov<span class="pl-pds">&#39;</span></span>, <span class="pl-v">metavar</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>GENE_COVERAGE<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span> <span class="pl-k">=</span> <span class="pl-c1">float</span>, <span class="pl-v">default</span> <span class="pl-k">=</span> <span class="pl-c1">20</span>, <span class="pl-v">help</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Gene coverage threshold. All genes, that are covered by reads on more than this value are reported in test results.<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">	arg(<span class="pl-s"><span class="pl-pds">&#39;</span>-out_fol<span class="pl-pds">&#39;</span></span>, <span class="pl-v">metavar</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>OUTPUT_FOLDER<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span> <span class="pl-k">=</span> <span class="pl-c1">str</span>, <span class="pl-v">default</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>output<span class="pl-pds">&#39;</span></span>, <span class="pl-v">help</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Folder for all output files.<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">return</span> <span class="pl-c1">vars</span>(p.parse_args())</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">make_tree_file</span>(<span class="pl-smi">mar_f</span>, <span class="pl-smi">path</span>):</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">	tree <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">	<span class="pl-c1">print</span> mar_f</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">	inp_f <span class="pl-k">=</span>  <span class="pl-c1">open</span>(mar_f,<span class="pl-s"><span class="pl-pds">&#39;</span>r<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> line <span class="pl-k">in</span> inp_f.readlines():</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>&gt;<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> line:</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">			name <span class="pl-k">=</span> line.strip().replace(<span class="pl-s"><span class="pl-pds">&#39;</span>&gt;<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>).split(<span class="pl-s"><span class="pl-pds">&#39;</span>~<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">			gene <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>_<span class="pl-pds">&#39;</span></span>.join(line.strip().replace(<span class="pl-s"><span class="pl-pds">&#39;</span>&gt;<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>).split(<span class="pl-s"><span class="pl-pds">&#39;</span>~<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>::])</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> name <span class="pl-k">not</span> <span class="pl-k">in</span> tree.keys():</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">				tree[name] <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">			tree[name].append(gene)</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">	inp_f.close()</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">	tree_f <span class="pl-k">=</span> <span class="pl-c1">open</span>(path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/tree<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> strain <span class="pl-k">in</span> tree:</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">		tree_f.write(strain <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>: <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>.join(tree[strain]) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">	tree_f.close()</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">make_seq_file</span>(<span class="pl-smi">seq</span>, <span class="pl-smi">path</span>):</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">	inp_f <span class="pl-k">=</span> <span class="pl-c1">open</span>(seq,<span class="pl-s"><span class="pl-pds">&#39;</span>r<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">	outp_f <span class="pl-k">=</span> <span class="pl-c1">open</span>(path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/markers.fasta<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> line <span class="pl-k">in</span> inp_f.readlines():</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>&gt;<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> line:</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">			outp_f.write(<span class="pl-s"><span class="pl-pds">&#39;</span>&gt;<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>_<span class="pl-pds">&#39;</span></span>.join(line.strip().replace(<span class="pl-s"><span class="pl-pds">&#39;</span>&gt;<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>).split(<span class="pl-s"><span class="pl-pds">&#39;</span>~<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>::]) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">			outp_f.write(line)</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">	inp_f.close()</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">	outp_f.close()</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">read_fasta</span>(<span class="pl-smi">fasta_f</span>):</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">	seq_d <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">with</span> <span class="pl-c1">open</span>(fasta_f, <span class="pl-s"><span class="pl-pds">&#39;</span>r<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> seq_f:</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> line <span class="pl-k">in</span> seq_f.readlines():</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>&gt;<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> line:</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">				s_name <span class="pl-k">=</span> line.strip().replace(<span class="pl-s"><span class="pl-pds">&#39;</span>&gt;<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">				seq_d[s_name] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">				seq_d[s_name] <span class="pl-k">=</span> seq_d[s_name] <span class="pl-k">+</span> line.strip()</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">return</span> seq_d</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">read_cigar</span>(<span class="pl-smi">c</span>):</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">	cig <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">	n <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">while</span> <span class="pl-c1">len</span>(c) <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span> <span class="pl-k">not</span> (c[<span class="pl-c1">0</span>] <span class="pl-k">&gt;=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>0<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> c[<span class="pl-c1">0</span>] <span class="pl-k">&lt;=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>9<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">			ch <span class="pl-k">=</span> c[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">			cig <span class="pl-k">=</span> cig <span class="pl-k">+</span> [[ch, <span class="pl-c1">int</span>(n)]]</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">			c <span class="pl-k">=</span> c[<span class="pl-c1">1</span>::]</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">			n <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">			n <span class="pl-k">=</span> n <span class="pl-k">+</span> c[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">			c <span class="pl-k">=</span> c[<span class="pl-c1">1</span>::]</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">return</span> cig</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">bt2_gene_coverage</span>(<span class="pl-smi">bt2_data</span>, <span class="pl-smi">markers_f</span>):</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">	genes_d <span class="pl-k">=</span> read_fasta(markers_f)</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">	cov <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">	names <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> l <span class="pl-k">in</span> bt2_data:</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">		name <span class="pl-k">=</span> l[<span class="pl-c1">2</span>]</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span> name <span class="pl-k">not</span> <span class="pl-k">in</span> names:</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">			names.append(name)</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">			cov[name] <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">			cov[name][<span class="pl-s"><span class="pl-pds">&#39;</span>pos<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> ()</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">			cov[name][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">for</span> n <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">len</span>(genes_d[name])):</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">				cov[name][<span class="pl-s"><span class="pl-pds">&#39;</span>pos<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> cov[name][<span class="pl-s"><span class="pl-pds">&#39;</span>pos<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+</span> ({<span class="pl-s"><span class="pl-pds">&#39;</span>A<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>C<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>G<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>T<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>c<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>g<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>t<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>U<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>R<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Y<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>K<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>M<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>S<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>W<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>B<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>X<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>D<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>H<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>V<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>N<span class="pl-pds">&#39;</span></span>:<span class="pl-c1">0</span>},)</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> l <span class="pl-k">in</span> bt2_data:</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">		cigar <span class="pl-k">=</span> read_cigar(l[<span class="pl-c1">5</span>])</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">		i <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">		name <span class="pl-k">=</span> l[<span class="pl-c1">2</span>]</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">		marker_pos <span class="pl-k">=</span> <span class="pl-c1">int</span>(l[<span class="pl-c1">3</span>])</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">		read_pos <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> el <span class="pl-k">in</span> cigar:</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> el[<span class="pl-c1">0</span>] <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>M<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>X<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">for</span> j <span class="pl-k">in</span> <span class="pl-c1">range</span>(el[<span class="pl-c1">1</span>]):</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">					cov[name][<span class="pl-s"><span class="pl-pds">&#39;</span>pos<span class="pl-pds">&#39;</span></span>][marker_pos <span class="pl-k">+</span> j <span class="pl-k">-</span> <span class="pl-c1">1</span>][l[<span class="pl-c1">9</span>][read_pos <span class="pl-k">+</span> j]] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> el[<span class="pl-c1">0</span>] <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>M<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>I<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>S<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>X<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>=<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">				read_pos <span class="pl-k">+=</span> el[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> el[<span class="pl-c1">0</span>] <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>M<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>X<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>D<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>N<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>H<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>P<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>=<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">				marker_pos <span class="pl-k">+=</span> el[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> al <span class="pl-k">in</span> cov.keys():</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> p <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">len</span>(cov[al][<span class="pl-s"><span class="pl-pds">&#39;</span>pos<span class="pl-pds">&#39;</span></span>])):</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">			check <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">for</span> ch <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>A<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>C<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>G<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>T<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>c<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>g<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>t<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>U<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>R<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>Y<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>K<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>M<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>S<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>W<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>B<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>X<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>D<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>H<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>V<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>N<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> cov[al][<span class="pl-s"><span class="pl-pds">&#39;</span>pos<span class="pl-pds">&#39;</span></span>][p][ch] <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">					check <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> check:</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">				cov[al][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">return</span> cov</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">write_g_cov</span>(<span class="pl-smi">g_cov</span>, <span class="pl-smi">genes_f</span>, <span class="pl-smi">outp</span>):</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">	genes_d <span class="pl-k">=</span> read_fasta(genes_f)</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">with</span> <span class="pl-c1">open</span>(outp, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> out:</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">		good_al <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> al <span class="pl-k">in</span> g_cov:</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">			check <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">for</span> n <span class="pl-k">in</span> g_cov[al][<span class="pl-s"><span class="pl-pds">&#39;</span>pos<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">for</span> ch <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>A<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>C<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>G<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>T<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>c<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>g<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>t<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>U<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>R<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>Y<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>K<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>M<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>S<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>W<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>B<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>X<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>D<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>H<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>V<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>N<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">if</span> n[ch] <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">						check <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> check:</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> check:</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">				good_al.append(al)</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> al <span class="pl-k">in</span> good_al:</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">			out.write(al <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>  <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(g_cov[al][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>]) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">for</span> n <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">len</span>(g_cov[al][<span class="pl-s"><span class="pl-pds">&#39;</span>pos<span class="pl-pds">&#39;</span></span>])):</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">				out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\t</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(n<span class="pl-k">+</span><span class="pl-c1">1</span>) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>: <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>(<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> genes_d[al][n] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>) <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>.join([ch <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> - <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(g_cov[al][<span class="pl-s"><span class="pl-pds">&#39;</span>pos<span class="pl-pds">&#39;</span></span>][n][ch]) <span class="pl-k">for</span> ch <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>A<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>C<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>G<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>T<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>c<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>g<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>t<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>U<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>R<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>Y<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>K<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>M<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>S<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>W<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>B<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>X<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>D<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>H<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>V<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>N<span class="pl-pds">&#39;</span></span>] <span class="pl-k">if</span> g_cov[al][<span class="pl-s"><span class="pl-pds">&#39;</span>pos<span class="pl-pds">&#39;</span></span>][n][ch] <span class="pl-k">!=</span> <span class="pl-c1">0</span>]) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">read_tree</span>(<span class="pl-smi">tree_path</span>):</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">	tree_file <span class="pl-k">=</span> <span class="pl-c1">open</span>(tree_path,<span class="pl-s"><span class="pl-pds">&#39;</span>r<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">	tree <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> line <span class="pl-k">in</span> tree_file.readlines():</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">		line <span class="pl-k">=</span> line.strip()</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">		strain <span class="pl-k">=</span> line.split(<span class="pl-s"><span class="pl-pds">&#39;</span>: <span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>].split(<span class="pl-s"><span class="pl-pds">&#39;</span>~<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span> strain <span class="pl-k">not</span> <span class="pl-k">in</span> tree:</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">			tree[strain] <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> gene <span class="pl-k">in</span> line.split(<span class="pl-s"><span class="pl-pds">&#39;</span>: <span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>].split(<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">			tree[strain][gene] <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">			tree[strain][gene][<span class="pl-s"><span class="pl-pds">&#39;</span>dic<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">			tree[strain][gene][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">	tree_file.close()</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">return</span> tree</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">suppl_tree</span>(<span class="pl-smi">tree</span>, <span class="pl-smi">bt2_data</span>, <span class="pl-smi">g_cov</span>, <span class="pl-smi">cov_threshold</span>):</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> strain <span class="pl-k">in</span> tree:</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> gene <span class="pl-k">in</span> tree[strain]:</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">for</span> l <span class="pl-k">in</span> bt2_data:</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> gene <span class="pl-k">==</span> l[<span class="pl-c1">2</span>] <span class="pl-k">and</span> g_cov[gene][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>] <span class="pl-k">&gt;</span> cov_threshold:</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">					length <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">for</span> el <span class="pl-k">in</span> read_cigar(l[<span class="pl-c1">5</span>]):</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">if</span> el[<span class="pl-c1">0</span>] <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>M<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>X<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">							length <span class="pl-k">+=</span> el[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">					det_pos <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">for</span> pos <span class="pl-k">in</span> val_pos[gene]:</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">if</span> pos <span class="pl-k">&lt;=</span> (<span class="pl-c1">int</span>(l[<span class="pl-c1">3</span>]) <span class="pl-k">+</span> length) <span class="pl-k">and</span> pos <span class="pl-k">&gt;=</span> <span class="pl-c1">int</span>(l[<span class="pl-c1">3</span>]):</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">							det_pos.append(pos)</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">					dic <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>read_name<span class="pl-pds">&#39;</span></span>: l[<span class="pl-c1">0</span>],</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">						<span class="pl-s"><span class="pl-pds">&#39;</span>pos<span class="pl-pds">&#39;</span></span>: [l[<span class="pl-c1">3</span>] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>..<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(<span class="pl-c1">int</span>(l[<span class="pl-c1">3</span>]) <span class="pl-k">+</span> length)],</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">						<span class="pl-s"><span class="pl-pds">&#39;</span>CIGAR<span class="pl-pds">&#39;</span></span>: [l[<span class="pl-c1">5</span>]],</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">						<span class="pl-s"><span class="pl-pds">&#39;</span>det_pos<span class="pl-pds">&#39;</span></span>: det_pos}</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">					tree[strain][gene][<span class="pl-s"><span class="pl-pds">&#39;</span>dic<span class="pl-pds">&#39;</span></span>].append(dic)</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">					tree[strain][gene][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> g_cov[gene][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">return</span> tree</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">write_test_result</span>(<span class="pl-smi">tree</span>, <span class="pl-smi">outp</span>):</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">	al_strs <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> s <span class="pl-k">in</span> tree:</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">		check <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> loc <span class="pl-k">in</span> tree[s]:</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> tree[s][loc][<span class="pl-s"><span class="pl-pds">&#39;</span>dic<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> []:</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">				check <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span> check:</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">			al_strs.append(s)</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">with</span> <span class="pl-c1">open</span>(outp,<span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> out:</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> s <span class="pl-k">in</span> al_strs:</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">			out.write(s <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">for</span> loc <span class="pl-k">in</span> tree[s]:</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">				out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\t\t</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> loc <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>  <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(tree[s][loc][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>]) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">for</span> dic <span class="pl-k">in</span> tree[s][loc][<span class="pl-s"><span class="pl-pds">&#39;</span>dic<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">					out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\t\t\t</span>read name: <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> dic[<span class="pl-s"><span class="pl-pds">&#39;</span>read_name<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">					out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\t\t\t</span>position in marker: <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>.join(dic[<span class="pl-s"><span class="pl-pds">&#39;</span>pos<span class="pl-pds">&#39;</span></span>]) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">					out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\t\t\t</span>CIGAR: <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>.join(dic[<span class="pl-s"><span class="pl-pds">&#39;</span>CIGAR<span class="pl-pds">&#39;</span></span>]) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">					out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\t\t\t</span>detected positions (valuable SNPs, deletions and insertions): <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>.join([ <span class="pl-c1">str</span>(n) <span class="pl-k">for</span> n <span class="pl-k">in</span> dic[<span class="pl-s"><span class="pl-pds">&#39;</span>det_pos<span class="pl-pds">&#39;</span></span>]]) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">			out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">write_test_result_short</span>(<span class="pl-smi">tree</span>, <span class="pl-smi">outp</span>):</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">	al_strs <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> s <span class="pl-k">in</span> tree:</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">		check <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> loc <span class="pl-k">in</span> tree[s]:</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> tree[s][loc][<span class="pl-s"><span class="pl-pds">&#39;</span>dic<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> []:</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">				check <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span> check:</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">			al_strs.append(s)</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">with</span> <span class="pl-c1">open</span>(outp,<span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> out:</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> s <span class="pl-k">in</span> al_strs:</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">			out.write(s <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">for</span> loc <span class="pl-k">in</span> tree[s]:</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">				poss <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">for</span> dic <span class="pl-k">in</span> tree[s][loc][<span class="pl-s"><span class="pl-pds">&#39;</span>dic<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">for</span> n <span class="pl-k">in</span> dic[<span class="pl-s"><span class="pl-pds">&#39;</span>det_pos<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">if</span> <span class="pl-c1">str</span>(n) <span class="pl-k">not</span> <span class="pl-k">in</span> poss:</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">							poss.append(<span class="pl-c1">str</span>(n))</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">				out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\t\t</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> loc <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>  <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(tree[s][loc][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>]) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\t\t\t</span>number of reads: <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(<span class="pl-c1">len</span>(tree[s][loc][<span class="pl-s"><span class="pl-pds">&#39;</span>dic<span class="pl-pds">&#39;</span></span>])) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\t\t\t</span>detected val. pos.: <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>.join(poss) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">			out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">diff_in_genes</span>(<span class="pl-smi">bln_xml</span>, <span class="pl-smi">genes_f</span>):</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">	genes_d <span class="pl-k">=</span> read_fasta(genes_f)</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">	blastn <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">	result_handle <span class="pl-k">=</span> <span class="pl-c1">open</span>(bln_xml,<span class="pl-s"><span class="pl-pds">&#39;</span>r<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">	blast_records <span class="pl-k">=</span> <span class="pl-c1">NCBIXML</span>.parse(result_handle)</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> blast_record <span class="pl-k">in</span> blast_records:</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">		blastn[blast_record.query] <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> alignment <span class="pl-k">in</span> blast_record.alignments:</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">			hsp_n <span class="pl-k">=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span> No definition line<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> alignment.title:</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">				al_title <span class="pl-k">=</span> alignment.title[<span class="pl-c1">0</span>:alignment.title.find(<span class="pl-s"><span class="pl-pds">&#39;</span> No definition line<span class="pl-pds">&#39;</span></span>)]</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">				al_title <span class="pl-k">=</span> alignment.title</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">			blastn[blast_record.query][al_title] <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">for</span> hsp <span class="pl-k">in</span> alignment.hsps:</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)] <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">				complement <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> hsp.frame <span class="pl-k">!=</span> ():</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">if</span> hsp.frame[<span class="pl-c1">0</span>] <span class="pl-k">&lt;</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">						complement <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">				seq <span class="pl-k">=</span> genes_d[blast_record.query][hsp.query_start<span class="pl-k">-</span><span class="pl-c1">1</span>:hsp.query_end]</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> complement:</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">					seq <span class="pl-k">=</span> compl(seq)</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)][<span class="pl-s"><span class="pl-pds">&#39;</span>seq<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> seq</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)][<span class="pl-s"><span class="pl-pds">&#39;</span>query_start<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hsp.query_start</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)][<span class="pl-s"><span class="pl-pds">&#39;</span>query_end<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hsp.query_end</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)][<span class="pl-s"><span class="pl-pds">&#39;</span>expect<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hsp.expect</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)][<span class="pl-s"><span class="pl-pds">&#39;</span>score<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hsp.score</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)][<span class="pl-s"><span class="pl-pds">&#39;</span>bits<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hsp.bits</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)][<span class="pl-s"><span class="pl-pds">&#39;</span>num_alignments<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hsp.num_alignments</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)][<span class="pl-s"><span class="pl-pds">&#39;</span>identities<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hsp.identities</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)][<span class="pl-s"><span class="pl-pds">&#39;</span>positives<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hsp.positives</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)][<span class="pl-s"><span class="pl-pds">&#39;</span>gaps<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hsp.gaps</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)][<span class="pl-s"><span class="pl-pds">&#39;</span>strand<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hsp.strand</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)][<span class="pl-s"><span class="pl-pds">&#39;</span>frame<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hsp.frame</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)][<span class="pl-s"><span class="pl-pds">&#39;</span>query<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hsp.query</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)][<span class="pl-s"><span class="pl-pds">&#39;</span>match<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hsp.match</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)][<span class="pl-s"><span class="pl-pds">&#39;</span>sbjct<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hsp.sbjct</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)][<span class="pl-s"><span class="pl-pds">&#39;</span>sbjct_start<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hsp.sbjct_start</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">				blastn[blast_record.query][al_title][<span class="pl-c1">str</span>(hsp_n)][<span class="pl-s"><span class="pl-pds">&#39;</span>sbjct_end<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hsp.sbjct_end</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">				hsp_n <span class="pl-k">=</span> hsp_n <span class="pl-k">+</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">	diff_pos <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> q <span class="pl-k">in</span> blastn.keys():</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">		diff_pos[q] <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> al <span class="pl-k">in</span> blastn[q]:</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> al <span class="pl-k">!=</span> q:</td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">				diff_pos[q][al] <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">				diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>snp<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">				diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>ins<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">				diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>del<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">for</span> hsp <span class="pl-k">in</span> blastn[q][al]:</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">					n <span class="pl-k">=</span> <span class="pl-c1">0</span> <span class="pl-c"><span class="pl-c">#</span>number in match string</span></td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">					delet_num <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">for</span> ch <span class="pl-k">in</span> blastn[q][al][hsp][<span class="pl-s"><span class="pl-pds">&#39;</span>match<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">if</span> ch <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">if</span> blastn[q][al][hsp][<span class="pl-s"><span class="pl-pds">&#39;</span>query<span class="pl-pds">&#39;</span></span>][n:n<span class="pl-k">+</span><span class="pl-c1">1</span>] <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> blastn[q][al][hsp][<span class="pl-s"><span class="pl-pds">&#39;</span>sbjct<span class="pl-pds">&#39;</span></span>][n:n<span class="pl-k">+</span><span class="pl-c1">1</span>] <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">								diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>snp<span class="pl-pds">&#39;</span></span>][blastn[q][al][hsp][<span class="pl-s"><span class="pl-pds">&#39;</span>query_start<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+</span> n <span class="pl-k">-</span> delet_num] <span class="pl-k">=</span> blastn[q][al][hsp][<span class="pl-s"><span class="pl-pds">&#39;</span>query<span class="pl-pds">&#39;</span></span>][n:n<span class="pl-k">+</span><span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-&gt;<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> blastn[q][al][hsp][<span class="pl-s"><span class="pl-pds">&#39;</span>sbjct<span class="pl-pds">&#39;</span></span>][n:n<span class="pl-k">+</span><span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">if</span> blastn[q][al][hsp][<span class="pl-s"><span class="pl-pds">&#39;</span>query<span class="pl-pds">&#39;</span></span>][n:n<span class="pl-k">+</span><span class="pl-c1">1</span>] <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> blastn[q][al][hsp][<span class="pl-s"><span class="pl-pds">&#39;</span>sbjct<span class="pl-pds">&#39;</span></span>][n:n<span class="pl-k">+</span><span class="pl-c1">1</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">								diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>ins<span class="pl-pds">&#39;</span></span>][blastn[q][al][hsp][<span class="pl-s"><span class="pl-pds">&#39;</span>query_start<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+</span> n <span class="pl-k">-</span> delet_num] <span class="pl-k">=</span> blastn[q][al][hsp][<span class="pl-s"><span class="pl-pds">&#39;</span>query<span class="pl-pds">&#39;</span></span>][n:n<span class="pl-k">+</span><span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">if</span> blastn[q][al][hsp][<span class="pl-s"><span class="pl-pds">&#39;</span>query<span class="pl-pds">&#39;</span></span>][n:n<span class="pl-k">+</span><span class="pl-c1">1</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> blastn[q][al][hsp][<span class="pl-s"><span class="pl-pds">&#39;</span>sbjct<span class="pl-pds">&#39;</span></span>][n:n<span class="pl-k">+</span><span class="pl-c1">1</span>] <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">								<span class="pl-k">if</span> blastn[q][al][hsp][<span class="pl-s"><span class="pl-pds">&#39;</span>query_start<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+</span> n <span class="pl-k">-</span> delet_num <span class="pl-k">-</span> <span class="pl-c1">1</span> <span class="pl-k">not</span> <span class="pl-k">in</span> diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>del<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">									diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>del<span class="pl-pds">&#39;</span></span>][blastn[q][al][hsp][<span class="pl-s"><span class="pl-pds">&#39;</span>query_start<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+</span> n <span class="pl-k">-</span> delet_num <span class="pl-k">-</span> <span class="pl-c1">1</span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">								diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>del<span class="pl-pds">&#39;</span></span>][blastn[q][al][hsp][<span class="pl-s"><span class="pl-pds">&#39;</span>query_start<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+</span> n <span class="pl-k">-</span> delet_num <span class="pl-k">-</span> <span class="pl-c1">1</span>] <span class="pl-k">=</span> diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>del<span class="pl-pds">&#39;</span></span>][blastn[q][al][hsp][<span class="pl-s"><span class="pl-pds">&#39;</span>query_start<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+</span> n <span class="pl-k">-</span> delet_num <span class="pl-k">-</span> <span class="pl-c1">1</span>] <span class="pl-k">+</span> blastn[q][al][hsp][<span class="pl-s"><span class="pl-pds">&#39;</span>sbjct<span class="pl-pds">&#39;</span></span>][n:n<span class="pl-k">+</span><span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">								delet_num <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">						n <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">return</span> diff_pos</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">write_diff_pos</span>(<span class="pl-smi">diff_pos</span>, <span class="pl-smi">outp</span>):</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">with</span> <span class="pl-c1">open</span>(outp, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> out:</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> q <span class="pl-k">in</span> diff_pos:</td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">			out.write(q <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">for</span> al <span class="pl-k">in</span> diff_pos[q]:</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">				out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\t</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> al <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>snp<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> {}:</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">					out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\t\t</span>snps:<span class="pl-cce">\n\t\t</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\t\t</span><span class="pl-pds">&#39;</span></span>.join([<span class="pl-c1">str</span>(k) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>snp<span class="pl-pds">&#39;</span></span>][k] <span class="pl-k">for</span> k <span class="pl-k">in</span> <span class="pl-c1">sorted</span>(diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>snp<span class="pl-pds">&#39;</span></span>])]) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>ins<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> {}:</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">					out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\t\t</span>insertions:<span class="pl-cce">\n\t\t</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\t\t</span><span class="pl-pds">&#39;</span></span>.join([<span class="pl-c1">str</span>(k) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>ins<span class="pl-pds">&#39;</span></span>][k] <span class="pl-k">for</span> k <span class="pl-k">in</span> <span class="pl-c1">sorted</span>(diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>ins<span class="pl-pds">&#39;</span></span>])]) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>del<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> {}:</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">					out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\t\t</span>deletions:<span class="pl-cce">\n\t\t</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\t\t</span><span class="pl-pds">&#39;</span></span>.join([<span class="pl-c1">str</span>(k) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>del<span class="pl-pds">&#39;</span></span>][k] <span class="pl-k">for</span> k <span class="pl-k">in</span> <span class="pl-c1">sorted</span>(diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>del<span class="pl-pds">&#39;</span></span>])]) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">genes_snp_ins_positions</span>(<span class="pl-smi">diff_pos</span>):</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">	val_pos <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> q <span class="pl-k">in</span> diff_pos:</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">		val_pos[q] <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> al <span class="pl-k">in</span> diff_pos[q]:</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">for</span> n <span class="pl-k">in</span> diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>snp<span class="pl-pds">&#39;</span></span>].keys() <span class="pl-k">+</span> diff_pos[q][al][<span class="pl-s"><span class="pl-pds">&#39;</span>ins<span class="pl-pds">&#39;</span></span>].keys():</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> n <span class="pl-k">not</span> <span class="pl-k">in</span> val_pos[q]:</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">					val_pos[q].append(n)</td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">		val_pos[q] <span class="pl-k">=</span> <span class="pl-c1">sorted</span>(val_pos[q])</td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">return</span> val_pos</td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">filter_maxerr</span>(<span class="pl-smi">bt2_data</span>, <span class="pl-smi">max_err</span>, <span class="pl-smi">markers_f</span>):</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">	genes_d <span class="pl-k">=</span> read_fasta(markers_f)</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">	bt2_filt_maxerr <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> l <span class="pl-k">in</span> bt2_data:</td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">		name <span class="pl-k">=</span> l[<span class="pl-c1">2</span>]</td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">		marker_pos <span class="pl-k">=</span> <span class="pl-c1">int</span>(l[<span class="pl-c1">3</span>])</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">		cigar <span class="pl-k">=</span> read_cigar(l[<span class="pl-c1">5</span>])</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">		read <span class="pl-k">=</span> l[<span class="pl-c1">9</span>]</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">		read_pos <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">		err <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> el <span class="pl-k">in</span> cigar:</td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> el[<span class="pl-c1">0</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>I<span class="pl-pds">&#39;</span></span> <span class="pl-k">or</span> el[<span class="pl-c1">0</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>D<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">				err <span class="pl-k">=</span> err <span class="pl-k">+</span> el[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> el[<span class="pl-c1">0</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>M<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">for</span> j <span class="pl-k">in</span> <span class="pl-c1">range</span>(el[<span class="pl-c1">1</span>]):</td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">if</span> genes_d[name][marker_pos <span class="pl-k">+</span> j <span class="pl-k">-</span> <span class="pl-c1">1</span>] <span class="pl-k">!=</span> read[read_pos <span class="pl-k">+</span> j]:</td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">						err <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> el[<span class="pl-c1">0</span>] <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>M<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>I<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>S<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>X<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>=<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">				read_pos <span class="pl-k">+=</span> el[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> el[<span class="pl-c1">0</span>] <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>M<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>X<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>D<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>N<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>H<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>P<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>=<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">				marker_pos <span class="pl-k">+=</span> el[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span> err <span class="pl-k">&lt;=</span> max_err:</td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">			bt2_filt_maxerr.append(l)</td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">return</span> bt2_filt_maxerr</td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">filter_valpos</span>(<span class="pl-smi">bt2_data</span>, <span class="pl-smi">val_pos</span>, <span class="pl-smi">val_pos_mismatch</span>, <span class="pl-smi">markers_f</span>):</td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line">	genes_d <span class="pl-k">=</span> read_fasta(markers_f)</td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">	bt2_filt_valpos <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> l <span class="pl-k">in</span> bt2_data:</td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">		cigar <span class="pl-k">=</span> read_cigar(l[<span class="pl-c1">5</span>])</td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">		name <span class="pl-k">=</span> l[<span class="pl-c1">2</span>]</td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">		marker_pos <span class="pl-k">=</span> <span class="pl-c1">int</span>(l[<span class="pl-c1">3</span>])</td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">		read <span class="pl-k">=</span> l[<span class="pl-c1">9</span>]</td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">		detected_val_pos <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">		mismatch_val_pos <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">		read_pos <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> el <span class="pl-k">in</span> cigar:</td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> el[<span class="pl-c1">0</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>M<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">for</span> j <span class="pl-k">in</span> <span class="pl-c1">range</span>(el[<span class="pl-c1">1</span>]):</td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">if</span> marker_pos <span class="pl-k">+</span> j <span class="pl-k">in</span> val_pos[name]:</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">if</span> genes_d[name][marker_pos <span class="pl-k">+</span> j <span class="pl-k">-</span> <span class="pl-c1">1</span>] <span class="pl-k">==</span> read[read_pos <span class="pl-k">+</span> j]:</td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">							detected_val_pos.append(marker_pos <span class="pl-k">+</span> j)</td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">							mismatch_val_pos.append(marker_pos <span class="pl-k">+</span> j)</td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> el[<span class="pl-c1">0</span>] <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>M<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>I<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>S<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>X<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>=<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line">				read_pos <span class="pl-k">+=</span> el[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> el[<span class="pl-c1">0</span>] <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>M<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>X<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>D<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>N<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>H<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>P<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>=<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">				marker_pos <span class="pl-k">+=</span> el[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span> <span class="pl-c1">len</span>(mismatch_val_pos) <span class="pl-k">&lt;=</span> val_pos_mismatch:</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">			bt2_filt_valpos.append(l)</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">return</span> bt2_filt_valpos</td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">write_summary</span>(<span class="pl-smi">sum_path</span>):</td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">with</span> <span class="pl-c1">open</span>(sum_path, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> out:</td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">		al_strs <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> s <span class="pl-k">in</span> tree:</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">			check <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">for</span> loc <span class="pl-k">in</span> tree[s]:</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> tree[s][loc][<span class="pl-s"><span class="pl-pds">&#39;</span>dic<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> []:</td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line">					check <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> check:</td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">				al_strs.append(s)</td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line">		out.write(<span class="pl-s"><span class="pl-pds">&#39;</span>good detected strains<span class="pl-cce">\n\n</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join([s <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> (<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(<span class="pl-c1">len</span>([g <span class="pl-k">for</span> g <span class="pl-k">in</span> tree[s] <span class="pl-k">if</span> tree[s][g][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> <span class="pl-c1">0</span>])) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(<span class="pl-c1">len</span>(tree[s].keys())) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>)<span class="pl-pds">&#39;</span></span> <span class="pl-k">for</span> s <span class="pl-k">in</span> al_strs <span class="pl-k">if</span> s <span class="pl-k">not</span> <span class="pl-k">in</span> chimeras[<span class="pl-s"><span class="pl-pds">&#39;</span>chim_by_genes<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+</span> chimeras[<span class="pl-s"><span class="pl-pds">&#39;</span>chim_by_snps<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+</span> prob_strains]) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\n</span>probable strains<span class="pl-cce">\n\n</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join(s <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> (<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(<span class="pl-c1">len</span>([g <span class="pl-k">for</span> g <span class="pl-k">in</span> tree[s] <span class="pl-k">if</span> tree[s][g][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> <span class="pl-c1">0</span>])) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(<span class="pl-c1">len</span>(tree[s].keys())) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>)<span class="pl-pds">&#39;</span></span> <span class="pl-k">for</span> s <span class="pl-k">in</span> prob_strains) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\n</span>chimeras by genes<span class="pl-cce">\n\n</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span>  <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join([s  <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> (<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(<span class="pl-c1">len</span>([g <span class="pl-k">for</span> g <span class="pl-k">in</span> tree[s] <span class="pl-k">if</span> tree[s][g][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> <span class="pl-c1">0</span>])) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(<span class="pl-c1">len</span>(tree[s].keys())) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>)<span class="pl-pds">&#39;</span></span> <span class="pl-k">for</span> s <span class="pl-k">in</span> chimeras[<span class="pl-s"><span class="pl-pds">&#39;</span>chim_by_genes<span class="pl-pds">&#39;</span></span>]]) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\n</span>chimeras by snps<span class="pl-cce">\n\n</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span>  <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join([s <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> (<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(<span class="pl-c1">len</span>([g <span class="pl-k">for</span> g <span class="pl-k">in</span> tree[s] <span class="pl-k">if</span> tree[s][g][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> <span class="pl-c1">0</span>])) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(<span class="pl-c1">len</span>(tree[s].keys())) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>)<span class="pl-pds">&#39;</span></span> <span class="pl-k">for</span> s <span class="pl-k">in</span> chimeras[<span class="pl-s"><span class="pl-pds">&#39;</span>chim_by_snps<span class="pl-pds">&#39;</span></span>]]))</td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">make_gene_matrix</span>(<span class="pl-smi">diff_pos</span>, <span class="pl-smi">tree</span>, <span class="pl-smi">outp</span>):</td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">	genes_pos <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> st <span class="pl-k">in</span> tree:</td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> g <span class="pl-k">in</span> tree[st]:</td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> tree[st][g][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line">				poss <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">for</span> dic <span class="pl-k">in</span> tree[st][g][<span class="pl-s"><span class="pl-pds">&#39;</span>dic<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">for</span> n <span class="pl-k">in</span> dic[<span class="pl-s"><span class="pl-pds">&#39;</span>det_pos<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">if</span> n <span class="pl-k">not</span> <span class="pl-k">in</span> poss:</td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line">							poss.append(n)</td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line">				genes_pos[g] <span class="pl-k">=</span> poss</td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line">	g_mat <span class="pl-k">=</span> {g1:{g2:<span class="pl-c1">0</span> <span class="pl-k">for</span> g2 <span class="pl-k">in</span> genes_pos.keys()} <span class="pl-k">for</span> g1 <span class="pl-k">in</span> genes_pos.keys()}</td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> g1 <span class="pl-k">in</span> genes_pos.keys():</td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> g2 <span class="pl-k">in</span> genes_pos.keys():</td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> g2 <span class="pl-k">in</span> diff_pos[g1].keys():</td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line">				t_pos <span class="pl-k">=</span> diff_pos[g1][g2][<span class="pl-s"><span class="pl-pds">&#39;</span>snp<span class="pl-pds">&#39;</span></span>].keys() <span class="pl-k">+</span> diff_pos[g1][g2][<span class="pl-s"><span class="pl-pds">&#39;</span>ins<span class="pl-pds">&#39;</span></span>].keys() <span class="pl-k">+</span> diff_pos[g1][g2][<span class="pl-s"><span class="pl-pds">&#39;</span>del<span class="pl-pds">&#39;</span></span>].keys()</td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">				check <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">for</span> p <span class="pl-k">in</span> t_pos:</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">if</span> p <span class="pl-k">in</span> genes_pos[g1]:</td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line">						check <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> <span class="pl-k">not</span> check:</td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">					g_mat[g1][g2] <span class="pl-k">=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> g1 <span class="pl-k">==</span> g2:</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line">				g_mat[g1][g2] <span class="pl-k">=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line">	<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join(g_mat.keys())</td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line">	<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>.join(<span class="pl-c1">str</span>(n) <span class="pl-k">for</span> n <span class="pl-k">in</span> g_mat[l].values()) <span class="pl-k">for</span> l <span class="pl-k">in</span> g_mat.keys())</td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">with</span> <span class="pl-c1">open</span>(outp, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> out:</td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line">		out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join(g_mat.keys()) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line">		out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>.join(<span class="pl-c1">str</span>(n) <span class="pl-k">for</span> n <span class="pl-k">in</span> g_mat[l].values()) <span class="pl-k">for</span> l <span class="pl-k">in</span> g_mat.keys()))</td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">return</span> g_mat</td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">make_strain_matrix</span>(<span class="pl-smi">tree</span>, <span class="pl-smi">g_mat</span>, <span class="pl-smi">outp</span>):</td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">	st_detgene <span class="pl-k">=</span> {} <span class="pl-c"><span class="pl-c">#</span>dictionary that contains strains and detected genes (only strains that have detected genes)</span></td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> st <span class="pl-k">in</span> tree:</td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line">		check <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line">		genes <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> g <span class="pl-k">in</span> tree[st]:</td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> tree[st][g][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line">				check <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line">				genes.append(g)</td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span> check:</td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line">			st_detgene[st] <span class="pl-k">=</span> genes</td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line">	st_mat <span class="pl-k">=</span> {st1 : {st2 : <span class="pl-c1">0</span> <span class="pl-k">for</span> st2 <span class="pl-k">in</span> st_detgene.keys()} <span class="pl-k">for</span> st1 <span class="pl-k">in</span> st_detgene.keys()}</td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> st1 <span class="pl-k">in</span> st_detgene.keys():</td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> st2 <span class="pl-k">in</span> st_detgene.keys():</td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line">			check_st <span class="pl-k">=</span> <span class="pl-c1">True</span> <span class="pl-c"><span class="pl-c">#</span>true if st1 can&#39;t be distinguished from st2</span></td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">for</span> g1 <span class="pl-k">in</span> st_detgene[st1]:</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line">				check_gene <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">for</span> g2 <span class="pl-k">in</span> st_detgene[st2]:</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">if</span> g_mat[g1][g2] <span class="pl-k">==</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line">						check_gene <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> <span class="pl-k">not</span> check_gene:</td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line">					check_st <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> check_st <span class="pl-k">and</span> <span class="pl-c1">len</span>(st_detgene[st2]) <span class="pl-k">&gt;=</span> <span class="pl-c1">len</span>(st_detgene[st1]):</td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line">				st_mat[st1][st2] <span class="pl-k">=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line">	<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join(st_mat.keys())</td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code blob-code-inner js-file-line">	<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>.join(<span class="pl-c1">str</span>(n) <span class="pl-k">for</span> n <span class="pl-k">in</span> st_mat[l].values()) <span class="pl-k">for</span> l <span class="pl-k">in</span> st_mat.keys())</td>
      </tr>
      <tr>
        <td id="L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="LC434" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">with</span> <span class="pl-c1">open</span>(outp, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> out:</td>
      </tr>
      <tr>
        <td id="L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="LC435" class="blob-code blob-code-inner js-file-line">		out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join(st_mat.keys()) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="LC436" class="blob-code blob-code-inner js-file-line">		out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>.join(<span class="pl-c1">str</span>(n) <span class="pl-k">for</span> n <span class="pl-k">in</span> st_mat[l].values()) <span class="pl-k">for</span> l <span class="pl-k">in</span> st_mat.keys()))</td>
      </tr>
      <tr>
        <td id="L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="LC437" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">return</span> st_mat</td>
      </tr>
      <tr>
        <td id="L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="LC438" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="LC439" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">sort_by_representation</span>(<span class="pl-smi">st_mat</span>):</td>
      </tr>
      <tr>
        <td id="L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="LC440" class="blob-code blob-code-inner js-file-line">	sts <span class="pl-k">=</span> st_mat.keys()</td>
      </tr>
      <tr>
        <td id="L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="LC441" class="blob-code blob-code-inner js-file-line">	groups <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="LC442" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">while</span> <span class="pl-c1">len</span>(sts) <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="LC443" class="blob-code blob-code-inner js-file-line">		gr <span class="pl-k">=</span> [sts[<span class="pl-c1">0</span>]]</td>
      </tr>
      <tr>
        <td id="L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="LC444" class="blob-code blob-code-inner js-file-line">		sts.remove(sts[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="LC445" class="blob-code blob-code-inner js-file-line">		check <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L446" class="blob-num js-line-number" data-line-number="446"></td>
        <td id="LC446" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">while</span> check:</td>
      </tr>
      <tr>
        <td id="L447" class="blob-num js-line-number" data-line-number="447"></td>
        <td id="LC447" class="blob-code blob-code-inner js-file-line">			check <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L448" class="blob-num js-line-number" data-line-number="448"></td>
        <td id="LC448" class="blob-code blob-code-inner js-file-line">			gr1 <span class="pl-k">=</span> gr</td>
      </tr>
      <tr>
        <td id="L449" class="blob-num js-line-number" data-line-number="449"></td>
        <td id="LC449" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">for</span> st1 <span class="pl-k">in</span> gr:</td>
      </tr>
      <tr>
        <td id="L450" class="blob-num js-line-number" data-line-number="450"></td>
        <td id="LC450" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">for</span> st2 <span class="pl-k">in</span> [st <span class="pl-k">for</span> st <span class="pl-k">in</span> st_mat <span class="pl-k">if</span> st_mat[st1][st] <span class="pl-k">==</span> <span class="pl-c1">1</span>]:</td>
      </tr>
      <tr>
        <td id="L451" class="blob-num js-line-number" data-line-number="451"></td>
        <td id="LC451" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">if</span> st2 <span class="pl-k">not</span> <span class="pl-k">in</span> gr1:</td>
      </tr>
      <tr>
        <td id="L452" class="blob-num js-line-number" data-line-number="452"></td>
        <td id="LC452" class="blob-code blob-code-inner js-file-line">						gr1.append(st2)</td>
      </tr>
      <tr>
        <td id="L453" class="blob-num js-line-number" data-line-number="453"></td>
        <td id="LC453" class="blob-code blob-code-inner js-file-line">						sts.remove(st2)</td>
      </tr>
      <tr>
        <td id="L454" class="blob-num js-line-number" data-line-number="454"></td>
        <td id="LC454" class="blob-code blob-code-inner js-file-line">						check <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L455" class="blob-num js-line-number" data-line-number="455"></td>
        <td id="LC455" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">for</span> st2 <span class="pl-k">in</span> [st <span class="pl-k">for</span> st <span class="pl-k">in</span> st_mat <span class="pl-k">if</span> st_mat[st][st1] <span class="pl-k">==</span> <span class="pl-c1">1</span>]:</td>
      </tr>
      <tr>
        <td id="L456" class="blob-num js-line-number" data-line-number="456"></td>
        <td id="LC456" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">if</span> st2 <span class="pl-k">not</span> <span class="pl-k">in</span> gr1:</td>
      </tr>
      <tr>
        <td id="L457" class="blob-num js-line-number" data-line-number="457"></td>
        <td id="LC457" class="blob-code blob-code-inner js-file-line">						gr1.append(st2)</td>
      </tr>
      <tr>
        <td id="L458" class="blob-num js-line-number" data-line-number="458"></td>
        <td id="LC458" class="blob-code blob-code-inner js-file-line">						sts.remove(st2)</td>
      </tr>
      <tr>
        <td id="L459" class="blob-num js-line-number" data-line-number="459"></td>
        <td id="LC459" class="blob-code blob-code-inner js-file-line">						check <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L460" class="blob-num js-line-number" data-line-number="460"></td>
        <td id="LC460" class="blob-code blob-code-inner js-file-line">			gr <span class="pl-k">=</span> gr1</td>
      </tr>
      <tr>
        <td id="L461" class="blob-num js-line-number" data-line-number="461"></td>
        <td id="LC461" class="blob-code blob-code-inner js-file-line">		groups.append(gr)</td>
      </tr>
      <tr>
        <td id="L462" class="blob-num js-line-number" data-line-number="462"></td>
        <td id="LC462" class="blob-code blob-code-inner js-file-line">	st_repr <span class="pl-k">=</span> [] <span class="pl-c"><span class="pl-c">#</span>this list contains dictionaries, each dictionary contains strain:privilegy (0 - the best, higher - worse), privelegy = number of strains, from which this strain can&#39;t be destingiushed</span></td>
      </tr>
      <tr>
        <td id="L463" class="blob-num js-line-number" data-line-number="463"></td>
        <td id="LC463" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">for</span> g <span class="pl-k">in</span> groups:</td>
      </tr>
      <tr>
        <td id="L464" class="blob-num js-line-number" data-line-number="464"></td>
        <td id="LC464" class="blob-code blob-code-inner js-file-line">		st_repr.append( {st:<span class="pl-c1">len</span>([s <span class="pl-k">for</span> s <span class="pl-k">in</span> st_mat <span class="pl-k">if</span> st_mat[st][s] <span class="pl-k">==</span> <span class="pl-c1">1</span>]) <span class="pl-k">-</span> <span class="pl-c1">1</span> <span class="pl-k">for</span> st <span class="pl-k">in</span> g} )</td>
      </tr>
      <tr>
        <td id="L465" class="blob-num js-line-number" data-line-number="465"></td>
        <td id="LC465" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">return</span> st_repr</td>
      </tr>
      <tr>
        <td id="L466" class="blob-num js-line-number" data-line-number="466"></td>
        <td id="LC466" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L467" class="blob-num js-line-number" data-line-number="467"></td>
        <td id="LC467" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L468" class="blob-num js-line-number" data-line-number="468"></td>
        <td id="LC468" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">write_summary</span>(<span class="pl-smi">st_repr</span>, <span class="pl-smi">tree</span>, <span class="pl-smi">genes_f</span>, <span class="pl-smi">out_f</span>):</td>
      </tr>
      <tr>
        <td id="L469" class="blob-num js-line-number" data-line-number="469"></td>
        <td id="LC469" class="blob-code blob-code-inner js-file-line">	seqs <span class="pl-k">=</span> read_fasta(genes_f)</td>
      </tr>
      <tr>
        <td id="L470" class="blob-num js-line-number" data-line-number="470"></td>
        <td id="LC470" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">with</span> <span class="pl-c1">open</span>(out_f, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> out:</td>
      </tr>
      <tr>
        <td id="L471" class="blob-num js-line-number" data-line-number="471"></td>
        <td id="LC471" class="blob-code blob-code-inner js-file-line">		out.write(<span class="pl-s"><span class="pl-pds">&#39;</span>[strain] [n1]/[n0] [cov_1, cov_2, ...] [p]<span class="pl-cce">\n</span>n1 - number of detected genetic markers<span class="pl-cce">\n</span>n0 - number of all genetic markers<span class="pl-cce">\n</span>cov_i - coverage of genetic marker number i<span class="pl-cce">\n</span>p - privelegy, number of strain from which this strain can not be distinguished<span class="pl-cce">\n\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L472" class="blob-num js-line-number" data-line-number="472"></td>
        <td id="LC472" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> dic <span class="pl-k">in</span> st_repr:</td>
      </tr>
      <tr>
        <td id="L473" class="blob-num js-line-number" data-line-number="473"></td>
        <td id="LC473" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">for</span> st <span class="pl-k">in</span> dic.keys():</td>
      </tr>
      <tr>
        <td id="L474" class="blob-num js-line-number" data-line-number="474"></td>
        <td id="LC474" class="blob-code blob-code-inner js-file-line">				n1 <span class="pl-k">=</span> <span class="pl-c1">str</span>(<span class="pl-c1">len</span>([g <span class="pl-k">for</span> g <span class="pl-k">in</span> tree[st].keys() <span class="pl-k">if</span> tree[st][g][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> <span class="pl-c1">0</span>]))</td>
      </tr>
      <tr>
        <td id="L475" class="blob-num js-line-number" data-line-number="475"></td>
        <td id="LC475" class="blob-code blob-code-inner js-file-line">				n0 <span class="pl-k">=</span> <span class="pl-c1">str</span>(<span class="pl-c1">len</span>(tree[st].keys()))</td>
      </tr>
      <tr>
        <td id="L476" class="blob-num js-line-number" data-line-number="476"></td>
        <td id="LC476" class="blob-code blob-code-inner js-file-line">				covs <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>, <span class="pl-pds">&#39;</span></span>.join([<span class="pl-c1">str</span>(tree[st][g][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>]) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(<span class="pl-c1">len</span>(seqs[g])) <span class="pl-k">for</span> g <span class="pl-k">in</span> tree[st].keys() <span class="pl-k">if</span> tree[st][g][<span class="pl-s"><span class="pl-pds">&#39;</span>cov<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> <span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L477" class="blob-num js-line-number" data-line-number="477"></td>
        <td id="LC477" class="blob-code blob-code-inner js-file-line">				out.write(st <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> n1 <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> n0 <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> [<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> covs <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>] <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(dic[st]) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L478" class="blob-num js-line-number" data-line-number="478"></td>
        <td id="LC478" class="blob-code blob-code-inner js-file-line">			out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L479" class="blob-num js-line-number" data-line-number="479"></td>
        <td id="LC479" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L480" class="blob-num js-line-number" data-line-number="480"></td>
        <td id="LC480" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L481" class="blob-num js-line-number" data-line-number="481"></td>
        <td id="LC481" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>__main__<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L482" class="blob-num js-line-number" data-line-number="482"></td>
        <td id="LC482" class="blob-code blob-code-inner js-file-line">	pars <span class="pl-k">=</span> read_params(sys.argv)</td>
      </tr>
      <tr>
        <td id="L483" class="blob-num js-line-number" data-line-number="483"></td>
        <td id="LC483" class="blob-code blob-code-inner js-file-line">	marker_f <span class="pl-k">=</span> pars[<span class="pl-s"><span class="pl-pds">&#39;</span>marf<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L484" class="blob-num js-line-number" data-line-number="484"></td>
        <td id="LC484" class="blob-code blob-code-inner js-file-line">	fastq_f <span class="pl-k">=</span> pars[<span class="pl-s"><span class="pl-pds">&#39;</span>metaf<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L485" class="blob-num js-line-number" data-line-number="485"></td>
        <td id="LC485" class="blob-code blob-code-inner js-file-line">	N <span class="pl-k">=</span> pars[<span class="pl-s"><span class="pl-pds">&#39;</span>nproc<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L486" class="blob-num js-line-number" data-line-number="486"></td>
        <td id="LC486" class="blob-code blob-code-inner js-file-line">	preset <span class="pl-k">=</span> pars[<span class="pl-s"><span class="pl-pds">&#39;</span>bt2_ps<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L487" class="blob-num js-line-number" data-line-number="487"></td>
        <td id="LC487" class="blob-code blob-code-inner js-file-line">	e_val <span class="pl-k">=</span> pars[<span class="pl-s"><span class="pl-pds">&#39;</span>evalue<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L488" class="blob-num js-line-number" data-line-number="488"></td>
        <td id="LC488" class="blob-code blob-code-inner js-file-line">	max_err <span class="pl-k">=</span> pars[<span class="pl-s"><span class="pl-pds">&#39;</span>max_err<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L489" class="blob-num js-line-number" data-line-number="489"></td>
        <td id="LC489" class="blob-code blob-code-inner js-file-line">	val_pos_mismatch <span class="pl-k">=</span> pars[<span class="pl-s"><span class="pl-pds">&#39;</span>val_pos_mismatch<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L490" class="blob-num js-line-number" data-line-number="490"></td>
        <td id="LC490" class="blob-code blob-code-inner js-file-line">	gene_cov_threshold <span class="pl-k">=</span> pars[<span class="pl-s"><span class="pl-pds">&#39;</span>gene_cov<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L491" class="blob-num js-line-number" data-line-number="491"></td>
        <td id="LC491" class="blob-code blob-code-inner js-file-line">	out_fol <span class="pl-k">=</span> pars[<span class="pl-s"><span class="pl-pds">&#39;</span>out_fol<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L492" class="blob-num js-line-number" data-line-number="492"></td>
        <td id="LC492" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L493" class="blob-num js-line-number" data-line-number="493"></td>
        <td id="LC493" class="blob-code blob-code-inner js-file-line">	mypath <span class="pl-k">=</span> os.getcwd()</td>
      </tr>
      <tr>
        <td id="L494" class="blob-num js-line-number" data-line-number="494"></td>
        <td id="LC494" class="blob-code blob-code-inner js-file-line">	folders <span class="pl-k">=</span> [f <span class="pl-k">for</span> f <span class="pl-k">in</span> listdir(mypath) <span class="pl-k">if</span> <span class="pl-k">not</span> isfile(join(mypath,f))]</td>
      </tr>
      <tr>
        <td id="L495" class="blob-num js-line-number" data-line-number="495"></td>
        <td id="LC495" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> out_fol <span class="pl-k">not</span> <span class="pl-k">in</span> folders:</td>
      </tr>
      <tr>
        <td id="L496" class="blob-num js-line-number" data-line-number="496"></td>
        <td id="LC496" class="blob-code blob-code-inner js-file-line">		os.mkdir(out_fol)</td>
      </tr>
      <tr>
        <td id="L497" class="blob-num js-line-number" data-line-number="497"></td>
        <td id="LC497" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L498" class="blob-num js-line-number" data-line-number="498"></td>
        <td id="LC498" class="blob-code blob-code-inner js-file-line">		shutil.rmtree(out_fol)</td>
      </tr>
      <tr>
        <td id="L499" class="blob-num js-line-number" data-line-number="499"></td>
        <td id="LC499" class="blob-code blob-code-inner js-file-line">		os.mkdir(out_fol)</td>
      </tr>
      <tr>
        <td id="L500" class="blob-num js-line-number" data-line-number="500"></td>
        <td id="LC500" class="blob-code blob-code-inner js-file-line">	make_tree_file(marker_f, out_fol)</td>
      </tr>
      <tr>
        <td id="L501" class="blob-num js-line-number" data-line-number="501"></td>
        <td id="LC501" class="blob-code blob-code-inner js-file-line">	make_seq_file(marker_f, out_fol)</td>
      </tr>
      <tr>
        <td id="L502" class="blob-num js-line-number" data-line-number="502"></td>
        <td id="LC502" class="blob-code blob-code-inner js-file-line">	os.mkdir(out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/blast<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L503" class="blob-num js-line-number" data-line-number="503"></td>
        <td id="LC503" class="blob-code blob-code-inner js-file-line">	os.mkdir(out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/blast/db<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L504" class="blob-num js-line-number" data-line-number="504"></td>
        <td id="LC504" class="blob-code blob-code-inner js-file-line">	subprocess.call([<span class="pl-s"><span class="pl-pds">&#39;</span>dustmasker<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-in<span class="pl-pds">&#39;</span></span>, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/markers.fasta<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-infmt<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>fasta<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-parse_seqids<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-outfmt<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>maskinfo_asn1_bin<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-out<span class="pl-pds">&#39;</span></span>, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/blast/db/genes.asnb<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L505" class="blob-num js-line-number" data-line-number="505"></td>
        <td id="LC505" class="blob-code blob-code-inner js-file-line">	subprocess.call([<span class="pl-s"><span class="pl-pds">&#39;</span>makeblastdb<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-in<span class="pl-pds">&#39;</span></span>, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/markers.fasta<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-input_type<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>fasta<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-dbtype<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>nucl<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-parse_seqids<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-mask_data<span class="pl-pds">&#39;</span></span>, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/blast/db/genes.asnb<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-out<span class="pl-pds">&#39;</span></span>, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/blast/db/genes<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-title<span class="pl-pds">&#39;</span></span>, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/blast/db/genes<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L506" class="blob-num js-line-number" data-line-number="506"></td>
        <td id="LC506" class="blob-code blob-code-inner js-file-line">	blastn_cline <span class="pl-k">=</span> NcbiblastnCommandline(<span class="pl-v">query</span><span class="pl-k">=</span> out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/markers.fasta<span class="pl-pds">&#39;</span></span>, <span class="pl-v">out</span><span class="pl-k">=</span> out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/blast/all_to_all.txt<span class="pl-pds">&#39;</span></span>, <span class="pl-v">outfmt</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">num_threads</span> <span class="pl-k">=</span> <span class="pl-c1">4</span>, <span class="pl-v">db</span> <span class="pl-k">=</span> out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/blast/db/genes<span class="pl-pds">&#39;</span></span>, <span class="pl-v">evalue</span> <span class="pl-k">=</span> e_val)</td>
      </tr>
      <tr>
        <td id="L507" class="blob-num js-line-number" data-line-number="507"></td>
        <td id="LC507" class="blob-code blob-code-inner js-file-line">	os.system(<span class="pl-c1">str</span>(blastn_cline))</td>
      </tr>
      <tr>
        <td id="L508" class="blob-num js-line-number" data-line-number="508"></td>
        <td id="LC508" class="blob-code blob-code-inner js-file-line">	blastn_cline <span class="pl-k">=</span> NcbiblastnCommandline(<span class="pl-v">query</span><span class="pl-k">=</span> out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/markers.fasta<span class="pl-pds">&#39;</span></span>, <span class="pl-v">out</span><span class="pl-k">=</span> out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/blast/all_to_all.xml<span class="pl-pds">&#39;</span></span>, <span class="pl-v">outfmt</span><span class="pl-k">=</span><span class="pl-c1">5</span>, <span class="pl-v">num_threads</span> <span class="pl-k">=</span> <span class="pl-c1">4</span>, <span class="pl-v">db</span> <span class="pl-k">=</span> out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/blast/db/genes<span class="pl-pds">&#39;</span></span>, <span class="pl-v">evalue</span> <span class="pl-k">=</span> e_val)</td>
      </tr>
      <tr>
        <td id="L509" class="blob-num js-line-number" data-line-number="509"></td>
        <td id="LC509" class="blob-code blob-code-inner js-file-line">	os.system(<span class="pl-c1">str</span>(blastn_cline))</td>
      </tr>
      <tr>
        <td id="L510" class="blob-num js-line-number" data-line-number="510"></td>
        <td id="LC510" class="blob-code blob-code-inner js-file-line">	diff_pos <span class="pl-k">=</span> diff_in_genes(out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/blast/all_to_all.xml<span class="pl-pds">&#39;</span></span>, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/markers.fasta<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L511" class="blob-num js-line-number" data-line-number="511"></td>
        <td id="LC511" class="blob-code blob-code-inner js-file-line">	write_diff_pos(diff_pos, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/genes_vs_genes_differences.txt<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L512" class="blob-num js-line-number" data-line-number="512"></td>
        <td id="LC512" class="blob-code blob-code-inner js-file-line">	val_pos <span class="pl-k">=</span> genes_snp_ins_positions(diff_pos)</td>
      </tr>
      <tr>
        <td id="L513" class="blob-num js-line-number" data-line-number="513"></td>
        <td id="LC513" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">with</span> <span class="pl-c1">open</span>(out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/genes_snp_ins_positions.txt<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> out:</td>
      </tr>
      <tr>
        <td id="L514" class="blob-num js-line-number" data-line-number="514"></td>
        <td id="LC514" class="blob-code blob-code-inner js-file-line">		out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join([name <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>: <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>, <span class="pl-pds">&#39;</span></span>.join([<span class="pl-c1">str</span>(i) <span class="pl-k">for</span> i <span class="pl-k">in</span> val_pos[name]]) <span class="pl-k">for</span> name <span class="pl-k">in</span> val_pos.keys()]))</td>
      </tr>
      <tr>
        <td id="L515" class="blob-num js-line-number" data-line-number="515"></td>
        <td id="LC515" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L516" class="blob-num js-line-number" data-line-number="516"></td>
        <td id="LC516" class="blob-code blob-code-inner js-file-line">	os.mkdir(out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/bowtie2_db<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L517" class="blob-num js-line-number" data-line-number="517"></td>
        <td id="LC517" class="blob-code blob-code-inner js-file-line">	subprocess.call([<span class="pl-s"><span class="pl-pds">&#39;</span>bowtie2-build<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-f<span class="pl-pds">&#39;</span></span>, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/markers.fasta<span class="pl-pds">&#39;</span></span>, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/bowtie2_db/bt2_db<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L518" class="blob-num js-line-number" data-line-number="518"></td>
        <td id="LC518" class="blob-code blob-code-inner js-file-line">	bowtie2_db <span class="pl-k">=</span> out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/bowtie2_db/bt2_db<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L519" class="blob-num js-line-number" data-line-number="519"></td>
        <td id="LC519" class="blob-code blob-code-inner js-file-line">	subprocess.call([<span class="pl-s"><span class="pl-pds">&#39;</span>bowtie2<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>--quiet<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>--sam-no-hd<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>--sam-no-sq<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>--<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> preset, <span class="pl-s"><span class="pl-pds">&#39;</span>-x<span class="pl-pds">&#39;</span></span>, bowtie2_db, <span class="pl-s"><span class="pl-pds">&#39;</span>-U<span class="pl-pds">&#39;</span></span>, fastq_f,</td>
      </tr>
      <tr>
        <td id="L520" class="blob-num js-line-number" data-line-number="520"></td>
        <td id="LC520" class="blob-code blob-code-inner js-file-line">			<span class="pl-s"><span class="pl-pds">&#39;</span>-S<span class="pl-pds">&#39;</span></span>, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/bt2_output<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-p<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">str</span>(N), <span class="pl-s"><span class="pl-pds">&#39;</span>-a<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L521" class="blob-num js-line-number" data-line-number="521"></td>
        <td id="LC521" class="blob-code blob-code-inner js-file-line">	bt2_data <span class="pl-k">=</span> [l.strip().split(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\t</span><span class="pl-pds">&#39;</span></span>) <span class="pl-k">for</span> l <span class="pl-k">in</span> <span class="pl-c1">open</span>(out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/bt2_output<span class="pl-pds">&#39;</span></span>) <span class="pl-k">if</span> l.strip().split(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\t</span><span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">2</span>][<span class="pl-k">-</span><span class="pl-c1">1</span>] <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>*<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L522" class="blob-num js-line-number" data-line-number="522"></td>
        <td id="LC522" class="blob-code blob-code-inner js-file-line">	bt2_filt_maxerr <span class="pl-k">=</span> filter_maxerr(bt2_data, max_err, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/markers.fasta<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L523" class="blob-num js-line-number" data-line-number="523"></td>
        <td id="LC523" class="blob-code blob-code-inner js-file-line">	bt2_filt_valpos <span class="pl-k">=</span> filter_valpos(bt2_filt_maxerr, val_pos, val_pos_mismatch, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/markers.fasta<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L524" class="blob-num js-line-number" data-line-number="524"></td>
        <td id="LC524" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">with</span> <span class="pl-c1">open</span>(out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/bt2_filtered<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>.sam<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> out:</td>
      </tr>
      <tr>
        <td id="L525" class="blob-num js-line-number" data-line-number="525"></td>
        <td id="LC525" class="blob-code blob-code-inner js-file-line">		out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join([<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\t</span><span class="pl-pds">&#39;</span></span>.join(l) <span class="pl-k">for</span> l <span class="pl-k">in</span> bt2_filt_valpos]))</td>
      </tr>
      <tr>
        <td id="L526" class="blob-num js-line-number" data-line-number="526"></td>
        <td id="LC526" class="blob-code blob-code-inner js-file-line">	os.remove(out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/bt2_output<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L527" class="blob-num js-line-number" data-line-number="527"></td>
        <td id="LC527" class="blob-code blob-code-inner js-file-line">	g_cov <span class="pl-k">=</span> bt2_gene_coverage(bt2_filt_valpos, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/markers.fasta<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L528" class="blob-num js-line-number" data-line-number="528"></td>
        <td id="LC528" class="blob-code blob-code-inner js-file-line">	write_g_cov(g_cov, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/markers.fasta<span class="pl-pds">&#39;</span></span>, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/gene_coverage.txt<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L529" class="blob-num js-line-number" data-line-number="529"></td>
        <td id="LC529" class="blob-code blob-code-inner js-file-line">	tree <span class="pl-k">=</span> read_tree(out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/tree<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L530" class="blob-num js-line-number" data-line-number="530"></td>
        <td id="LC530" class="blob-code blob-code-inner js-file-line">	suppl_tree(tree, bt2_filt_valpos, g_cov, gene_cov_threshold)</td>
      </tr>
      <tr>
        <td id="L531" class="blob-num js-line-number" data-line-number="531"></td>
        <td id="LC531" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L532" class="blob-num js-line-number" data-line-number="532"></td>
        <td id="LC532" class="blob-code blob-code-inner js-file-line">	write_test_result(tree, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/test_results.txt<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L533" class="blob-num js-line-number" data-line-number="533"></td>
        <td id="LC533" class="blob-code blob-code-inner js-file-line">	write_test_result_short(tree, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/test_results_short.txt<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L534" class="blob-num js-line-number" data-line-number="534"></td>
        <td id="LC534" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L535" class="blob-num js-line-number" data-line-number="535"></td>
        <td id="LC535" class="blob-code blob-code-inner js-file-line">	g_mat <span class="pl-k">=</span> make_gene_matrix(diff_pos, tree, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/gene_matrix.txt<span class="pl-pds">&#39;</span></span>) <span class="pl-c"><span class="pl-c">#</span> matrix with gene vs gene differences</span></td>
      </tr>
      <tr>
        <td id="L536" class="blob-num js-line-number" data-line-number="536"></td>
        <td id="LC536" class="blob-code blob-code-inner js-file-line">	<span class="pl-c"><span class="pl-c">#</span>g_mat[g1][g2] = 1 means that g1 can not be distinguished from g2 (0 if can be distinduished)</span></td>
      </tr>
      <tr>
        <td id="L537" class="blob-num js-line-number" data-line-number="537"></td>
        <td id="LC537" class="blob-code blob-code-inner js-file-line">	st_mat <span class="pl-k">=</span> make_strain_matrix(tree, g_mat, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/strain_matrix.txt<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L538" class="blob-num js-line-number" data-line-number="538"></td>
        <td id="LC538" class="blob-code blob-code-inner js-file-line">	st_repr <span class="pl-k">=</span> sort_by_representation(st_mat)</td>
      </tr>
      <tr>
        <td id="L539" class="blob-num js-line-number" data-line-number="539"></td>
        <td id="LC539" class="blob-code blob-code-inner js-file-line">	write_summary(st_repr, tree, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/markers.fasta<span class="pl-pds">&#39;</span></span>, out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/summary.txt<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L540" class="blob-num js-line-number" data-line-number="540"></td>
        <td id="LC540" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">with</span> <span class="pl-c1">open</span>(out_fol <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/privilegy.txt<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> out:</td>
      </tr>
      <tr>
        <td id="L541" class="blob-num js-line-number" data-line-number="541"></td>
        <td id="LC541" class="blob-code blob-code-inner js-file-line">		out.write(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n\n</span><span class="pl-pds">&#39;</span></span>.join(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join(st <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>: <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(dic[st]) <span class="pl-k">for</span> st <span class="pl-k">in</span> dic.keys()) <span class="pl-k">for</span> dic <span class="pl-k">in</span> st_repr))</td>
      </tr>
</table>

  <details class="details-reset details-overlay BlobToolbar position-absolute js-file-line-actions dropdown d-none" aria-hidden="true">
    <summary class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1" aria-label="Inline file action toolbar">
      <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 13 16" version="1.1" width="13" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zm5 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM13 7.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/></svg>
    </summary>
    <details-menu>
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2">
        <li><clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-lines" style="cursor:pointer;" data-original-text="Copy lines">Copy lines</clipboard-copy></li>
        <li><clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;" data-original-text="Copy permalink">Copy permalink</clipboard-copy></li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" role="menuitem" href="/LabGenMO/TAGMA/blame/37ba3a7237c9ea75b28603ada8a57891cbc2c27c/bt2_snp_11.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" role="menuitem" href="/LabGenMO/TAGMA/issues/new">Open new issue</a></li>
      </ul>
    </details-menu>
  </details>

  </div>

    </div>

  

  <details class="details-reset details-overlay details-overlay-dark">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>


  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

        
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2018 <span title="0.28725s from unicorn-74954c4d44-trxqp">GitHub</span>, Inc.</li>
        <li class="mr-3"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3"><a href="/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3"><a href="https://blog.github.com" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    
    <script crossorigin="anonymous" integrity="sha512-Ax8so2RYXS5IplklIjBUPCs/H8jumancM4AKLTR35EuK3eUxGRyo1EkTBkTQnSUzk5ZQ9pYsHYLJ1ImS2Fcerg==" type="application/javascript" src="https://assets-cdn.github.com/assets/frameworks-755e0c008571c9f249a478f4cda76ecf.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-qggDJEZ3OB7G2oJ1fGvN9VRp3Tf1faPXSByOj7GlCkU6k3Ml7wtuU7xVoJmbBhdUlcVw6j9bx4BNQUiciEcIcg==" type="application/javascript" src="https://assets-cdn.github.com/assets/github-cb1dd6d465d3a31da1f1a1585029385c.js"></script>
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
  </div>
</div>

  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark" open>
    <summary aria-haspopup="dialog" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

<div id="hovercard-aria-description" class="sr-only">
  Press h to open a hovercard with more details.
</div>


  </body>
</html>

