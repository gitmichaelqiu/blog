---
comments: true
---

## Untie

```cpp
ios::sync_with_stdio(0);
cin.tie(0);
cout.tie(0);
```

!!! tip
    The untied cin & cout are actually faster than scanf & printf.

!!! warning
    You **CANNOT** use functions in `<stdio>` after untie, including `printf()`, `scanf()`, `puts()`, `freopen()`.

## endl

endl can be about **10 times slower** than the "\n".

```cpp
#define endl '\n'
```
