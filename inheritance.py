class Contact(object):
    all_contacts = []
    def __init__(self,name,email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self,order_details):
        self.order = order_details
        print("your order details have been saved")
if __name__=="main":
    main()
