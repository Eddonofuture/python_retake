class Document:
    def __init__(self):
        self.characters = []
        self.cursor = 0
        self.filename = ''

    def insert(self, character):
        self.characters.insert(self.cursor, character)
        self.cursor += 1
    
    def delete(self):
        del self.characters[self.cursor]

    def save(self):
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

doc = Document()
doc.filename = 'some'
doc.insert('a')
doc.insert('b')
doc.insert('c')
doc.insert('d')
doc.insert('e')
print("".join(doc.characters))
doc.back()
doc.delete()
doc.insert('p')
print("".join(doc.characters))
