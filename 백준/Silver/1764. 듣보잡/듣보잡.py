import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_set = set()
M_set = set()
for i in range(N):
    N_set.add(input().rstrip())
for i in range(M):
    M_set.add(input().rstrip())

union = set()
for i in N_set:
    if i in M_set:
        union.add(i)

union = sorted(union)
print(len(union))
for i in union:
    print(i)