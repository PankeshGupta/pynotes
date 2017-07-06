# We can re- instantize and object using the __init__ method explicitly

class a:
    def __init__(self,x,y):
        self.x = x
        self.y = y

if __name__=="main":
    main()

# abc = a(1,2)
# abc.x returns 1
# abc.y return  2
# if we do somethig like abc.__init__(122,123)
# it works perfectly fine
# i know that we can obviously do something like abc.x = 122
# but here i was just checking if ths works
