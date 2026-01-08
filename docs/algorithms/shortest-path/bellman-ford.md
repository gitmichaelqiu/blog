---
comments: true
---

## Video Recommendation

- [4.4 Bellman Ford Algorithm - Single Source Shortest Path - Dynamic Programming - Adbul Bari](https://youtu.be/FtN3BYH2Zes?si=Dc4eQoTKZMcSWMru)

## Template

=== "Head Files"
    ```cpp
    #include <vector>
    ```
=== "C++ Version"
    ```cpp
    -std=c++11
    ```

```cpp title="Constants"
const int inf = 0x3f;
const int maxn = 1e4 + 5;
```

```cpp title="struct"
struct edge {
    int v, w;
};

struct node {
    int u, dis;

    bool operator>(const node &x) const {
        return dis > x.dis;
    }
};

vector<edge> e[maxn];
```

```cpp title="Bellman Ford"
void bellman_ford(const int &sz, const int &st) {
    vector<int> dis(sz+1, inf);
    dis[st] = 0;
    
    bool flag;
    for (int i=1; i<=sz; ++i) {
        flag = 0;
        for (int u=1; u<=sz; ++u) {
            for (auto &e : e[u]) {
                int v = e.v, w = e.w;
                if (dis[v] > dis[u] + w) {
                    dis[v] = dis[u] + w;
                    flag = 1;
                }
            }
        }

        if (!flag) return;
    }
}
```
