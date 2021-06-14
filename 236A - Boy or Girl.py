// ==================================================
// https://codeforces.com/problemset/problem/236/A
// ==================================================

user_name = input().lower()
letters = []
for i in user_name:
    if i not in letters:
        letters.append(i)
if len(letters) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')

