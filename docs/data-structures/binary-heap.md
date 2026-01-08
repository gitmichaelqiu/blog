---
comments: true
---

Time Complexity:

- Emplace: $O(\log n)$
- Pop: $O(\log n)$

---

=== "Head Files"
	```cpp
	#include <cstddef>
	#include <algorithm>
	```
=== "C++ Version"
	```cpp
	-std=c++11
	```

```cpp title="Template"
template <typename Type, size_t Size>
class heap {
private:
	int cnt;
	Type val[Size];

public:
	heap() {cnt=0;}
	
	void emplace(int x) {
		val[++cnt] = x;
		int now = cnt;
	
		while (now){
			int fa = now >> 1;
			
			if (val[fa] > val[now]) {
				swap(val[fa], val[now]);
			} else {
				break;
			}
				
			now = fa;
		}
	}
	
	void pop() {
		swap(val[cnt--], val[1]);
		
		int now = 1;
		while ((now << 1) <= cnt) { 
	    	int ls = now << 1;
	    	
	        if (ls+1 <= cnt && val[ls+1] < val[ls]) {
				++ls;
			}
	        if (val[ls] < val[now]) {
				swap(val[now], val[ls]);
			} else {
				break;
			}
			
	        now = ls;
		}
	}
	
	int size() {
		return cnt;	
	}

	bool empty() {
		return cnt == 0;
	}
	
	Type top() {
		return val[1];
	}
};
```
