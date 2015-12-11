# enumerating lists

```python

a = [1,2,3,4]
for x in a:
    print x

# if we wanted a index of every entry,
for x in enumerate(a):
    print x
```

Outputs,
```python
1
2
3
4
(0, 1)
(1, 2)
(2, 3)
(3, 4)
```
