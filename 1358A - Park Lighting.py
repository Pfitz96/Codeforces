// ==================================================
// https://codeforces.com/problemset/problem/1358/A
// ==================================================

t = int(input())
count = 0
numbs = []
while t > 0:
    n, m = map(int, input().split())
    if n % 2 == 0 and m % 2 == 0:
        count += (n * m) // 2
        numbs.append(count)
    elif n % 2 != 0 and m % 2 != 0:
        count += ((n - 1) * m) //2 + ((m + 1) // 2)
        numbs.append(count)
    elif n % 2 != 0 or n % 2 != 0:
        count += (n * m +1) // 2
        numbs.append(count)
    else:
        count += (n * m) // 2
        numbs.append(count)
    count = 0
    t -= 1
 
for i in numbs:
    print(i)

