# 10451
T = int(input())
for i in range(T):
    N = int(input())
    C = list(map(int, input().split()))

    for i in range(N):
        C[i] = C[i]-1

    visited_lst = [0]*N
    cycle = 0
    for i in range(N):
        visited_lst[i] = 1
        s = [i]
        while len(s) > 0:
            node = s.pop()
            next_node = C[node]
            if visited_lst[next_node] == 0:
                s.append(C[node])
                visited_lst[next_node] = 1
        
        if next_node == i:
            cycle += 1

    print(cycle)
