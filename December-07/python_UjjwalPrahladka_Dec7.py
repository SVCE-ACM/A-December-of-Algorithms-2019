queue = []

def enqueue(patient,pos):
	queue.insert(pos, patient)

def dequeue(pos = 0):
    return queue.pop(pos)

n = 0
while True:
	try:
		n = int(input('Enter no. of patients: '))
	except:
		print('Enter integer please')
	else:
		break

for token_no in range(1,n+1,1):
	patient_id = input(f'Enter patient{token_no} id: ')
	patient = (token_no,patient_id)
	enqueue(patient,token_no - 1)

for patient in queue:
	print(patient)

vip = ()
found = False
while not found:
	k = input("Enter k: ")
	for patient in queue:
		if patient[1] == k:
			vip = patient
			found = True
			break

vip = dequeue(vip[0] - 1)
enqueue(vip,0)
print('The order is:')
for patient in queue:
	print(patient)


