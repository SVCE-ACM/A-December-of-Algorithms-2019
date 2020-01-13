n = int(input('How many lines of input are there: '))
print("Enter the lines(* for missing, P- for parity bit):")
data = []
restored_data = []
for i in range(n):
    data.append(input().split())
for line in data:
    if line.count('*') > 1:
        print('Missing bits are more then 1')
        break
    else:
        parity_bit = '0'
        for x in line:
            if 'P' in x:
                parity_bit = x[0]
                break
        if line.count('1') % 2 == 0:
            if parity_bit == '0':
                res = [sub.replace('*','0') for sub in line]
            else:
                res = [sub.replace('*','1') for sub in line]
        else:
            if parity_bit == '0':
                res = [sub.replace('*','1') for sub in line]
            else:
                res = [sub.replace('*','0') for sub in line]
        restored_data.append(res)
print('Data after restoration:')
for line in restored_data:
    print(' '.join(line)) 