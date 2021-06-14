// ==================================================
// https://codeforces.com/problemset/problem/1354/A
// ==================================================

for i in range(int(input())):
    a,b,c,d = map(int, input().split())
    if b >= a:
        print(b)
        continue
    if c <= d:
        print(-1)
        continue
    a -= b
    dif = c - d
    print(b + (a + dif - 1) // dif * c)

