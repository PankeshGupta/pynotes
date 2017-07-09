#author : pankesh gupta
#email : post4pankesh@gmail.com

# this is an example of overiding and  concept of super in python

class Mailer():
    def send_mailer(self):
        print("sending email to {}...... ".format(self.name))

class Contact():
    
    all_contacts= list()

    def __init__(self,name,email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)        
class Friend(Contact):
    def __init__(self,name,email,ph):
        super().__init__(name,email)
        self.ph = ph
    def try0(self):
        super.try0()
        print("hi i m inside the class friends")
class EmailableContact(Contact,Mailer):
    pass

if __name__=="main":
    main()
