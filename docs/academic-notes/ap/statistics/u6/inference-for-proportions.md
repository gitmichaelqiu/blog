---
comments: true
---

# Inference for Proportions

## One-Sample z-test for Population Proportion

### z-test for Population Proportion

> Used to test whether the population proportion, $p$, has changed
> A random sample of $n$ individuals from the population with a sample proportion of $\hat{p}$ is used to try to prove the case

### Conditions for A z-test for Population Proportion

- Items in the sample satisfy the independence condition
	- Random sampling/assignment
	- If without replacement, $n < 0.1N$
- Sample size is large enough such that sampling distribution is approximately a normal distribution
	- $np_0 \geq 10$
	- $n(1-p_0) \geq 10$
	- $p_0$ is the population proportion in the null hypothesis, $p = p_0$

- $z = \dfrac{statistics - parameter}{standard\ error\ of\ the\ statistic}$
- $standard\ error\ of\ the\ statistic = \sqrt{\dfrac{p_0(1-p_0)}n}$

## Confidence Interval

$confidence\ interval = \hat{p} \pm z \cdot \sqrt{\dfrac{p_0(1-p_0)}n}$