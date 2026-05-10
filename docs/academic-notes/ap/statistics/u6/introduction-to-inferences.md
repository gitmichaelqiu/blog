---
comments: true
---

# Introduction to Inferences

## Tails on A Normal Distribution

> The regions on the extreme left or right sides

- For common percentages, it is easier and more accurate to use the last row of the t-table, $\infty$

## Introduction to Hypothesis Testing

### Hypothesis Test

> A procedure for determining whether or not a population parameter has changed significantly from its previous parameter

### Null Hypothesis

> $H_0$, the assumption that the population parameter has not changed

### Alternative Hypothesis

> $H_a$, how you think the population parameter has changed

### One-Tailed Test

> When you suspect the population parameter has in a particular direction (either increase or decrease)

- $H_a: \mu > ...$
- $H_a: \mu < ...$

### Two-Tailed Test

> When you suspect the population parameter has changed

- $H_a: \mu \neq ...$

### Test Statistics

> An unbiased estimate of the population parameter from the recent sample from the population

### Standardized Test Statistics

> How far the test statistic is from the population parameter
>
> $\dfrac{statistic - parameter}{standard\ error\ of\ the\ statistic}$

### Conditions for A Hypothesis Test

- Independence
	1. Data is collected by random sampling or random assignment
	2. If sampling without replacement, $n \leq 0.1 N$
- Normality
	- Approximately symmetric
	- No outliers

### p-value

> The probability of obtaining a test statistic as extreme, or more extreme, than the on observed in the sample, assuming the null hypothesis is true

- The more extreme the test statistic is compared to the sample, the smaller the p-value, and the more evidence there is to suggest that the null hypothesis can be rejected
- $p$-value is calculated by finding probabilities from the sample distribution for that test statistic
	- Use the population parameter from the null hypothesis
	- Work out the standardized test statistic

### Significance Level

> $\alpha$, the probability threshold at which you reject the null hypothesis.
> 
> $p < \alpha \implies$ the null hypothesis should be rejected

## Introduction to Confidence Intervals

### Confidence Interval

> A symmetric range of values centered about an estimate from a sample designed to capture the actual value of the population parameter

### Confidence Level

> The percentage of all possible confidence intervals that capture the population parameter

- $confidence\ interval = statistic \pm margin\ of\ error$
	- The statistic is the estimate from the sample
- $margin\ of\ error = critical\ value \cdot standard\ error\ of\ statistic$
	- The critical value depends on the confidence level, C%
	- The critical value is $z$-score
	- The standard error is an estimate of the population standard deviation from the data
	- The width of Margin of Error is half of the width of the Confidence Interval