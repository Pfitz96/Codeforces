// ==================================================
// https://codeforces.com/problemset/problem/71/A
// ==================================================


r = input()
w = int(r)
for i in range (w):
    x = input().lower()
    if (len(x) > 10):
        print(x[0] + str(len(x)- 2) + x[-1])
    else:
        print(x)


