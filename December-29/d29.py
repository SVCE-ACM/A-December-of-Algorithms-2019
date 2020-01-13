def rotate(array,n = 26):
    arr = array[0:26] 
    temp = arr[0] 
    for i in range(n-1): 
        arr[i] = arr[i+1] 
    arr[n-1] = temp
    return arr 
table = [ 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()]
for i in range(25):
    table.append(rotate(table[-1]))

cipher = input('Enter the ciphered text:').upper()
keyword = input('Enter the keyword:').upper()
keystream = (keyword*(int(len(cipher)/len(keyword))+1))[0:len(cipher)]

for i in range(len(keystream)):
    col = ord(keystream[i]) - 65
    for j in range(26):
        if(table[j][col] == cipher[i]):
            print(chr(j+65),end="")
            break