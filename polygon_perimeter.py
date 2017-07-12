import math
def distance(point1,point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
def perimeter(polygon):
    perimeter = 0
    points = polygon + [polygon[0]]
    for i  in range(len(polygon)):
        perimeter+=distance(points[i],points[i+1])
        return perimeter
