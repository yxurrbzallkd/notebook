from datetime import date
import os
import pickle
import sys


working_directory = os.getcwd()

class Note:
    '''Represent a note in the notebook. Match against a
    string in searches and store tags for each note.'''
    def __init__(self, memo='', tags='', i_d=0):
        '''initialize a note with memo and optional space-separated tags.
         Automatically set the note's creation date and a unique id.

        >>> test_note = Note('Hello World!', tags='test hello', i_d=123)
        >>> test_note.id
        123
        >>> test_note.memo
        'Hello World!'
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = date.today()
        self.id = i_d

        self.__mold = "Note {}\n\n{}\n\n{}\n".format

    def _rewrite(self, memo: str, tags: str):
        '''Edit note (change memo and tags)
        
        >>> test_note = Note('Hello World!', tags='test hello', i_d=123)
        >>> print(test_note)
        Note 123
        <BLANKLINE>
        Hello World!
        <BLANKLINE>
        #test #hello
        <BLANKLINE>
        >>> test_note._rewrite('hello', tags='new')
        >>> print(test_note)
        Note 123
        <BLANKLINE>
        hello
        <BLANKLINE>
        #new
        <BLANKLINE>
        '''
        self.memo = memo
        self.tags = tags

    def match(self, given_filter: str):
        '''Determine if this note matches the filter text.
        Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and tags.

        >>> test_note = Note('Hello World!', tags='test hello', i_d=123)
        >>> test_note.match('hello')
        True
        >>> test_note.match('tag')
        False
        '''
        return given_filter in self.memo or given_filter in self.tags

    def __str__(self):
        '''String representation of the Note
    
        >>> test_note = Note('Hello World!', tags='test hello', i_d=123)
        >>> print(test_note)
        Note 123
        <BLANKLINE>
        Hello World!
        <BLANKLINE>
        #test #hello
        <BLANKLINE>
        '''
        return self.__mold(self.id, self.memo, ' '.join('#'+i for i in self.tags.split(' ')))


class Notebook:
    '''Represent a collection of notes that can be tagged, modified, and searched.'''
    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''Create a new note and add it to the list.

        >>> test_notebook = Notebook()
        >>> test_notebook.notes = [Note('MemoMemo', tags='tag1 tag2', i_d=12)]
        >>> print(test_notebook.notes[0])
        Note 12
        <BLANKLINE>
        MemoMemo
        <BLANKLINE>
        #tag1 #tag2
        <BLANKLINE>
        '''
        self.notes.append(Note(memo, tags, i_d=len(self.notes)))

    def _find_note(self, note_id):
        '''Locate the note with the given id.
        
        >>> test_notebook = Notebook()
        >>> note = Note(i_d=12)
        >>> test_notebook.notes.append(note)
        >>> test_notebook._find_note(12) == note
        True
        >>> test_notebook._find_note(2)

        '''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None 

    def modify_memo(self, note_id: int, memo: str):
        '''Find the note with the given id and change its
        memo to the given value.

        >>> test_notebook = Notebook()
        >>> test_notebook.notes.append(Note('MemoMemo', tags='tag1 tag2', i_d=12))
        >>> test_notebook.modify_memo(12, 'NEWTEXT')
        True
        >>> print(test_notebook._find_note(12))
        Note 12
        <BLANKLINE>
        NEWTEXT
        <BLANKLINE>
        #tag1 #tag2
        <BLANKLINE>
        '''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        print('No such note...')
        return False

    def modify_tags(self, note_id: int, tags: str):
        '''Find the note with the given id and change its
        memo to the given value.

        >>> test_notebook = Notebook()
        >>> test_notebook.notes.append(Note('MemoMemo', tags='tag1 tag2', i_d=12))
        >>> test_notebook.modify_tags(12, 'new_tag')
        True
        >>> test_notebook._find_note(12).tags
        'new_tag'
        '''
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        print('No such note...')
        return False

    def edit_note(self, note_id, memo: str, tags: str):
        '''
        >>> test_notebook = Notebook()
        >>> test_notebook.notes.append(Note('MemoMemo', tags='tag1 tag2', i_d=1))
        >>> test_notebook.edit_note(1, 'Noooo', 'tag')
        True
        >>> note = test_notebook._find_note(1)
        >>> note.memo
        'Noooo'
        >>> note.tags
        'tag'
        '''
        note = self._find_note(note_id)
        if note:
            note._rewrite(memo, tags)
            return True
        print('No such note...')
        return

    def search(self, given_filter: str) -> list:
        '''Find all notes that match the given filter
        string.'''
        return [note for note in self.notes if note.match(given_filter)]


def get_notebook():
    global working_directory
    files = os.listdir(working_directory+r'\notebooks')
    notebooks = [i for i in files if i.startswith('Notebook_object_') and i.endswith('.pickle')]

    if notebooks:
        print("Which notebook do you want to open?")
        print(f"{len(notebooks)} notebooks available:\n\n").format()
        print('\n'.join([str(i)+'. '+notebooks[i] for i in range(len(notebooks))]))
        print(str(len(notebooks))+'. New notebook!')

        notebook_n = int(input(f"\nChose notebook (options 0 through {len(notebooks)}): "))
        if notebook_n < len(notebooks):
            with open('notebooks\\'+notebooks[notebook_n], 'rb') as f:
                return pickle.load(f), notebooks[notebook_n]

    return Notebook(), 'Notebook_object_'+str(len(os.listdir(working_directory+'\\notebooks')))+'.pickle'


class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.notebook, self.savename = get_notebook()
        self.choices = {
             "1": self.show_notes,
             "2": self.search_notes,
             "3": self.add_note,
            "4": self.edit_note,
            "5": self.quit,
            "6": self.save}

    def display_menu(self):
        print("""
        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        6. Save changes""")

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                  action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(note)

    def search_notes(self):
        given_filter = input("Search for: ")
        notes = self.notebook.search(given_filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        tags = input("Enter tags (separated by spaces): ")
        self.notebook.new_note(memo, tags)
        print("Your note has been added.")

    def modify_note(self):
        i_d = input("Enter a note id: ")
        print("if you enter empty string, no changes will be saved!")
        memo = input("Enter a memo: ")
        tags = input("Enter tags (separated by spaces): ")
        if memo:
            self.notebook.modify_memo(i_d, memo)
        if tags:
            self.notebook.modify_tags(i_d, tags)

    def edit_note(self):
        i_d = input("Enter a note id: ")
        note = self.notebook._find_note(i_d)
        if note:
            print(note)
            memo = input("Enter new memo: ")
            tags = input("Enter new tags (separated by spaces): ")
            self.notebook.edit_note(memo, tags)
            return True
        print("Can't modify this note: Invalid note id {}".format(i_d))
        return

    def save(self):
        with open('notebooks/'+self.savename, 'wb') as f:
            pickle.dump(self.notebook, f)

    def quit(self):
        print("Thank you for using your notebook today.")
        self.save()
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
