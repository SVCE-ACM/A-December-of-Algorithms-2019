def check(h, i):
    return h >=i
mylist = input('Enter comma separated citations : ')
mylist = [int(x) for x in mylist if x != ',']
i = 1
while i <= max(mylist):
    comparelist = list(str(i)*len(mylist))
    comparelist = [int(x) for x in comparelist]
    result = list(map(check, mylist, comparelist))
    count  = result.count(True)
    if count < i:
        break
    i = i + 1
print('h_index is : {}'.format(i-1))
