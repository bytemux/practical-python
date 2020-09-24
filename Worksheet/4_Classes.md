## If init is defined, you must init parent class
```python
class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # Check the call to `super` and `__init__`
        super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        return self.factor * super().cost()

    def test(self):
      raise NotImplementedError()
```


## Use interfaces to own/3rd party classes for loose coupling
As long as your application uses the programming interface of your class, you can change the internal implementation to work in any way that you want. You can write all-custom code. You can use someone’s third party package. You swap out one third-party package for a different package when you find a better one. It doesn’t matter–none of your application code will break as long as you preserve keep the interface.

## Attribute Access
```python
def print_table(objects, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [str(getattr(obj, name)) for name in columns]
        formatter.row(rowdata)
```
