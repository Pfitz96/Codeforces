
// ==================================================
// https://codeforces.com/problemset/problem/1324/A
// ==================================================

t = int(input())
while t > 0:
    n = int(input())
    a = sum(list(map(lambda x: int(x) % 2, input().split())))
    if a == 0 or a == n:
        print("YES")
    else:
        print("NO")
    t -= 1

