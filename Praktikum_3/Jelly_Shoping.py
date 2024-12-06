visited = set()
def rute(x, y, m, n, mall, visited, all_2):
    if not (0 <= x < m and 0 <= y < n) or mall[x][y] == '1' or (x, y) in visited:
        return False
    visited.add((x, y)) 

    if mall[x][y] == '2':
        all_2[0] -= 1

    if x == m - 1 and y == n - 1 and all_2[0] == 0:
        return True
    
    around = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    for dx, dy in around:
        if rute(x + dx, y + dy, m, n, mall, visited, all_2):
            return True
    
    visited.remove((x, y))
    if mall[x][y] == '2':
        all_2[0] += 1
    
    return False

n, m = map(int, input().split())
mall = []
all_2 = [0]
for i in range(m):
    temp = list(input()) 
    all_2[0] += temp.count('2')  
    mall.append(temp)

rute(0, 0, m, n, mall, visited, all_2)

for x_new, y_new in visited:
    mall[x_new][y_new] = '*'
    
for row in mall:
    print(''.join(row))
      
# 0 ubin, 1 tembok, 2 barang -> prioritaskan 2 -> hindari 1 ,
# input
# 5 6
# 00020
# 10101
# 12001
# 10100
# 00021
# 11100

# 5 5
# 02000
# 00010
# 21010
# 00000
# 11110