// ==================================================
// https://codeforces.com/problemset/problem/1374/A
// ==================================================

t = int(input())
rez = []
while t > 0:
    x ,y ,n = map(int, input().split())
    t -= 1
    if (n - n % x + y <= n):
        j = (n - n % x + y)
        rez.append(j)
    else:
        j = (n - n % x - (x - y))
        rez.append(j)
for i in rez:
    print(i)

