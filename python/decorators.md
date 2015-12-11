# Decorators

- Decorators can modify the functionality of a method without modifying the method
itself.

```python
# double is our decorator function which returns another function
def double(old_fn):
    def new_fn(*args, **kwds):
        old_fn(*args, **kwds)
        old_fn(*args, **kwds)
    return new_fn

def hello():
    print "Hello, How are you?"

# the decorator is interpreted as below,
# square = double(square())
@double
def square(n):
    print n*n

# the decorator is interpreted as below
# add = double(add())
@double
def add(a,b):
    print a+b

add(1,2)    # prints twice
square(34)  # prints twice
hello()     # prints once
```

Outputs,

```python
3
3
1156
1156
Hello, How are you?
```
