# Author : Nilesh D
# December 11 - Is This A Valid Email Address
import re


def valid_email(email):
    parts = email.split('@')
    if len(parts) != 2:
        return False

    domain = parts[1]
    if domain[-4:] != ".com":
        return False

    service = domain[:-4]
    if not service.isalpha():
        return False

    if re.match('^[A-za-z0-9._-]*$', parts[0]) == None:
        return False

    return True


print(valid_email('john-doe31@gmail.com'))
print(valid_email('jane.austen_691@dnarifle.com'))
