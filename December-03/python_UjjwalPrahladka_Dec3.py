test_list =[int(x) for x in input('Enter comma separated values: ').split(',')]
while not all(test_list[i] <= test_list[i + 1] for i in range(len(test_list)-1)):
    test_list = test_list[0:len(test_list)//2] # REMOVING LAST HALF
print(test_list)