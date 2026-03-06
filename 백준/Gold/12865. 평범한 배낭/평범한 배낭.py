# 12865
M, N = map(int, input().split())
book_lst = []
book_lst.append((0,0))
for i in range(M):
    n, d = map(int, input().split())
    book_lst.append((n,d))

dp_lst = [[0]*(1+N) for i in range(1+M)]

for i in range(1,M+1):
    for j in range(N+1):
        if j < book_lst[i][0]:
            dp_lst[i][j] = dp_lst[i-1][j]
        if j >= book_lst[i][0]:
            dp_lst[i][j] = max(book_lst[i][1] + dp_lst[i-1][j-book_lst[i][0]], dp_lst[i-1][j])

print(dp_lst[-1][-1])