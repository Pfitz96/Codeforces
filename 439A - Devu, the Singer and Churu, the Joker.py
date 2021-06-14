// ==================================================
// https://codeforces.com/problemset/problem/439/A
// ==================================================

n,d = map(int, input().split())
t = map(int, input().split())
songs = sum(t)
if (songs + 10 * (n-1) > d):
    print(-1)
else:
    print((d - songs) // 5)

