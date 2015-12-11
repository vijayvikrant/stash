# Python Database API

- python uses DBAPI 2.0 to abstract database APIs
- sqlite is a file based database driver
```python
import sqlite3

# connects to a database mydatabase.db if it exists
# if it does not exist that it creates it
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# create a table books with three columns
cursor.execute("""CREATE TABLE books
                    (id int, title text, author text)
                """)

# add a record to the table books
cursor.execute("INSERT INTO books VALUES (1, 'Wings of Fire', 'Abdul Kalam')")

#save data to db
conn.commit()

mybooks = [(2, 'My Experiments with Truth', 'M K Gandhi'),
           (3, 'Discovery of India', 'J Nehru')]


# insert multiple records
cursor.executemany("INSERT INTO books VALUES (?,?,?)", mybooks)

# save data to db
conn.commit()

# using multiline strings are good for readability
sql = """
UPDATE books
SET author = "Jawaharlal Nehru"
WHERE id = 3
"""

cursor.execute(sql)
conn.commit()

# delete a record
sql = """
DELETE FROM books
WHERE id = 3
"""

cursor.execute(sql)
conn.commit()

# query all records from table books
# this is a bad way of doing it
for row in cursor.execute("SELECT * FROM books"):
    print row[0], row[1], row[2]

# this is a better way of doing the above 
sql = "SELECT * FROM books"
cursor.execute(sql)
for id, bookname, author in cursor.fetchall():
    print "The book {} was written by {}".format(bookname, author)

conn.close()

```

Outputs,
```
(1, u'Wings of Fire', u'Abdul Kalam')
(2, u'My Experiments with Truth', u'M K Gandhi')
Results
The book Wings of Fire was written by Abdul Kalam
The book My Experiments with Truth was written by M K Gandhi
```

