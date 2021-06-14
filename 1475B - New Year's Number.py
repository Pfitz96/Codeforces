// ==================================================
// https://codeforces.com/problemset/problem/1475/B
// ==================================================

t = int(input())
while t > 0:
    n = int(input())
    while n > 0:
        if n % 2020 == 0:
            n = n - 2020
        else:
            n = n - 2021
    if n == 0:
        print("YES")
    else:
        print("NO")
    t -= 1

