matrix = []
rows, columns = list(map(int, input('Enter no. of rows and columns(space separated):').split()))
print("Enter Matrix:")
try:
    for row in range(rows):
        inputs = input().split()
        if len(inputs) == columns:
            matrix.append(inputs)
        else:
            raise
except:
    print('Data entered in the row was not equal to the number of columns')
upper = 0
lower = rows - 1
left = 0
right = columns - 1

while upper <= lower and left <= right:
    for i in range(left, right + 1):
        print(matrix[upper][i], end = ' ')
    upper += 1
    
    for i in range(upper, lower + 1):
        print(matrix[i][right], end = ' ')
    right -= 1
    
    if upper <= lower:
        for i in range(right, left - 1, -1):
            print(matrix[lower][i], end = ' ')
        lower -= 1    
    
    if left <= right:
        for i in range(lower, upper - 1, -1):
            print(matrix[i][left], end = ' ')
        left += 1