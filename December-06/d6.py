import math

def isSquare(n):
    rt = int(math.sqrt(n))
    return rt*rt == n

def isFib(n):
    return isSquare(5*n*n + 4) or isSquare(5*n*n - 4)

def generate(m):
    if(m>9):
        print('This leads to memory error')
        return
    primes = [True for i in range(10**7)]
    primes[0] = primes[1] = False
    n = len(primes)
    count = 0
    for i in range(2,n):
        if(primes[i]):
            if(isFib(i)):
                print(i)
                count += 1
                if(count == m):
                    return
            ind = 2
            tmp = i*ind
            while(tmp < n):
                primes[tmp] = False
                ind += 1
                tmp = i*ind

            
    


n = int(input("Enter a number between 1-9:"))
generate(n)






