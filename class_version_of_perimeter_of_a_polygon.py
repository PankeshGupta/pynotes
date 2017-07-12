import math
class point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(p1,p2):
        return math.sqrt((p1.x-p2.x)**2 +(p1.y-p2.y)**2)
class polygon():
    def __init__(self):
        self.vertices = []
    def add_point(self,point):
        self.vertices.append(point)
    def perimeter(self):
        perimeter = 0
        point = []
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter
if __name__ == "main":
    main()
    
    
