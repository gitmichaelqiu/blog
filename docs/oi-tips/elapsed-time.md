---
comments: true
---

```cpp title="Head File"
#include <chrono>
```

```cpp title="global variables"
auto chrono_start_time = chrono::high_resolution_clock::now();
```

```cpp title="Start Measuring"
void start_measuring() {
    chrono_start_time = chrono::high_resolution_clock::now();
}
```

=== "Milliseconds"
    ```cpp title="End Measuring"
    void end_measuring() {
        auto chrono_end_time = chrono::high_resolution_clock::now();
        chrono::duration<double, milli> chrono_elapsed_seconds = chrono_end_time - chrono_start_time;
        double chrono_elapsed_ms = chrono_elapsed_seconds.count();
        cout << "Elapsed time: " << chrono_elapsed_ms << "ms" << endl;
    }
    ```

=== "Seconds"
    ```cpp title="End Measuring"
    void end_measuring() {
        auto chrono_end_time = chrono::high_resolution_clock::now();
        chrono::duration<double> chrono_elapsed_seconds = chrono_end_time - chrono_start_time;
        double chrono_elapsed_ms = chrono_elapsed_seconds.count();
        cout << "Elapsed time: " << chrono_elapsed_ms << "s" << endl;
    }
    ```
=== "Minutes"
    ```cpp title="End Measuring"
    void end_measuring() {
        auto chrono_end_time = chrono::high_resolution_clock::now();
        chrono::duration< double, ratio<60> > chrono_elapsed_seconds = chrono_end_time - chrono_start_time;
        double chrono_elapsed_ms = chrono_elapsed_seconds.count();
        cout << "Elapsed time: " << chrono_elapsed_ms << "min" << endl;
    }
    ```
