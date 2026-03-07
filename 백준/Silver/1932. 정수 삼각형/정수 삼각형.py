# 1932
N = int(input())
T = [[] for _ in range(N)]

for i in range(N):
    tmp = list(map(int, input().split()))
    T[i] = tmp

dp_lst = [[0]*(1+_) for _ in range(N)]

dp_lst[0] = T[0]
for i in range(1,N):
    for j in range(len(T[i])):
        if j <= i-1:
            dp_lst[i][j] = max(dp_lst[i][j], dp_lst[i-1][j]+T[i][j])
        if j > 0:
            dp_lst[i][j] = max(dp_lst[i][j], dp_lst[i-1][j-1]+T[i][j])

print(max(dp_lst[-1]))