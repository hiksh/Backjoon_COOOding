# 1152
s = input()
s_ = s.split(" ")
while '' in s_:
    s_.remove('')
print(len(s_))