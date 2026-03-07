# 11727
N = int(input())
dp_lst = [0]*N
dp_lst[0] = 1
if N > 1:
    dp_lst[1] = 3
    for i in range(2,N):
        dp_lst[i] = dp_lst[i-1]+dp_lst[i-2]*2
print(dp_lst[-1]%10007)