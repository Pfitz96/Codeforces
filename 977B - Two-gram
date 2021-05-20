
// ==================================================
// https://codeforces.com/problemset/problem/977/B
// ==================================================

n = int(input())
s = input()
count = 0
two_letters = []
for i in range(0, n-1):
    v = (s[i] + s[i+1])
    two_letters.append(v)
for i in two_letters:
    cnt = two_letters.count(i)
    if cnt > count:
        count = cnt
        letters = i
 
print(letters)

