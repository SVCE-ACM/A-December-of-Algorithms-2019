def get(setn,no):
    print('Enter the elements in set {}'.format(no))
    setn.update([int(e) for e in input().split()])

def check(set1,set2,function):
    set3 = set()
    func = function.replace('x','{}')
    func = func.replace('^','**')
    for e in set1:
        set3.add(int(eval(func.format(e))))
    if(len(set1) == len(set3) and set3.issubset(set2)):
        print('It is one-to-one function')
    else:
        print('It is not one-to-one function')

set1 = set()
set2 = set()
get(set1,1)
get(set2,2)
function = input('Enter the function use \'x\' as placeholder:')
check(set1,set2,function)
