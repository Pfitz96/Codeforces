// ==================================================
// https://codeforces.com/problemset/problem/556/A
// ==================================================

n = int(input())
m = input()
v = m.replace("0","")
d = m.replace("1","")
print(len(m)-(min(len(v),len(d)) * 2))

