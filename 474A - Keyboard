// ==================================================
// https://codeforces.com/problemset/problem/474/A
// ==================================================

qwe = "qwertyuiop"
asd = "asdfghjkl;"
zxc = "zxcvbnm,./"
direction = input().upper()
letters = input()
words = []
if direction == "R":
    for i in letters:
        if i in qwe:
            x = qwe.find(i)
            words.append(qwe[x-1])
        elif i in asd:
            x = asd.find(i)
            words.append(asd[x-1])
        else:
            x = zxc.find(i)
            words.append(zxc[x-1])
 
else:
    for i in letters:
        if i in qwe:
            x = qwe.find(i)
            words.append(qwe[x+1])
        elif i in asd:
            x = asd.find(i)
            words.append(asd[x+1])
        else:
            x = zxc.find(i)
            words.append(zxc[x+1])
 
print("".join(words))

