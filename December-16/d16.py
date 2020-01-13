def order(inp):
    ord =  {'a':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'j':10,'q':11,'k':12}
    return ord[inp[0:-1]]

def sort(inp):
    for i in range(len(inp)-1):
        for j in range(len(inp)-i-1):
            if(order(inp[j]) > order(inp[j+1])):
                inp[j],inp[j+1] = inp[j+1],inp[j]

def straight_flush(inp):
    flag1 = True
    flag2 = True
    for i in range(len(inp)-1):
        if( inp[i][-1] != inp[i+1][-1] ):
            flag1 = False
            break
    for i in range(len(inp)-1):
        if(  order(inp[i+1]) - order(inp[i]) != 1 and (order(inp[i+1]) == 10 and order(inp[i]) == 0)):
            flag2 = False
            break
    if(flag1 and flag2):
        print('straight-flush')
    elif(flag1):
        print('flush')
    elif(flag2):
        print('straight')
    if(flag1 or flag2):
        return True
    else:
        return False


def x_of_kind(inp):
    count = 1
    result = []
    for i in range(len(inp)-1):
        if(inp[i][0:-1] == inp[i+1][0:-1]):
            count += 1
        else:
            result.append(count)
            count = 1
    result.append(count)
    return result

def poker(inp):
    sort(inp)
    if(straight_flush(inp)):
        return
    elif(1):
        res = sorted(x_of_kind(inp))
        if(res == [5]):
            print('five-of-kind')
        elif(res == [1,4]):
            print('four-of-kind')
        elif(res == [1,1,3]):
            print('three-of-kind')
        elif(res == [2,3]):
            print('full-house')
        elif(res == [1,2,2]):
            print('two-pair')
        elif(res == [1,1,1,2]):
            print('one-pair')
        elif(res == [1,1,1,1,1]):
            print('high-card')
        else:
            print('invalid')

inp = [e for e in input('Enter the cards:').split()]
poker(inp)
