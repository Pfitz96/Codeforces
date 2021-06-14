// ==================================================
// https://codeforces.com/problemset/problem/405/A
// ==================================================

n = int(input())
a = list(map(int, input().split()))
c = sorted(a)
b = []
for i in c:
    b.append(str(i))
print(' '.join(b))

