// ==================================================
// https://codeforces.com/problemset/problem/791/A
// ==================================================

limak, bob =map(int, input().split())
count = 0
while limak <= bob:
    limak = limak * 3
    bob = bob * 2
    count += 1
print(count)

