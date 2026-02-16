---
comments: true
---

# Bignum

## Time Complexity:

- Addition: $O(n)$
- Subtraction: $O(n)$
- Comparison: $O(n)$
- Multiplication: $O(n \cdot m)$
- Division: $O(n \cdot m)$

---

## Template

=== "Head Files"
    ```cpp
    #include <iostream>
    #include <vector>
    #include <string>
    #include <algorithm>
    ```
=== "C++ Version"
    ```cpp
    -std=c++11
    ```

```cpp title="Template"
struct Bignum {
    static const int BASE = 1000000000;
    std::vector<int> digits;
    bool negative;

    Bignum() : negative(false) {}
    Bignum(long long v) : negative(false) {
        if (v < 0) negative = true, v = -v;
        if (v == 0) digits.push_back(0);
        while (v > 0) {
            digits.push_back(v % BASE);
            v /= BASE;
        }
    }
    Bignum(std::string s) : negative(false) {
        if (s.empty()) { digits.push_back(0); return; }
        if (s[0] == '-') { negative = true; s = s.substr(1); }
        for (int i = s.size(); i > 0; i -= 9) {
            if (i < 9) digits.push_back(std::stoi(s.substr(0, i)));
            else digits.push_back(std::stoi(s.substr(i - 9, 9)));
        }
        trim();
    }

    void trim() {
        while (digits.size() > 1 && digits.back() == 0) digits.pop_back();
        if (digits.empty()) digits.push_back(0);
        if (digits.size() == 1 && digits[0] == 0) negative = false;
    }

    bool operator<(const Bignum& other) const {
        if (negative != other.negative) return negative;
        if (digits.size() != other.digits.size())
            return (digits.size() < other.digits.size()) ^ negative;
        for (int i = digits.size() - 1; i >= 0; i--) {
            if (digits[i] != other.digits[i])
                return (digits[i] < other.digits[i]) ^ negative;
        }
        return false;
    }
    bool operator>(const Bignum& other) const { return other < *this; }
    bool operator<=(const Bignum& other) const { return !(*this > other); }
    bool operator>=(const Bignum& other) const { return !(*this < other); }
    bool operator==(const Bignum& other) const { return negative == other.negative && digits == other.digits; }
    bool operator!=(const Bignum& other) const { return !(*this == other); }

    Bignum operator-() const {
        Bignum res = *this;
        if (res != 0) res.negative = !res.negative;
        return res;
    }

    Bignum operator+(const Bignum& other) const {
        if (negative == other.negative) {
            Bignum res = *this;
            for (int i = 0, carry = 0; i < std::max(res.digits.size(), other.digits.size()) || carry; i++) {
                if (i == res.digits.size()) res.digits.push_back(0);
                long long cur = (long long)res.digits[i] + carry + (i < other.digits.size() ? other.digits[i] : 0);
                res.digits[i] = cur % BASE;
                carry = cur / BASE;
            }
            return res;
        }
        return *this - (-other);
    }

    Bignum operator-(const Bignum& other) const {
        if (negative != other.negative) return *this + (-other);
        if (negative) return (-other) - (-*this);
        if (*this < other) return -(other - *this);
        Bignum res = *this;
        for (int i = 0, carry = 0; i < other.digits.size() || carry; i++) {
            long long cur = res.digits[i] - carry - (i < other.digits.size() ? other.digits[i] : 0);
            carry = cur < 0;
            if (carry) cur += BASE;
            res.digits[i] = cur;
        }
        res.trim();
        return res;
    }

    Bignum operator*(const Bignum& other) const {
        Bignum res;
        res.negative = negative != other.negative;
        res.digits.resize(digits.size() + other.digits.size(), 0);
        for (int i = 0; i < digits.size(); i++) {
            long long carry = 0;
            for (int j = 0; j < other.digits.size() || carry; j++) {
                long long cur = res.digits[i + j] + digits[i] * 1LL * (j < other.digits.size() ? other.digits[j] : 0) + carry;
                res.digits[i + j] = cur % BASE;
                carry = cur / BASE;
            }
        }
        res.trim();
        return res;
    }

    friend std::ostream& operator<<(std::ostream& os, const Bignum& b) {
        if (b.negative) os << '-';
        os << b.digits.back();
        for (int i = b.digits.size() - 2; i >= 0; i--) {
            std::string s = std::to_string(b.digits[i]);
            os << std::string(9 - s.size(), '0') << s;
        }
        return os;
    }
};
```

```cpp title="Usage"
signed main() {
    Bignum a("12345678901234567890");
    Bignum b(987654321);
    
    cout << "a + b = " << a + b << endl;
    cout << "a - b = " << a - b << endl;
    cout << "a * b = " << a * b << endl;
    
    if (a > b) cout << "a is greater than b" << endl;
    
    return 0;
}
```
