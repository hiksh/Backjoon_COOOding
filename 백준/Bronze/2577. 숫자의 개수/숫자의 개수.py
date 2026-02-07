# 2577
lst = []
for i in range(3):
    lst.append(int(input()))

MT = lst[0]*lst[1]*lst[2]
num_lst = [0 for i in range(10)]

for i in str(MT):
    num_lst[int(i)] += 1

for i in num_lst:
    print(i)