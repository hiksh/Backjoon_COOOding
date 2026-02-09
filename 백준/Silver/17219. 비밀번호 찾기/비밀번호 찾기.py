import sys
sys.stdin.readline

dic = dict()
N, M = map(int, input().split())
for i in range(N):
    address, pwd = map(str, input().split())
    dic[address] = pwd

for i in range(M):
    print(dic[input()])