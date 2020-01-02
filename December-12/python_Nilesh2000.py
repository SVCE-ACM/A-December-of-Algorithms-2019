# Author - Nilesh D
# December 12 - Show JaSON the way
import json
import math


def main():
    input_file = open("../src/res/JaSON.json", 'r')
    input_str = input_file.read()
    markers = json.loads(input_str)

    start = None
    destination = None
    for marker in markers["markers"]:
        if "start" in marker["name"]:
            start = marker["location"]
        elif "destination" in marker["name"]:
            destination = marker["location"]

    directions = {}
    directions["message"] = "Meet at the destination point"
    directions["distance"], directions["direction"] = distanceInKmBetweenEarthCoordinates(
        start[0], start[1], destination[0], destination[1])

    output_file = open("JaSONMessage.json", 'w')
    outputDirections = json.dumps(directions)
    output_file.write(outputDirections)


def degreesToRadians(degrees):
    return degrees * math.pi / 180


def distanceInKmBetweenEarthCoordinates(lat1, lon1, lat2, lon2):
    earthRadiusKm = 6371

    dLat = degreesToRadians(lat2-lat1)
    dLon = degreesToRadians(lon2-lon1)

    lat1 = degreesToRadians(lat1)
    lat2 = degreesToRadians(lat2)

    a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * \
        math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

# Latitude and longitude are angles that uniquely define points on a sphere. ... Latitudes of +90 and -90 degrees correspond to the north   and south geographic poles on the earth, respectively.
    if dLat > 0 and abs(dLon) < abs(dLat):
        return earthRadiusKm * c, 'N'
    elif dLat < 0 and abs(dLon) < abs(dLat):
        return earthRadiusKm * c, 'S'
    elif dLon > 0 and abs(dLon) > abs(dLat):
        return earthRadiusKm * c, 'E'
    elif dLon < 0 and abs(dLon) > abs(dLat):
        return earthRadiusKm * c, 'W'


if __name__ == "__main__":
    main()
