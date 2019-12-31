def restore(arr):
    print("D1| D2| D3| D4| D5")
    for e1 in arr:
        count = 0
        for e2 in e1:
            if(e2[0] == '1'):
                count += 1
        if(count % 2 == 0):
            e1[e1.index('*')] = '0'
        else:
            e1[e1.index('*')] = '1'
        for e2 in e1:
            print(e2,end="   ")
        print()
n = int(input("Enter # of data:"))
arr = []
print("D1| D2| D3| D4| D5")
for _ in range(n):
    arr.append([e for e in input().split()])
print()
restore(arr)
