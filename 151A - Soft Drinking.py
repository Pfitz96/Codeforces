// ==================================================
// https://codeforces.com/problemset/problem/151/A
// ==================================================

n, k, l, c, d, p, nl, np = map(int, input().split())
toasts = (k * l) // nl
lime_slices = c * d
salt = p // np
mix =(min(toasts,lime_slices,salt)//n)
print(mix)

