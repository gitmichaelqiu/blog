---
comments: true
---

## Complexity

Time Complexity: $O(n^3)$

Space Complexity: $O(n^2)$

---

```cpp title="Floyd"
void floyd(int dis[][], int sz) {
    for (int k=1; i<=sz; ++i) {
        for (int x=1; x<=sz; ++x) {
            for (int y=1; y<=sz; ++y) {
                dis[x][y] = min(dis[x][y], dis[x][k] + dis[k][y]);
            }
        }
    }
}
```

## Problems

### [Luogu P119 灾后重建](https://www.luogu.com.cn/problem/P1119)

??? note "Solution"
    ```cpp
    #include <bits/stdc++.h>
    #define endl "\n"
    using namespace std;
    const int maxn = 202;
    const int maxm = 20000;
    const int inf = 0x3f3f3f3f;

    int n, m;
    vector< vector<int> > adj(maxn, vector<int>(maxn, inf));
    vector<int> t(maxn, 0);

    signed main() {
        ios::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        
        cin >> n >> m;
        
        for (int i=0; i<n; ++i) {
            adj[i][i] = 0;
        }
        
        for (int i=0; i<n; ++i) {
            cin >> t[i];
        } for (int i=0; i<m; ++i) {
            int x, y, z;
            cin >> x >> y >> z;
            adj[x][y] = adj[y][x] = z;
        }
        
        int Q; cin >> Q;
        int last = 0; // last accessed time
        while (Q--) {
            int x, y, z;
            cin >> x >> y >> z;

            if (t[x] > z || t[y] > z) {cout << -1 << endl; continue;}
            
            while (last < n && t[last] <= z) {
                // Floyd
                for (int i=0; i<n; ++i) {
                    for (int j=0; j<n; ++j) {
                        adj[i][j] = min(adj[i][j], adj[i][last] + adj[last][j]);
                    }
                }
                ++last;
            }
            
            cout << (adj[x][y] == inf ? -1 : adj[x][y]) << endl;
        }
    } 
    ```
