n = int(input('Length of the output:'))
output = [int(e) for e in input().split()][0:n]
print()
count = 0
for i in range(0,n,3):
    try:
        count += 1
        print(output[i],end=" ")
    except(e):
        break
print()
print("Length:",count)