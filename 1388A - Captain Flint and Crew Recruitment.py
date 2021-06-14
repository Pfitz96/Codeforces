// ==================================================
// https://codeforces.com/problemset/problem/1388/A
// ==================================================

t = int(input())
v = ["6","10","14"]
g = ["6","10","15"]
while t > 0:
    n = int(input())
    if n <= 30:
        print('NO')
        
    elif n == 36 or n == 40 or n == 44:
        print('YES')
        d = n - 31
        g.append(str(d))
        print(' '.join(g))
    else:
        print('YES')
        d = n - 30
        v.append(str(d))
        print(' '.join(v))
    
    g = ["6","10","15"]
    v = ["6","10","14"]
    t -= 1

