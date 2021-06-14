// ==================================================
// https://codeforces.com/problemset/problem/381/A
// ==================================================

n = int(input())
cards = list(map(int, input().split()))
sereja = []
dima = []
while len(cards) > 0:
    if n % 2 == 0:
        if len(sereja) == 0 or len(cards) % 2 == 0:
            if cards[0] > cards[-1]:
                sereja.append(cards[0])
                cards.remove(cards[0])
            else:
                sereja.append(cards[-1])
                cards.remove(cards[-1])
        else:
            if cards[0] > cards[-1]:
                dima.append(cards[0])
                cards.remove(cards[0])
            else:
                dima.append(cards[-1])
                cards.remove(cards[-1])
    else:
        if len(sereja) == 0 or len(cards) % 2 != 0:
            if cards[0] > cards[-1]:
                sereja.append(cards[0])
                cards.remove(cards[0])
            else:
                sereja.append(cards[-1])
                cards.remove(cards[-1])
        else:
            if cards[0] > cards[-1]:
                dima.append(cards[0])
                cards.remove(cards[0])
            else:
                dima.append(cards[-1])
                cards.remove(cards[-1])
 
print(str(sum(sereja)) + ' ' + str(sum(dima)))

