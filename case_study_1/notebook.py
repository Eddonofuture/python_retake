import datetime
from datetime import date
# Store the next available id for all new notes

last_id = 0


class Note:
    """
    Represent a note in the nobook. Match against a string in searches and store tags for each note.
    """

    def __init__(self, memo, tags=""):
        """
        initialize a note with memo and optional space-separated tags. Automatically set the note's creation date and unique id.
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        return filter in self.memo or filter in self.tags


class Notebook:

    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=""):
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modidy_tags(self, note_id, tags):
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter):
        return [note for note in self.notes if note.math(filter)]
