// ==================================================
// https://codeforces.com/problemset/problem/1234/A
// ==================================================

import math
q = int(input())
while q > 0:
    n = int(input())
    a = map(int, input().split())
    v = (sum(a) / n)
    print(math.ceil(v))
    q -= 1

