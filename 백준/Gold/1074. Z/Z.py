N, r, c = map(int, input().split())

order = 0
while N != 1:
    R = r + 1
    C = c + 1

    if R <= 2**(N-1) and C <= 2**(N-1):
        pass
    if R <= 2**(N-1) and C > 2**(N-1):
        order += 2**(2*N-2)
        c = C - 1 - 2**(N-1)
    if R > 2**(N-1) and C <= 2**(N-1):
        order += 2**(2*N-2)*2
        r = R - 1 - 2**(N-1)
    if R > 2**(N-1) and C > 2**(N-1):
        order += 2**(2*N-2)*3
        r = R - 1 - 2**(N-1)
        c = C - 1 - 2**(N-1)
    
    N -= 1

if r == 0 and c == 0:
    print(order)
elif r == 0 and c == 1:
    print(order + 1)
elif r == 1 and c == 0:
    print(order + 2)
else:
    print(order + 3)