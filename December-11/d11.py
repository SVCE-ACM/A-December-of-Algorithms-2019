def check(email):
    if('@' not in email):
        print('@ is required')
        return
    elif(email.count('@') > 1):
        print('@ is used more than once')
        return
    else:
        alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number = "1234567890"
        chars = "._-"
        parts = email.split('@')
        name = parts[0]
        domain = parts[1]
        for e in name:
            if(e not in alpha and e not in number and e not in chars):
                print('Invalid characters')
                return
        for e in domain:
            if(e not in alpha and e != '.'):
                print('Invalid domain')
                return
        if(domain[-1:-5:-1] != "moc."):
            print('.com is required')
            return
        if(len(domain) < 5):
            print('domain is required')
            return
    print('Email is valid')

email = input('Enter the email:')
check(email)