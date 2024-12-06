dict_SB = {1:1}

def SB(n):
    if n in dict_SB:
        return dict_SB[n]
    else:
        if n % 2 == 0:
            dict_SB[n] = 1 + SB(n/2)
        else:
            dict_SB[n] = 1 + SB(n-1)
        return dict_SB[n]
    
n = int(input())
print(SB(n))    