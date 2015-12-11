# bottle web framework

```python
# wget https://github.com/bottlepy/bottle/raw/master/bottle.py
from bottle import route, run, request, template


@route('/')
def hello():
    return "routes available - (1) /env (2) /hello/name"


@route('/wish/<name>')
def wish(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/books')
def books_get():
    import sqlite3
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM books"
    cursor.execute(sql)
    output = '<table border=1>'
    for id, bookname, author in cursor.fetchall():
        output += '<tr><td>' + str(id) + '</td><td> '+ bookname + '</td><td>' + author + '</td></tr>'
    conn.close()
    output += '</table>'
    return output


def books_put(index, name, author):
    import sqlite3
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "INSERT INTO books VALUES (" + index + ',"' + name + '","' + author + '")'
    cursor.execute(sql)
    conn.commit()
    conn.close()


@route('/book/<bookid>')
def book_get(bookid):
    import sqlite3
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "SELECT * from books WHERE id == " + bookid
    cursor.execute(sql)
    id, bookname, author = cursor.fetchone()
    conn.commit()
    conn.close()
    return "Name:" + bookname + " Author:" + author


@route('/add')
def showform():
    return """
    <html>
        <form method=post action="http://localhost:8080/addbook">
            <table>
            <tr>
            <td>Id </td><td><input type=text name=id></td>
            </tr>
            <tr>
            <td>Bookname </td><td><input type=text name=bookname></td>
            </tr>
            <tr>
            <td>Author </td><td><input type=text name=author></td>
            </tr>
            </table>
            <input type=submit>
        </form>
    </html>
    """


@route('/addbook', method='POST')
def bookadd():
    index = request.forms.get('id')
    bookname = request.forms.get('bookname')
    author = request.forms.get('author')
    books_put(index, bookname, author)
    return "Added"


@route('/env')
def get_env():
    import os
    output = '<table border=1>'
    for x, y in os.environ.items():
        output += '<tr><td>' + x + '</td><td>' + y + '</td></tr>'
    output += '</table>'
    return output

run(host='localhost', port=8080, debug=True)
```
