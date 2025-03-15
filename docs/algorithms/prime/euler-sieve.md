---
comments: true
---

## Complexity

Time Complexity: $O(n)$

## Template

```cpp
vector<int> pri;
bool not_prime[maxn];

void get_prime(const int &n) {
    for (int i=2; i<=n; ++i) {
        if (!not_prime[i]) pri.push_back(i);
        for (const int &pri_j : pri) {
            if (i * pri_j > n) break;
            not_prime[i * pri_j] = true;
            if (i % pri_j == 0) break;
        }
    }
}
```
