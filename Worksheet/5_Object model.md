## Internals
```python
# get FULL global variables dict
# You populate this dict (and instance) when assigning to self.
## Instance vars
foo.__dict__
globals()
## Class vars & Methods
Stock.__dict__

# get important variables dict (can be overriden by class)
foo.__dir__
dir()

# only vars
foo.__vars__
vars()

# class
foo.__class__
foo.__bases__ # tuple of parent classes links
foo.__mro__ # inheritance chain (Method Resolution Order
)

# lookup method in class hierarchy (5.5)
for cls in n.__class__.__mro__:
        if 'cost' in cls.__dict__:
            break

```

## Private VS Public convention. Property, setter, getter
```python
# _           used for private vars & methods
# @           decorator, modifies folloving function
# __slots__   restricts attributes names, used on data structure classes

# override setters and getters
# notice private var '_shares' and public property 'shares'
class Stock:
    __slots__ = ('name','_shares','price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value

>>> s = Stock('IBM', 50, 91.1)
>>> s.shares         # Triggers @property
50
>>> s.shares = 75    # Triggers @shares.setter
```
