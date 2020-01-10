s = input("Enter the string: ")
A= []
B= []
for i in range (0,len(s)):
    if(s[i]== 'a'or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
        m=i
        r=1
        if m==0:
            m+=1
            p = int(len(s)+1)
        else:
            p = int(len(s))
        while m<=p-1:
            k = s[i:i+r]
            r+=1
            m+=1
            A.append(k)
    else:
        j=i
        k=1
        if j==0:
            j+=1
            p = int(len(s)+1)
        else:
            p = int(len(s))
        while j<=p-1:
            l = s[i:i+k]
            j+=1
            k+=1
            B.append(l)
print("A's Score is",len(A))
print(A)
print("B's Score is",len(B))
print(B)
if(len(A)>len(B)):
    print("The Winner is A with",len(A),"pts" )
else:
    print("The Winner is B with",len(B),"pts" )
