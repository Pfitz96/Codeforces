// ==================================================
// https://codeforces.com/problemset/problem/116/A
// ==================================================

n = int(input())
x = []
while n > 0:
    a = list(map(int, input().split()))
    x.append(a)
    n = n - 1
max_num = 0
count = 0
for i in x:
    count = count - i[0] + i[1]
    if max_num < count:
        max_num = count
print(max_num)

