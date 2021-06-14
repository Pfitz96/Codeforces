// ==================================================
// https://codeforces.com/problemset/problem/707/A
// ==================================================

n,m = list(map(int, input().split()))
colors = []
while n > 0:
    c = map(str, input().split())
    for i in c:
        colors.append(i.upper())
    n -= 1
 
if 'C' in colors or 'M' in colors or 'Y' in colors:
    print('#Color')
else:
    print('#Black&White')

