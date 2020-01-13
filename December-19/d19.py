def left_ind(P): 
	M = 0
	for i in range(1,len(P)): 
		if P[i][0] < P[M][0]: 
			M = i 
		elif P[i][0] == P[M][0]: 
			if P[i][1] > P[M][1]: 
				M = i 
	return M 

def pos(p, q, r): 
	val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]) 
	if val == 0: 
		return 0
	elif val > 0: 
		return 1
	else: 
		return 2

def covex(P, n): 
	if n < 3: 
		return
	l = left_ind(P) 
	hull = [] 
	p = l 
	q = 0
	while(True): 
		hull.append(p) 
		q = (p + 1) % n 
		for i in range(n): 
			if(pos(P[p], 
						P[i], P[q]) == 2): 
				q = i 
		p = q 
		if(p == l): 
			break
	for each in hull: 
		print(P[each][0], P[each][1]) 

n = int(input('Enter # of points:'))
P = [] 
for _ in range(n):
    print('Enter x & y co-orinates:')
    P.append([int(e) for e in input().split()][0:2]) 

print('The covering points are:')
covex(P, len(P)) 

