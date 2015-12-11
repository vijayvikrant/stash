# pexpect 

The following automates getting a file via ftp,
```python
import pexpect

child = pexpect.spawn('ftp ftp.openbsd.org')
child.expect('Name .*: ')
child.sendline('anonymous')
child.expect('Password:')
child.sendline('noah@example.com')
child.expect('ftp> ')
child.sendline('get robots.txt')
child.expect('ftp> ')
child.sendline('bye')
child.close()
```
