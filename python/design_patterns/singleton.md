
# Singleton Design Pattern

The following code implements a Singleton design pattern in python,
```python
class Singleton(object):
    _cache = {}
    def __new__(cls):
        if cls not in cls._cache:
            cls._cache[cls] = super(Singleton, cls).__new__(cls)
        return cls._cache[cls]

class MyClass(Singleton):
    pass

obj1 = MyClass()
obj2 = MyClass()

class YourClass(Singleton):
    pass

obj3 = YourClass()
obj4 = YourClass()

print obj1 is obj2
print obj3 is obj4
```

outputs

```python
True
True
```
