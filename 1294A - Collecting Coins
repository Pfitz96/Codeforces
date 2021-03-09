// ==================================================
// https://codeforces.com/problemset/problem/1294/A
// ==================================================

t = int(input())
out = []
while t > 0:
    a,b,c,n = map(int, input().split())
    if a >= b and a >= c:
        if n < ((2 * a) - (b + c)):
            out.append('NO')
        elif (n - ((2 * a)- (b +c))) % 3 == 0:
            out.append('YES')
        else:
            out.append('NO')
    
    elif c >= b and c >= a:
        if n < ((2 * c) - (b + a)):
            out.append('NO')
        elif (n - ((2 * c)- (b + a))) % 3 == 0:
            out.append('YES')
        else:
            out.append('NO')
            
    elif b >= c and b >= a:
        if n < ((2 * b) - (c + a)):
            out.append('NO')
        elif (n - ((2 * b)- (c + a))) % 3 == 0:
            out.append('YES')
        else:
            out.append('NO')
    t -= 1
 
for i in out:
    print(i)

