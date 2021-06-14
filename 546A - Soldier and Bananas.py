// ==================================================
// https://codeforces.com/problemset/problem/546/A
// ==================================================

k, n, w = map(int, input().split())
x = 0
cnt = []
for i in range(0, w):
    x = k + (k * i)
    cnt.append(x)
 
cash = sum(cnt) - n
if cash <= 0:
    print(0)
else:
    print(cash)

