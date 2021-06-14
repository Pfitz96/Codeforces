// ==================================================
// https://codeforces.com/problemset/problem/110/A
// ==================================================

n = input()
count = 0
for i in n:
    if i == '7' or i == '4':
        count = count + 1
counter = 0
for j in str(count):
    if j == '4' or j == '7':
        counter = counter + 1
 
if counter == len(str(count)):
    print('YES')
else:
    print('NO')


