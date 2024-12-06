dict_kat = {}
def Secret(x):
    if -1 < int(x) < 10:
        return x
    else:
        sum = 0
        for i in range(len(x)):
            sum += int(x[i])
        return Secret(str(sum))

Inputnya = list(map(int, input().split()))
Final = []
Array_1 = []
Array_2 = []
Array_3 = []
Array_4 = []
Array_5 = []
Array_6 = []
Array_7 = []
Array_8 = []
Array_9 = []

for i in Inputnya:
    if Secret(str(i)) == '1':
        Array_1.append(i)
    elif Secret(str(i)) == '2':
        Array_2.append(i)
    elif Secret(str(i)) == '3':
        Array_3.append(i)
    elif Secret(str(i)) == '4':
        Array_4.append(i)
    elif Secret(str(i)) == '5':
        Array_5.append(i)
    elif Secret(str(i)) == '6':
        Array_6.append(i)
    elif Secret(str(i)) == '7':
        Array_7.append(i)
    elif Secret(str(i)) == '8':
        Array_8.append(i)
    elif Secret(str(i)) == '9':
        Array_9.append(i)
    
Array_1.sort()
Array_2.sort()
Array_3.sort()
Array_4.sort()    
Array_5.sort()
Array_6.sort()
Array_7.sort()
Array_8.sort()
Array_9.sort()

Final = Array_1 + Array_2 + Array_3 + Array_4 + Array_5 + Array_6 + Array_7 + Array_8 + Array_9
for i in Final:
    print(i,end=" ")
# print(dict_kat)


# 111 33 123 456 12 789 999
