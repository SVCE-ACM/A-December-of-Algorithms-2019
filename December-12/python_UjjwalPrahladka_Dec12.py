import json
import math

def calc_distance_and_angle(start_lat, start_long, end_lat, end_long):
    R = 6371
    start_lat, start_long, end_lat, end_long = list(map(to_radians,[start_lat, start_long, end_lat, end_long]))
    dif_lat = end_lat - start_lat
    dif_long = end_long - start_long
    a = math.sin(dif_lat/2) * math.sin(dif_lat/2) + math.cos(start_lat) * math.cos(end_lat) * math.sin(dif_long/2) * math.sin(dif_long/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    angle = math.atan2(math.sin(dif_long) * math.cos(dif_lat) , math.cos(start_lat) * math.sin(end_lat) - math.sin(start_lat) * math.cos(end_lat) * math.cos(dif_long) )
    angle = to_degrees(angle)
    return (d, angle)

def to_radians(point):
    return math.pi * point / 180

def to_degrees(point):
    return 180 * point / math.pi
try:
	with open('E:/JaSON.json','r') as f:
		data = json.load(f)
except:
	print("Please provide resource file in E drive and tr again")
else:
	start_lat, start_long = [i['location'] for i in data['markers'] if i['name'] == 'start'][0]   
	end_lat, end_long = [i['location'] for i in data['markers'] if i['name'] == 'destination'][0]
	distance, angle = calc_distance_and_angle(start_lat, start_long, end_lat, end_long)
	mydict = {"directions": [{"message": "Meet at the destination point","distance": distance,"direction": f'Go {angle} in compass'}]}
	information = json.dumps(mydict, indent=2)
	try:
		with open('E:/direction.json','w') as f:
			f.write(information)
	except:
		print('Error while creating the file')
	else:
		print('Json File created in E drive named: direction')