#author : pankesh gupta
#email : post4pankesh@gmail.com

# this is an example of overiding and  concept of super in python

class Contact():
    
    all_contacts= list()

    def __init__(self,name,email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def try0(self):
        print("hi im inside the contacts class")
    def try1(self):
        print("hi this method is for testing the tr1 in contacts")
        print("this method is an instace method")
    def try2():
        print("this is tr2 this method is inside the tr2 method in contacts class")
        
class Friend(Contact):
    def __init__(self,name,email,ph):
        super().__init__(name,email)
        self.ph = ph
    def try0(self):
        super.try0()
        print("hi i m inside the class friends")


if __name__=="main":
    main()
#=========== console output ======== #    
#>>> c = Contact('c','c@gmail.com')
#>>> f = Friend('f','f@gmail.com',1234)
#>>> f.try0()
#hi i m inside the class friends
#>>> f.tr1()
#hi this method is for testing the tr1 in contacts
#this method is an instace method
#>>> f.tr1
#<bound method Contact.tr1 of <__main__.Friend object at 0x028ED4F0>>
#>>> c.tr1
#<bound method Contact.tr1 of <__main__.Contact object at 0x028D2BD0>>
#>>>
