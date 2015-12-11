# Functions - first class citizens

In python functions also have the same capabilities that every other data type has

```python

def converter(unit):
    def convert(x):
        return unit * x
    return convert

cm = converter(100)
mm = converter(1000)

print cm(2)
print mm(1.5)
```
outputs,
```python

200
1500.0
```
