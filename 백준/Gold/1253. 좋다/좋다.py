import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

n = 0
for i in range(len(A)):
    pt_1 = 0
    pt_2 = N-1
    while pt_2 > pt_1 + 1:
        if A[pt_2] + A[pt_1] == A[i]:
            if pt_1 != i and pt_2 != i:
                break
            else:
                if pt_1 == i:
                    pt_1 += 1
                else:
                    pt_2 -= 1

        elif A[pt_2] + A[pt_1] > A[i]:
            pt_2 -= 1
        else:
            pt_1 += 1
    
    if A[pt_2] + A[pt_1] == A[i]:
        if pt_1 != i and pt_2 != i:
            n += 1
print(n)