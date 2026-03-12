## Type I & Type II Errors

| Reality\\Conclusion | Reject   | Not reject |
| ------------------ | -------- | ---------- |
| True               | Type I   | No error   |
| False              | No error | Type II    |

- Type I = False positive
	- Innocent but judged guilty
- Type II = False negative
	- Guilty but judged innocent

## Probability of Type I Error

- If significance level $\alpha$ is known, $P(Type\ I\ error) = \alpha$
- If unknown, $P(Type\ I\ error)=$ probability of being in the critical region given $H_0$ is true

## Probability of Type II Error

- $P(Type\ II\ error) = P($not in the critical region, given the actual population parameter is true$)$

### Reduce Probability of Type II Error

- $\uparrow n$
- $\uparrow \alpha$
- $\downarrow \sigma$ of the hypothesis test
- Actual population parameter is farther from the null population parameter

### Relationship Between Possibilities of Type I & II Errors

- $\uparrow \alpha \implies \uparrow P(Type\ I), \downarrow P(Type\ II)$
- $\downarrow \alpha \implies \downarrow P(Type\ I), \uparrow P(Type\ II)$
- $\uparrow n \implies \downarrow P(Type\ I), \downarrow P(Type\ II)$

## Power of A Test

> The probability that it will correctly reject a false null hypothesis
>
> $Power = 1 - P(Type\ II\ error)$
