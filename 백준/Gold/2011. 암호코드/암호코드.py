def remove_zero(n):
    n_ret = n
    if n_ret[0] == "0":
        return None
    
    while "0" in n_ret:
        for i in range(len(n_ret)):
            if n_ret[i] == "0":
                try:
                    if n_ret[i-1] == "1" or n_ret[i-1] == "2":
                        n_ret = n_ret[:i-1] + "J" + n_ret[i+1:]
                        break
                    else:
                        return None
                except:
                    return None
    return n_ret

def decoding(N): # type : str
    n = remove_zero(N)
    if n == None:
        return 0
    
    dp_lst = [0]*len(n)
    dp_lst[0] = 1

    if len(n) == 1:
        return 1

    if n[0] == "2":
        if n[1] in ["1","2","3","4","5","6"]:
            dp_lst[1] = 2
        else:
            dp_lst[1] = 1
    elif n[0] == "1":
        if n[1] != "J":
            dp_lst[1] = 2
        else:
            dp_lst[1] = 1
    else:
        dp_lst[1] = 1
    
    if len(n) == 2:
        return dp_lst[1]

    for i in range(2,len(n)):
        if n[i] in ["1","2"]:
            if n[i-1] in ["1","2"]:
                if n[i-2] in ["1","2"]:
                    dp_lst[i] = dp_lst[i-1] + dp_lst[i-2]
                else:
                    dp_lst[i] = dp_lst[i-2]*2
            else:
                dp_lst[i] = dp_lst[i-1]
            
        elif n[i] in ["3","4","5","6"]:
            if n[i-1] in ["1","2"]:
                if n[i-2] in ["1","2"]:
                    dp_lst[i] = dp_lst[i-1] + dp_lst[i-2]
                else:
                    dp_lst[i] = dp_lst[i-2]*2
            else:
                dp_lst[i] = dp_lst[i-1]
        elif n[i] in ["7","8","9"]:
            if n[i-1] == "1":
                if n[i-2] in ["1","2"]:
                    dp_lst[i] = dp_lst[i-1] + dp_lst[i-2]
                else:
                    dp_lst[i] = dp_lst[i-2]*2
            else:
                dp_lst[i] = dp_lst[i-1]
        else:
            dp_lst[i] = dp_lst[i-1]

    
    return dp_lst[-1]

N = input()
print(decoding(N)%1000000)