class ContactList(list):
    def search(self,arg):
        "search any contact in the list"
        matching_contact= list()
        for contact in self:
            if arg in contact.name:
                matching_contact.append(contact.name)

        return matching_contact

class Contact:
    all_contacts = ContactList()

    def __init__(self,name,email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

if __name__ == "main":
    main()
