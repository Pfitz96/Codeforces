// ==================================================
// https://codeforces.com/problemset/problem/34/B
// ==================================================

n, m = map(int, input().split())
a = list(map(int, input().split()))
v = sorted(a)
count = 0
for i in range(1, m+1):
    no = v.pop(0)
    if no <= 0:
        count += abs(no)
 
print(count)

