def assasin(arr,n):
    group = flag = 0
    result = [set() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if(arr[i][j] == 1):
                result[i].add(j)
    for i in range(n):
        for j in range(i+1,n):
            if(result[j].issubset(result[i])):
                result[j] = set({})
    for e in result:
        if(len(e) > 0):
            group += 1
        if(len(e) == 1):
            flag = 1
    print('No of groups: ',group)
    if(flag == 1):
        print('An Assassin is present')
    else:
        print('No Assassins')

n = int(input('Enter no of people:'))
arr = []
print('Enter the relation matrix:')
for _ in range(n):
    row = [int(e) for e in input().split()][0:n]
    arr.append(row)

assasin(arr,n)