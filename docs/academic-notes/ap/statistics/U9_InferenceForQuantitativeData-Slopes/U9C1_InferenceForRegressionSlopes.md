## Sampling Distributions for Sample Slopes

### Population Least-Squares Regression Line

> Theoretical, best-fitting straight line that described the true linear relationship between two variables for an entire population
>
> $\hat{y} = \alpha + \beta x$
>
> - $\hat{y}$: predicted response
> - $\alpha$: population $\hat{y}$-intercept
> - $\beta$: population slope
>
> Least-squares indicate that the sum of squared residuals are minimized

### Sample Least-Squares Regression Line

> The line of best fit for a set of data points that minimize the sum of squared residuals
>
> $\hat{y} = a+bx$

- Different samples produce different sample least-square regression lines. These all have different sample sloped $b$. This means $b$ has a sampling distribution.

### Mean and Standard Deviation of Sampling Distribution for Sample Slopes

For the sample slopes $b$:

- $\mu = \beta$
- $\sigma = \dfrac{\sigma}{\sigma_x \sqrt{n}}$
	- $n$: sample size
	- $\sigma$: $\sigma$ of all population residuals
	- $\sigma_x = \sqrt{\dfrac{\sum (x_i - \overline{x})^2}{n}}$: $\sigma$ of the $x$-values only
- $\dfrac{\sigma}{\sigma_x \sqrt{n}}$ is unknown in practice and must be estimated from the sample (standard error)
	- $s_b = \dfrac{s}{s_x \sqrt{n-1}}$: the standard error of sample slopes
	- $s = \sqrt{\dfrac{\sum (y_i - \hat{y_i})^2}{n-2}}$
		- Divided by $n-2$ as two parameters, $\alpha$ and $\beta$, are estimated
	- $s_x = \sqrt{\dfrac{\sum (x_i - \overline{x})^2}{n-1}}$

### Sampling Distributions for Standardized Sample Slopes

- $t = \dfrac{b - \beta}{s_b}$: standardized sample slope
- $t$-distribution with $dof=n-2$

## Hypothesis Tests for Slopes of Regression Lines

### Conditions for A t-Test for A Slope

- Relationship between $x$ and $y$ is linear
- $\sigma_y$ cannot vary with $x$
- Residuals are independent
	- Data is collected by random sampling/assignment
	- If sampling without replacement, $n < 0.1N$
- For a given value of $x$, $y$-values follow an approximate normal distribution
- If $n<30$, $y$-values distribution have no strong skew and no outliers

### Computer Output Table

| Predictor    | Coef | SE Coef | T   | P   |
| ------------ | ---- | ------- | --- | --- |
| Constant     | $a$  |         |     |     |
| $x$-variable | $b$  | $s_b$   |     |     |
|              |      |         |     |     |

