# 10250
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    h = N % H
    w = N // H + 1
    if h == 0:
        h = H
        w -= 1
    
    print(h, end = "")
    if w // 10 < 1:
        print(0, end = "")
    print(w)