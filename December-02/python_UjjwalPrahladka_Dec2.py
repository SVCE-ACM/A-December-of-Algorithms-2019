card_number = str(input('Enter credit card number : '))
try:
	card_number = card_number[::-1]
	s1 = 0
	s2 = 0
	for odd_index in range(0,len(card_number),2):
	    s1 = s1 + int(card_number[odd_index])
	for even_index in range(1,len(card_number),2):
	    num = int(card_number[even_index])*2
	    num = [int(x) for x in str(num)]
	    s2 = s2 + sum(num)
	total_sum = s1 + s2
	card_number = card_number[::-1]
	if total_sum % 10 == 0:
	    print('{} passes the test'.format(card_number))
	else:
	    print('{} did not pass the test'.format(card_number))
except:
	print('{} did not pass the test'.format(card_number))