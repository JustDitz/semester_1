t = int(input())

while(t>0):
    n,k = map(int,input().split()) # n adalah size array, k adalah size sub-array
    A = list(map(int,input().split()))
    L,R = 0, k-1
    Total = 0    
    q = int(input()) # 1 Max, 2 Min
    
    if (q==1):
        maxi = float("-inf")
        for j in range(1,(k+1)):
            L = 0
            Total = sum(A[:j])
            
            maxi = max(maxi,Total)
            for R in range(j, n):
                Total = Total - A[L] + A[R]
                L += 1
                maxi = max(maxi,Total)
        print(maxi)
    elif(q == 2):
        mini = float("inf")
        for j in range(1,(k+1)):
            L = 0
            Total = sum(A[:j])
            
            mini = min(mini,Total)
            for R in range(j, n):
                Total = Total - A[L] + A[R]
                L += 1
                mini = min(mini,Total)
        print(mini)
    t-=1
    
# 1 
# 12 3
# 1 1 2 1 3 1 1 2 1 1 4 1

# Expect output : 1 = 6, 2 = 1

# 1
# 2 2
# 4 9
# 1

# Expected Output : 13