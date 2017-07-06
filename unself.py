# Author : Pankesh
# Email  :  post4pankesh@gmail.com
# This program demostartes that we can use anything instead of 'self' keyword
# But according to convention we use self and its important to us

class Point:
    "Class Point which describes a point in 2-D ' x ' and ' y '"
    def __init__(point,x,y): #initializer
        point.x = x  # see here we are using point in place of self
        point.y = y  # point is used used to reffer to the current object
        print("Point Object initialized sucessfully")
    def reset(pankesh): # this is an instace method and can be called only by an instance of Point class
        pankesh.x = 0
        pankesh.y = 0
        print(" the point has been reset to origin ")
if __name__ == "main":
    main()
        
    
