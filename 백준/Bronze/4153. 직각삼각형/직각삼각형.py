while True:
    abc = list(map(int, input().split()))
    if abc == [0,0,0]:
        break
    abc.sort()
    if abc[0]**2 + abc[1]**2 == abc[2]**2:
        print("right")
    else:
        print("wrong")