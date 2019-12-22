import itertools
import threading
import os

def search(s,e,ele):
    comb = [e for e in itertools.product([ chr(e) for e in range(s,e+1)], repeat=len(ele))]
    for e in comb:
        tmp = ''.join(e)
        if(tmp == ele):
            print('found')
            break

def thread(s,e,ele):
    t1 = threading.Thread(target = search, args = (s,e,ele,))
    t1.start()

inp = input('Enter the password:')
for i in range(32,127,10):
    thread(i,i+10,inp)