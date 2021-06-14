// ==================================================
// https://codeforces.com/problemset/problem/282/A
// ==================================================

n = int(input())
 
x = 0
for i in range(0,n):
    z = input().lower()
    if z == '++x' or z == 'x++':
        x += 1
    elif z == '--x' or z == 'x--':
        x -= 1
    else:
        pass
print(x)

