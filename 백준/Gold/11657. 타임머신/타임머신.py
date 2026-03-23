#  11657
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edge_lst = [[] for i in range(N)]
for i in range(M):
    u, v, w = map(int, input().split())
    edge_lst[u-1].append((v-1, w))

D = [float('inf') for i in range(N)]
D[0] = 0

for i in range(N-1):
    for u in range(N):
        for v, w in edge_lst[u]:
            D[v] = min(D[v], D[u] + w)

flag = 0
for u in range(N):
    for v, w in edge_lst[u]:
        if D[v] > D[u] + w:
            flag = 1

if flag == 0:
    for i in range(1,N):
        if D[i] == float('inf'):
            print(-1)
        else:
            print(D[i])
else:
    print(-1)