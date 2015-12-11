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

Other uses of a list comprehension with filters,
```python
def get_all_positions_of_char_in_word(word, c):
    return [x for x in range(len(word)) if word[x] == c]

print get_all_positions_of_char_in_word('cisco', 'c')
print get_all_positions_of_char_in_word('vijay vikrant balyan', 'v')
```
Outputs,
```python
[0, 3]
[0, 6]
```
