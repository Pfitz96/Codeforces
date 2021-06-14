// ==================================================
// https://codeforces.com/problemset/problem/313/A
// ==================================================

n = int(input())
g = str(n)
v = []
for i in g:
    v.append(i)
 
if v[-1] > v[-2]:
    v.pop(-1)
elif v[-1] < v[-2]:
    v.pop(-2)
else:
    v.pop(-2)
 
h ="".join(v)    
    
if n > 0:
    print(n)
elif h == "-0":
    print("0")
else:
    print("".join(v))

