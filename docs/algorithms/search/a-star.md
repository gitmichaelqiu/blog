---
comments: true
---

## Complexity

Time Complexity: $O((n+m) \log m)$

## Template

=== "Head Files"
    ```cpp
    #include <vector>
    #include <queue>
    #include <utility>
    #include <algorithm>
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
pair<int, int> coord[maxn];
```

=== "Manhattan distance"
    ```cpp
    int heuristic(const pair<int, int> &u, const pair<int, int> &tg) {
        return abs(u.first - tg.first) + abs(u.second - tg.second);
    }
    ```

=== "Euclidean Distance"
    ```cpp
    int heuristic(const pair<int, int> &u, const pair<int, int> &tg) {
        return sqrt(pow(u.first - tg.first, 2) + pow(u.second - tg.second, 2)); // Euclidean distance
    }
    ```

```cpp title="A*"
vector<int> a_star(const int &sz, const int &st, const int &tg) {
    vector<int> dis(sz+1, inf);
    vector<int> prev(sz+1, -1);
    priority_queue< node, vector<node>, greater<node> > pq;

    dis[st] = 0;
    pq.emplace((node){st, 0});

    while (!pq.empty()) {
        int u = pq.top().u; pq.pop();

        if (u == tg) break;

        for (const auto &ed : e[u]) {
            int v = ed.v, w = ed.w;
            if (dis[v] > dis[u] + w) {
                dis[v] = dis[u] + w;
                pq.emplace((node){v, dis[v]+heuristic(coord[u], coord[tg])});
            }
        }
    }

    vector<int> path;
    if (dis[tg] != inf) {
        for (int i = tg; i != -1; i = prev[i]) {
            path.emplace_back(i);
        }
        reverse(path.begin(), path.end());
    }
    return path;
}
```
