// ==================================================
// https://codeforces.com/problemset/problem/276/A
// ==================================================

n, k= map(int, input().split())
lunch = []
for i in range(n):
    f, t= map(int, input().split())
    if t > k:
        fun = f-(t-k)
        lunch.append(fun)
    else:
        fun = f
        lunch.append(fun)
print(max(lunch))

