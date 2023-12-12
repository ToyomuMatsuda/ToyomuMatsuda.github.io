---
layout: post
title:  "Journey on the paper \"Level crossings of fractional Brownian motion\""
mathjax: true
---

Here I record my journey on writing the
paper "Level crossings of fractional Brownian motion" ([preprint](https://arxiv.org/abs/2308.08274)).

The project started when Nicolas (my PhD supervisor) suggested the open problem left in [his previous work](https://www.ams.org/journals/btran/2019-06-05/S2330-0000-2019-00034-1/). 
The problem is easy to state (if you know [fractional Brownian motion](https://en.wikipedia.org/wiki/Fractional_Brownian_motion)): 
let $B^H$ be a 1D fractional Brownian motion with Hurst parameter $H \in (0, 1)$. Given an $\varepsilon > 0$, 
we consider the number of upcrossings from $0$ to $\varepsilon$ in the interval $[0, T]$. 
More precisely, we consider a sequence of stopping times by setting $T_0(\varepsilon) := 0$ and 
\\[
T_n(\varepsilon) := \inf\{t > T_{n-1}(\varepsilon) : B^H_{t} \in \varepsilon \mathbb{Z} \setminus \{B^H_{T_{n-1}(\varepsilon)} \}  \}.
\\]
Then we set $U_{0, T}(\varepsilon) := \# \{n : T_n(\varepsilon) \leq T, \,\, B^H_{T_{n-1}(\varepsilon)} = 0, \,\, B^H_{T_{n}(\varepsilon)} = \varepsilon, \}$. 
The question is: what is the asymptotics of $U_{0, T}(\varepsilon)$ as $\varepsilon \to 0$? 

The answer for Brownian motion is classical (see Itô--Mckean or Revuz--Yor): 
after appropriate normalization, it converges to one-half times Brownian local time at $0$.
A similar result has been expected to hold for fractional Brownian motion, but remained open. 
The difficulty is obvious, since the proof for the Brownian case heavily relies on its maringale or Markovian properties, which are not available for fractional Brownian motion.

When I started to work on the problem, I didn't know anything about fractional Brownian motion, so I was excited as well as worried about if I could prove anything about the problem. 
Surprisingly (or it is just a common trait of great mathematicians), even at the initial stage Nicolas suggested me to look at the [stochastic sewing](https://projecteuclid.org/journals/electronic-journal-of-probability/volume-25/issue-none/A-stochastic-sewing-lemma-and-applications/10.1214/20-EJP442.full). 
Starting at his insight, we have written a paper on new stochastic sewing, with its journey written in [the previous post](https://toyomumatsuda.github.io/2022/10/30/stochastic-sewing.html). 

In the previous post, I only discussed the positive aspects on our work of the new stochastic sewing. 
But I was not very satisfied with the results of Section 4 and 5. 
For instance, the result of Section 4 is an easy version of the level crossing problem. 
Recalling the notation above, we can write 
$$
\varepsilon^{\frac{1}{H} - 1} U_{0, T}(\varepsilon) 
= \sum_{[s, t] \in  \pi(\varepsilon)} |B^H_t - B^H_s|^{\frac{1}{H} - 1} \mathbf{1}_{\{B^H_s \leq 0 < B^H_t\}} + \text{(small error)},
$$
where $\pi(\varepsilon)$ is a random partition defined by $T_0(\varepsilon), T_1(\varepsilon), \ldots, T_n(\varepsilon)$ until $T_n(\varepsilon) \leq T$. 
However, the stochastic sewing cannot deal with random partitions, we ended up considering deterministic partitions, in which case it converges to local time up to multiple of constant. 

It took around one year to finish the paper on the stochastic sewing, and to some degree I was happy about the result, 
but at the same time I was dismayed too by the fact that our new stochastic sewing would not be useful for the problem of level crossings. So I forgot the problem. 

Before long, Purba (PhD student from Oxford back then) came to visit Nicolas, and interestingly she was discussing the same problem with Nicolas! Precisely, the setting was a bit different: instead of considering level crossings only from $0$ to $\varepsilon$, they considered all $\varepsilon$-level crossings. Namely, 
$$
K_{0, T}(\varepsilon) := \# \{n : T_n(\varepsilon) \leq T \}. 
$$
They were discussing the idea of Rafael (professor from Warsaw) to use subadditivity of $K$. 
That is a simple observation, but was out of box for me! Then they tried to repeat the argument of the subadditive ergodic theorem. At that moment, it occurred to me that the stochastic sewing of Nicolas and I could help. 
Although there were some technical steps, our strategy to use the stochastic sewing was correct, 
and we were able to prove the convergence of $K_{0, T}(\varepsilon)$, but ***NOT*** for $U_{0, T}(\varepsilon)$. 

The problems of $K$ and $U$ are substantially different in that for $K$ we can take advantage of some sort of stationarity. But for $U$ we only look at fractional Brownian motion around $0$, and we cannot expect any sort of stationarity. So we were not able to say anything about $U$ --- hence no progress--- for a long time. 

Then, around the summer of 2022, I went back for vacation to Japan for the first time in two years (due to Covid). I was completely different from an ambitious boy when I left for Germany two years ago. I have completely lost my confidence. I was a bit depressed, so to forget about it, I enjoyed beaches of Okinawa (my hometown). 

One day I received a long email from Nicolas at midnight in Japan. It said that Xue-Mei (my future postdoc advisor) is interested in me as a possible postdoc. Initially, I couldn't believe it; at that time I only had one so-so publication and one preprint on stochastic sewing...so how come someone can be interested in me as a postdoc? But I realized that Xue-Mei was looking for new postdocs due to her new position at EPFL and Nicolas suggested me to Xue-Mei in a too good way.  Anyway, it was an email exciting enough to stay me up. 

It was a good moment to look again at math, instead of just going to beaches. I kind of determined that if I could solve the problem of level crossings, it might not be a too bad idea to continue as a postdoc. 
So again I started work on the problem. Of course, even since before, I continued to work on the problem; just I was writing down meaningless computations and didn't make any progress. But, my previous work on stochastic sewing (especially the result of Section 4) and these meaningless computations gave me intuition that Girsanov's theorem should do something. Based on this intuition, I continued meaningless computations.

At some point, though I don't know why, I came up with an idea of technical argument. It involves six parameters, which already explains how technical the argument is :). Then I sat in front of the desk for computation, and for an entire week I was just working to go through this technical argument. After that, I was convinced that it would work. Next month was solely devoted to write down the details and simplify the argument.  It worked.

This was the biggest eureka moment for my PhD research. Looking back, the intuition was developed from the result of Section 4 from the previous paper, for which I was not very confident. But maybe you can try boring problems, as long as there is a tiny chance that it could lead to solving your dream problem. 