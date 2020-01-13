def check_for_prime(x):
    if x % 2 == 0 and x != 2:
        return False
    else:
        for i in range(3,x,2):
            if x % i == 0:
                return False
        return True

n = int(input('Enter the value for n : '))
fib_prime = []
fib = [1,1]
while (len(fib_prime)!= n):
    fib.append(fib[0] + fib[1])
    fib.pop(0)
    if check_for_prime(fib[1]):
        fib_prime.append(fib[1])

print('Generated Fibonacci Prime Number Generation Upto {} is : {}'.format(n,fib_prime))
