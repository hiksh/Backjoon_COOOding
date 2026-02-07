# 3052
lst = []
for i in range(10):
    n = int(input())
    lst.append(n%42)

s = set(lst)
print(len(s))