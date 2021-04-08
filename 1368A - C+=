// ==================================================
// https://codeforces.com/problemset/problem/1368/A
// ==================================================

t = int(input())
count = 0
for i in range(0, t):
    a, b, n= map(int, input().split())
    while a <= n and b <= n:
        if a > b:
            b += a
            count += 1
        elif b > a:
            a += b
            count += 1
        else:
            a += b
            count += 1
    print(count)
    count = 0

