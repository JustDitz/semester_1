def Searching_Combo_rawr(arr, target):
    left = 0
    right = len(arr) - 1
    if target <= arr[0]:
        return 0
    if target >= arr[-1]:
        return len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and (arr[mid-1] != target if mid > 0 else True):
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target or (arr[mid] == target and arr[mid-1] == target):
            right = mid - 1
    # Apabila angkanya tidak ada maka ambil yang lebih besar terdekat
    for i in range(right,len(arr)):
        if arr[i] > target:
            return i
    return -1

M,N = map(int, input().split())
U = []
for i in range(N):
    temp = list(map(int, input().split()))
    U.append(temp)
Q = int(input())
R = list(map(int, input().split()))

U_1D = [Element for Row in U for Element in Row]
U_1D.sort()

Soal = 0
while Q:
    print(Searching_Combo_rawr(U_1D, R[Soal]),end=" ")
    Soal+=1
    Q-=1
# input
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
# 3
# 2 3 4
# output
# 1 2 3

# input 2
# 5 3
# 1 3 1 9 2
# 2 2 1 9 11
# 19 9 2 4 3
# 2
# 10 4

# 13 9