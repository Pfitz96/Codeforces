// ==================================================
// https://codeforces.com/problemset/problem/32/B
// ==================================================

n = input()
m = []
j = []
for i in n:
    m.append(i)
while len(m) != 0:
    if m[0] == '-' and m[1] == '-':
        m.pop(0)
        m.pop(0)
        j.append('2')
    elif m[0] == '-' and m[1] == '.':
        m.pop(0)
        m.pop(0)
        j.append('1')
    else:
        m.pop(0)
        j.append('0')
print(''.join(j))

