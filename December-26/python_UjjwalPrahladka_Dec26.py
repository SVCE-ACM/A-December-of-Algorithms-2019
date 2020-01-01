import math

def give_blueprint(n):
    #gives the blueprint. Eg. if n = 3 temp= [1,2,1], n = 5 temp = [1,2,3,2,1]
    temp = [1]
    mid = n // 2
    for i in range(1, mid + 1):
        temp.append(temp[-1] + 1)
    for i in range(mid + 1, n):
        temp.append(temp[-1] - 1)
    return temp

def build_tower(n, h_arr):
    operation = [math.inf,[]]
    #for every index we build towers with different no. of compartments
    for start in range(n):
        total_no_of_compartments = 1
        #check if there are that many compartments available or not after the given index
        while total_no_of_compartments <= (n - start):
            #getting the blueprint of how the tower is gonna look
            blueprint = give_blueprint(total_no_of_compartments)
            #getting the part of the list where the tower is going to be built
            compare_with = h_arr[start:start + total_no_of_compartments]
            #this list contains the no of operation needed to covert each compartment to its equivalent size in blueprint
            temp = [x1 - x2 for (x1, x2) in zip(compare_with, blueprint)]
            #if list contains negative number that design of tower cannot be built
            if sum(n < 0 for n in temp) > 0:
                total_no_of_compartments += 2
                continue
            else:
                operations_required = sum(temp) + sum(h_arr[:start]) + sum(h_arr[start + total_no_of_compartments:])
                if operations_required < operation[0]:
                    operation[0] = operations_required
                    operation[1] = [0 for i in range(start)] + blueprint + [0 for i in range(start + total_no_of_compartments,len(h_arr))]
                #total no of compartments in the tower cannot be an even number due to the given restrictions
                total_no_of_compartments += 2
            
            
    print('Minimum no.of operations required = {} \t Design = {}'.format(operation[0], operation[1]))