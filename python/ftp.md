# ftp 

```python
import ftplib

ftp = ftplib.FTP("ftp.kernel.org")
ftp.login("anonymous", "ftplib-example-1")

ftp.cwd("/pub/software/java/jato")
ftp.retrlines('LIST')

# to download a file named readme
# takes remote filename string as argument 1
# takes a function as argument 2
# the second argument is executed when arg1 is downloaded
ftp.retrbinary('RETR jato-0.3.tar.xz', open('jato-0.3.tar.xz', 'wb').write)

ftp.quit()

```
Outputs,
```
-rw-rw-r--    1 ftp      ftp        374958 Dec 08  2011 jato-0.0.1.tar.bz2
-rw-rw-r--    1 ftp      ftp        435706 Dec 08  2011 jato-0.0.1.tar.gz
-rw-rw-r--    1 ftp      ftp           543 Dec 08  2011 jato-0.0.1.tar.sign
-rw-rw-r--    1 ftp      ftp        355020 Dec 08  2011 jato-0.0.1.tar.xz
-rw-rw-r--    1 ftp      ftp        350765 Dec 08  2011 jato-0.0.2.tar.bz2
-rw-rw-r--    1 ftp      ftp        414013 Dec 08  2011 jato-0.0.2.tar.gz
-rw-rw-r--    1 ftp      ftp           543 Dec 08  2011 jato-0.0.2.tar.sign
-rw-rw-r--    1 ftp      ftp        336984 Dec 08  2011 jato-0.0.2.tar.xz
-rw-rw-r--    1 ftp      ftp        962613 Dec 08  2011 jato-0.1.0.tar.bz2
-rw-rw-r--    1 ftp      ftp       1140318 Dec 08  2011 jato-0.1.0.tar.gz
-rw-rw-r--    1 ftp      ftp           543 Dec 08  2011 jato-0.1.0.tar.sign
-rw-rw-r--    1 ftp      ftp        859628 Dec 08  2011 jato-0.1.0.tar.xz
-rw-rw-r--    1 ftp      ftp       1010479 Dec 08  2011 jato-0.1.1.tar.bz2
-rw-rw-r--    1 ftp      ftp       1190938 Dec 08  2011 jato-0.1.1.tar.gz
-rw-rw-r--    1 ftp      ftp           543 Dec 08  2011 jato-0.1.1.tar.sign
-rw-rw-r--    1 ftp      ftp        895396 Dec 08  2011 jato-0.1.1.tar.xz
-rw-rw-r--    1 ftp      ftp       1045100 Dec 08  2011 jato-0.2.tar.bz2
-rw-rw-r--    1 ftp      ftp       1241600 Dec 08  2011 jato-0.2.tar.gz
-rw-rw-r--    1 ftp      ftp           543 Dec 08  2011 jato-0.2.tar.sign
-rw-rw-r--    1 ftp      ftp        925456 Dec 08  2011 jato-0.2.tar.xz
-rw-rw-r--    1 ftp      ftp       1088531 Jan 04  2012 jato-0.3.tar.bz2
-rw-rw-r--    1 ftp      ftp       1303623 Jan 04  2012 jato-0.3.tar.gz
-rw-rw-r--    1 ftp      ftp           836 Jan 04  2012 jato-0.3.tar.sign
-rw-rw-r--    1 ftp      ftp        966428 Jan 04  2012 jato-0.3.tar.xz
-rw-r--r--    1 ftp      ftp          2391 Apr 02  2014 sha256sums.asc
'221 Goodbye.'
```
