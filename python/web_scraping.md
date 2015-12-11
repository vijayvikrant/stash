# web scraping

```python
import urllib2
words = [x for x in urllib2.urlopen("http://www.cisco.com").read().split() if x.isalpha()]
print words
```
