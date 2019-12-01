def sevenis(n):
    arr = [] 
    i = 0
    while(n > len(arr)):
        tmp = pow(7,i)
        arr.append(tmp)
        for j in range(len(arr)-1):
            arr.append(arr[j]+tmp)
        if(len(arr) > n):
            break
        i += 1
    return arr[n-1]

n = int(input())

print(sevenis(n))


