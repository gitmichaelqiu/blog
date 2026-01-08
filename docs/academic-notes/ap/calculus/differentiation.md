## Derivative

$f'(x_0) = \lim\limits_{\Delta x \to 0} \dfrac{\Delta y}{\Delta x} = \lim\limits_{\Delta x \to 0} \dfrac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$

$f'_-(x_0) = \lim\limits_{\Delta x \to 0^-} \dfrac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} = \lim\limits_{x \to x_0^-} \dfrac{f(x) - f(x_0)}{x - x_0}$

$f'_+(x_0) = \lim\limits_{\Delta x \to 0^+} \dfrac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} = \lim\limits_{x \to x_0^+} \dfrac{f(x) - f(x_0)}{x - x_0}$

$f'(x_0)\ exists \iff f'_-(x) = f'_+(x)$

## Algorithms

$[f(x) \pm g(x)]' = f'(x) \pm g'(x)$

$[f(x) \cdot g(x)]' = f'(x) \cdot g(x) + f(x) \cdot g'(x)$

$[\dfrac{f(x)}{g(x)}]' = \dfrac{f'(x) \cdot g(x) - f(x) \cdot g'(x)}{[g(x)]^2}$

## Differentiation Rules

$(C)' = 0$

$\boxed{(x^n)' = nx^{n-1}}$

$\boxed{(\sin x)' = \cos x}$

$\boxed{(\cos x)' = -\sin x}$

$\boxed{(\tan x)' = \sec^2 x}$

$\boxed{(\sec x)' = \sec x \cdot \tan x}$

$(\cot x)' = - \csc^2 x$

$(\csc x)' = - \csc x \cdot \cot x$

$\boxed{(a^x)' = a^x \cdot \ln a}$

$(e^x)' = e^x$

$\boxed{(\log_ax)' = \frac{1}{x \cdot \ln a}}$

$(\ln x)' = \frac{1}{x}$

## The Chain Rule

$\boxed{(f(g(x)))' = f'(g(x)) \cdot g'(x)}$

## Inverse Functions

!!! note "Inverse Functions"

    $f^{-1}(f(x)) = x \iff f(f^{-1}(x)) = x$ 

if $\ g(x) = f^{-1}(x)$,

then $\ \boxed{g'(x) = \dfrac{1}{f'(g(x))}},\ f'(g(x)) \neq 0$

## L'Hôpital's Rule

when $x \to a$,

if $\left\{\begin{aligned} f(x) & \to 0 \\ g(x) & \to 0 \end{aligned}\right.\ or \left\{\begin{aligned} f(x) & \to \infty\\ g(x) & \to \infty \end{aligned}\right.$,

then $\boxed{\lim\limits_{x \to a} \dfrac{f(x)}{g(x)} = \lim\limits_{x \to a} \dfrac{f'(x)}{g'(x)}}$

## Intermediate Value Theorem

If $f$ is **continuous** on $[a, b]$, $u$ is a number such that $\min(f(a), f(b)) < u < \max(f(a), f(b))$,

then there is a $c \in (a, b)$ such that $f(c) = u$

## Mean Value Theorem

If $f$ is **continuous** on $[a, b]$ and **differentiable** on $(a, b)$, then

$\exists c \in (a, b)$ such that $\boxed{f'(c) = \dfrac{f(b)-f(a)}{b-a}}$

## Extreme Value Theorem

If $f$ is **continuous** on the $[a, b]$, then $f$ must attain a **maximum** and a **minimum**, each at least once, i.e.

$\exists c, d \in [a, b]$ such that $\boxed{f(c) \leq f(x) \leq f(d), \forall x \in [a, b]}$

## Concavity

- If $\boxed{f'' > 0}$, then $f$ concave up
- If $\boxed{f'' < 0}$, then $f$ concave down

!!! note "Points of Inflection"

    $\left\{\begin{aligned}
    f'' & = 0\ or\ DNE \\
    f'' & change\ sign
    \end{aligned}\right.$
