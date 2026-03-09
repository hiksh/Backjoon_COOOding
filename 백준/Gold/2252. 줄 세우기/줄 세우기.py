# 2252
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    x,y = map(int, input().split())
    G[x-1].append(y-1)

visited_lst = [0 for i in range(N)]
ret_list = []

def dfs(w):
    visited_lst[w] = 1
    for e in G[w]:
        if visited_lst[e] == 0:
            visited_lst[e] = 1
            dfs(e)
    
    ret_list.append(w)

for i in range(N):
    if visited_lst[i] == 0:
        dfs(i)

for i in range(1,1+N):
    print(ret_list[-i]+1, end=" ")