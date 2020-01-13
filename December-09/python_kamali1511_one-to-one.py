import string
l1 = []
l2 = []
l3 = []
x =0
n1 = int(input("n1:"))
for i in range (0,n1):
    el = int(input())
    l1.append(el)
n2 = int(input("n2:"))
for j in range(0,n2):
    el = int(input())
    l2.append(el)

function = input("enter the function:")
for i in range(len(l1)):
    x = l1[i]
    answer = eval(function)
    if answer in l2:
        l2.remove(answer)
        l3.append(answer)

if(len(l1)==len(l3)):
    print("one to one")
else:
    print("not one to one")