import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon_dict_1 = {}
pokemon_dict_2 = {}
for i in range(1,1+N):
    # .rstrip()으로 뒤에 붙은 \n을 제거 (백준 오류)
    x = input().rstrip()
    pokemon_dict_1[x] = i
    pokemon_dict_2[i] = x

for i in range(M):
    quiz = input().rstrip() # 여기서도 \n을 제거
    try:
        print(pokemon_dict_2[int(quiz)])
    except:
        print(pokemon_dict_1[quiz])