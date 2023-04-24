def h_index(n,arr):
    arr.sort()
    max = -1
    for i in range(len(arr)):
        if(len(arr) - i == arr[i]):
            if(arr[i] > max):
                max = arr[i]
    return max



n = int(input('Enter # of papers:'))
arr = [int(e) for e in input().split()]

print(h_index(n,arr))