import sys
sys.setrecursionlimit(10 ** 9)

dict_pan = {1:0, 2:1, 3:1, 4:2, 5:2, 6:4}

def ZJP(n):
    if n in dict_pan:
        return dict_pan[n]
    else:
        dict_pan[n] = int((ZJP(n-2) + ZJP(n-3) + ZJP(n-4)) % (1e9 + 7))
        return dict_pan[n]

n = int(input())
print(ZJP(n))