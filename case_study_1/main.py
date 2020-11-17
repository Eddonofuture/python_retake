from notebook import Note

n1 = Note("hello world")

n2 = Note('Again')

print(n1.id)
print(n2.id)

print(n1.match('hello'))
print(n2.match('a'))