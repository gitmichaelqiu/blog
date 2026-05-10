---
comments: true
---

# Binomial and Geometric Distributions

## Binomial Distributions

> Counts the number of success
> 
> $X \sim B(n, p)$
>
> - Fixed number of repeated trials
> - Trials are independent
> - Two outcomes
> - Probability of success is constant

### Shape of Binomial Distributions

$p$ in $X \sim B(n, p)$ determines the skewness

| $p$     | Skewness                                                                                                                                                                        |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $< 0.5$ | Positive<br>![](https://cdn.savemyexams.com/cdn-cgi/image/f=auto,width=3840/https://cdn.savemyexams.com/uploads/2024/08/45033_binomial-distribution-when-p-is-less-than-0-5)    |
| $= 0.5$ | Symmetrical<br>![](https://cdn.savemyexams.com/cdn-cgi/image/f=auto,width=3840/https://cdn.savemyexams.com/uploads/2024/08/38947_binomial-distribution-when-p-is-equal-to-0-5)  |
| $< 0.5$ | Negative<br>![](https://cdn.savemyexams.com/cdn-cgi/image/f=auto,width=3840/https://cdn.savemyexams.com/uploads/2024/08/55815_binomial-distribution-when-p-is-greater-than-0-5) |

### Mean & Standard Deviation of Binomial Distributions

$\mu_X = np$

$\sigma_X = \sqrt{np(1-p)}$

### Probabilities for Binomial Distributions

$P(X=x) = C_n^x \cdot p^x (1-p)^{n-x}$

## Geometric Distributions

> Counts the number of trials needed to obtain the first success
>
> $X \sim Geo(P)$
>
> - Trials are independent
> - Two outcomes
> - Probability of success is constant

### Shape of Geometric Distributions

- Geometric distributions always have positive skew

![](https://cdn.savemyexams.com/cdn-cgi/image/f=auto,width=3840/https://cdn.savemyexams.com/uploads/2024/08/48548_graphs-of-geometric-distributions)

### Mean & Standard Deviation of Geometric Distributions

$\mu_X = \dfrac1p$

$\sigma_X = \dfrac{\sqrt{1-p}}p$

### Probabilities for Geometric Distributions

$P(X=x) = (1-p)^{x-1} p$