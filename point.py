import math
class Point:
    def __init__(self,x,y):
        print("initializing the new point")
        self.x = x
        self.y = y
        print("point created sucessfully")
    def move(self,x,y):
        self.x = x
        self.y = y
        print("point moved sucessfully")
    def calculate_distance(self,point2):
        return math.sqrt(
            (self.x-point2.x)**2 + (self.y - pont2.y)**2)
if __name__ == "main":
    main()
