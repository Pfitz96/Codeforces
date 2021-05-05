// ==================================================
// https://codeforces.com/problemset/problem/160/A
// ==================================================

n = int(input())
a = list(map(int, input().split()))
count = 0
coins = sorted(a)
noob = []
while sum(noob) <= sum(coins):
    v = coins.pop(-1)
    noob.append(v)
    count += 1
print(count)

