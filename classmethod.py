#author : Pakesh Gupta
#email : post4pankesh@gmail.com
# program to demonastrate class methods and class attributes

class Contact:
    all_contacts = [] # class atttribute that has no effect to creation of new objects
    def __init__(self,name,number):
        self.name = name
        self.number = number
        print(" contact succesfully created ")
        Contact.all_contacts.append(self)
    def fetch_all_contacts(): # class method 'Contact.fetch_all_contacts()'
        for i in Contact.all_contacts:
            print("============")
            print(i.name)
            print(i.number)
            print("====xxx======")
if __name__ == "main" :
    main()
