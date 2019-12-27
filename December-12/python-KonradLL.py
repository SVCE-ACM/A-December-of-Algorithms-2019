import json
import math
import os.path
_dir = os.path.dirname(os.path.abspath(__file__))

def main():
    inputFile = open(_dir + "/../src/res/jaSON.json", 'r')
    inputStr = inputFile.read()
    markers = json.loads(inputStr)

    start = None
    destination = None
    for marker in markers["markers"]:
        if ("start" in marker["name"]):
            start = marker["location"]
        elif ("destination" in marker["name"]):
            destination = marker["location"]
    
    directions = {}
    directions["message"] = "Meet at the destination point"
    directions["distance"] = distanceInKmBetweenEarthCoordinates(start[0], start[1], destination[0], destination[1])
    directions["direction"] = direction(start[0], start[1], destination[0], destination[0])
    
    outputFile = open(_dir + "/../src/res/jaSON-KonradLL.json", 'w')
    outputDirections = json.dumps(directions)
    outputFile.write(outputDirections)

    
def degreesToRadians(degrees):
  return degrees * math.pi / 180


def distanceInKmBetweenEarthCoordinates(lat1, lon1, lat2, lon2):
  earthRadiusKm = 6371

  dLat = degreesToRadians(lat2-lat1)
  dLon = degreesToRadians(lon2-lon1)

  lat1 = degreesToRadians(lat1)
  lat2 = degreesToRadians(lat2)

  a = math.sin(dLat/2) * math.sin(dLat/2) + \
          math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2) 
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)) 
  return earthRadiusKm * c


def direction(lat1, lon1, lat2, lon2):
  earthRadiusKm = 6371

  dLat = degreesToRadians(lat2-lat1)
  dLon = degreesToRadians(lon2-lon1)

  if (dLat > 0 and abs(dLon) < abs(dLat)):
      return 'N'
  elif (dLat < 0 and abs(dLon) < abs(dLat)):
      return 'S'
  elif (dLon > 0 and abs(dLon) > abs(dLat)):
      return 'E'
  elif (dLon < 0 and abs(dLon) > abs(dLat)):
      return 'W'



if __name__ == "__main__":
    main()