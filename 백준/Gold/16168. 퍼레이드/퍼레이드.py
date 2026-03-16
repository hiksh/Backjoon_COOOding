# 16168
# import sys
# input = sys.stdin.readline

def dfs(head):
    ret_lst = [head]
    visited_lst[head] = 1
    st = [head]
    while len(st) > 0:
        cur = st.pop()
        for j in Adjacency_lst[cur]:
            if visited_lst[j] == 0:
                visited_lst[j] = 1
                st.append(j)
                ret_lst.append(j)

V, E = map(int, input().split())
Adjacency_lst = [[] for i in range(V)]
for i in range(E):
    x, y = map(int, input().split())
    Adjacency_lst[x-1].append(y-1)
    Adjacency_lst[y-1].append(x-1)

cnt = 0
visited_lst = [0]*V
dfs(0)

if 0 in visited_lst:
    print("NO")
else:
    for i in Adjacency_lst:
        if len(i)%2 == 1:
            cnt += 1
    if cnt == 0 or cnt == 2:
        print("YES")
    else:
        print("NO")