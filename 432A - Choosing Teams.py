// ==================================================
// https://codeforces.com/problemset/problem/432/A
// ==================================================

n, k= map(int, input().split())
y = map(int, input().split())
count = 0
for i in y:
    if 5 - k >= i:
        count += 1
    else:
        pass
print(count//3)

