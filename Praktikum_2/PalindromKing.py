S = str(input())
Count = 0

for i in range(0,len(S)):
    if(S[i] == S[len(S)-(i+1)]):
        Count+=1
if(Count == len(S)):
    print("Palindrome King!")
else:
    print("Bukan King!")
    
# Input
# acumalaka

# Output
# BUkan King!