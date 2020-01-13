room = []
rows = 0
columns = 0

def calculate_prob(current,i,j):
	prob = 0 
	if (j+1) < columns and room[i][j+1] == current:
		prob += 0.2
	if (j-1) >= 0 and room[i][j-1] == current:
		prob += 0.2
	if (i-1) >= 0 and room[i-1][j] == current:
		prob += 0.3
	if (i+1) < rows and room[i+1][j] == current :
		prob += 0.2
	if (i-1) >= 0 and (j-1) >= 0 and room[i-1][j-1] == current:
		prob += 0.025
	if (i+1) < rows and (j-1) >= 0 and room[i+1][j-1] == current:
		prob += 0.025
	if (i-1) >= 0 and (j+1) < columns and room[i-1][j+1] == current:
		prob += 0.025
	if (i+1) < rows and (j+1) < columns and room[i+1][j+1] == current:
		prob += 0.025

	return round(prob,3)

while True:
	try:
		rows = int(input('Enter no. of rows: '))
	except:
		print('Enter integer please')
	else:
		break
		
while True:
	try:
		columns = int(input('Enter no. of columns: '))
	except:
		print('Enter integer please')
	else:
		break

print('Enter Branches')
for i in range(rows):
	print(f'Enter row {i+1}:')
	entered = False
	while not entered:
		row = input()
		row = row.split()
		if len(row) != columns:
			print("No. of Branches provided were not equal to columns")
			print("Please enter again")
		else:
			entered = True
	room.append(row)

cheat_prob = [[0 for i in range(columns)] for j in range(rows)]

for i in range(rows):
	for j in range(columns):
		current = room[i][j]
		prob = calculate_prob(current,i,j)
		cheat_prob[i][j] = prob
		
for prob in cheat_prob:
	print(prob)