import math
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(p1,p2):
        return math.sqrt((p1.x-p2.x)**2 +(p1.y-p2.y)**2)
class Polygon():
    # this doesnt do anything just initializes a vertices instance attribute
    def __init__(self,points = []):
        self.vertices = []
        # we add this for loop to extend our polygon class
        # using this we ca instantiate points by pasing them here
        for point in points:
            if isinstance(point,tuple):
                point = Point(*point)
                self.vertices.append(point)
            self.vertices.append(point)    
        
    # call add_point : add_point(Point(1,1))
    def add_point(self,point):
        self.vertices.append(point)
    # method to find perimeter of the polygon
    
    def perimeter(self):
        perimeter = 0
        # this is just to felicitate the traversal of points
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter
if __name__ == "main":
    main()
    
    
