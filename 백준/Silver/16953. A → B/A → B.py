from collections import deque

A, B = map(int, input().split())
q = deque([[A,1]])

yn = 0
while len(q) > 0:
    loc = q.popleft()
    if loc[0] == B:
        print(loc[1])
        yn = 1
        break
    if loc[0]*2 <= B:
        q.append([loc[0]*2, loc[1]+1])
    if loc[0]*10 + 1 <= B:
        q.append([loc[0]*10 + 1, loc[1]+1])

if yn == 0:
    print(-1)