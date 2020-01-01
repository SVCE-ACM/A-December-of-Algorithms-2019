given_string = input('Enter String: ')
a_index = [i for i in range(len(given_string)) if given_string[i] in 'aeiou']
b_index = [i for i in range(len(given_string)) if given_string[i] not in 'aeiou']

a_string = []
for index in a_index:
    temp = ''
    for i in range(index,len(given_string)):
        temp += given_string[i]
        a_string.append(temp)
        
b_string = []
for index in b_index:
    temp = ''
    for i in range(index,len(given_string)):
        temp += given_string[i]
        b_string.append(temp)

if len(a_string) > len(b_string):
    print('WINNER IS A WITH {} POINTS.'.format(len(a_string)))
elif len(b_string) > len(a_string):
    print('WINNER IS B WITH {} POINTS.'.format(len(b_string)))
else:
    print('NO ONE WINS AS BOTH HAVE {} POINTS'.format(len(a_string)))
