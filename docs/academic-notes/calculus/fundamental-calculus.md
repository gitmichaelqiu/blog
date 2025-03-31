## Antiderivative

$y = \int f(x) dx = F(x) + C$

!!! note

    $f$: integrand

    $dx$: variable of integration

    $F(x)$: an antiderivative of $f(x)$

    $C$: constant of integration

??? example

    $\int x^3\ dx = \frac{x^4}{4} + C$

## Definition of Definite Integral

$\int^b_a f(x) dx = \lim\limits_{n \to \infty} \sum\limits^n_{k=1} f(x^*_k) \cdot \Delta x$

- Left point：$x_k^* = a + (k-1)\Delta x$
- Right point：$x_k^* = a + k\Delta x$
- Middle point：$x_k^* = a + \left(k - \frac{1}{2}\right)\Delta x$

### Definite Integral

$\int^b_a f(x) dx = \lim\limits_{n \to \infty} \sum\limits^n_{k=1} f(a + k \cdot \dfrac{b-a}{n}) \cdot \dfrac{b-a}{n}$

### Left Riemann Sum

$\int^b_a f(x) dx = \lim\limits_{n \to \infty} \sum\limits^n_{k=1} f(a + (k-1) \cdot \dfrac{b-a}{n}) \cdot \dfrac{b-a}{n}$

## Right Riemann Sum

$\int^b_a f(x) dx = \lim\limits_{n \to \infty} \sum\limits^n_{k=1} f(a + k \cdot \dfrac{b-a}{n}) \cdot \dfrac{b-a}{n}$

## Midpoint Riemann Sum

$\int^b_a f(x) dx = \lim\limits_{n \to \infty} \sum\limits^n_{k=1} f(a + (k-\frac12) \cdot \dfrac{b-a}{n}) \cdot \dfrac{b-a}{n}$

## Trapezoidal Sum

$\int^b_a f(x)dx = \lim\limits_{n \to \infty} \dfrac{b-a}{2n}[f(a) + 2\sum\limits^{n-1}{k=1}f(a + k \cdot \dfrac{b-a}{n} + f(b))]$

$\iff$

$\int^b_a f(x) dx = \lim\limits_{n \to \infty} \sum\limits^n_{k=1} \dfrac{f(a + (k-1) \cdot \frac{b-a}n + f(a+k \cdot \frac{b-a}n))}{2} \cdot \dfrac{b-a}n$

## Basic Integration Formulas

- $\boxed{\int dx = x + C}$
- $\boxed{\int k\ dx = kx + C}$
- $\boxed{\int kf(x)dx = k \int f(x)dx}$
- $\boxed{\int[f(x) \pm g(x)] dx = \int f(x) dx \pm \int g(x) dx}$
- $\boxed{\int x^n dx = \frac1{n+1} x^{n+1} + C}$ & $\boxed{\int \frac1x dx = \ln |x| + C}$
- $\boxed{\int a^x dx = (\frac1{\ln a}) a^x + C}$
- $\int e^x dx = e^x + C$
- $\boxed{\int \sin x dx = - \cos x + C}$
- $\boxed{\int \cos x dx = \sin x + C}$
- $\boxed{\int \sec^2 x\ dx = -\tan x + C}$
- $\int \csc^2 x\ dx = -\cot x + C$
- $\int \sec x \tan x \ dx = \sec x + C$
- $\int \csc x \cot x \ dx = - \csc x + C$
- $\int \dfrac{dx}{\sqrt{1-x^2}} = \arcsin x + C$
- $\boxed{\int \dfrac{dx}{1+x^2}} = \arctan x + C$
- $\int \dfrac{dx}{\sqrt{a^2-x^2}} = \arcsin \dfrac ac + C$
- $\int \dfrac{dx}{a^2+x^2} = \dfrac 1a \arctan \dfrac xa + C$
