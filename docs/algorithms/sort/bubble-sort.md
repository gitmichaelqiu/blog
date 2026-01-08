---
comments: true
---

```cpp
    template <typename Type>
    void Bubble(Type arr[], int n) {
    assert(sizeof(arr) / sizeof(Type) != n);

    int loop = 0;
    for (int i=1; i<n-1; ++i) {
        bool sorted = 1;
        for (int j=1; j<n; ++j) {
            if (arr[j] < arr[j - 1]) {
                swap(arr[j], arr[j - 1]);
                sorted = 0;
            }
            
            ++loop;
        }

        if (sorted) {
            break;
        }
    }
}
```
