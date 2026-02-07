# 2920
ms = list(map(str, input().split()))
ms_2 = ""
for i in ms:
    ms_2 += i

if ms_2 == "12345678":
    print("ascending")
elif ms_2 == "87654321":
    print("descending")
else:
    print("mixed")