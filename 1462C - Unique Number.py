
// ==================================================
// https://codeforces.com/problemset/problem/1462/C
// ==================================================

for i in range(int(input())):
    x = int(input())
    v = []
    unique = 9
    d = False
    if x > 45:
        d = True
    else:
        while x > 0:
            if x >= unique:
                x -= unique
                v.insert(0,str(unique))
                unique -= 1
            else:
                unique -= 1
 
    if d:
        print("-1")
    else:
        print("".join(v))
 
    v = []


// ==================================================
// another way
// ==================================================

for i in range(int(input())):
    x = int(input())
    v = []
    d = False
    if x > 45:
        d = True
    else:
        while x > 0:
            if x >= 9 and "9" not in v:
                x -= 9
                v.append("9")
            elif x >= 8 and "8" not in v:
                x -= 8
                v.insert(0,"8")
            elif x >= 7 and "7" not in v:
                x -= 7
                v.insert(0,"7")
            elif x >= 6 and "6" not in v:
                x -= 6
                v.insert(0,"6")
            elif x >= 5 and "5" not in v:
                x -= 5
                v.insert(0,"5")
            elif x >= 4 and "4" not in v:
                x -= 4
                v.insert(0,"4")
            elif x >= 3 and "3" not in v:
                x -= 3
                v.insert(0,"3")
            elif x >= 2 and "2" not in v:
                x -= 2
                v.insert(0,"2")
            elif x >= 1 and "1" not in v:
                x -= 1
                v.insert(0,"1")
    
    if d:
        print("-1")
    else:
        print("".join(v))
    
    v = []


