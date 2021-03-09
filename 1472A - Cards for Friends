// ==================================================
// https://codeforces.com/problemset/problem/1472/A
// ==================================================

t = int(input())
sheet = 1
while t > 0:
    w, h, n= map(int, input().split())
    while w % 2 == 0:
        w /= 2
        sheet *= 2
    while h % 2 == 0:
        h /= 2
        sheet *= 2
    t -= 1
    if sheet >= n:
        print('YES')
    else:
        print('NO')
    sheet = 1

