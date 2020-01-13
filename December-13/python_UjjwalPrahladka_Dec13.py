import math
def linear_time(n):
	mylist = [True]*n
	print('After Iteration 1:', mylist)
	for i in range(2, n+1):
	    j = i
	    while j <= n:
	        mylist[j-1] = not mylist[j-1]
	        j += i
	    print('After Iteration {}: {}'.format(i, mylist))
	print('No. of switches in on state(linear time):', mylist.count(True))

def constant_time(n):
	print('No. of switches in on state(constant time):', math.floor(n**0.5)) 

n = int(input("ENTER N(+ve and greater than zero): "))
linear_time(n)
constant_time(n)