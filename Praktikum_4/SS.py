Left_Copy = 0
Right_Copy = 0
Merge_Prog = 0
def merge(arr, left, mid, right):
    global Left_Copy, Right_Copy, Merge_Prog
    Merge_Prog += 1
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            Left_Copy += 1
        else:
            arr[k] = R[j]
            j += 1
            Right_Copy += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        Left_Copy += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        Right_Copy += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    merge_sort(A, 0, n-1)
    
    # Merge_Prog = min(Left_Copy, Right_Copy)
    print(Left_Copy)
    print(Right_Copy)
    print(Merge_Prog)
    
    # 3
    # 3 2 1
    #  TODO : Implementasikan kode program disini