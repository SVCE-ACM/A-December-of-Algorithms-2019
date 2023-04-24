def count(s,pat):
    c = 0
    for i in range(len(s)):
        if(s[i] in pat):
            c += len(s) - i
    return c

s = input('Enter the string:')

A = count(s,'aeiou')
B = count(s,'bcdfghjklmnqrstvwxyz')

if(A >B):
    print('The winner is A with {} points'.format(A))
else:
    print('The winner is B with {} points'.format(B))