---
comments: true
---

## Complexity

Time Complexity: $O(nm)$

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
vector<edge> e[maxn];
```

```cpp title="Template"
vector<int> spfa(const int &sz, const int &st) {
	vector<int> dis(maxn, inf);
	vector<bool> vis(maxn, 0);
	queue<int> q;
	
	dis[st] = 0;
	vis[st] = 1;
	q.push(st);
	while (!q.empty()) {
		int u = q.front(); q.pop();
		vis[u] = 0;
		
		for (const auto &ed : e[u]) {
			int v = ed.v, w = ed.w;
			if (dis[v] > dis[u] + w) {
				dis[v] = dis[u] + w;
				
				if (!vis[v]) {
					q.push(v);
					vis[v] = 1;
				}
			}
		}
	}
	
    return dis;
}
```

## Problems

[Luogu P3371](https://www.luogu.com.cn/problem/P3371)

???- note "Solution"
    ```cpp
    #include <bits/stdc++.h>
    #define int unsigned long long
    using namespace std;
    const int maxn = 2e5 + 2;
    const int inf = (1ull<<31) - 1;

    struct edge {
        int v, w;
    };
    vector<edge> e[maxn];

    void spfa(const int &sz, const int &st) {
        vector<int> dis(maxn, inf);
        vector<bool> vis(maxn, 0);
        queue<int> q;
        
        dis[st] = 0;
        vis[st] = 1;
        q.push(st);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            vis[u] = 0;
            
            for (const auto &ed : e[u]) {
                int v = ed.v, w = ed.w;
                if (dis[v] > dis[u] + w) {
                    dis[v] = dis[u] + w;
                    
                    if (!vis[v]) {
                        q.push(v);
                        vis[v] = 1;
                    }
                }
            }
        }
        
        for (int i=1; i<=sz; ++i) {
            cout << dis[i] << " ";
        }
    }

    int n, m, s;

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
        
        spfa(n, s);
    }
    ```
