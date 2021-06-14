// ==================================================
// https://codeforces.com/problemset/problem/443/A
// ==================================================

myset = set(input())
second_set = set()
for i in myset:
    if i.isalpha():
        second_set.add(i.lower())
print(len(second_set))

