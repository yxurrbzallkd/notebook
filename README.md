# notebook
Notebook with textual user interface

# About Project
Notebook with textual user interface for making quick notes through command line
# Project
<pre>
  +--------------------------------+
  |      Note                      |
  |--------------------------------|
  |  + id                          |
  |  + memo                        |
  |  + tags                        |
  |  + __mold                      |
  +--------------------------------+
  | + __str__() -&gt; str             |
  |  (return readable string       |
  |   representation of the note)  |
  +--------------------------------+
  | + match(filter: str) -&gt; bool   |
  |   (look for filter in contents |
  |    of the note (memo and tags))|
  +--------------------------------+
  | + _rewrite(new_memo, new_tags) |
  |   (store new memo and tags)    |
  +--------------------------------+</pre>

<pre>
  +---------------------------------------------+
  |            Notebook                         |
  |---------------------------------------------|
  |  + notes (list of Note objects              |
  |---------------------------------------------|
  |  + new_note(memo, tags)                     |
  |    (add new note to notebook)               |
  |---------------------------------------------|
  |  + _find_note(note_id)                      |
  |   (find note with give id in stored notes)  |
  |---------------------------------------------|
  |  + modify_memo(node_id, new_memo: str)      |
  |   (change memo of a note with given id,     |
  |    if there isn&#39;t such a note, do nothing)  |
  |---------------------------------------------|
  |  + modify_tags(node_id, new_tags: str)      |
  |   (change tags of a note with given id,     |
  |    if there isn&#39;t such a note, do nothing)  |
  |---------------------------------------------|
  |  + edit_note(node_id, new_memo, new_tags)   |
  |   (rewrite a note (note&#39;s _rewrite method)  |
  |    with given id)                           |
  +---------------------------------------------+
  |  + search(filter: str) -&gt; list              |
  |   (find all notes that contain given filter)|
  +---------------------------------------------+</pre>

<pre>
  +---------------------------------------------------------+
  |            Menu                                         |
  |---------------------------------------------------------|
  | + notebook: Notebook                                    |
  | + savename: str (name to store notebook under)          |
  | + choices: dict (commands available to user)            |
  |---------------------------------------------------------|
  | + run()                                                 |
  |  (main cycle: ask and execute commands                  |
  |   until interrupted)                                    |
  |---------------------------------------------------------|
  | + display_menu()                                        |
  |   (prints available commands)                           |
  +---------------------------------------------------------+
  | + show_notes()                                          |
  |  (prints all notes)                                     |
  +---------------------------------------------------------+
  | + search_notes()                                        |
  |  (ask user for a filter and find and display            |
  |   all notes that contain that filter)                   |
  +---------------------------------------------------------+
  | + add_note()                                            |
  +---------------------------------------------------------+
  | + modify_note()                                         |
  |  (change memo and/or tags)                              |
  +---------------------------------------------------------+
  | + edit_note()                                           |
  |  (display old note and store changed one)               |
  +---------------------------------------------------------+
  | + save()                                                |
  |  (save self.notebook with pickle under self.savename)   |
  +---------------------------------------------------------+
  | + quit() - save and exit                                |
  +---------------------------------------------------------+</pre>

## Storing notebooks
- Save notebook
```python
import pickle
notebook = Notebook()
with open('notebooks\Notebook_1.pickle', 'wb') as f:
	pickle.dump(notebook, f)
```
- Loading notebooks
<pre>                           +------------------------------------------+
                            | list all files from notebooks           |
                            | folder that start with &quot;Notebook_object_&quot;|
                            | and end with &quot;.pickle&quot;                   |
                         +------------------------------------------------------+
                 +-------+Are there any files that match the requirements above?|-----+
                 | YES   +------------------------------------------------------+ NO  |
                 v                                                                    v
      +----------------------------------------+                   +------------------------------+
      |Let the user choose any of the available|                   | create a new notebook object |
      |notebooks or create a new one           |                   |                              |
      +----------------------------------------+                   +------------------------------+</pre>

# OOP in action
## Objects
classes and objects of those classes son't really exist. OOP is an approach to programming built around creating objects with certain properties (objects can "store" information (as its *attributes*) and manipulate it, as well as any other given information, with a set of functions (*methods*)) to solve problems.
## self and methods
a conventional parameter. It is highlighted just to increase readability.

Let's take a look at Note class:
```python
class Note:
    '''Represent a note in the notebook. Match against a
    string in searches and store tags for each note.'''
    def __init__(self, memo='', tags='', i_d=0):
        '''initialize a note with memo and optional
         space-separated tags. Automatically set the note's creation date and a unique id.'''
        self.memo = memo
        self.tags = tags
        self.creation_date = date.today()
        self.id = i_d

        self.__mold = "Note {}\n\n{}\n\n{}\n".format

    def _rewrite(self, memo: str, tags: str):
        self.memo = memo
        self.tags = tags

    def match(self, given_filter: str):
        '''Determine if this note matches the filter text.
        Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and tags.'''
        return given_filter in self.memo or given_filter in self.tags

    def __str__(self):
        return self.__mold(self.id, self.memo, ' '.join('#'+i for i in self.tags.split(' ')))
```
```shell
>>> note = Note('Hello World', tags='hello test some_tag', i_d=0)
>>> print(note)
Note 0

Hello World

#hello #test #some_tag

>>> node._rewrite('Hi World!', tags='hi test')
>>> print(note)
Note 0

Hi World!

#hi #test

>>> note.match('test')
True
>>> node.math('World')
True
```
We can change self for anything else.
```python
class Note:
    def __init__(self, tags, memo, i_d):
    	self.memo = memo
	self.tags = tags
	self.id = i_d
    ...
    def _rewrite(NOT_SELF, memo: str, tags: str):
        NOT_SELF.memo = memo
        NOT_SELF.tags = tags
    ...
```
Everything works as before, because for the function our method is it will still be just a parameter of type Note
```python
>>> type(Note._rewrite)
<class 'function'>
>>> a = lambda x: x**2
>>> type(a)
<class 'function'>
```
## __init__ and attributes
before __init__ function (method) is called, objects of Note class don't have any attributes
```shell
>>> type(Note.memo)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Note' has no attribute 'memo'
>>>
```

if we modify first lines of our code like this:
```python
class Note:
    i = 'wow'
    def __init__(self, memo, tags, i_d):
    	self.id = i_d
    ...
```
We won't get error, because i had been initialised right away
```shell
>>> type(Note.i)
<class 'str'>
>>> Note.i
'wow'
```
To understand better what is goig on here, let's use dir() function
After class declaration ("class Note:") dir() results in
```python
['__module__', '__qualname__']
```
After initialising variable i:
```python
['__module__', '__qualname__', 'i']
```
After after all methods had been initialized:
```python
['__init__', '__module__', '__qualname__', '__str__', '_rewrite', 'i', 'match']
```
For a note object that had been initialized:
```shell
>>> note = Note()
>>> dir(note)  # some information is hidden for readability purposes
['_Note__mold', ..., '__init__', '__init_subclass__', ..., '__str__', ..., '_rewrite', 'creation_date', 'i', 'id', 'match', 'memo', 'tags']
```
## __str__
When print is called on any object, it is its .__str__ attribute (a string) that gets printed
