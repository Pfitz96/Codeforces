// ==================================================
// https://codeforces.com/problemset/problem/158/A
// ==================================================

n, k = map(int, input().split())
a = list(map(int, input().split()))
count = 0
for i in range(0, n):
    if a[k-1] == 0 and a[i] == a[k-1]:
        count += 0
    elif a[k-1] <= a[i]:
        count += 1
    else:
        count += 0
print(count)

