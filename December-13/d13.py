n = int(input('Enter no of switches:'))
res = [False for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j%i == 0):
            res[j] = not res[j]
print('No of switches in the \'on\' state at the end:',res[1:n+1].count(True))