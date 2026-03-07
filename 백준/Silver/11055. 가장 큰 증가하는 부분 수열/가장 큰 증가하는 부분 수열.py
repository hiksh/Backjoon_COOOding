# 11055
N = int(input())
lst = list(map(int, input().split()))

dp_lst = lst[:]
for i in range(1,N):
    for j in range(i):
        if lst[j] < lst[i]:
            dp_lst[i] = max(dp_lst[i], dp_lst[j]+lst[i])
print(max(dp_lst))