// ==================================================
// https://codeforces.com/problemset/problem/96/A
// ==================================================

n = input()
count_1 = 0
count_0 = 0
d = False
for i in n:
    if i == "1":
        count_1 += 1
        count_0 = 0
        if count_1 > 6:
            d = True
            break
    else:
        count_0 += 1
        count_1 = 0
        if count_0 > 6:
            d = True
            break
if d:
    print('YES')
else:
    print('NO')

