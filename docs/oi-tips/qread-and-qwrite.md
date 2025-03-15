---
comments: true
---

```cpp title="Quick Read"
char *P1,*P2,BUF[100000];
#define NC() (P1==P2 && (P2 = (P1=BUF) + fread(BUF, 1, 100000, stdin), P1==P2) ? EOF : *P1++)
int read() {
    int x = 0, f = 1;
    char CH = NC();
    while(CH < 48 || CH > 57)
    {
        if(CH == '-')
            f = -1;
        CH = NC();
    }
    while(CH>=48&&CH<=57)
        x = x*10 + CH-48, CH=NC();
   	return x*f;
}
```

```cpp title="Quick Write"
void write(int x) {
    if(x < 0)
        putchar('-'), x = -x;
    if(x > 9)
        qwrite(x/10);
    putchar(x%10 + '0');
    return;
}
```
