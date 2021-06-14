// ==================================================
// https://codeforces.com/problemset/problem/80/A
// ==================================================

prime_numbers  = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
big = []
small = []
n, m = map(int, input().split())
for i in prime_numbers:
    if i > n:
        big.append(i)
    elif i <= n:
        small.append(i)
if m == big[0]:
    print('YES')
else:
    print('NO')

