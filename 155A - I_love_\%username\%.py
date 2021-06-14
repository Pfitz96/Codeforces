// ==================================================
// https://codeforces.com/problemset/problem/155/A
// ==================================================

n = int(input())
k = list(map(int, input().split()))
records = []
count = 0
for i in k:
    if len(records) == 0:
        records.append(i)
    elif i > max(records) or i < min(records):
        records.append(i)
        count += 1
print(count)

