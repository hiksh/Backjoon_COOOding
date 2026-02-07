# 10809
S = input()
lst = [-1]*(26)
for i in range(1,len(S)+1):
    lst[ord(S[-i])-97] = len(S)-i

for i in lst:
    print(i, end=" ")