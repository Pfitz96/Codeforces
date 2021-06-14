// ==================================================
// https://codeforces.com/problemset/problem/61/A
// ==================================================

n = input()
m = input()
n_ls = []
m_ls = []
dc = []
out = ''
for i in n:
    n_ls.append(i)
for j in m:
    m_ls.append(j)
for i in range(0, len(n)):
    if n_ls[i] > m_ls[i]:
        dc.append(n_ls[i])
    elif m_ls[i] > n_ls[i]:
        dc.append(m_ls[i])
    else:
        dc.append('0')
print(out.join(dc))

