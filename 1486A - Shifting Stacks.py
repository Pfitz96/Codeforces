// ==================================================
// https://codeforces.com/problemset/problem/1486/A
// ==================================================

t = int(input())
while t > 0:
    n = int(input())
    h = list(map(int, input().split()))
    ans = True
    current_num = 0
    next_num = 0
    for i in h:
        for j in range(n):
            current_num += j
            next_num += h[j]
            if current_num > next_num:
                ans = False
    if ans:
        print("YES")
    else:
        print("NO")
    t -= 1

