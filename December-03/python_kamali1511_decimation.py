
n = int(input())
lst=[]
for i in range(0,n):
    element = int(input())
    lst.append(element)
if(lst == sorted(lst)):
  print(lst)
else:
    print(lst,end=" -> ")
    while(len(lst)>=0)and(lst!=sorted(lst)):
        del lst[1::2]
        print(lst,end="")
        if(lst!=sorted(lst)):
            print(" -> ",end="")



