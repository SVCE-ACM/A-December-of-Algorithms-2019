#if i says he knows j then j should know i. If j doesnt know i then i was lying
def make_symmetric(matrix, n):
    for i in range(n):
        for j in range(i):
            if matrix[i][i] != matrix[j][i]:
                matrix[i][j] = matrix[j][i] = '0'
                
def add_group(x):
    is_grouped[x] = 1
    temp.append(x)
    for y in range(n):
        if x != y and matrix[x][y] == '1' and is_grouped[y] != 1:
            add_group(y)
    
    
matrix = []
n = int(input('Enter no. of people: '))
print('Enter matrix:')
for i in range(n):
    matrix.append(input().split())
make_symmetric(matrix, n)
is_grouped = [0] * n
groups = []
#forming groups for every member. Similar to traversing in graph
for member in range(n):
    if is_grouped[member] == 0:
        temp = []
        add_group(member)
        groups.append(temp)
is_there_assassin = False    
group_count = len(groups)
for group in groups:
    if len(group) == 1:
        is_there_assassin = True
        break
print('No. of groups = {}'.format(group_count))
if is_there_assassin:
    print("An assassin is present")
else:
    print('Assassin is not present')