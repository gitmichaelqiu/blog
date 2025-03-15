---
comments: true
---

# Most Common Quick Read & Write Function
## Quick Read `getchar()`
head file: `<cctype>`
=== "int"
    ```cpp
    int read() {
        int x=0, f=1; char ch=getchar();
        while (!isdigit(ch)) f = ((ch=='-') ? -1 : f);
        while (isdigt(ch)) x = (x<<1) + (x<<3) + (ch ^ 48), ch = getchar();
        return x * f;
    }
    ```

=== "All Types"
    ```cpp
    template<typename type>
    void read(type &x) {
        x=0; bool f(0); char ch=getchar();
        while(!isdigit(ch)) f = ch =='-', ch =getchar();
        while(isdigit(ch)) x = (x<<1) + (x<<3) + (ch^48), ch=getchar();
        f ? x=-x : 0;
    }
    ```
    
=== "Multi-Var"
    ```cpp
    template<typename type, typename ..._type>
    void read(type &x, _type&...y) {read(x), read(y);}
    ```

    > Add code above under the "All Types" code.

## Quick Write `putchar()`
=== "int"
    ```cpp
    void write(int x) {
        x<0 ? x=-x, putchar('-') : 0;
        x>9 ? putchar(x/10) : 0;
        putchar(x%10|48);
    }
    ```

=== "All Types"
    head file: `<cctype>`

    ```cpp
    template<typename type>
    void write(type x, bool md=1) {
        x<0 ? x=-x, putchar('-') : 0; static short bf[50], tp(0);
        do bf[++tp] = x%10, x /= 10; while(x);
        while(tp) putchar(bf[tp--]|48);
        md ? putchar('\n') : putchar(' ');
    }
    ```
    > md=0 for space

    > md=1 for new line

# Even Faster: `fread()`
We will just need to modify the `getchar()` function in the qread template above.

## `fread()`
```cpp title="Since C99"
size_t fread( void *restrict buffer, size_t size, size_t count,
    FILE *restrict stream );
```

### Parameters
buffer	-	pointer to the array where the read objects are stored

size	-	size of each object in bytes

count	-	the number of the objects to be read

stream	-	the stream to read

### Return Value
Number of objects read successfully, which may be less than `count` if an error or end-of-file condition occurs.

If `size` or `count` is zero, fread returns zero and performs no other action.

fread does not distinguish between end-of-file and error, and callers must use feof and ferror to determine which occurred.

## New Variables Needed
```cpp
char buf[1<<20], *p1=buf, *p2=buf;
```

- `buf`: buffer.
- `p1`: points to the currently read element.
- `p2`: points to the end of the buffer.

## Redefined `getchars()` Function
```cpp
#define getchar() (p1==p2&&(p2=(p1=buf)+fread(buf,1,1<<20,stdin),p1==p2)?EOF:*p1++)
```

# Even Faster: `fwrite`
We will just need to modify the `putchar()` function in the qread template above.
## `fwrite()`
```cpp
size_t fwrite( const void* restrict buffer, size_t size, size_t count,
    FILE* restrict stream );
```

## Parameters
buffer	-	pointer to the first object in the array to be written

size	-	size of each object

count	-	the number of the objects to be written

stream	-	pointer to the output stream

## Return Value
Number of objects read successfully, which may be less than `count` if an error or end-of-file condition occurs.

If `size` or `count` is zero, fread returns zero and performs no other action.

fread does not distinguish between end-of-file and error, and callers must use feof and ferror to determine which occurred.

## New Variables Needed
```cpp
char buf[1<<20], *p3=buf;
```
## Redefined `putchar()` Function
We implement a `flush()` function to output the buffer, so that it can be called many times in the future.

```cpp title="flush() Function"
#define flush() (fwrite(p3=out,1,1<<20,stdout))
```

You can actually take advantage of the principle of calling destructors at the end of a program by defining a class that calls flush() at the end of the program.

```cpp title="Destructor flush()"
class Flush{public:~Flush(){flush();}}_;
```

Now here's the redefined `putchar()` function
```cpp title="The Redefined putchar() Function"
#define putchar(ch) (p3==out+SIZE&&flush(),*p3++=(ch))
```