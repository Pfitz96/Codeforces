// ==================================================
// https://codeforces.com/problemset/problem/723/A
// ==================================================

x = map(int, input().split())
loc = []
for i in x:
    loc.append(i)
print(max(loc)-min(loc))

