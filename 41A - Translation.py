// ==================================================
// https://codeforces.com/problemset/problem/41/A
// ==================================================


s = input().lower()
t = input().lower()
s_list = []
t_list = []
for i in s:
    s_list.append(i)
for j in t:
    t_list.insert(0, j)
if s_list == t_list:
    print('YES')
else:
    print('NO')


