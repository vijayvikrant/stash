# List comprehension with Filters

The following stores sqaures of odd numbers which are also multiples of 7,

```python

# list filtering
a = []
for x in range(1,100,2):
    if x*x % 7 == 0:
        a.append(x*x)

# the above is shortcut
b = [x * x for x in range(1,100,2) if x % 7 ==0]


print a
print b
```
Outputs,

```python
[49, 441, 1225, 2401, 3969, 5929, 8281]
[49, 441, 1225, 2401, 3969, 5929, 8281]
```
