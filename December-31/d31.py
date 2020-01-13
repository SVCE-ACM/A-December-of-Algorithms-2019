import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = open('../src/res/build_city_csv.csv', 'r')
x = []
y = []
for d in data:
    tmp = d.split(',')
    x.append(float(tmp[0]))
    y.append(float(tmp[1]))
X = np.array(list(zip(x,y)))
kmeans = KMeans(n_clusters=3)
kmeans = kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_
cx = []
cy = []
i = 0
for e in centroids.tolist():
    print('Store {} : '.format(i),e)
    cx.append(e[0])
    cy.append(e[1])
    i += 1
plt.scatter(x,y,c='blue')
plt.scatter(cx,cy,c='red')
plt.show()