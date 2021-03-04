// ==================================================
// https://codeforces.com/problemset/problem/1360/B
// ==================================================

t = int(input())
dif = []
min_dif = []
while t > 0:
    n = int(input())
    s = list(map(int, input().split()))
    j = sorted(s)
    for i in range(0, n-1):
        x = (j[i + 1] - j[i])
        min_dif.append(x)
        x = 0
    dif.append(min(min_dif))
    min_dif.clear()
    t -= 1
for i in dif:
    print(i)

