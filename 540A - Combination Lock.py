// ==================================================
// https://codeforces.com/problemset/problem/540/A
// ==================================================

n = int(input())
g = list(input())
s = list(input())
a = []
b = []
count = 0
for i in g:
    a.append(int(i))
for j in s:
    b.append(int(j))
for k in range(0,n):
    v = (min(abs(a[k] - b[k]), 10 - abs(a[k] - b[k])))
    count += v
print(count)

