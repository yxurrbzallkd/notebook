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
<pre>                            +------------------------------------------+
                            | list all files from notebooks\           |
                            | folder that start with &quot;Notebook_object_&quot;|
                            | and end with &quot;.pickle&quot;                   |
                         +------------------------------------------------------+
                 +-------+Are there any files that match the requirements above?|-----+
                 | YES   |                                                      | NO  |
                 |       +------------------------------------------------------+     |
                 v                                                                    v
      +----------------------------------------+                   +------------------------------+
      |Let the user choose any of the available|                   | create a new notebook object |
      |notebooks or create a new one           |                   |                              |
      +----------------------------------------+                   +------------------------------+</pre>

# OOP in action
