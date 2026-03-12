## Procedures for Hypothesis Test

1. Define context
	- $H_0: parameter =\ ...$
	- $H_a: parameter\ condition\ ...$
	- $parameter$ is the ...
	- $\alpha =\ ...$
2. Verify inference conditions
3. Find p-value
4. Conclusion
	- $p\ condition\ \alpha$
	- $H_0$ should/should not be rejected
	- The data provides sufficient evidence that ...

## Procedures for Confidence Interval

1. Verify confidence interval conditions
2. Find confidence interval
	- $CI = statistic \pm (critical\ value) \times (standard\ error\ of\ statistic)$
3. We can be $C\%$ confident that the interval from $lower\ limit$ to $upper\ limit$ captures the actual value of the $parameter$

## Population Proportions

One-sample z-test.

**Conditions**:

- Independence condition
	- Random sampling/assignment
	- If sampling without replacement, $n < 0.1 N$
- Approximately normally distributed
	- $\left\{\begin{aligned} np_0 &\geq 10 \\ n(1-p_0) &\geq 10 \end{aligned}\right.$

**Test statistic**:

- $z = \dfrac{\hat{p} - p_0}{\sqrt{\dfrac{p_0 (1-p_0)}{n}}}$
- standard error = $\sqrt{\dfrac{p_0 (1-p_0)}{n}}$

## Differences in Population Proportions

Two-sample z-test .

**Conditions**:

- Independence condition
	- Random sampling/assignment
	- If sampling without replacement, $n < 0.1 N$
- Approximately normally distributed
	- Combined proportion/pooled proportion $\hat{p}_c = \dfrac{X_1 + X_2}{n_1 + n_2}$, $X = n \hat{p}$
	- $\left\{\begin{aligned} n_1\hat{p}_c &\geq 10 \\ n_1(1-\hat{p}_c) &\geq 10 \\ n_2\hat{p}_c &\geq 10 \\ n_2(1-\hat{p}_c) &\geq 10 \end{aligned}\right.$

**Test statistic**:

- $z = \dfrac{(\hat{p}_1 - \hat{p}_2) - 0}{\sqrt{\dfrac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \dfrac{\hat{p}_2(1-\hat{p}_2)}{n_2}}}$
- standard error = $\sqrt{\dfrac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \dfrac{\hat{p}_2(1-\hat{p}_2)}{n_2}}$

## Population Means

One-sample t-test.

**Conditions**:

- Independence condition
	- Random sampling/assignment
	- If sampling without replacement, $n < 0.1 N$
- Approximately normally distributed
	- Approximately symmetric
	- No outliers
- If very skewed, $n \geq 30$

**Test statistic**:

- $t = \dfrac{\overline{x} - \mu}{\frac{s}{\sqrt{n}}}$
- standard error = $\dfrac{s}{\sqrt{n}}$

## Differences in Population Means

Two-sample t-test.

**Conditions**:

- Independence condition
	- Random sampling/assignment
	- If sampling without replacement, $n < 0.1 N$
- Approximately normally distributed
	- Approximately symmetric
	- No outliers
- If very skewed, $n \geq 30$

**Test statistic**:

- $t = \dfrac{\overline{x}_1 - \overline{x}_2}{\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}}$
- standard error = $\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}$

## Differences in Matched Pairs

One-sample t-test.

**Conditions**:

- Two measures come from the same items within the population
- Independence condition
	- Random sampling/assignment
	- If sampling without replacement, $n < 0.1 N$
- Approximately normally distributed
	- Approximately symmetric
	- No outliers
- If very skewed, $n \geq 30$

**Test statistic**:

- $t = \dfrac{\overline{x}_d - \mu_d}{\frac{s_d}{\sqrt{n}}}$
- standard error = $\dfrac{s_d}{\sqrt{n}}$

## Goodness of Fit

$\chi^2$-test.

**Conditions**:

- Independence condition
	- Random sampling
	- If sampling without replacement, $n < 0.1 N$
- Large counts condition
	- Each expected value ≥ 5

**Test statistic**:

- $\chi^2 = \sum \dfrac{(observed - expected)^2}{expected}$

## Independence

One-sample $\chi^2$-test.

**Conditions**:

- Independence condition
	- Random sampling
	- If sampling without replacement, $n < 0.1 N$
- Large counts condition
	- Each expected value ≥ 5
	- or ≥ 80\% expected values > 5 and all are ≥ 1

**Test statistic**:

- $\chi^2 = \sum \dfrac{(observed - expected)^2}{expected}$
- $Expected\ value$ = $\dfrac{Row\ total \times Column\ total}{Total\ number\ in\ sample}$
- $dof = (n_{row}-1)(n_{col}-1)$

## Homogeneity

Multi-sample $\chi^2$-test.

**Conditions**:

- Independence condition
	- Random sampling
	- If sampling without replacement, $n < 0.1 N$
- Large counts condition
	- Each expected value ≥ 5

**Test statistic**:

- $\chi^2 = \sum \dfrac{(observed - expected)^2}{expected}$
- $dof = (n_{row}-1)(n_{col}-1)$

## Regression Line

One-sample t-test.

**Conditions**:

- Relationship between $x$ and $y$ is linear
- $\sigma_y$ cannot vary with $x$
- Independence condition
	- Random sampling
	- If sampling without replacement, $n < 0.1 N$
- For a given value of $x$, $y$-values follow an approximate normal distribution
- If $n<30$, $y$-values distribution have no strong skew and no outliers

**Test statistic**:

- $t = \dfrac{b - \beta}{s_b}$
- standard error $s_b = \dfrac{s}{s_x \sqrt{n-1}}$
	- $s = \sqrt{\dfrac{\sum (y_i - \hat{y_i})^2}{n-2}}$
	- $s_x = \sqrt{\dfrac{\sum (x_i - \overline{x})^2}{n-1}}$
- $t$-distribution with $dof=n-2$

| Predictor    | Coef | SE Coef | T   | P   |
| ------------ | ---- | ------- | --- | --- |
| Constant     | $a$  |         |     |     |
| $x$-variable | $b$  | $s_b$   |     |     |
