// ==================================================
// https://codeforces.com/problemset/problem/750/A
// ==================================================

n, k= map(int, input().split())
time_left = 240 - k
solve = 0
count = 0
for i in range(1, n+1):
    if solve <= time_left:
        solve += 5 * i
        if solve <= time_left:
            count += 1
        else:
            count += 0
            
print(count)

