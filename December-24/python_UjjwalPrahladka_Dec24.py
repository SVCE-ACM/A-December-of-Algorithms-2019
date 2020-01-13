sequence = input('Enter part of algo output(space separated data): ').split()
mylist = []
if len(sequence) >= 3:
    #taking first three numbers as they would always be part of the input 
    mylist.append(sequence[0])
    mylist.append(sequence[1])
    mylist.append(sequence[2])
    #taking all third elements
    for i in range(5,len(sequence),3):
        mylist.append(sequence[i])
    i = 0
    found = False
    #looking for repeating patterns as the list is circuar. Eg. [1,2,1,2,1,2] = [1,2] , [1,2,3,1,2] = [1,2,3]
    while not found:
        pattern = mylist[:i+1]
        length = len(pattern)
        x = 0
        j = i + 1
        while j < len(mylist):
            if mylist[x] != mylist[j]:
                break
            x = (x + 1) % (i + 1)
            j += 1
        else:
            found = True
        i += 1
    print(mylist[:i])
else:
    print('The input should contain atleat 3 numbers')