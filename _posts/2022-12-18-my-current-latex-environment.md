---
layout: post
title:  "My current TeX environment"
---

Here I record my current (December 2022) TeX environement: VS code, TeXmacs and GitHub. 
# Visual Studio Code
I use [Visual Studio Code](https://code.visualstudio.com/) (VS code) for LaTeX typing. 
<figure>
<img src="/assets/2022_12_18/vscode.png" alt="vscode" style="width:100%">
<figcaption align = "center">Fig.1 - A screenshot of LaTeX environment in VS code.</figcaption>
</figure>

The greatest feature of VS code is that it has many extensions. For LaTeX, I use the following extensions.
- [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop),
- [Vim](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim).

You can also make your own customization by modifying json files. 
To change the general setting, go to `Code > Preferences > Settings` or open settings.json file (type <kbd>&#8984;</kbd> + <kbd>SHIFT</kbd> + <kbd>P</kbd> (for Mac) and enter 'settings.json'). For me, the settings.json file is as follows.

>{
>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"workbench.colorTheme": "Quiet Light",
>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"editor.minimap.enabled": false,
>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"latex-workshop.intellisense.citation.backend": "biblatex",
>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"git.autofetch": true,
>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"editor.tabCompletion": "onlySnippets",
>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"explorer.excludeGitIgnore": true,
>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"editor.fontSize": 14
>
>}

There are json files specific to some file types. For instance, if you want to define snippets for .tex files, you should modify latex.json (go to `Code > Preferences > Configure User Snippets` and find or create 'latex.json'). [My latex.json](/assets/2022_12_18/latex.json) file is quite long due to many snippets, which are inspired by TeXmacs. In the long run, defining snippets increases efficiency. Let's say that you want to type the following.
>\begin{align*}
>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\alpha = \int_s^t \mathcal{A}(x) \mathrm{d} x.
>
>\end{align*}

With my latex.json, you can just type <kbd>eq</kbd> + <kbd>TAB</kbd> + <kbd>*</kbd> + <kbd>TAB</kbd> + <kbd>a</kbd> + <kbd>TAB</kbd> + <kbd> = \int_s^t</kbd> + <kbd>cA</kbd> + <kbd>TAB</kbd> + <kbd>(x)</kbd> + <kbd>rd</kbd> + <kbd>TAB</kbd> + <kbd>x.</kbd>. See Fig 2.

<figure>
<img src="/assets/2022_12_18/latex_snippets.gif" alt="latex snippets" style="width:120%">
<figcaption align = "center">Fig.2 - LaTeX typing with snippets. </figcaption>
</figure>

# TeXmacs
[TeXmacs](https://www.texmacs.org/tmweb/home/welcome.en.html) is something like Word for LaTeX. 

<figure>
<img src="/assets/2022_12_18/texmacs.gif" alt="texmacs" style="width:120%">
<figcaption align = "center">Fig.3 - TeXmacs. </figcaption>
</figure>

I use TeXmacs to record some primitive mathematical ideas, and to create slides (to me it is much easier than beamer). I also used TeXmacs for an online seminar, like [Gubinelli's lecture](https://www.youtube.com/watch?v=FL50D2PpswE).

# GitHub
[GitHub](https://github.com/) is a code sharing platform based on version control [git](https://git-scm.com/). Although it is famous for open source repository, you can also create private repositories and use them for collaborative works. Currently all my projects are associated with GitHub repositories. VS code is equipped with basic GitHub user interface.
I prefer GitHub over Dropbox, because GitHub has more functions such as the concept of branches, and with GitHub it is easier to see which parts are modified (Fig 4). I prefer GitHub over Overleaf, because you can use your own favorite text editor: I cannot do it without Vim.

<figure>
<img src="/assets/2022_12_18/github.png" alt="github changes" style="width:100%">
<figcaption align = "center">Fig.4 - GitHub, display of changes. </figcaption>
</figure>