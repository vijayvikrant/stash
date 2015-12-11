# List comprehension

```python
# the below stores squares of all odd numbers in a list a
a = []
for x in range(1,10,2):
    a.append(x*x)
        
# a shorter way to write this is,
b = [x*x for x in range(1,10,2)]

print a
print b
```

outputs,
```python
[1, 9, 25, 49, 81]
[1, 9, 25, 49, 81]
```
