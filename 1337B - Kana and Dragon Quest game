// ==================================================
// https://codeforces.com/problemset/problem/1337/B
// ==================================================

t = int(input())
while t > 0:
    x,n,m= map(int, input().split())
    while x > 0 or n == 0 and m == 0:
        if x > 20 and n > 0:
            x = (x//2) + 10
            n -= 1
        elif m > 0:
            x = x - 10
            m -= 1
        else:
            break
    if x <= 0:
        print("YES")
    else:
        print("NO")
    t -= 1


