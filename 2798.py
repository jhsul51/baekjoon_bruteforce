#check all the possible cases, nC3
N,M = map(int,input().split())
cards = list(map(int,input().split()))
pick = 0
for i in range(len(cards)-2):
    for j in range(i+1, len(cards)-1):
        for k in range(j+1, len(cards)):
            now = cards[i] + cards[j] + cards[k]
            if now <= M and M-pick > M-now:
                pick = now
print(pick)
