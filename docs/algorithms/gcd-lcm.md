---
comments: true
---

## STL

[cppreference](https://en.cppreference.com/w/cpp/numeric/gcd)

=== "Head Files"
    ```cpp
    #include <numeric>
    ```
=== "C++ Version"
    ```cpp
    -std=c++17
    ```

=== "std::gcd"
    ```cpp
    template< class M, class N >
    constexpr std::common_type_t<M, N> gcd( M m, N n );
    ```

=== "std::lcm"
    ```cpp
    template< class M, class N >
    constexpr std::common_type_t<M, N> lcm( M m, N n );
    ```

## GCD [^1]

[^1]: Greatest Common Divisor

=== "Conditional Operator"
    ```cpp
    int gcd(int x, int y) {
        return y>0 ? gcd(y, x%y) : x;
    }
    ```

=== "Bitwise Operation"
    ```cpp
    int gcd(int x, int y) {
        while (y^=x^=y^=x%=y);
        return x;
    }
    ```

## LCM [^2]

[^2]: Least Common Multiple

```cpp
int lcm(int x, int y) {
    return a / gcd(x, y) * y;
}
```

!!! tips
    Performing division before multiplication can help avoid overflow.
