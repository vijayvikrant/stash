# Decorators

```python
def double_in(old_fn):
    def new_fn(arg):
        return old_fn(2*arg)
    return new_fn

def double_out(old_fn):
    def new_fn(*args, **kwds):
        return 2*old_fn(*args, **kwds)
    return new_fn

def sqaure(n):
    return n*n

print sqaure(2)

@double_in
def sqaure(n):
    return n*n

print sqaure(2)

@double_out
@double_in
def sqaure(n):
    return n*n

print sqaure(2)
```
Outputs,
```python
4
16
32
```
