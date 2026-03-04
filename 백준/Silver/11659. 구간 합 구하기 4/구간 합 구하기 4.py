# 11659
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_lst = list(map(int, input().split()))
sum_lst = [0]*N
sum_lst[0] = n_lst[0]

for i in range(1,N):
    sum_lst[i] = sum_lst[i-1] + n_lst[i]

for i in range(M):
    I, J = map(int, input().split())
    if I != 1:
        print(sum_lst[J-1] - sum_lst[I-2])
    else:
        print(sum_lst[J-1])