// ==================================================
// https://codeforces.com/problemset/problem/141/A
// ==================================================

m = list(input().upper())
n = list(input().upper())
o = list(input().upper())
x = o[:]
for i in m:
    if i in x:
        x.remove(i)
        
for i in n:
    if i in x:
        x.remove(i)
        
if len(x) == 0 and len(o) == len(m + n):
    print('YES')
else:
    print('NO')

