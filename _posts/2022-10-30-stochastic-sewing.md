---
layout: post
title:  "Journey on the paper "An extension of the stochastic sewing lemma""
mathjax: true
---

Here I record my journey on writing the
paper "An extension of the stochastic sewing lemma and its
applications to fractional stochastic calculus".

It started around the middle of 2021. As a member of PhD program, I was
supposed to visit Oxford for research. At that time I was mainly working
on a topic called singular SPDE, which was a new and active field after
Hairer received the Field medal in 2014. But no professor in Oxford
worked on singular SPDE (as this was one year before Gubinelli joined
Oxford), and this means that to visit Oxford, I needed to find a new
topic that interests a professor in Oxford. Actually this was a good
opportunity for me. The field of singular SPDE witnessed extremely rapid
speed of progress after Hairer's breakthrough, and as a result there
were already enough strong researchers in that field and I felt
inadequacy to continue to work on singular SPDE. So I asked Nicolas (my
supervisor) about this, and he suggests to check some papers of Rama
Cont, as Nicolas had some works with him.

Rama Cont is a giant in the mathematical finance and, as I was not
familiar with math finance, it was not easy for me to find a paper of
him that I can actually understand. Fortunately, his latest paper at
that time was about excursion. This is a topic of pure probability
theory and without fluency in math finance I was able to understand a
large part of the paper (although the paper is motivated by applications
to finance). Then, Nicolas, Rama and I had a zoom meeting to organize my
stay in Oxford and to discuss a possible project. I must admit that this
was an embarrassing meeting for me: basically Nicolas and Rama were
discussing ideas and I only said a couple of very simple sentences such
as ``that problem sounds interesting''. This was not only
because their discussion is at too high level for me but also because I
was too nervous to talk with Rama. This was my first time to talk with
such a big figure.

After the meeting I was a bit lost in a sense that I didn't know
concretely which problem I should work on. Probably Nicolas felt it, and
he suggested me a concrete problem. It is an open problem from the paper
with Nicolas and Rama, and it is about fractional Brownian motion (or
fractional stochastic calculus, a phrase from the title of our paper).
This was the first time for me to learn fractional stochastic calculus,
and as such novice how come I can solve the problem that Nicolas and
Rama left open! Luckily Nicolas is such a friendly professor that we
have lunch together with other members of his group. During lunch I
discussed the problem, and Nicolas suggested me to use <i>stochastic
sewing lemma</i>, another key phrase from the title of our paper.

The [stochastic sewing lemma](https://projecteuclid.org/journals/electronic-journal-of-probability/volume-25/issue-none/A-stochastic-sewing-lemma-and-applications/10.1214/20-EJP442.full) was a result proved by Khoa Lê, and
was regarded as a breakthrough result in Berlin community. For a week I spent almost all my time to read the paper,
and it was a very beautiful paper! No wonder why it was (and is as of writing) so popular in Berlin.
However, it was no obvious how one can use the stochastic sewing to tackle the problem of Nicolas and Rama.
During another lunch, we talked about it, and he suggested a simpler problem: for a fractional
Brownian motion $B^H$ with Hurst parameter $H \in (0, 1)$ it is well-known that

\\[
\lim_{\vert \pi \vert \to 0} \sum_{[s,t] \in \pi} \vert B^H_t - B^H_s \vert^{1/H} = c_H, \tag{1}
\\]

where $\pi$ is a partition of $[0, 1]$ and $c_H$ is a some constant, and can we give a proof by stochastic sewing?
It became clear soon to me that Khoa's stochastic sewing is not sufficient to prove this fundamental result.

Meanwhile, Nicolas sent me a paper of [Mukeru](https://www.sciencedirect.com/science/article/abs/pii/S0167715217302596), hoping that it could help solve the problem.
The paper was difficult, but it cited an interesting result of [Picard](https://projecteuclid.org/journals/annals-of-probability/volume-36/issue-6/A-tree-approach-to-p-variation-and-to-integration/10.1214/07-AOP388.full).
In fact, the discovery of Picard's result was the most important step in our work.
It showed the *asymptotic independence* of fractional Brownian motion, and
based on that idea I proved an asymptotic version of Khoa's stochastic sewing, which
proves the convergence (1).

I was very happy about it, and next day I went to Nicolas' office to show my proof.
Well, actually it was not a proof. Nicolas spotted a mistake in the proof,
and then I felt a bit devastated for my stupidity.
But Nicolas is so kind that he encouraged me to push my idea.
So after going back to home, I tried to fix my mistake, and fortunately it worked,
but under some technical conditions.

During a coffee time, I was talking with Helena (PhD student of Nicolas) about it, and we were discussing if
it can be used for the stochastic integral $\int_0^t f(B^H_s) \mathrm{d} B^H_s$ (of course this question was raised by Nicolas).
During the discussion we didn't make any success but afterwards I got an idea, which became Section 3 of our paper.
Another day I was discussing with Hannes (PhD student of Peter Friz) if we could use the new stochastic sewing for a result on
local time. Again during the discussion we went nowhere, but afterwards I got an idea, which became Section 4 of our paper.
However it took a while to remove the technical conditions mentioned in the previous paragraph.

It was a day when I was tired, too tired to go to a social event of the Berlin mathematical society.
Before that, I had a very vague idea to remove the technical conditions, but due to the afraid that it probably wouldn't work,
I had not tried the idea. But I needed my personal excuse for not going to the social event, I decided to try the idea.
On the contrary to my expectation that it would fail, after some calculations I started to feel like something is going on,
I got so excited that I couldn't sleep, and  I worked on until 2am. Next days I continued to work on the problem,
and I was able to remove the technical conditions (which forms Appendix of the paper).

This was the first moment that I felt I did real mathematics.
