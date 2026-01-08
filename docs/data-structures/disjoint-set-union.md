---
comments: true
---

=== "Head Files"
    ```cpp
    #include <vector>
    ```

```cpp title="Template"

class dsu {
private:
    vector<int> fa;

public:
    dsu(const int &sz) {
        fa.resize(sz+1, 0);
        
        for (int i=1; i<=sz; ++i) {
            fa[i] = i;
        }
    }

    inline int find(const int &x) {
        return x == fa[x] ? x : fa[x] = find(fa[x]);
    }

    inline void merge(const int &x, const int &y) {
        int fx = find(x), fy = find(y);
        if (fx != fy) {
            fa[fx] = fy;
        }
    }
};
```
