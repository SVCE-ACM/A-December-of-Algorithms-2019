from  collections import deque
list1 = input('Enter railline 1(comma separated stations): ').lower().split(',')
list2 = input('Enter railline 2(comma separated stations): ').lower().split(',')
stations = list(set(list1 + list2))
try:
    starting_node, end_node = input('Enter start and destination(comma separated): ').lower().split(',')
    if starting_node not in stations or end_node not in stations:
        raise
except:
    print('Station not found. Please try again')
else:
    #preparing an adjacency list 
    connection = [[0 for i in range(len(stations))] for j in range(len(stations))]
    for i in range(len(list1) - 1):
        prev_station = stations.index(list1[i])
        next_station = stations.index(list1[i+1])
        connection[prev_station][next_station] = 1
        connection[next_station][prev_station] = 1
    for i in range(len(list2) - 1):
        prev_station = stations.index(list2[i])
        next_station = stations.index(list2[i+1])
        connection[prev_station][next_station] = 1
        connection[next_station][prev_station] = 1
    paths = ['' for i in range(len(stations))]
    visited = [0 for i in range(len(stations))]
    #performing bfs and storing the individual paths
    queue = deque()
    queue.append(starting_node)
    visited[stations.index(starting_node)] = 1

    while len(queue) != 0:
        current = queue.popleft()
        for i in range(len(stations)):
            if connection[stations.index(current)][i] == 1 and visited[i] == 0:
                queue.append(stations[i])
                paths[i] = paths[stations.index(current)] + ' ' + current
                visited[i] = 1
    print('Shortest route: ')
    mypath = paths[stations.index(end_node)]
    mypath = mypath.strip().replace(' ', '->')
    print(mypath + '->' + end_node)