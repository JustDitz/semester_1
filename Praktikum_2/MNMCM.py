N = int(input())
Bz = list(map(int,input().split()))
Total = 1

for i in range(N-1):
    for j in range(i+1,N):
        if Total == 0:
            break
        Total *= (Bz[i]^Bz[j])
print(Total)

# input
# 3
# 2 3 5

# Output
# 42