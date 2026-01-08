---
comments: true
---

## Difference Between GCC Optimizations
- O1: Enable basic optimizations, including function inlining and loop unrolling.
- O2: Enable more optimizations, including function inlining, loop unrolling, constant propagation, dead code removal, etc.
- O3: Enable more advanced optimizations, including function inlining, loop unrolling, constant propagation, dead code removal, vectorization, etc.
- Os: Enable optimizations with code size reduction as the main goal.

!!! warning
    Enabling higher-level optimization options may result in increased compilation times and, in some cases, may result in less efficient code execution.

!!! warning
    Enabling GCC optimization manually is not allowed in Luogu OJ

## Usage
!!! tip
    If you have STL in your code, you'd better turn on O2 or even O3 optimization.

```cpp title="O2 Optimization"
#pragma GCC optimize(2)
```