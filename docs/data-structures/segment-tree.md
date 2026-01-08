---
comments: true
---

## Time Complexity:

- Build: $O(n)$
- Query: $O(\log n)$
- Update: $O(\log n)$
- Modify: $O(\log n)$

---

## Template

=== "Head Files"
    ```cpp
    #include <vector>
    #include <functional>
    ```
=== "C++ Version"
    ```cpp
    -std=c++11
    ```

### Integrated Version

```cpp title="Template"
template<typename Type>
class segment_tree {
using func_type = function<Type(const Type &, const Type &)>;
private:
    vector<Type> val;
    vector<Type> add_tag;
    vector<Type> set_tag;
    vector<bool> is_set;
    int len;
    
    inline int ls(const int &x) { return x << 1; }
    inline int rs(const int &x) { return x << 1 | 1; }
    
    func_type opr;
    static Type default_func_type(const Type &x, const Type &y) { return x + y; }
    
    void push_up(const int &x) {
        val[x] = opr(val[ls(x)], val[rs(x)]);
    }
    
    void add_tag_func(const int &x, const int &l, const int &r, const Type &d) {
        add_tag[x] += d;
        val[x] += d * (r - l + 1);
    }

    void set_tag_func(const int &x, const int &l, const int &r, const Type &d) {
        set_tag[x] = d;
        val[x] = d * (r - l + 1);
        add_tag[x] = 0;
        is_set[x] = true;
    }
    
    void push_down(const int &x, const int &l, const int &r) {
        int mid = (l + r) >> 1;
        if (is_set[x]) {
            set_tag_func(ls(x), l, mid, set_tag[x]);
            set_tag_func(rs(x), mid + 1, r, set_tag[x]);
            is_set[x] = false;
        }
        if (add_tag[x] != 0) {
            add_tag_func(ls(x), l, mid, add_tag[x]);
            add_tag_func(rs(x), mid + 1, r, add_tag[x]);
            add_tag[x] = 0;
        }
    }

    void build(const vector<Type> &s, const int &x, const int &l, const int &r) {
        add_tag[x] = 0;
        set_tag[x] = 0;
        is_set[x] = false;
        if (l == r) {
            val[x] = s[l];
            return;
        }
        
        int mid = (l + r) >> 1;
        build(s, ls(x), l, mid);
        build(s, rs(x), mid + 1, r);
        push_up(x);
    }

    Type query(const int &L, const int &R, const int x, const int &l, const int &r) {
        if (L <= l && r <= R) return val[x];
        push_down(x, l, r);
        
        Type res = Type();
        int mid = (l + r) >> 1;
        
        if (L <= mid) res = opr(res, query(L, R, ls(x), l, mid));
        if (R > mid) res = opr(res, query(L, R, rs(x), mid + 1, r));
        
        return res;
    }

    void update(const int &L, const int &R, const int &x, const int &l, const int &r, const Type &d) {
        if (L <= l && r <= R) {
            add_tag_func(x, l, r, d);
            return;
        }
        
        push_down(x, l, r);
        int mid = (l + r) >> 1;
        if (L <= mid) update(L, R, ls(x), l, mid, d);
        if (R > mid) update(L, R, rs(x), mid + 1, r, d);
        
        push_up(x);
    }

    void modify(const int &L, const int &R, const int &x, const int &l, const int &r, const Type &d) {
        if (L <= l && r <= R) {
            set_tag_func(x, l, r, d);
            return;
        }

        push_down(x, l, r);
        int mid = (l + r) >> 1;
        if (L <= mid) modify(L, R, ls(x), l, mid, d);
        if (R > mid) modify(L, R, rs(x), mid + 1, r, d);

        push_up(x);
    }

public:
    segment_tree(vector<Type> v, func_type _opr = default_func_type) {
        val.resize(v.size() << 2, Type());
        add_tag.resize(v.size() << 2, Type());
        set_tag.resize(v.size() << 2, Type());
        is_set.resize(v.size() << 2, false);
        len = v.size();
        opr = _opr;

        v.insert(v.begin(), Type());
        build(v, 1, 1, len);
    }

    int size() const {
        return len;
    }

    Type query(const int &L, const int &R) {
        return query(L, R, 1, 1, len);
    }
     
    void update(const int &L, const int &R, const Type &d) {
        update(L, R, 1, 1, len, d);
    }

    void modify(const int &L, const int &R, const Type &d) {
        modify(L, R, 1, 1, len, d);
    }
};
```

```cpp title="Usage"
signed main() {
    vector<int> a;
    int b[]={5, 4, 3, 2, 1};

    for (int i=0; i<5; ++i) {
        a.emplace_back(b[i]);
    }
    segment_tree<int> sg(a);

    cout << sg.query(1, 4) << endl;
    sg.update(1, 2, 2);
    cout << sg.query(1, 4) << endl;
    sg.modify(1, 2, 2);
    cout << sg.query(1, 4) << endl;
}
```

---

### Add Version

```cpp
class segment_tree {
using VI = vector<int>;
using CI = const int;

private:
    VI val, tag;
    int len;

    inline int ls(CI &x) {
        return x << 1;
    }
    inline int rs(CI &x) {
        return x << 1 | 1;
    }

    void push_up(CI &x) {
        val[x] = val[ls(x)] + val[rs(x)];
    }

    void add_tag(CI &x, CI &l, CI &r, CI &d) {
        tag[x] += d;
        val[x] += d * (l - r + 1);
    }

    void push_down(CI &x, CI &l, CI &r) {
        if (tag[x]) {
            int mid = (l + r) >> 1;
            add_tag(ls(x), l, mid, tag[x]);
            add_tag(rs(x), mid+1, r, tag[x]);
            tag[x] = 0;
        }
    }

    void build(const VI &s, CI &x, CI &l, CI &r) {
        tag[x] = 0;
        if (l == r) {
            val[x] = s[x];
            return;
        }

        int mid = (l + r) >> 1;
        build(s, ls(x), l, mid);
        build(s, rs(x), mid+1, r);
        push_up(x);
    }

    int query(CI &L, CI &R, CI &x, CI &l, CI &r) {
        if (L <= l && r <= R) {
            return val[x];
        }
        push_down(x, l, r);

        int ret = 0;
        int mid = (l+r) >> 1;

        if (L <= mid) ret += query(L, R, ls(x), l, mid);
        if (R > mid) ret += query(L, R, rs(x), mid+1, r);

        return ret;
    }

    void update(CI &L, CI &R, CI &x, CI &l, CI &r, CI &d) {
        if (L <= l && r <= R) {
            add_tag(x, l, r, d);
            return;
        }

        push_down(x, l, r);
        int mid = (l+r) >> 1;

        if (L <= mid) update(L, R, ls(x), l, mid, d);
        if (R > mid) update(L, R, rs(x), mid+1, r, d);

        push_up(x);
    }

public:
    segment_tree(VI &s) {
        val.resize(s.size() << 2, 0);
        tag.resize(s.size() << 2, 0);
        len = s.size();

        s.emplace(s.begin(), 0);
        build(s, 1, 1, len);
    }
};
```

<!-- === "Sum of Elements"
    ```cpp
    template<size_t Size>
    class segment_tree_sum {
    public:
        int val[Size << 2];
        
    private:
        int tag[Size << 2];
        
        int ls(const int &x) {return x << 1;}
        int rs(const int &x) {return x << 1 | 1;}
        
        void push_up(const int &x) {
            val[x] = val[ls(x)] + val[rs(x)];
        }
        
        void add_tag(const int &x, const int &l, const int &r, const int &d) {
            tag[x] += d;
            val[x] += d * (r - l + 1);
        }
        
        void push_down(const int &x, const int &l, const int &r) {
            if (tag[x]) {
                int mid = (l + r) >> 1;
                add_tag(ls(x), l, mid, tag[x]);
                add_tag(rs(x), mid+1, r, tag[x]);
                tag[x] = 0;
            }
        }
        
    public:
        void build(const int s[], const int &x, const int &l, const int &r) {
            tag[x] = 0;
            if (l == r) {
                val[x] = s[l];
                return;
            }
            
            int mid = (l + r) >> 1;
            build(s, ls(x), l, mid);
            build(s, rs(x), mid+1, r);
            push_up(x); 
        }
        
        int query(const int &L, const int &R, const int x, const int &l, const int &r) {
            if (L <= l && r <= R) return val[x];
            push_down(x, l, r);
            
            int res = 0;
            int mid = (l + r) >> 1;
            
            if (L <= mid) res += query(L, R, ls(x), l, mid);
            if (R > mid) res += query(L, R, rs(x), mid+1, r);
            
            return res;
        }
        
        void update(const int &L, const int &R, const int &x, const int &l, const int &r, const int &d) {
            if (L <= l && r >= R) {
                add_tag(x, l, r, d);
                return;
            }
            
            push_down(x, l, r);
            int mid = (l + r) >> 1;
            if (L <= mid) update(L, R, ls(x), l, mid, d);
            if (R > mid) update(L, R, rs(x), mid+1, r, d);
            
            push_up(x);
        }
    };
    ```

=== "Max Element"
    ```cpp
    template<size_t Size>
    class segment_tree_max {
    public:
        int val[Size << 2];
        
    private:
        int tag[Size << 2];
        
        int ls(const int &x) {return x << 1;}
        int rs(const int &x) {return x << 1 | 1;}
        
        void push_up(const int &x) {
            val[x] = val[ls(x)] > val[rs(x)] ? val[ls(x)] : val[rs(x)];
        }
        
        void add_tag(const int &x, const int &l, const int &r, const int &d) {
            tag[x] += d;
            val[x] += d * (r - l + 1);
        }
        
        void push_down(const int &x, const int &l, const int &r) {
            if (tag[x]) {
                int mid = (l + r) >> 1;
                add_tag(ls(x), l, mid, tag[x]);
                add_tag(rs(x), mid+1, r, tag[x]);
                tag[x] = 0;
            }
        }
        
    public:
        void build(const int s[], const int &x, const int &l, const int &r) {
            tag[x] = 0;
            if (l == r) {
                val[x] = s[l];
                return;
            }
            
            int mid = (l + r) >> 1;
            build(s, ls(x), l, mid);
            build(s, rs(x), mid+1, r);
            push_up(x); 
        }
        
        int query(const int &L, const int &R, const int x, const int &l, const int &r) {
            if (L <= l && r <= R) return val[x];
            push_down(x, l, r);
            
            int res = 0;
            int mid = (l + r) >> 1;
            
            if (L <= mid) res += query(L, R, ls(x), l, mid);
            if (R > mid) res += query(L, R, rs(x), mid+1, r);
            
            return res;
        }
        
        void update(const int &L, const int &R, const int &x, const int &l, const int &r, const int &d) {
            if (L <= l && r >= R) {
                add_tag(x, l, r, d);
                return;
            }
            
            push_down(x, l, r);
            int mid = (l + r) >> 1;
            if (L <= mid) update(L, R, ls(x), l, mid, d);
            if (R > mid) update(L, R, rs(x), mid+1, r, d);
            
            push_up(x);
        }
    };
    ```

=== "Min Element"
    ```cpp
    template<size_t Size>
    class segment_tree_min {
    public:
        int val[Size << 2];
        
    private:
        int tag[Size << 2];
        
        int ls(const int &x) {return x << 1;}
        int rs(const int &x) {return x << 1 | 1;}
        
        void push_up(const int &x) {
            val[x] = val[ls(x)] < val[rs(x)] ? val[ls(x)] : val[rs(x)];
        }
        
        void add_tag(const int &x, const int &l, const int &r, const int &d) {
            tag[x] += d;
            val[x] += d * (r - l + 1);
        }
        
        void push_down(const int &x, const int &l, const int &r) {
            if (tag[x]) {
                int mid = (l + r) >> 1;
                add_tag(ls(x), l, mid, tag[x]);
                add_tag(rs(x), mid+1, r, tag[x]);
                tag[x] = 0;
            }
        }
        
    public:
        void build(const int s[], const int &x, const int &l, const int &r) {
            tag[x] = 0;
            if (l == r) {
                val[x] = s[l];
                return;
            }
            
            int mid = (l + r) >> 1;
            build(s, ls(x), l, mid);
            build(s, rs(x), mid+1, r);
            push_up(x); 
        }
        
        int query(const int &L, const int &R, const int x, const int &l, const int &r) {
            if (L <= l && r <= R) return val[x];
            push_down(x, l, r);
            
            int res = 0;
            int mid = (l + r) >> 1;
            
            if (L <= mid) res += query(L, R, ls(x), l, mid);
            if (R > mid) res += query(L, R, rs(x), mid+1, r);
            
            return res;
        }
        
        void update(const int &L, const int &R, const int &x, const int &l, const int &r, const int &d) {
            if (L <= l && r >= R) {
                add_tag(x, l, r, d);
                return;
            }
            
            push_down(x, l, r);
            int mid = (l + r) >> 1;
            if (L <= mid) update(L, R, ls(x), l, mid, d);
            if (R > mid) update(L, R, rs(x), mid+1, r, d);
            
            push_up(x);
        }
    };
    ``` -->
