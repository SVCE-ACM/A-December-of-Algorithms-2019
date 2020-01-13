def check(num):
    s1 = 0
    s2 = 0
    for i in range(len(num)):
        if(i%2 == 0):
            s1 += int(num[i])
        else:
            tmp = int(num[i]) * 2
            while (tmp > 9):
                tmp -= 9
            s2 += tmp
    tot = s1 + s2
    if( tot % 10 == 0):
        print(num + " passes the test")
    else:
        print(num + " failed the test")


inp = input()

check(inp)
