# Variadic function argument
```python
# args is tuple
def f(x, *args)

# kwargs is dictionary
def f(x, y, **kwargs):

# tuple expansion
def avg(x,*more):
        return float(x+sum(more))/(1+len(more))

# dict expansion
f(data, **options)

```

# Inline sort
```python
# callback function
def stock_name(s):
    return s.name
portfolio.sort(key=stock_name)

# lambda way
portfolio.sort(key=lambda s: s.shares)

```

# Returning Functions
```python
def after(seconds, func):
    time.sleep(seconds)
    func()

def greeting():
    print('Hello Guido')

after(30, greeting)
```

# Properties type checking code generator
typedproperty.py + stock.py

# Decorators (and wrapper functions)
timethis.py

## decorator syntax
```python
def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logged
def add(x, y):
    return x + y

add(3,4)
```

## wrapping explanation
```python
# Wrapping function
def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

def add(x, y):
    return x + y

logged_add = logged(add)
logged_add(3, 4)      # You see the logging message appear

```

# Built-in decorators
```python
# function that is part of the class, but which does not operate on instances
@staticmethod

# method that receives the class object as the first parameter instead of the instance.
@classmethod



```
