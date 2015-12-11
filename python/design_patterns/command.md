# Command wrapping

Here we wrap the command in a class to provide various methods that can be
executed easily,

```python
import os

class MoveFileName(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        os.rename(self.src, self.dest)

    def undo(self):
        os.rename(self.dest, self.src)

# the above is the code to rename a file
# only os.rename(src, dest) could have done it
# but to add more functionality we wrap it in a class 
# this gets us more methods - like undo
# below is a usage example

stack = []
stack.append(MoveFileName("foo", "bar"))
stack.append(MoveFileName("foo1", "bar1"))

# to undo the last operation
# we can just call undo now, without providing any args.
# the arguments are saved in the class context
stack.pop().undo()

```
