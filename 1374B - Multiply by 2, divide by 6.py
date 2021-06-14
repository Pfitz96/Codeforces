// ==================================================
// https://codeforces.com/problemset/problem/1374/B
// ==================================================

t = int(input())
count = 0
while t > 0:
    n = int(input())
    while n != 1:
        if count > 150:
            count = -1
            break
        elif n % 6 == 0:
            n = n // 6
            count += 1
        else:
            n = n * 2
            count += 1
            
    print(count)
    count = 0
    t -= 1

