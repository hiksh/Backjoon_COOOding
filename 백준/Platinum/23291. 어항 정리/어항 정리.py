import sys
from collections import deque

N, K = map(int, input().split())
U = list(map(int, input().split()))

dx = [1,0,-1,0]
dy = [0,1,0,-1]
def setting_fish(lst): # 수정 요함
  visited = [arr[:] for arr in lst]
  origin = [arr[:] for arr in lst]
  sorted = []
  q = deque([[0,0]])
  while True:
    if len(q) == 0:
      break

    p = q.popleft()
    sorted.append(p)
    visited[p[0]][p[1]] = 0
    for i in range(4):
      if p[0]+dx[i] >= 0 and p[1]+dy[i] >= 0: # list -1번째 접근 막기
        try:
          if visited[p[0]+dx[i]][p[1]+dy[i]]:
            q.append([p[0]+dx[i],p[1]+dy[i]])
            visited[p[0]+dx[i]][p[1]+dy[i]] = 0
          if [p[0]+dx[i],p[1]+dy[i]] not in sorted:
            dif = (origin[p[0]+dx[i]][p[1]+dy[i]] - origin[p[0]][p[1]])
            if dif//5 > 0 or dif%5 == 0:
              dif = dif//5
              lst[p[0]+dx[i]][p[1]+dy[i]] -= dif
              lst[p[0]][p[1]] += dif
            elif dif//5+1 < 0:
              dif = dif//5+1
              lst[p[0]+dx[i]][p[1]+dy[i]] -= dif
              lst[p[0]][p[1]] += dif
        except:
          pass
    # print(lst)
  return lst

step = 0
while True:
  # step 7.5
  if max(U) - min(U) <= K:
    break
  else:
    step += 1

  # step 1
  m = min(U)
  for i in range(len(U)):
    if U[i] == m:
      U[i] += 1

  # step 2
  h = 1
  u = U[:]
  u = [[u[0]]] + [u[1:]]
  while True:
    if len(u) > len(u[-1])-len(u[0]):
      break
    tmp_lst = []
    for i in range(len(u[0])):
      tmp_lst.append([u[x][i] for x in range(len(u))])
    u = [[j[-k] for k in range(1,1+len(j))] for j in tmp_lst] + [u[-1][len(tmp_lst):]]

  # step 3
  # print(u)
  u = setting_fish(u)
  # print("1:",u)

  # step 4
  tmp_lst = []
  for i in range(len(u[0])):
    tmp_lst.append([u[-j][i] for j in range(1,1+len(u))])
  tmp = []
  for t in tmp_lst:
    tmp += t
  u = tmp + u[-1][len(tmp_lst):]
  # print(u)

  # step 5
  u = [list(reversed(u[:len(u)//2]))] + [u[len(u)//2:]]
  tmp_lst = []
  for i in range(1,3):
    tmp_lst.append([u[-i][-j] for j in range((len(u[0])//2)+1,len(u[0])+1)])
  u = tmp_lst + [[u[i][j] for j in range(len(u[0])//2,len(u[0]))] for i in range(2)]

  # step 6
  u = setting_fish(u)
  # print("2:",u)

  # step 7
  tmp_lst = []
  for i in range(len(u[0])):
    tmp_lst.append([u[-j][i] for j in range(1,len(u)+1)])
  t = []
  for i in tmp_lst:
    for j in i:
      t.append(j)
  u = t
  # print(u)
  # print()
  U = u

print(step)