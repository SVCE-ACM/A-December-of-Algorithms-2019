values = input()
l = values.split(',')
while l != sorted(l):
    size = len(l)
    l = l[:size//2]

print(l)
