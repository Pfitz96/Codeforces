// ==================================================
// https://codeforces.com/problemset/problem/978/B
// ==================================================

n = int(input())
letters = input()
v = 0
count = 0
for i in letters:
    if i == 'x':
        v += 1
        if v > 2:
            count += 1
    else:
        v = 0
print(count)

