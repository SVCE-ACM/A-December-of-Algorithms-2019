def hasFront(arr,r,c,i,j):
    if(i-1 >= 0):
        return arr[i-1][j] == arr[i][j]
    return False

def hasBack(arr,r,c,i,j):
    if(i+1 < r):
        return arr[i+1][j] == arr[i][j]
    return False

def hasLR(arr,r,c,i,j):
    if(j+1 < c):
        if(arr[i][j+1] == arr[i][j]):
            return True
    if(j-1 >= 0):
        if(arr[i][j-1] == arr[i][j]):
            return True
    return False

def hasDiagonal(arr,r,c,i,j):
    if(i-1 >=0 and j-1 >=0):
        if(arr[i-1][j-1] == arr[i][j]):
            return True
    if(i+1 < r and j+1 < c):
        if(arr[i+1][j+1] == arr[i][j]):
            return True
    if(i-1 >=0 and j+1 < c):
        if(arr[i-1][j+1] == arr[i][j]):
            return True
    if(i+1 < r and j-1 >= 0):
        if(arr[i+1][j-1] == arr[i][j]):
            return True
    return False


r = int(input('Enter # of rows:'))
c = int(input('Enter # of columns:'))
print('-Enter the student arrangement-')
arr = []
for _ in range(r):
    arr.append([e for e in input().split()])

result = []
for _ in range(r):
    result.append([0.0 for i in range(c)])

for i in range(r):
    for j in range(c):
        if(hasFront(arr,r,c,i,j)):
            result[i][j] += 0.3
        if(hasBack(arr,r,c,i,j)):
            result[i][j] += 0.2
        if(hasLR(arr,r,c,i,j)):
            result[i][j] += 0.2
        if(hasDiagonal(arr,r,c,i,j)):
            result[i][j] += 0.025

for e in result:
    print(e)