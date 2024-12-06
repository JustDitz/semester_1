size_x,size_y = map(int, input().split())
x,y = map(int, input().split())
m = int(input())

# Berapa kali pengecekan
if((x==0 and y==0) or (x==0 and y ==size_y) or (x==size_x and y==0) or (x==size_x and y==size_y)):
    Petak = 3
elif((x==0 ) or (x==size_x) or (y==0) or (y==size_y)):
    Petak = 5
else:
    Petak = 8
     
if(m==1):
    x1,y1 = map(int,input().split())
    if (x1+1 == x or x1-1 == x) or (y1+1 == y or y1-1 == y):
        Petak-=1
elif(m==2):
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    if(x1+1 == x or x1-1 == x) or (y1+1 == y or y1-1 == y):
        Petak-=1
    if(x2+1 == x or x2-1 == x) or (y2+1 == y or y2-1 == y):
        Petak-=1
elif(m==3):
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    if(x1+1 == x or x1-1 == x) or (y1+1 == y or y1-1 == y):
        Petak-=1
        print("x1")
    if(x2+1 == x or x2-1 == x) or (y2+1 == y or y2-1 == y):
        Petak-=1
        print("x2")
    if(x3+1 == x or x3-1 == x) or (y3+1 == y or y3-1 == y):
        Petak-=1
        print("x3")
elif(m==4):
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    x4,y4 = map(int,input().split())
    if(x1+1 == x or x1-1 == x) or (y1+1 == y or y1-1 == y):
        Petak-=1
    if(x2+1 == x or x2-1 == x) or (y2+1 == y or y2-1 == y):
        Petak-=1
    if(x3+1 == x or x3-1 == x) or (y3+1 == y or y3-1 == y):
        Petak-=1
    if(x4+1 == x or x4-1 == x) or (y4+1 == y or y4-1 == y):
        Petak-=1
elif(m==5):
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    x4,y4 = map(int,input().split())
    x5,y5 = map(int,input().split())
    if(x1+1 == x or x1-1 == x) or (y1+1 == y or y1-1 == y):
        Petak-=1
    if(x2+1 == x or x2-1 == x) or (y2+1 == y or y2-1 == y):
        Petak-=1
    if(x3+1 == x or x3-1 == x) or (y3+1 == y or y3-1 == y):
        Petak-=1
    if(x4+1 == x or x4-1 == x) or (y4+1 == y or y4-1 == y):
        Petak-=1
    if(x5+1 == x or x5-1 == x) or (y5+1 == y or y5-1 == y):
        Petak-=1
elif(m==6):
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    x4,y4 = map(int,input().split())
    x5,y5 = map(int,input().split())
    x6,y6 = map(int,input().split())
    if(x1+1 == x or x1-1 == x) or (y1+1 == y or y1-1 == y):
        Petak-=1
    if(x2+1 == x or x2-1 == x) or (y2+1 == y or y2-1 == y):
        Petak-=1
    if(x3+1 == x or x3-1 == x) or (y3+1 == y or y3-1 == y):
        Petak-=1
    if(x4+1 == x or x4-1 == x) or (y4+1 == y or y4-1 == y):
        Petak-=1
    if(x5+1 == x or x5-1 == x) or (y5+1 == y or y5-1 == y):
        Petak-=1
    if(x6+1 == x or x6-1 == x) or (y6+1 == y or y6-1 == y):
        Petak-=1
elif(m==7):
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    x4,y4 = map(int,input().split())
    x5,y5 = map(int,input().split())
    x6,y6 = map(int,input().split())
    x7,y7 = map(int,input().split())
    if(x1+1 == x or x1-1 == x) or (y1+1 == y or y1-1 == y):
        Petak-=1
    if(x2+1 == x or x2-1 == x) or (y2+1 == y or y2-1 == y):
        Petak-=1
    if(x3+1 == x or x3-1 == x) or (y3+1 == y or y3-1 == y):
        Petak-=1
    if(x4+1 == x or x4-1 == x) or (y4+1 == y or y4-1 == y):
        Petak-=1
    if(x5+1 == x or x5-1 == x) or (y5+1 == y or y5-1 == y):
        Petak-=1
    if(x6+1 == x or x6-1 == x) or (y6+1 == y or y6-1 == y):
        Petak-=1
    if(x7+1 == x or x7-1 == x) or (y7+1 == y or y7-1 == y):
        Petak-=1
elif(m==8):
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    x4,y4 = map(int,input().split())
    x5,y5 = map(int,input().split())
    x6,y6 = map(int,input().split())
    x7,y7 = map(int,input().split())
    x8,y8 = map(int,input().split())
    if(x1+1 == x or x1-1 == x) or (y1+1 == y or y1-1 == y):
        Petak-=1
    if(x2+1 == x or x2-1 == x) or (y2+1 == y or y2-1 == y):
        Petak-=1
    if(x3+1 == x or x3-1 == x) or (y3+1 == y or y3-1 == y):
        Petak-=1
    if(x4+1 == x or x4-1 == x) or (y4+1 == y or y4-1 == y):
        Petak-=1
    if(x5+1 == x or x5-1 == x) or (y5+1 == y or y5-1 == y):
        Petak-=1
    if(x6+1 == x or x6-1 == x) or (y6+1 == y or y6-1 == y):
        Petak-=1
    if(x7+1 == x or x7-1 == x) or (y7+1 == y or y7-1 == y):
        Petak-=1
    if(x8+1 == x or x8-1 == x) or (y8+1 == y or y8-1 == y):
        Petak-=1
else:
    Petak = 0

if Petak>0:
    print("Senshi makan hari ini!")
else:
    print("Senshi makannya besok aja deh.")

# Misal senshi di 
# 2,4

# 5 M8 F  F  F     M3
# 4    F  S  F     
# 3 M2 F  F  F     M7
# 2                 
# 1 M5       M6    
# 0 M1       M4    
#   _0 _1 _2 _3 _4 _5 

# FREE : (1,5) (2,5) (3,5) (1,4) (3,4) (1,3) (2,3) (3,3)
# (1,0) (0,3) (5,5) (3,0) (1,1) (3,1) (5,3) (0,5)
# Expected : "Senshi makan hari ini!"
# Output AC : "Senshi makannya besok aja deh."

# Menuju X = 2 dan Y = 4
# Bandingkan dengan codemu di coretan.py

# 5 5 
# 2 4
# 8
# 1 0
# 0 3
# 5 5
# 3 0
# 1 1
# 3 1
# 5 3
# 0 5

# size_x,size_y = map(int, input().split())
# x,y = map(int, input().split())
# m = int(input())

# # Berapa kali pengecekan
# if((x==0 and y==0) or (x==0 and y ==size_y) or (x==size_x and y==0) or (x==size_x and y==size_y)):
#     Petak = 3
#     Con1,Con2,Con3 = True,False,False
# elif((x==0 ) or (x==size_x) or (y==0) or (y==size_y)):
#     Petak = 5
#     Con1,Con2,Con3 = False,True,False
# else:
#     Petak = 8
#     Con1,Con2,Con3 = False,False,True

# # lu : x+1 == x and y-1 == y
# # u  : x == x and y-1 == y
# # ru : x-1 == x and y-1 == y
# # l  : x+1 == x and y==y
# # r  : x-1 == x and y==y
# # ld : x+1 == x and y+1 == y
# # d  : x == x and y+1 == y
# # rd : x-1 == x and y+1 == y
# Cooked = 0     
# if(m==1):
#     x1,y1 = map(int,input().split())
#     if(x1+1 == x and y1-1 == y) or (x1 == x and y1-1 == y) or (x1-1 == x and y1-1 == y) or (x1+1 == x and y1==y) or (x1-1 == x and y1 == y) or (x1+1 == x and y1+1 == y) or (x1 == x and y1+1 == y) or (x1-1 == x and y1+1 == y):
#         Petak-=1
#         Cooked+=1
# elif(m==2):
#     x1,y1 = map(int,input().split())
#     x2,y2 = map(int,input().split())
#     if(x1+1 == x and y1-1 == y) or (x1 == x and y1-1 == y) or (x1-1 == x and y1-1 == y) or (x1+1 == x and y1==y) or (x1-1 == x and y1 == y) or (x1+1 == x and y1+1 == y) or (x1 == x and y1+1 == y) or (x1-1 == x and y1+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x2+1 == x and y2-1 == y) or (x2 == x and y2-1 == y) or (x2-1 == x and y2-1 == y) or (x2+1 == x and y2==y) or (x2-1 == x and y2 == y) or (x2+1 == x and y2+1 == y) or (x2 == x and y2+1 == y) or (x2-1 == x and y2+1 == y):
#         Petak-=1
#         Cooked+=1
# elif(m==3):
#     x1,y1 = map(int,input().split())
#     x2,y2 = map(int,input().split())
#     x3,y3 = map(int,input().split())
#     if(x1+1 == x and y1-1 == y) or (x1 == x and y1-1 == y) or (x1-1 == x and y1-1 == y) or (x1+1 == x and y1==y) or (x1-1 == x and y1 == y) or (x1+1 == x and y1+1 == y) or (x1 == x and y1+1 == y) or (x1-1 == x and y1+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x2+1 == x and y2-1 == y) or (x2 == x and y2-1 == y) or (x2-1 == x and y2-1 == y) or (x2+1 == x and y2==y) or (x2-1 == x and y2 == y) or (x2+1 == x and y2+1 == y) or (x2 == x and y2+1 == y) or (x2-1 == x and y2+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x3+1 == x and y3-1 == y) or (x3 == x and y3-1 == y) or (x3-1 == x and y3-1 == y) or (x3+1 == x and y3==y) or (x3-1 == x and y3 == y) or (x3+1 == x and y3+1 == y) or (x3 == x and y3+1 == y) or (x3-1 == x and y3+1 == y):
#         Petak-=1
#         Cooked+=1
# elif(m==4):
#     x1,y1 = map(int,input().split())
#     x2,y2 = map(int,input().split())
#     x3,y3 = map(int,input().split())
#     x4,y4 = map(int,input().split())
#     if(x1+1 == x and y1-1 == y) or (x1 == x and y1-1 == y) or (x1-1 == x and y1-1 == y) or (x1+1 == x and y1==y) or (x1-1 == x and y1 == y) or (x1+1 == x and y1+1 == y) or (x1 == x and y1+1 == y) or (x1-1 == x and y1+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x2+1 == x and y2-1 == y) or (x2 == x and y2-1 == y) or (x2-1 == x and y2-1 == y) or (x2+1 == x and y2==y) or (x2-1 == x and y2 == y) or (x2+1 == x and y2+1 == y) or (x2 == x and y2+1 == y) or (x2-1 == x and y2+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x3+1 == x and y3-1 == y) or (x3 == x and y3-1 == y) or (x3-1 == x and y3-1 == y) or (x3+1 == x and y3==y) or (x3-1 == x and y3 == y) or (x3+1 == x and y3+1 == y) or (x3 == x and y3+1 == y) or (x3-1 == x and y3+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x4+1 == x and y4-1 == y) or (x4 == x and y4-1 == y) or (x4-1 == x and y4-1 == y) or (x4+1 == x and y4==y) or (x4-1 == x and y4 == y) or (x4+1 == x and y4+1 == y) or (x4 == x and y4+1 == y) or (x4-1 == x and y4+1 == y):
#         Petak-=1
#         Cooked+=1
# elif(m==5):
#     x1,y1 = map(int,input().split())
#     x2,y2 = map(int,input().split())
#     x3,y3 = map(int,input().split())
#     x4,y4 = map(int,input().split())
#     x5,y5 = map(int,input().split())
#     if(x1+1 == x and y1-1 == y) or (x1 == x and y1-1 == y) or (x1-1 == x and y1-1 == y) or (x1+1 == x and y1==y) or (x1-1 == x and y1 == y) or (x1+1 == x and y1+1 == y) or (x1 == x and y1+1 == y) or (x1-1 == x and y1+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x2+1 == x and y2-1 == y) or (x2 == x and y2-1 == y) or (x2-1 == x and y2-1 == y) or (x2+1 == x and y2==y) or (x2-1 == x and y2 == y) or (x2+1 == x and y2+1 == y) or (x2 == x and y2+1 == y) or (x2-1 == x and y2+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x3+1 == x and y3-1 == y) or (x3 == x and y3-1 == y) or (x3-1 == x and y3-1 == y) or (x3+1 == x and y3==y) or (x3-1 == x and y3 == y) or (x3+1 == x and y3+1 == y) or (x3 == x and y3+1 == y) or (x3-1 == x and y3+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x4+1 == x and y4-1 == y) or (x4 == x and y4-1 == y) or (x4-1 == x and y4-1 == y) or (x4+1 == x and y4==y) or (x4-1 == x and y4 == y) or (x4+1 == x and y4+1 == y) or (x4 == x and y4+1 == y) or (x4-1 == x and y4+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x5+1 == x and y5-1 == y) or (x5 == x and y5-1 == y) or (x5-1 == x and y5-1 == y) or (x5+1 == x and y5==y) or (x5-1 == x and y5 == y) or (x5+1 == x and y5+1 == y) or (x5 == x and y5+1 == y) or (x5-1 == x and y5+1 == y):
#         Petak-=1
#         Cooked+=1
# elif(m==6):
#     x1,y1 = map(int,input().split())
#     x2,y2 = map(int,input().split())
#     x3,y3 = map(int,input().split())
#     x4,y4 = map(int,input().split())
#     x5,y5 = map(int,input().split())
#     x6,y6 = map(int,input().split())
#     if(x1+1 == x and y1-1 == y) or (x1 == x and y1-1 == y) or (x1-1 == x and y1-1 == y) or (x1+1 == x and y1==y) or (x1-1 == x and y1 == y) or (x1+1 == x and y1+1 == y) or (x1 == x and y1+1 == y) or (x1-1 == x and y1+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x2+1 == x and y2-1 == y) or (x2 == x and y2-1 == y) or (x2-1 == x and y2-1 == y) or (x2+1 == x and y2==y) or (x2-1 == x and y2 == y) or (x2+1 == x and y2+1 == y) or (x2 == x and y2+1 == y) or (x2-1 == x and y2+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x3+1 == x and y3-1 == y) or (x3 == x and y3-1 == y) or (x3-1 == x and y3-1 == y) or (x3+1 == x and y3==y) or (x3-1 == x and y3 == y) or (x3+1 == x and y3+1 == y) or (x3 == x and y3+1 == y) or (x3-1 == x and y3+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x4+1 == x and y4-1 == y) or (x4 == x and y4-1 == y) or (x4-1 == x and y4-1 == y) or (x4+1 == x and y4==y) or (x4-1 == x and y4 == y) or (x4+1 == x and y4+1 == y) or (x4 == x and y4+1 == y) or (x4-1 == x and y4+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x5+1 == x and y5-1 == y) or (x5 == x and y5-1 == y) or (x5-1 == x and y5-1 == y) or (x5+1 == x and y5==y) or (x5-1 == x and y5 == y) or (x5+1 == x and y5+1 == y) or (x5 == x and y5+1 == y) or (x5-1 == x and y5+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x6+1 == x and y6-1 == y) or (x6 == x and y6-1 == y) or (x6-1 == x and y6-1 == y) or (x6+1 == x and y6==y) or (x6-1 == x and y6 == y) or (x6+1 == x and y6+1 == y) or (x6 == x and y6+1 == y) or (x6-1 == x and y6+1 == y):
#         Petak-=1
#         Cooked+=1
# elif(m==7):
#     x1,y1 = map(int,input().split())
#     x2,y2 = map(int,input().split())
#     x3,y3 = map(int,input().split())
#     x4,y4 = map(int,input().split())
#     x5,y5 = map(int,input().split())
#     x6,y6 = map(int,input().split())
#     x7,y7 = map(int,input().split())
#     if(x1+1 == x and y1-1 == y) or (x1 == x and y1-1 == y) or (x1-1 == x and y1-1 == y) or (x1+1 == x and y1==y) or (x1-1 == x and y1 == y) or (x1+1 == x and y1+1 == y) or (x1 == x and y1+1 == y) or (x1-1 == x and y1+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x2+1 == x and y2-1 == y) or (x2 == x and y2-1 == y) or (x2-1 == x and y2-1 == y) or (x2+1 == x and y2==y) or (x2-1 == x and y2 == y) or (x2+1 == x and y2+1 == y) or (x2 == x and y2+1 == y) or (x2-1 == x and y2+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x3+1 == x and y3-1 == y) or (x3 == x and y3-1 == y) or (x3-1 == x and y3-1 == y) or (x3+1 == x and y3==y) or (x3-1 == x and y3 == y) or (x3+1 == x and y3+1 == y) or (x3 == x and y3+1 == y) or (x3-1 == x and y3+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x4+1 == x and y4-1 == y) or (x4 == x and y4-1 == y) or (x4-1 == x and y4-1 == y) or (x4+1 == x and y4==y) or (x4-1 == x and y4 == y) or (x4+1 == x and y4+1 == y) or (x4 == x and y4+1 == y) or (x4-1 == x and y4+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x5+1 == x and y5-1 == y) or (x5 == x and y5-1 == y) or (x5-1 == x and y5-1 == y) or (x5+1 == x and y5==y) or (x5-1 == x and y5 == y) or (x5+1 == x and y5+1 == y) or (x5 == x and y5+1 == y) or (x5-1 == x and y5+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x6+1 == x and y6-1 == y) or (x6 == x and y6-1 == y) or (x6-1 == x and y6-1 == y) or (x6+1 == x and y6==y) or (x6-1 == x and y6 == y) or (x6+1 == x and y6+1 == y) or (x6 == x and y6+1 == y) or (x6-1 == x and y6+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x7+1 == x and y7-1 == y) or (x7 == x and y7-1 == y) or (x7-1 == x and y7-1 == y) or (x7+1 == x and y7==y) or (x7-1 == x and y7 == y) or (x7+1 == x and y7+1 == y) or (x7 == x and y7+1 == y) or (x7-1 == x and y7+1 == y):
#         Petak-=1
#         Cooked+=1
# elif(m==8):
#     x1,y1 = map(int,input().split())
#     x2,y2 = map(int,input().split())
#     x3,y3 = map(int,input().split())
#     x4,y4 = map(int,input().split())
#     x5,y5 = map(int,input().split())
#     x6,y6 = map(int,input().split())
#     x7,y7 = map(int,input().split())
#     x8,y8 = map(int,input().split())
#     if(x1+1 == x and y1-1 == y) or (x1 == x and y1-1 == y) or (x1-1 == x and y1-1 == y) or (x1+1 == x and y1==y) or (x1-1 == x and y1 == y) or (x1+1 == x and y1+1 == y) or (x1 == x and y1+1 == y) or (x1-1 == x and y1+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x2+1 == x and y2-1 == y) or (x2 == x and y2-1 == y) or (x2-1 == x and y2-1 == y) or (x2+1 == x and y2==y) or (x2-1 == x and y2 == y) or (x2+1 == x and y2+1 == y) or (x2 == x and y2+1 == y) or (x2-1 == x and y2+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x3+1 == x and y3-1 == y) or (x3 == x and y3-1 == y) or (x3-1 == x and y3-1 == y) or (x3+1 == x and y3==y) or (x3-1 == x and y3 == y) or (x3+1 == x and y3+1 == y) or (x3 == x and y3+1 == y) or (x3-1 == x and y3+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x4+1 == x and y4-1 == y) or (x4 == x and y4-1 == y) or (x4-1 == x and y4-1 == y) or (x4+1 == x and y4==y) or (x4-1 == x and y4 == y) or (x4+1 == x and y4+1 == y) or (x4 == x and y4+1 == y) or (x4-1 == x and y4+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x5+1 == x and y5-1 == y) or (x5 == x and y5-1 == y) or (x5-1 == x and y5-1 == y) or (x5+1 == x and y5==y) or (x5-1 == x and y5 == y) or (x5+1 == x and y5+1 == y) or (x5 == x and y5+1 == y) or (x5-1 == x and y5+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x6+1 == x and y6-1 == y) or (x6 == x and y6-1 == y) or (x6-1 == x and y6-1 == y) or (x6+1 == x and y6==y) or (x6-1 == x and y6 == y) or (x6+1 == x and y6+1 == y) or (x6 == x and y6+1 == y) or (x6-1 == x and y6+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x7+1 == x and y7-1 == y) or (x7 == x and y7-1 == y) or (x7-1 == x and y7-1 == y) or (x7+1 == x and y7==y) or (x7-1 == x and y7 == y) or (x7+1 == x and y7+1 == y) or (x7 == x and y7+1 == y) or (x7-1 == x and y7+1 == y):
#         Petak-=1
#         Cooked+=1
#     if(x8+1 == x and y8-1 == y) or (x8 == x and y8-1 == y) or (x8-1 == x and y8-1 == y) or (x8+1 == x and y8==y) or (x8-1 == x and y8 == y) or (x8+1 == x and y8+1 == y) or (x8 == x and y8+1 == y) or (x8-1 == x and y8+1 == y):
#         Petak-=1
#         Cooked+=1
# else:
#     Petak = 0
    
# if Con1 and 0<Petak<3 and Cooked>0:
#     print("Senshi makan hari ini!")
# elif Con2 and 0<Petak<5 and Cooked>0:
#     print("Senshi makan hari ini!")
# elif Con3 and 0<Petak<8 and Cooked>0:
#     print("Senshi makan hari ini!")
# else:
#     print("Senshi makannya besok aja deh.")