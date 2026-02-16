---
comments: true
---

# Summary Statistics

## Definitions

### Parameters & Statistics

- **$\overline{x}$**: The sample mean
- **$\mu$**: the population mean
- **$S$**: Sample standard deviation
- **$\sigma$**: Population standard deviation
- **$X^2$**: Sample chi-square value
- **$\chi^2$**: Population chi-quare value
- **$\hat{\rho}$**: Sample proportion
- **$p$**: Population proportion

### Quartiles

- **Q1**: One quarter (25%) of the data is less than or equal to Q1
- **Q3**: Three quarters (75%) of the data is less than or equal to Q3

### Interquartile Range (IQR)

- **IQR** = Q3 - Q1

### Standard Deviation & Variance

- The standard deviation for a **population**: $\sigma_x = \sqrt{\dfrac{\sum (X_i - \overline{x})^2}{n}}$
- The standard deviation for a **sample**: $s_x = \sqrt{\dfrac{\sum(x_i - \overline{x})^2}{n-1}}$
- **Variance** is the square of the standard deviation, i.e., $\sigma^2$ and $s^2$

### Frequency

- **Frequency**: number of times that a certain value has appeared, denoted by **$f$**
- $\overline{x} = \dfrac{\sum\limits_{i=1}^n f_i x_i}{n}$
- **Relative Frequency**: $\dfrac{f}{n}$

### Outliers

- $x$ is an outlier if **$x < Q1 - 1.5 \cdot IQR$** or **$x > Q3 + 1.5 \cdot IQR$**
- $x$ is an outlier if **$x \geq \mu + 2\sigma$** or **$x \leq \mu - 2\sigma$**

### Five-Number Summary

- **min value**
- **first quartile**
- **median**
- **third quartile**
- **max value**

### Boxplots

- A **box** is used to represent the **middle 50%** of the data
- The **width** of the box represents **IQR**
- Two **whiskers** (horizontal lines) represent **min** and **max** value
- **Outliers** are represented with a **cross** and are outside of the whiskers

### Skewness

- **Skewness** describes the **direction** in which a **non-symmetrical** distribution of data is leaning
    - A distribution that has its **tail** on the **right** side has **positive skew**
    - A distribution that has its **tail** on the **left** side has **negative skew**
- Find the skewness from a **boxplot**:
    - If the **median** is roughly in the middle of the first and third quartiles, then the distribution is approximately **symmetrical**
    - If the **median** is **closer to Q1**, then the distribution has **positive skew**
    - If the **median** is **closer to Q3**, then the distribution has **negative skew**
- Find the skewness from **the median** and **the mean**
    - **Positively skewed**: median **<** mean
    - **Negatively skewed**: median **>** mean

### Data Comparison
- Compare numerical values
- Describe meaning in real life