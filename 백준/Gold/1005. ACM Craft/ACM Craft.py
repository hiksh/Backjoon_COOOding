# 1005
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(w):
    visited_lst[w] = 1
    for e in Adjacency_lst[w]:
        if visited_lst[e] == 0:
            visited_lst[e] = 1
            dfs(e)
    ordered_lst.append(w)

T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))

    Adjacency_lst = [[] for j in range(N)]
    Reversed_adjacency_lst = [[] for j in range(N)]

    head_node = [1]*N
    for j in range(K):
        x, y = map(int, input().split())
        Adjacency_lst[x-1].append(y-1)
        Reversed_adjacency_lst[y-1].append(x-1)
        head_node[y-1] = 0

    # 위상정렬
    ordered_lst = []
    visited_lst = [0 for i in range(N)]
    for j in range(N):
        if visited_lst[j] == 0:
            dfs(j)
    
    ordered_lst.reverse()

    dp_lst = [0]*N
    for j in ordered_lst:
        if head_node[j] == 1:
            dp_lst[j] = D[j]
        else:
            for k in Reversed_adjacency_lst[j]:
                dp_lst[j] = max((dp_lst[j], dp_lst[k]+D[j]))
    key_point = int(input())
    print(dp_lst[key_point-1])