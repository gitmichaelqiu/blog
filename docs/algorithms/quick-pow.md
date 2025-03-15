---
comments: true
---

```cpp title="O(log n)"
long long qpow(long long a, const long long &n, const long long &m=1) {
    if (n == 0) return 1;
    else if (n == 1) return a;

    long long tmp = qpow(a, n>>1, m);
    if (n & 1) return tmp * tmp * a % m;
    else return tmp * tmp % m;
}
```
