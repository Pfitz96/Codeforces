// ==================================================
// https://codeforces.com/problemset/problem/263/A
// ==================================================

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
e = list(map(int, input().split()))
count = 0
if 1 in a:
    c = a[:]
    count += 2
elif 1 in b:
    c = b[:]
    count += 1
elif 1 in d:
    c = d[:]
    count += 1
elif 1 in e:
    c = e[:]
    count += 2
else:
    count += 0
if 1 in c:
    if 1 == c[0] or 1 == c[4]:
        count += 2
    elif 1 == c[1] or 1 == c[3]:
        count += 1
    else:
        count += 0
print(count)

