def alt_balls(n,arr):
    count = 1
    ind = 0
    while(ind < n):
        for i in range(ind, n - 1):
            if(arr[i] != arr[i+1]):
                count += 1
            else:
                break
        ind += count
        while(count >= 1):
            print(count,end=" ")
            count -= 1
        count = 1

n = int(input('Enter # of balls ;) :'))
arr = [e for e in input().split()][0:n]

alt_balls(n,arr)