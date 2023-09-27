---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Home
---

<div class="image-container">
  <img src="./pictures/selfie_phd.jpg" width="200"/>
  <div class="text-container">
    <p>Since October 1st 2023, I am a postdoc in <a href="https://www.epfl.ch/labs/stoan/">STOAN</a> group at EPFL, directed by <a href="https://www.xuemei.org/">Xue-Mei Li</a>.</p>
    <p>I defended my PhD thesis at Freie Universität Berlin supervised by <a href="https://www.mi.fu-berlin.de/math/groups/stoch/members/Professors/perkowski.html">Nicolas Perkowski</a>. 
    I was a member of <a href="https://www3.math.tu-berlin.de/stoch/IRTG/">International Research Training Group (IRTG) 2544: Stochastic Analysis in Interaction</a>.</p>
    <p>My <a href="/assets/cv/latex_cv.pdf">CV</a>.</p>
    <p>I have recently defended my PhD thesis, whose introduction is available <a href="/assets/thesis/thesis_intro.pdf">here</a>. (full online version will be available soon.)</p>
    <a href="https://arxiv.org/a/matsuda_t_1.html"><i class="ai ai-arxiv-square ai-2x"></i></a>
    <a href="https://orcid.org/0000-0002-2422-0863"><i class="ai ai-orcid-square ai-2x"></i></a>
    <a href="https://scholar.google.com/citations?hl=en&user=6YeVU1EAAAAJ&view_op=list_works"><i class="ai ai-google-scholar-square ai-2x"></i></a>
  </div>
</div>

<style>
  .image-container {
    display: flex;
    align-items: center;
    gap: 20px;
  }

  .text-container {
    flex: 1;
  }

  @media (max-width: 768px) {
    .image-container {
      flex-direction: column;
      text-align: center;
    }
    .image-container img {
      margin-bottom: 10px;
    }
    .text-container {
      width: 100%;
    }
  }
</style>
