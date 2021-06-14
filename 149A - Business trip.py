// ==================================================
// https://codeforces.com/problemset/problem/149/A
// ==================================================

k = int(input())
a = list(map(int, input().split()))
v = sorted(a)
count = 0
cnt = 0
while count < k:
    if len(v) != 0:
        w = v.pop(-1)
        count += w
        cnt += 1
    else:
        cnt = -1
        break
print(cnt)

