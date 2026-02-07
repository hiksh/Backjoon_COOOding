N, K = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))

n = 0
price = 0
while price != K:
    x = K - price
    for i in range(1, N+1):
        if coin[-i] <= x:
            break
    
    price += x // coin[-i] * coin[-i]
    n += x // coin[-i]

print(n)