dp_lst = [[1,0],[0,1],[1,1]] + [[]]*38
for i in range(3,41):
    dp_lst[i] = [dp_lst[i-1][0]+dp_lst[i-2][0], dp_lst[i-1][0]+dp_lst[i-1][1]]

T = int(input())
for i in range(T):
    tmp = dp_lst[int(input())]
    print(tmp[0], tmp[1])