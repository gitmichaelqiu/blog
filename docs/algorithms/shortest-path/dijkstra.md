---
comments: true
---

## Video Recommendation

- [3.6 Dijkstra Algorithm - Single Source Shortest Path - Greedy Method - Abdul Bari](https://youtu.be/XB4MIexjvY0?si=TQ26gFkRjFhhRMBm)
- [【C++】单源最短路Dijkstra-迪杰斯特拉算法](https://www.bilibili.com/video/BV1MU4y1D729/?share_source=copy_web&vd_source=175473930ca0ed01bc70c00b3fe391c0)

## Complexity

Time Complexity: $O(m \log m)$

## Template

=== "Head Files"
    ```cpp
    #include <vector>
    #include <queue>
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


```cpp title="priority_queue Template"
vector<int> dijkstra(const int &sz, const int &st) {
    vector<int> dis(sz+1, inf);
    vector<bool> vis(sz+1, 0);
    priority_queue<node, vector<node>, greater<node> > pq;

    dis[st] = 0;
    pq.emplace((node){st, 0});

    while (!pq.empty()) {
        int u = pq.top().u; pq.pop();
        if (vis[u]) continue;
        vis[u] = 1;

        for (const auto &ed : e[u]) {
            int v = ed.v, w = ed.w;
            if (dis[v] > dis[u] + w) {
                dis[v] = dis[u] + w;
                pq.emplace((node){v, dis[v]});
            }
        }
    }
}
```

## Problems

[Luogu](https://www.luogu.com.cn/problem/P4779)

???- note "Solution"
    ```cpp
    #include <bits/stdc++.h>
    using namespace std;
    const int maxn = 1e5 + 2;
    const int inf = 0x3f3f3f3f;

    struct edge {
        int v, w;
    }; vector<edge> e[maxn];

    struct node {
        int u, dis;
        
        bool operator>(const node &x) const {
            return dis > x.dis;
        } 
    };

    int n, m, s;

    void dijkstra(const int &sz, const int &st) {
        vector<int> dis(sz+1, inf);
        vector<bool> vis(sz+1, 0);
        priority_queue<node, vector<node>, greater<node> > pq;
        
        dis[st] = 0;
        pq.push((node){st, 0});
        while (!pq.empty()) {
            int u = pq.top().u; pq.pop();
            if (vis[u]) continue;
            vis[u] = 1;
            
            for (const auto &ed : e[u]) {
                int v = ed.v, w = ed.w;
                if (dis[v] > dis[u] + w) {
                    dis[v] = dis[u] + w;
                    pq.push((node){v, dis[v]});
                }
            }
        }
        
        for (int i=1; i<=n; ++i) {
            cout << dis[i] << (i == n ? "\n" : " ");
        }
    }

    signed main() {
        ios::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        
        cin >> n >> m >> s;
        for (int i=1; i<=m; ++i) {
            int u, v, w;
            cin >> u >> v >> w;
            
            e[u].push_back((edge){v, w});
        }
        
        dijkstra(n, s);
    }
    ```
