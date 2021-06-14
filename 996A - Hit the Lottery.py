// ==================================================
// https://codeforces.com/problemset/problem/996/A
// ==================================================

n = int(input())
count = 0
while n != 0:
    if n >= 100:
        n = n - 100
        count += 1
    elif n >= 20:
        n = n - 20
        count += 1
    elif n >= 10:
        n = n - 10
        count += 1
    elif n >= 5:
        n = n - 5
        count += 1
    else:
        n = n - 1
        count += 1
print(count)

