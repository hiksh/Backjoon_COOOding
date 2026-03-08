from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def check_near_baechu(m, n, x, y, arce, visited, next_p):
  visited[x][y] = 1
  next_p.append([x, y])
  while True:
    if len(next_p) == 0:
      return
    
    next_ = next_p.popleft()
    x = next_[0]
    y = next_[1]
    for i in range(4):
      if 0 <= x+dx[i] < m and 0 <= y+dy[i] < n:
        if arce[x+dx[i]][y+dy[i]] == 1:
          if visited[x+dx[i]][y+dy[i]] == 0:
            visited[x+dx[i]][y+dy[i]] = 1
            next_p.append([x+dx[i], y+dy[i]])
    

def Cabbage_worm(m,n,k):
  Cabbage = []
  for i in range(k):
    tmp = list(map(int, input().split()))
    Cabbage.append(tmp)
  # tmp = list(map(int, input().split()))
  # for i in range(k):
  #   Cabbage.append([tmp[2*k],tmp[2*k+1]])

  Acre = []

  for i in range(m):
    tmp = []
    for j in range(n):
      tmp.append(0)
    Acre.append(tmp)

  visited_Acre = [arr[:] for arr in Acre]

  for i in Cabbage:
    Acre[i[0]][i[1]] = 1

  worm_count = 0
  for i in range(m):
    for j in range(n):
      if Acre[i][j] == 1:
        if visited_Acre[i][j] == 0:
          Next_p = deque()
          check_near_baechu(m, n, i,j, Acre, visited_Acre, Next_p)
          worm_count += 1

  print(worm_count)

T = int(input())
for _ in range(T):
  M, N, K = map(int, input().split())
  Cabbage_worm(M,N,K)