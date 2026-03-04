dp_lst = [0]*1000
dp_lst[0] = 1
dp_lst[1] = 2
for i in range(2,1000):
    dp_lst[i] = dp_lst[i-1] + dp_lst[i-2]

N = int(input())
print(dp_lst[N-1]%10007)