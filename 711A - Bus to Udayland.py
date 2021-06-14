// ==================================================
// https://codeforces.com/problemset/problem/711/A
// ==================================================

n = int(input())
bus = []
count = 0
for i in range(0,n):
    x = input()
    bus.append(x)
for j in range(0, n):
    if 'OO|OX' == bus[j]:
        bus[j] = '++|OX'
        count += 1
        break
    elif 'OO|XO' == bus[j]:
        bus[j] = '++|XO'
        count += 1
        break
    elif 'OO|XX' == bus[j]:
        bus[j] = '++|XX'
        count += 1
        break
    elif 'OO|OO' == bus[j]:
        bus[j] = '++|OO'
        count += 1
        break
    elif 'XO|OO' == bus[j]:
        bus[j] = 'XO|++'
        count += 1
        break
    elif 'OX|OO' == bus[j]:
        bus[j] = 'OX|++'
        count += 1
        break
    elif 'XX|OO' == bus[j]:
        bus[j] = 'XX|++'
        count += 1
        break
 
if count == 0:
    print('NO')
else:
    print('YES')
    for i in bus:
        print(i)

