def buildTower(n,arr):
    count = 0
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        if(diff == 1):
            continue
        elif(diff == 0):
            count += 1
            mid = int(len(arr)/2)
            if( i < mid):
                arr[i] -= 1
            else:
                arr[i+1] -= 1
        else:
            count += diff-1
            arr[i+1] -= diff-1
    print("Minimum operation:",count)
    print("After operation:",arr)

n = int(input('Enter # of compartments: '))
arr = [int(e) for e in input().split()][0:n]

buildTower(n,arr)