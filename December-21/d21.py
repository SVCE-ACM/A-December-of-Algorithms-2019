def marching_partners(n,stu,d):
    stu.sort()
    count = i = 0
    while(i < n-1):
        if(abs(stu[i] - stu[i+1]) <= d):
            count += 1
            i += 2
        else:
            i += 1
    return count

n = int(input('Enter # of students:'))
print('Enter height of each student')
stu = [int(e) for e in input().split()][0:n]
d = int(input('Enter the threshold:'))

print('No of pairs: ',marching_partners(n,stu,d))