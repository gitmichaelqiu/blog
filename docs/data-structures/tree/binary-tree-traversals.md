---
comments: true
---

```cpp title="node"
struct node {
    int val;
    node *ls, *rs;
}
```

## Preorder Traversal

```cpp
void preorder(node *rt) {
    cout << rt -> val << endl;
    preorder(rt -> ls);
    preorder(rt -> rs);
}
```

## Inorder Traversal

```cpp
void inorder(node *rt) {
    inorder(rt -> ls);
    cout << rt -> val << endl;
    inorder(rt -> rs);
}
```

## Postorder Traversal

```cpp
void postorder(node *rt) {
    postorder(rt -> ls);
    postorder(rt -> rs);
    cout << rt -> val << endl;
}
```

## Get Preorder Traversal

```cpp
```
