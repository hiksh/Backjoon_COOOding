# 8958
T = int(input())
for i in range(T):
    test = input()
    score = 0
    const = 1
    for i in test:
        if i == "O":
            score += const
            const += 1
        else:
            const = 1

    print(score)