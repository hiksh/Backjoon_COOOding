import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    Note_1 = list(map(int, input().split()))
    Note_1 = set(Note_1)

    M = int(input())
    Note_2 = list(map(int, input().split()))

    result = []
    for j in Note_2:
        if j in Note_1:
            result.append(1)
        else:
            result.append(0)
    
    for r in result:
        print(r)