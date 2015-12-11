# ftp 

```python
import ftplib

ftp = ftplib.FTP("ftp.kernel.org")
ftp.login("anonymous", "ftplib-example-1")

ftp.cwd("/pub/software/java/jato")
ftp.retrlines('LIST')

# to download a file named readme
ftp.retrbinary('RETR jato-0.3.tar.xz', open('jato-0.3.tar.xz', 'wb').write)

ftp.quit()

```
