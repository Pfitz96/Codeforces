// ==================================================
// https://codeforces.com/problemset/problem/1472/B
// ==================================================

t = int(input())
candy_1 = []
candy_2 = []
while t > 0:
    n = int(input())
    a = map(int, input().split())
    for i in a:
        if i == 1:
            candy_1.append(i)
        else:
            candy_2.append(i)
    
    if len(candy_2) % 2 != 0 and len(candy_1) % 2 == 0 and len(candy_1) >= 2:
        print('yes')
    elif (sum(candy_1) + sum(candy_2)) % 2 == 0 and len(candy_1) >= 2:
        print('Yes')
    elif len(candy_2) % 2 == 0 and len(candy_1) == 0 or len(candy_1) % 2 == 0 and len(candy_2) == 0:
        print('yes')
    else:
        print('no')
    
    candy_1.clear()
    candy_2.clear()
    t -= 1
 
 
