def path1(r,start,end):
    try:
        return abs(r.index(start) - r.index(end))
    except ValueError:
        return 10000

def path2(r1,r2,inter,start,end):
    try:
        d1 = abs(r1.index(start) - r1.index(inter))
        d2 = abs(r2.index(inter) - r2.index(end))
        return d1 + d2
    except ValueError:
        return 10000

def intersection(r1,r2):
    inter = []
    for e in r1:
        if(e in r2):
            inter.append(e)
    return inter

def print1(r,start,end):
    for i in range(r.index(start),r.index(end)+1):
        print(r[i],end=" -> ")

def print2(r1,r2,inter,start,end):
    print1(r1,start,inter)
    print1(r2,r2[r2.index(inter)+1],end)

def path(r1,r2,start,end):
    d1 = path1(r1,start,end) # start & end in r1
    d2 = path1(r2,start,end) # start & end in r2
    d3 = d4 = 10000 # start & end in r1 & r2
    mini = None
    inter = intersection(r1,r2)
    for e in inter:
        md3 = path2(r1,r2,e,start,end)
        md4 = path2(r2,r1,e,start,end)
        if(md3 < d3):
            d3 = md3
            mini = e
        if(md4 < d4):
            d4 = md4
            mini = e
    short = min(d1,d2,d3,d4)
    print('Shortest path:')
    if(short == d1):
        print1(r1,start,end)
    elif(short == d2):
        print1(r2,start,end)
    elif(short == d3):
        print2(r1,r2,mini,start,end)
    elif(short == d4):
        print2(r2,r1,mini,start,end)

r1 = [s for s in input('Line 1: ').split(',')]
r2 = [s for s in input('Line 2: ').split(',')]
start = input('Start: ')
end = input('End: ')

path(r1,r2,start,end)

