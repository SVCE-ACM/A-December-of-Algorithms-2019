index = input('Enter the number : ')
sevenish = []
i = 0
while len(sevenish) < index:
	#all powers of seven would be sevenish 
    sevenish.append(7**i)
    last_index = len(sevenish)-1
    for num in range(len(sevenish)-1):
    	#adding the current power of seven to all the present elements
        sevenish.append(sevenish[last_index]+sevenish[num])
        if len(sevenish) == index:
            break
    i = i + 1
print('The {} sevenish number is {}'.format(index, sevenish.pop()))
