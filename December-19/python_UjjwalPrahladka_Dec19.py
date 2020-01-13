from collections import deque
def dist(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def orientation(x1, y1, x2, y2, x3, y3):
    val = (y2 - y1) * (x3 - x2) - (x2 - x1) * (y3 - y2)
    if val == 0:
        return 0
    else:
        return 1 if val > 0 else 2

def sort_based_on_angle(points, x1, y1):
    size = len(points)
    i = 0
    while i < size:
        j = 0
        swapped = False
        while j < size - 1 - i:
            (x2, y2), (x3, y3) = points[j], points[j+1]
            dif = (y2 - y1) * (x3 - x1) - (y3 - y1) * (x2 - x1)
            if dif == 0:
                if dist(x1, y1, x2, y2) < dist(x1, y1, x3, y3):
                    points.pop(j)
                else: 
                    points.pop(j+1)
                j -= 1
                size -= 1
            elif dif > 0:
                swapped = True
                temp = points[j]
                points[j] = points[j+1]
                points[j+1] = temp
            j += 1
        if not swapped:
            break
        i += 1
                

def give_minY(points):
    minimum = points[0][1]
    pos = 0
    for (index,(x,y)) in enumerate(points):
        if y < minimum:
            minimum = y
            pos = index
            
    return pos
points = input('Enter space separated points(x,y): ').split()
for index,point in enumerate(points):
    x,y = point.split(',')
    points[index] = (int(x),int(y))
minimum_index = give_minY(points)
periphery = deque()
periphery.append(points.pop(minimum_index))
sort_based_on_angle(points, *periphery[0])
if len(points) >= 2:
    periphery.append(points.pop(0))
    periphery.append(points.pop(1))
    for i in range(len(points)):
        while orientation(*periphery[len(periphery) - 2], *periphery[len(periphery) - 1], *points[i]) != 2:
            periphery.pop()
        periphery.append(points[i])
    print('The outer limits are:',end = ' ')
    while periphery:
        print(periphery.popleft(), end = '  ')
else:
    print("Convex Hull Not Possible")

