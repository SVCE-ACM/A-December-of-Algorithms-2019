import json
import math

def degreesToRadians(degrees):
  return degrees * math.pi / 180

def distance(lat1, lon1, lat2, lon2):
  earthRadiusKm = 6371
  dLat = degreesToRadians(lat2-lat1)
  dLon = degreesToRadians(lon2-lon1)
  lat1 = degreesToRadians(lat1)
  lat2 = degreesToRadians(lat2)
  a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2); 
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)); 
  return earthRadiusKm * c

JaSON = open('./src/res/JaSON.json','r')
parsed = json.loads(JaSON.read())

result = {
    'directions':[
        {
            'message':'',
            'distance':0,
            'direction':'N'
        }
    ]
}
markers = parsed['markers']
start = markers[0]['location']
destination = markers[1]['location']

result['directions'][0]['distance'] = distance(start[0],start[1],destination[0],destination[1])
result['directions'][0]['message'] = input('Enter some message:')
result['directions'][0]['direction'] = input('Enter the direction(N,S,W,E):')
 
print( json.dumps(result,indent = 4) )

JaSON.close()