# 2675
T = int(input())
for i in range(T):
    R, S = map(str, input().split())
    r = int(R)

    ret = ""
    for s in S:
        ret += s*r
    print(ret)