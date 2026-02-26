N = 1000
lst = [[0] * N for _ in range(N)]
for i in range(N):
    lst[0][i] = 1
    lst[i][0] = 1
direction = [[0,1],[1,0],[1,1]]
for i in range(1,N):
    for j in range(1,N):
        for d in direction:
            if i-d[0] >= 0 and j-d[1] >= 0:
                lst[i][j] += lst[i-d[0]][j-d[1]]


n, m = map(int, input().split())
print(lst[n-1][m-1]%(10**9+7))
