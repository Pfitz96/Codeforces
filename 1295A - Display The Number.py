// ==================================================
// https://codeforces.com/problemset/problem/1295/A
// ==================================================

for i in range(int(input())):
    n = int(input())
    digits = []
    if n % 2 != 0:
        n = n - 3
        digits.append("7")
        n = n // 2
        digits.append(n * '1')
    else:
        n = n // 2
        digits.append(n * '1')
    print(''.join(digits))

