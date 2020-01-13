from itertools import permutations
quantity_of_A = int(input('Quantity Of A(in grams): '))
cases = 'A' * quantity_of_A + 'B' * quantity_of_A

cases = permutations(cases)
cases = list(set(cases))

result = []
for case in cases:
    if case[-1] == 'A' or case[0] == 'B':
        continue
    quantity = 0
    for ingred in case:
        if ingred == 'A':
            quantity += 1
        else:
            quantity -= 1
        if quantity < 0:
            break
    else:
        result.append(''.join(case))
print('Combination:',result)
print(end - start)
    