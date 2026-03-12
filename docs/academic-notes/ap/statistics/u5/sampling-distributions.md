# Sampling Distributions

## Sampling Distributions for Sample Means

> Take all possible samples of size $n$ from a population and calculate the sample mean $\overline{x}$  for each, all possible values of the sample mean are calculated

### Parameters of Sampling Distributions for Sample Means

- Mean = $\mu$
- Standard deviation = $\dfrac{\sigma}{\sqrt{n}}$
- Standardized $z$-score = $\dfrac{\overline{x} - \mu}{\frac{\sigma}{\sqrt{n}}}$

### Normality of Sampling Distributions for Sample Means

- If the population is normally distributed, the sampling distribution for sample means is normally distributed

## Central Limit Theorem

> - If a population is not normally distributed
> - A large enough random sample of size $n \geq 30$  is taken while sample values are independent
> - Then the sampling distribution for sample means is approximately normally distributed

## Sampling Distributions for Differences in Sample Means

### One-Sample Problem

> When one random sample of size $n$ has been taken from one population

### Two-Sample Problem

> If one random sample of size $n_1$ is taken from one population, then a different random sample of size $n_2$ is taken from a different population that is independent to the first population

### Parameters of Sampling Distribution for Differences in Sample Means

- Mean = $\mu_1 - \mu_2$
- Standard deviation = $\sqrt{\dfrac{\sigma_1^2}{n_1} + \dfrac{\sigma_2^2}{n_2}}$
	- Sampling with replacement or each sample size is less than 10% of the population size
	- Otherwise, $\sigma$ will be smaller
- Standardized $z$-score = $\dfrac{(\overline{x_1} - \overline{x_2}) - (\mu_1 - \mu_2)}{\sqrt{\dfrac{\sigma_1^2}{n_1} + \dfrac{\sigma_2^2}{n_2}}}$

### Normality of Sampling Distributions for Differences in Sample Means

- If two independent populations are normally distributed, the sampling distribution for differences in sample means is also normally distributed

## Sampling Distributions for Sample Proportions

- **Population proportion**, $p$, is the percentage of success
- $n$ is the sample size
- $X$ is the number of successes in a sample, following **binomial distribution**
- Sample proportion $\hat{p} = \dfrac{X}{n}$

If

- $np \geq 10$
- $n(1-p) \geq 10$

Then $\hat{p}$

- Normally distributed
- Mean = $p$
- Standard deviation = $\sqrt{\dfrac{p(1-p)}n}$
- $z$-score = $\dfrac{\hat{p} - p}{{\sqrt{\dfrac{(1-p)}{n}}}}$

## Sampling Distributions for Differences in Sample Proportions

If

- $n_1p_1 \geq 10$
- $n_1(1-p_1) \geq 10$
- $n_2p_2 \geq 10$
- $n_2(1-p_2) \geq 10$

Then $\hat{p_1} - \hat{p_2}$

- Normally distributed
- Mean = $p_1 - p-2$
- Standard deviation = $\sqrt{\dfrac{p_1(1-p_1)}{n_1} + \dfrac{p_2(1-p_2)}{n_2}}$
- Standardized $z$-score = $\dfrac{(\hat{p_1} - \hat{p_2}) - (p_1 - p_2)}{\sqrt{\dfrac{p_1(1-p_1)}{n_1} + \dfrac{p_2(1-p_2)}{n_2}}}$

## Biased & Unbiased Estimators

> **Estimator** is used to estimate the population parameter

To know if an estimator is a good predictor

- All possible estimates from all possible samples of size $n$ must be generated
- Check to see if, on average, estimates are centered around the value of the population parameter
- An estimator is said to be **unbiased** if the mean of its sampling distribution equals the population parameter being estimated

### Unbiased Estimators

- Sample mean $\overline{x}$
- Sample proportion $\hat{p}$
- Sample standard deviation $s$

### Affects on Unbiased Estimators

- $n$ does not affect $\overline{x}$
- Greater $n$ gives more accurate $S = \dfrac{\sigma}{\sqrt{n}}$