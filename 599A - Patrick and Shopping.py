// ==================================================
// https://codeforces.com/problemset/problem/599/A
// ==================================================


d1,d2,d3 = map(int, input().split())
dis1 = (d1 + d2) * 2
dis2 = (d2 + d3) * 2
dis3 = (d3 + d1) * 2
dis_total = d1 + d2 + d3
print(min(dis1 ,dis2 ,dis3 ,dis_total))

