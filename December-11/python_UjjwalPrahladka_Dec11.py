import re 

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
email = input("Enter email: ")

if(re.search(regex,email)):  
    print("Valid Email")  
          
else:  
     print("Invalid Email")  
    