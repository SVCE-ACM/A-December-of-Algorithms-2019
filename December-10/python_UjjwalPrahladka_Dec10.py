def cookieCount(n,p,c):
    no_of_cookies = 0
    no_of_jars = 0
    no_of_cookies = no_of_jars = n // p
    while no_of_jars >= c:
        no_of_jars -= c
        no_of_cookies += 1
    return no_of_cookies
n,p,c = input('Enter n p c: ').split()
print('Total Cookies Eaten: {}'.format(cookieCount(int(n), int(p), int(c))))
