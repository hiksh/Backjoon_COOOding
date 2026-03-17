import sys
import heapq
input = sys.stdin.readline

def Dijkstra(head):
    h = []
    dist_lst = [2*10**9]*V
    dist_lst[head] = 0
    heapq.heappush(h, (0, head))

    while h:
        curr_d, curr = heapq.heappop(h)
        if curr_d > dist_lst[curr]: # not been executed
            continue
        dist_lst[curr] = curr_d
        for neighbor in edge_lst[curr]:
            if dist_lst[neighbor[0]] > dist_lst[curr] + neighbor[1]:
                dist_lst[neighbor[0]] = dist_lst[curr] + neighbor[1]
                heapq.heappush(h, (dist_lst[curr] + neighbor[1], neighbor[0]))
    
    return dist_lst

V, E = map(int, input().split())
edge_lst = [[] for i in range(V)]
for i in range(E):
    u, v, w = map(int, input().split())
    edge_lst[u-1].append((v-1,w))
    edge_lst[v-1].append((u-1,w))

must_visited = list(map(int, input().split()))

dist = Dijkstra(0)
first_to_second = Dijkstra(must_visited[0]-1)
dist_backward = Dijkstra(V-1)

plan_A = dist[must_visited[0]-1]+dist_backward[must_visited[1]-1]
plan_B = dist[must_visited[1]-1]+dist_backward[must_visited[0]-1]
final_dist = min(plan_A, plan_B) + first_to_second[must_visited[1]-1]
if final_dist < 2*10**9:
    print(final_dist)
else:
    print(-1)