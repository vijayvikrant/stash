# paramiko - inbuilt ssh client

Python has an inbuilt ssh client

```python
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1', username='username', password='password')
stdin, stdout, stderr = ssh.exec_command('ls')

for line in stdout.readlines():
    print line

ssh.close()
```
