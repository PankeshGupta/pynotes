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
        distance =  math.sqrt(
            (self.x-point2.x)**2 + (self.y - point2.y)**2)

        print("The distance between 2 points is ",distance,"units ")
if __name__ == "main":
    main()
