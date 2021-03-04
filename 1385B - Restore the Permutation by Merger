// ==================================================
// https://codeforces.com/problemset/problem/1385/B
// ==================================================

t = int(input())
p = []
str_p = []
ps = []
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i not in p:
            p.append(i)
    for i in p:
        str_p.append(str(i))
    ps.append(str_p)
    p = []
    a = []
    str_p = []
    t -= 1
for i in ps:
    print(' '.join(i))

