class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacs = ContactList() # Se comparte en todas las instancias, instancio la clase contactList

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacs.append(self)

class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest


c = Contact("uss1", "asd1")
c2 = Contact("uss2", "asd2")
c3 = Contact("uss3", "asd3")
assert [] == list()
print(isinstance([], object))
[print(c.name) for c in Contact.all_contacs.search('us')]

lg = LongNameDict()
lg['hello'] = 1
lg['longest yet'] = 5
lg['hello2'] = 'world'
print(lg.get('hello'))
print(lg['hello'])
# print(lg.hello) error
print(lg.longest_key())