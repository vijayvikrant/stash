# pexpect with output

```python
# when we don't know what to expect, we can ask pexpect to get everything.
# timeout = None will wait for ever
child.expect(pexpect.EOF, timeout=None)

# child.before has the previous output
cmd_show_data = child.before
cmd_output = cmd_show_data.split('\r\n')
for data in cmd_output:
    print data
```
