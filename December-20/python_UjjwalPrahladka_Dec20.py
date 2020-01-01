def give_cost(start, left = []):
    #salesman has reachead to the last point 
    if len(left) == 0:
        return cost[start][starting_point]

    else:
        possible_paths = []
        for index,k in enumerate(left):
            possible_paths.append(cost[start][k]+give_cost(k,(left[0:index]+left[index+1:])))
        return min(possible_paths)

n = int(input('Enter no. of cities: '))
print('Enter matrix:\n')
cost = []
cities = [i for i in range(n)]
for i in range(n):
    row = [int(x) for x in input().split()]
    cost.append(row)
starting_point = 0
minimum = give_cost(starting_point, cities[1:])
print('Shortest distance:', minimum)