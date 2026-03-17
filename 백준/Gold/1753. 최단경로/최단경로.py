# 1753
import sys
import heapq
input = sys.stdin.readline

def Dijkstra(head):
    h = []
    dist_lst = [10**9]*V
    dist_lst[head] = 0
    heapq.heappush(h, (0, head))

    while h:
        curr_d, curr = heapq.heappop(h)
        if curr_d > dist_lst[curr]: # not been executed
            continue

        for neighbor in edge_lst[curr]:
            if dist_lst[neighbor[0]] > dist_lst[curr] + neighbor[1]:
                dist_lst[neighbor[0]] = dist_lst[curr] + neighbor[1]
                heapq.heappush(h, (dist_lst[curr] + neighbor[1], neighbor[0]))
    
    return dist_lst


V, E = map(int, input().split())
K = int(input())-1
edge_lst = [[] for i in range(V)]
for i in range(E):
    u, v, w = map(int, input().split())
    edge_lst[u-1].append((v-1,w))

ret_lst = Dijkstra(K)
for i in ret_lst:
    if i == 10**9:
        print("INF")
    else:
        print(i)