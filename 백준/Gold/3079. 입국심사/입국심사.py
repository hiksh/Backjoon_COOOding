import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T = []
for i in range(N):
    T.append(int(input()))

T.sort()

def calc_time(x):
    ret = 0
    ret += sum(x//t for t in T)
    return ret

hi = T[0]*M
lo = 0

while hi > lo + 1:
    mid = (hi + lo) // 2
    if calc_time(mid) >= M:
        hi = mid
    else:
        lo = mid

if calc_time(lo) >= M:
    print(lo)
else:
    print(hi)