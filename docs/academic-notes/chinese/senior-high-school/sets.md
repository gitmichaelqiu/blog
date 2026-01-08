# 集合及基本关系
## 定义
对象(即元素)所构成的整体

## 表示
**集合:** 大写字母 $\mathbb{A}, \mathbb{B}, \mathbb{C},...$

**元素:** 小写字母 $a, b, c,...$

## 写法
### 数集的写法
=== "列举法"
    $\mathbb{A} = \\{a, b, c, ..., z\\}$

=== "描述法"
    $\mathbb{A} = \\{x \mid p(x)\\}$ [^1]

[^1]: 默认 $x \in \mathbb{R}$

???+ note "特殊的集合"
    $\mathbb{N}$: 自然数集

    $\mathbb{N}_+\ or\ \mathbb{N}^*$: 正整数集

    $\mathbb{Z}$: 整数集

    $\mathbb{Q}$: 有理数集

    $\mathbb{R}$: 实数集

    $\mathbb{C}$: 复数集

### 关系的写法
=== "元素与集合的关系"
    属于: $a \in \mathbb{A}$

    不属于: $b \notin \mathbb{A}$

=== "集合与集合的关系"
    子集: $\mathbb{B} \subseteq \mathbb{A}
    \iff
    \mathbb{A} \supseteq \mathbb{B}
    $

    相等: $\mathbb{A} = \mathbb{B}$

    真子集: $\mathbb{B} \subsetneqq \mathbb{A}
    \iff
    \mathbb{A} \supsetneqq \mathbb{B}
    $

## 数集 & 点集
数集，表范围: $\mathbb{A} = \\{x \mid p(x)\\}$

点集，表图像: $\mathbb{B} = \\{(x, y) \mid y = x^2 \\}$

# 集合间的运算及运用
=== "交集"
    $\mathbb{A} \cap \mathbb{B} = \\{x \mid x \in \mathbb{A}\ and\ x \in \mathbb{B}\\}$

    即对集合进行 "与 $\land$" 操作

=== "并集"
    $\mathbb{A} \cup \mathbb{B} = \\{x \mid x \in \mathbb{A}\ or\ x \in \mathbb{B}\\}$

    即对集合进行 "或 $\lor$" 操作

=== "补集"
    $\complement_\mathbb{U} \mathbb{A} = \\{x \mid x \in \mathbb{U}\ and\ x \notin \mathbb{A}\\}$

???+ tip "运算变形 & 性质"
    === "并集的性质"
        $\mathbb{A} \cup \emptyset = \mathbb{A}$

        $(\mathbb{A} \cup \mathbb{B}) \supseteq \mathbb{A}$

        $\mathbb{A} \cup \mathbb{B} \iff \mathbb{B} \subseteq \mathbb{A}$

    === "补集的性质"
        $\complement_\mathbb{U} \mathbb{U} = \emptyset$

        $\complement_\mathbb{U} \emptyset = \mathbb{U}$

        $\complement_\mathbb{U} (\complement_\mathbb{U} \mathbb{A}) = \mathbb{A}$

        $\mathbb{A} \cup (\complement_\mathbb{U} \mathbb{A}) = \mathbb{U}$

        $\mathbb{A} \cap (\complement_\mathbb{U} \mathbb{A}) = \emptyset$