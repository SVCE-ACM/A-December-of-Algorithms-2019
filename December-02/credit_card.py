n = input("Credit Card No.: ")
s1 = 0
s2 = 0
for i in range(len(n)):
    if(i%2 == 0):
        s1 += int(n[i])
    else:
        tmp = int(n[i]) * 2
        while (tmp > 9):
            tmp -= 9
        s2 += tmp
tot = s1 + s2
if( tot % 10 == 0):
    print(n + " passes the test")
else:
    print(n + " failed the test")
