N = int(input())
stair = []
for i in range(N):
    stair.append(int(input()))

if N < 3:
    print(sum(stair))
else:
    dp_lst_1 = [stair[0],stair[1]] + [0]*(N-2)
    dp_lst_2 = [0,stair[0]+stair[1]] + [0]*(N-2)
    for i in range(2,N):
        dp_lst_1[i] = max(dp_lst_1[i-2], dp_lst_2[i-2]) + stair[i]
        dp_lst_2[i] = dp_lst_1[i-1] + stair[i]
    
    print(max(dp_lst_1[-1],dp_lst_2[-1]))