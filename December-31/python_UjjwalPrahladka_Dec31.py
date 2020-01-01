import random
from matplotlib import pyplot as plt
def closest(point, centroid1, centroid2, centroid3):
    dist1 = ((point[0] - centroid1[0])**2 + (point[1] - centroid1[1])**2)**0.5
    dist2 = ((point[0] - centroid2[0])**2 + (point[1] - centroid2[1])**2)**0.5
    dist3 = ((point[0] - centroid3[0])**2 + (point[1] - centroid3[1])**2)**0.5
    minimum = min(dist1, dist2, dist3)
    if minimum == dist1:
        return centroid1
    elif minimum == dist2:
        return centroid2
    return centroid3

def calc_centroid(cluster):
    x = 0
    y = 0
    for xcord, ycord in cluster:
        x += xcord
        y += ycord
    return (round(x / len(cluster)),round(y / len(cluster)))

dataset = []
with open('E:/build_city_csv.csv','r') as f:
    data = f.readlines()
    for line in data:
        line = line.rstrip('\n')
        line = line.split(',')
        dataset.append((float(line[0]), float(line[1])))

centroid1 = dataset[0]
centroid2 = dataset[1]
centroid3 = dataset[2]
while True:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    for point in dataset:
        centroid = closest(point, centroid1, centroid2, centroid3)
        if centroid == centroid1:
            cluster1.append(point)
        elif centroid == centroid2:
            cluster2.append(point)
        else:
            cluster3.append(point)
    newcentroid1 = calc_centroid(cluster1)
    newcentroid2 = calc_centroid(cluster2)
    newcentroid3 = calc_centroid(cluster3)
    if centroid1 == newcentroid1 and centroid2 == newcentroid2 and centroid3 == newcentroid3:
        break
    centroid1 = newcentroid1
    centroid2 = newcentroid2
    centroid3 = newcentroid3
print('Store1: {}\nStore2: {}\nStore3: {}'.format(centroid1,centroid2,centroid3))

X = []
Y = []
for point in cluster1:
    X.append(point[0])
    Y.append(point[1])
plt.scatter(X, Y, c='#ff0000')

X = []
Y = []
for point in cluster2:
    X.append(point[0])
    Y.append(point[1])
plt.scatter(X, Y, c='#00ff00')

X = []
Y = []
for point in cluster3:
    X.append(point[0])
    Y.append(point[1])
plt.scatter(X, Y, c='#0000FF')

plt.scatter(*centroid1,c='#000000')
plt.scatter(*centroid2,c='#000000')
plt.scatter(*centroid3,c='#000000')

plt.show()