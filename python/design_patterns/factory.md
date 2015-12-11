# Factory pattern

The factory pattern helps segregate all logic into one factory method.

```python
class Cup:
color = ""

    @staticmethod
    def getCup(cup_color):
        if (cup_color == "red"):
            return RedCup()
        elif (cup_color == "blue"):
            return BlueCup()
        else:
            return None

class RedCup(Cup):
    color = "red"

class BlueCup(Cup):
    color = "blue"

```
