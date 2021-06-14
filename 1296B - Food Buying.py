// ==================================================
// https://codeforces.com/problemset/problem/1296/B
// ==================================================

import math
t = int(input())
while t > 0:
    s = int(input())
    if s % 9 == 0:
        v = s // 9
        d = math.floor(v)
        s = s + d
        print(s-1)
    elif s > 9:
        v = s // 9
        d = math.floor(v)
        s = s + d
        print(s)
    else:
        print(s)
    t -= 1

