K, N = map(int, input().split())
LAN = []
for i in range(K):
    LAN.append(int(input()))
hi = sum(LAN)//N
lo = 0

def calc(x):
    ret = 0
    for i in LAN:
        ret += i//x
    if ret >= N:
        return 1
    return 0

while hi > lo + 1:
    mid = (hi + lo) // 2
    if calc(mid) == 1:
        lo = mid
    else:
        hi = mid

if calc(hi) == 1:
    print(hi)
else:
    print(lo)