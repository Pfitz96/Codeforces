// ==================================================
// https://codeforces.com/problemset/problem/1311/A
// ==================================================

t = int(input())
moves = []
while t > 0:
    a, b = map(int, input().split())
    if a == b:
        moves.append(0)
    elif a > b and (a - b) % 2 == 0:
        moves.append(1)
    elif a < b and (b - a) % 2 != 0:
        moves.append(1)
    else:
        moves.append(2)
    t -= 1
    
for i in moves:
    print(i)

