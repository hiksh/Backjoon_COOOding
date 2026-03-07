# 9084
T = int(input())
for i in range(T):
    N = int(input())
    coin_lst = list(map(int, input().split()))
    M = int(input())
    dp_lst = [0]*(M+1)
    dp_lst[0] = 1
    
    for k in coin_lst:
        for j in range(1,M+1):
            if j >= k:
                dp_lst[j] += dp_lst[j-k]
    print(dp_lst[-1])