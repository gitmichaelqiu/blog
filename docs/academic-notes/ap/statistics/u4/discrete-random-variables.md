# Discrete Random Variables

## Discrete Random Variables

> A random variable with a countable number of values
> 
> - The number of variables could be either finite or infinite

### Discrete Probability Distribution

> Describes the probabilities of the occurrences of each possible outcome associated with a discrete random variable

![](https://cdn.savemyexams.com/cdn-cgi/image/f=auto,width=3840/https://cdn.savemyexams.com/uploads/2024/08/12838_discrete-probability-distributions.png)

> **Discrete uniform distributions**: when all outcomes have the same possibility

## Cumulative Probability Distributions for Discrete Random Variables

> The probability that a discrete random variable is less than or equal to each of its possible values

## Mean & Standard Deviation of A Discrete Random Variable

> The weighted average of the possible values based on their probabilities, i.e. the expected value $\mu_X$ or $E(X)$
> 
> $\mu_X = \sum x_i \cdot P(x_i)$


> The variance of a discrete random variable is the expected value of the squared differences between the values and the mean
>
> $\sigma_X = \sqrt{\sum (x_i - \mu_X)^2 \cdot P(x_i)}$

## Linear Transformation of Random Variables

### Definition

> Every value of the variable is either multiplied by a constant or added to another constant or a combination of both
>
> $Y = a + bX$

- Linear transformation can be used to make the numbers more manageable

### Affects on Mean & Standard Deviation

$\mu_Y = a + b\mu_X$

$\sigma_Y = |b| \sigma_X$

### Affects on the Shape of Distribution

- **Addition**: does not change
- **Multiplication**: does not change if $b > 0$, otherwise flipped horizontally

## Linear Combinations of Random Variables

> Multiples of given random variables are added together

$Y = \sum\limits_{i=1}^n a_iX_i$

### Affects on Mean & Standard Deviation

$\mu_Y = \sum\limits_{i=1}^n a_i\mu_i$

$\sigma_Y = \sqrt{\sum\limits_{i=1}^n a_i^2\sigma_i^2}$
