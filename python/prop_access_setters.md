# Property setter and getter

```python
class Celsius(object):
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print "Getting Value"
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print "Setting Value"
        self._temperature = value

c = Celsius(40)
print c.temperature
print c.to_fahrenheit()
c.temperature = 37
print c.to_fahrenheit()
```
Outputs
```python

Getting Value
40
Getting Value
104.0
Setting Value
Getting Value
98.6
```
