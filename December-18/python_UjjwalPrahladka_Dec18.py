import threading
import time
from itertools import product
#thread 1's work
#checks password which start with char(32) to char(80)
def work1():
    global found 
    global guessed_password 
    while not found:
        try:
            #getting a combination of n - 1 characters
            word = generatorfor1.__next__()
            for char in range(32,80):
                #combines the given combinaton with ascii(32 - 63) 
                if list(chr(char)) + list(word) == password:
                    found = True 
                    guessed_password = list(chr(char)) + list(word)
                    break
        except:
            return

#thread 2's work
#checks password which start with char(80) to char(127)
def work2():
    global found 
    global guessed_password 
    while not found:
        try:
            word = generatorfor2.__next__()
            for char in range(80,127):
                if list(chr(char)) + list(word) == password:
                    found = True 
                    guessed_password = list(chr(char)) + list(word)
                    break
        except:
            return

                
password = list(input('Enter password: '))
length = len(password)
mypassword = [chr(i) for i in range(32,127)]
#combinations for thread 1
generatorfor1 = product(mypassword, repeat = length - 1)
#combinations for thread 2
generatorfor2 = product(mypassword, repeat = length - 1)
found = False
guessed_password = ''

t1 = threading.Thread(target = work1)
t2 = threading.Thread(target = work2)

start = time.perf_counter()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.perf_counter()

print('Your Password: {}  Time Taken: {}'.format((''.join(guessed_password)), end - start))