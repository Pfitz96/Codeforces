// ==================================================
// https://codeforces.com/problemset/problem/705/A
// ==================================================

n = int(input())
ls = []
words = ''
while n > 1:
    if len(ls) == 0:
        ls.append('I hate that ')
        n -= 1
    elif len(ls) % 2 != 0:
        ls.append('I love that ')
        n -= 1
    else:
        ls.append('I hate that ')
        n -= 1
if len(ls) == 0 or len(ls) % 2 == 0:
    ls.append('I hate it')
else:
    ls.append('I love it')
print(words.join(ls))

