// ==================================================
// https://codeforces.com/problemset/problem/1454/A
// ==================================================

t = int(input())
nums = []
while t > 0:
    n = int(input())
    for i in range(2,n+1):
        nums.append(str(i))
    nums.append('1')
    print(' '.join(nums))
    nums.clear()
    t -= 1
    
    
