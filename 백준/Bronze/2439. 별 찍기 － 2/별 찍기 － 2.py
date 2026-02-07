# 2439
N = int(input())
for i in range(N):
    tmp_blank = " "*(N-i-1)
    tmp_star = "*"*(i+1)
    print(f"{tmp_blank}{tmp_star}")