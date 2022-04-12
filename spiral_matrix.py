import random
import pprint
def get_spiral_matrix(matrix):
    
    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])
    
    res = []
    while (top < bottom) and (left < right):
        # parsing from left to right
        for i in range(left, right):
            res.append(matrix[top][i])
        
        top +=1
        # parsing from right to bottom
        for i in range(top, bottom):
            res.append(matrix[i][right-1])
            
        right -=1
        
        if not (top < bottom) and (left < right):
            break
            
        # parsing from bottom right to bottom left
        
        for i in range(right-1, left-1, -1):
            res.append(matrix[bottom-1][i])
            
        bottom -=1
        
        for i in range(bottom-1, top-1, -1):
            res.append(matrix[i][left])
            
        left +=1
        
    return res

no_of_rows = random.randint(3,6)
no_of_columns = random.randint(3,6)

matrix = []
for i in range(0,no_of_rows):
    randomlist = []
    for j in range(0,no_of_columns):
        n = random.randint(1,10)
        randomlist.append(n)
    matrix.append(randomlist)
print(matrix)
# matrix = [[27, 24, 9, 25], [24, 10, 6, 25], [23, 8, 4, 8]]
matrix = [[21, 26, 23, 23, 24], [27, 8, 4, 26, 9], [29, 15, 2, 3, 22]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(get_spiral_matrix(matrix))
print(matrix)

