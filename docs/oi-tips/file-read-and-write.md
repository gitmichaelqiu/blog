---
comments: true
---

# C: FILE `freopen()`
head file: `<cstdio>

```cpp title="Definition"
std::FILE* freopen( const char* filename, const char* mode, std::FILE* stream );
```

## File Access Mode String
> From [CPPReference](https://en.cppreference.com/w/cpp/io/c/freopen)

| File access mode string | Meaning | Explanation | Action if file  already exists | Action if file  does not exist |
|:---:|:---:|:---:|:---:|:---:|
| "r" | read | Open a file for reading | read from start | return NULL and set error |
| "w" | write | Create a file for writing | destroy contents | create new |
| "a" | append | Append to a file | write to end | create new |
| "r+" | read extended | Open a file for read/write | read from start | return NULL and set error |
| "w+" | write extended | Create a file for read/write | destroy contents | create new |
| "a+" | append extended | Open a file for read/write | write to end | create new |

!!! note
    std::freopen is the only way to change the narrow/wide orientation of a stream once it has been established by an I/O operation or by std::fwide.

??? example
    ```cpp
    #include <cstdio>
    #include <iostream>
    using namespace std;

    int main() {
        freopen("in.in", "r", stdin);
        freopen("out.out", "w", stdout);

        int a, b;
        cin >> a >> b;
        cout << a * a + b * b << endl;
        return 0;
    }
    ```

!!! warning
    If you have used the [untie](accelerate-ios.md#untie) operation, you shouldn't use freopen because you would have already disabled `<cstdio>`.

???+ tip
    If you are using an [Online Judge](../some-websites.md#online-judges), you can add this macro definition to your code:

    ```cpp title="ONLINE_JUDGE"
    #ifdef ONLINE_JUDGE
    #else
    #endif
    ```

    Most OJ will use this macro definition, while your computer won't have one, thus you can add freopen in ONLINE_JUDGE so that you can use freopen as it'll be disabled on your OJ.

    ??? example
        ```cpp
        int main() {
            #ifdef ONLINE_JUDGE
            #else   // when run on local
                freopen("in.in", "r", "stdin");
                freopen("out.out", "w", "stdout");
            #endif
        }
        ```

# C++: fstream `fiostream`
## headfile: `<fiostream>`
=== "Read"
    ```cpp
    ifstream in("FILENAME", ios::in);
    ```

=== "Write"
    ```cpp
    ofstream out("FILENAME", ios::out);
    ```
=== "Read & Write"
    ```cpp
    fstream foi("FILENAME", ios::in|ios::out);
    ```

## function `open()`
=== "General Using"
    ```cpp
    void open(const char * filename,
        ios_base::openmode mode = ios_base::in | ios::base::out);
    ```

=== "Protocol"
    ```cpp
    void open(const wchar_t *_Filename,
        ios_base::in | ios_base::out, int prot = ios_base::_Openprot);
    ```

??? Parameters
    === "mode"
        ```cpp
            ios::app: //open the file as append  

            ios::ate: //Locate the file to the end of the file when it is opened. ios:app includes this property.  

            ios::binary: //Open the file as binary, the default is text. See the previous section for the difference between the two methods  
            
            ios::in: // the file is opened as input (file data is entered into memory)  

            ios::out: //files are opened as output (memory data is output to the file)  

            ios::nocreate: //doesn't create the file, so it fails to open if the file doesn't exist  

            ios::noreplace: // doesn't overwrite the file, so opening the file fails if the file exists  

            ios::trunc: // set file length to 0 if file exists
        ```

    === "prot" 
        ```text
            0: Ordinary file, open access  
            1: Read-only file  
            2: Implicit files  
            4: system file 
        ```

    !!! tip
        You can use "or" or "+" to connect the above attributes, such as 3 or 1 | 2 is to open the file with read-only and implicit attributes.

## Status Indicator
```cpp
is_open() //whether the file is normally open
bad() // read and write process whether the error
fail() // read and write process whether the error 
eof() // read the file to reach the end of the file, return true
good () // any of the above return true, this will return false
```