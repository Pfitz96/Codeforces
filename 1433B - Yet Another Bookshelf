// ==================================================
// https://codeforces.com/problemset/problem/1433/B
// ==================================================

t = int(input())
count = 0
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    while a[0] != 1 or a[-1] != 1:
        if a[0] == 0:
            a.pop(0)
        elif a[-1] == 0:
            a.pop(-1)
    for i in a:
        if i == 0:
            count += 1
    print(count)
    count = 0
    t -= 1

