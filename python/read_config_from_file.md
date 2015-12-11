# Reading config from file
The following will read key=value pairs from a config file and create a
dictionary
```python
# -- config.ini contents --
# cfg1=value1
# cfg2=value2
# cfg3=value3
# cfg4=value4

words = dict(line.strip().split('=') for line in open('config.ini'))
print words
```
Outputs,
```python
{'cfg1': 'value1', 'cfg2': 'value2', 'cfg3': 'value3', 'cfg4': 'value4'}
```
