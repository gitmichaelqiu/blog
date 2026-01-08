---
comments: true
---

Time Complexity:

- Build: $O(n \log n)$
- Query: $O(1)$

---

=== "Head Files"
    ```cpp
    #include <vector>
    #include <algorithm>
    #include <functional>
    #include <cmath>
    ```
===  "C++ Version"
    ```cpp
    -std=c++11
    ```

```cpp title="build log2 table"
vector<int> _log2;
void build_log2(int x) {
    if (x < _log2.size()) return;

    _log2.resize(x+1);
    _log2[1] = 0;
    for (int i=2; i<=x; ++i) {
        _log2[i] = _log2[i >> 1] + 1;
    }
}
```

```cpp title="sparse_table"
template<typename Type>
class sparse_table {
using func_type = function<Type(const Type &, const Type &)>;
private:
    vector< vector<Type> > val;
    static Type default_func_type(const Type &x, const Type &y) { return max(x, y); }
    func_type opr;

public:
    sparse_table(const vector<Type> &v, func_type _opr = default_func_type) {
        opr = _opr;
        int row = v.size();

        if (_log2.empty()) { build_log2(row); }

        int col = ceil(_log2[row]) + 1;

        val.assign(row, vector<Type>(col, 0));
        for (int i=0; i<row; ++i) {
            val[i][0] = v[i];
        }
        for (int j=1; j<col; ++j) {
            int _j = (1 << (j-1));
            for (int i=0; i + _j < row; ++i) {
                val[i][j] = opr(val[i][j-1], val[i + (1 << (j-1))][j-1]);
            }
        }
    }

    Type query(int l, int r) {
        --l; --r;
        int len = r-l+1;
        int q = floor(_log2[len]);
        return opr(val[l][q], val[r - (1 << q) + 1][q]);
    }
};
```
