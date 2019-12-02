# Started On : December 1, 2019
# Author : Nilesh D
# Objective : Check for a valid credit card number

num = input()
rev_num = "".join(reversed(num))
odd_list_sum = 0
even_list=[]

for i in range(0, len(rev_num), 2):
  odd_list_sum += int(rev_num[i])

for i in range(1, len(rev_num), 2):
  even_list.append(int(rev_num[i]))
  
for i in range(0, len(even_list)):
  even_list[i] *= 2
  if even_list[i]%9 == 0 and even_list[i] != 0:
    even_list[i] = 9
  else:
    even_list[i] %= 9

even_list_sum = sum(even_list)
total = odd_list_sum + even_list_sum

if total%10 == 0:
  print(num, " passes the test.")
else:
  print(num, " does not pass the test.")
    