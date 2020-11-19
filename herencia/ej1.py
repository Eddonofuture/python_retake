class Contact:
    all_contacs = [] # Se comparte en todas las instancias

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacs.append(self)

class Supplier(Contact):
    def order(self, order):
        print("Si fuera un sistema real "f"'{order}' order to '{self.name}'")

c = Contact("Some body", "asd")
s = Supplier("Sup", "email")

print(c.name, c.email, s.name, s.email)
print(c.all_contacs)

# c.order("i need some") error!
s.order('give me something')
#for n in range(0, len(Contact.all_contacs)):
    #print(Contact.all_contacs[n].name)