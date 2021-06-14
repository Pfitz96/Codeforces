// ==================================================
// https://codeforces.com/problemset/problem/1369/A
// ==================================================

t = int(input())
good = []
while t > 0:
    n = int(input())
    if n % 4 == 0:
        good.append('YES')
    else:
        good.append('NO')
    t -= 1
 
for i in good:
    print(i)

