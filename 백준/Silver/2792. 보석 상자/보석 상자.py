import sys
input = sys.stdin.readline

N, M = map(int, input().split())
GEM = []
for i in range(M):
    GEM.append(int(input()))

lo = 0
hi = max(GEM)

def solv(s, lst):
    tmp = 0
    for element in lst:
        if element >= s:
            ss = element//s
            tmp += ss
            if element - s*ss > 0:
                tmp += 1
        else:
            tmp += 1
    return tmp

while hi > lo + 1:
    mid = (hi + lo) // 2
    
    if solv(mid, GEM) <= N:
        hi = mid
    else:
        lo = mid

if lo == 0:
    print(1)
else:
    if solv(lo,GEM) <= N:
        print(lo)
    else:
        print(hi)