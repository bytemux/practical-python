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
