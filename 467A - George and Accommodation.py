// ==================================================
// https://codeforces.com/problemset/problem/467/A
// ==================================================

n = int(input())
count = 0
for i in range(0, n):
    p,q = map(int, input().split())
    if q - p >= 2:
        count += 1
    else:
        count += 0
print(count)

