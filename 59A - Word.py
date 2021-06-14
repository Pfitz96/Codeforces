// ==================================================
// https://codeforces.com/problemset/problem/59/A
// ==================================================

s = input()
low = []
upp = []
for i in s:
    if i.isupper():
        upp.append(i)
    else:
        low.append(i)
if len(upp) > len(low):
    print(s.upper())
else:
    print(s.lower())


