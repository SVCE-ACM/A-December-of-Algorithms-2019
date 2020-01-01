def give_centroid(x1, y1, x2, y2):
    return ((x1 + x2) / 3, (y1 + y2) / 3)
def give_area(x1, y1, x2, y2):
    return 0.5 * ((x1 * y2) - (x2 * y1))
set_of_points = input('Enter vertices(space separated coordinates): ').split()
set_of_points = [(int(point.split(',')[0]), int(point.split(',')[1])) for point in set_of_points]
#sum(Area)
sum_of_areas = 0
#sum(x(i) * area(i)
sum_of_area_times_x = 0
#sum(y(i) * area(i)
sum_of_area_times_y = 0
set_of_points.append(set_of_points[0])

for i in range(len(set_of_points) - 1):
    first_point, second_point = set_of_points[i], set_of_points[i+1]
    area = give_area(*first_point, *second_point)
    sum_of_areas += area
    centroid = give_centroid(*first_point, *second_point)
    sum_of_area_times_x += (area * centroid[0])
    sum_of_area_times_y += (area * centroid[1])

centroid_x = sum_of_area_times_x / sum_of_areas
centroid_y = sum_of_area_times_y / sum_of_areas
print('X:', centroid_x, '  Y:', centroid_y)