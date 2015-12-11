# Decorators

```python
def double(old_fn):
    def new_fn(*args, **kwds):
        return 2 * old_fn(*args, **kwds)
    return new_fn

def square1(old_fn):
    def new_fn(arg):
        return arg*arg
    return new_fn


@double
@square1
def square(n):
    return n*n

print square(2)

@square1
@double
def square(n):
    return n*n

print square(2)
```
Outputs,
```python
8
4
```
