---
comments: true
---

Time Complexity:

- Emplace $O(1)$
- Pop: $O(1)$

---

```cpp title="mystack"
template <typename Type, size_t Size>
class mystack {
private:
    int cnt;
    Type val[Size];
    
public:
    mystack() {cnt=0;}

    void emplace(int x) {
        val[++cnt] = x;
    }

    void pop() {
        --cnt;
    }

    Type top() {
        return val[cnt];
    }

    bool empty() {
        return cnt == 0;
    }

    void clear() {
        cnt = 0;
    }
}
```
