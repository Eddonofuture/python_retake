from notebook import Note, Notebook

n = Notebook()
n.new_note("hello words")
n.new_note("hello again")
print(n.notes)
print(n.notes[0].id)
print(n.notes[1].id)
n.modify_memo(1,'some algo')
print(n.notes[1].id)
print(n.notes[0].memo)
print(n.search('hello'))