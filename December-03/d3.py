import math
def snap(arr,n):
    if(len(arr) == 1):
        return arr
    elif(sorted(arr) == arr):
        return arr
    flag = count = 1
    limit = math.ceil(n/2)
    tmp = [arr[0]]
    for i in range(1,len(arr)):
        if(tmp[-1] < arr[i]):
            tmp.append(arr[i])
            count += 1
            if(count == limit):
                return tmp
            flag = 0
    if(flag == 1):
        return arr[0:1]
    else:
        snap(arr[0:limit],limit)

n = int(input('Enter the size:'))
arr = [int(i) for i in input().split()]
print(snap(arr,n))