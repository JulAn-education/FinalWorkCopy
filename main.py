from notes import Notes
from notesApp import NotesApp

if __name__ == '__main__':
    notes = Notes('notes.json')  
    app = NotesApp(notes)  
    app.run()