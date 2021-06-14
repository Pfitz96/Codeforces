// ==================================================
// https://codeforces.com/problemset/problem/703/A
// ==================================================

n = int(input())
mishka = 0
chris = 0
while n > 0:
    m, c = map(int, input().split())
    if m > c:
        mishka += 1
    elif c > m:
        chris += 1
    else:
        chris += 1
        mishka += 1
    n -= 1
if mishka > chris:
    print('Mishka')
elif chris > mishka:
    print('Chris')
else:
    print('Friendship is magic!^^')

