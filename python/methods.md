# class methods

- defined with decorator @classmethod
- always takes cls as argument
```python
class MyClass(object):
    country = "India"

    @classmethod
    def mymethod(cls):
        print "hi {} is my country".format(cls.country)

MyClass.mymethod()
```
Outputs,
```python
hi India is my country
```

# static methods

- defined with decorator @staticmethod
- does not take cls or self as argument
- it is not dependent on the class itself
- these don't require the class at all, but packaged in a class for better
    structure
```python
class MyClass(object):

    @staticmethod
    def mymethod(country):
        print "hi {} is my country".format(cls.country)

# does not need an instance of the class
MyClass.mymethod("India")

# but can also work on an instance of the class
a = MyClass()
a.mymethod("India")
```
Outputs,
```python
hi India is my country
hi India is my country
```



