# Tuples. read-only, rows/vectors
```python
# prints as ( 1, 2, '3' )

# pack tuple
s = ('GOOG', 100, 490.1)
# unpack tuple
name, shares, price = s
```

# Dictionaries / hash table / associative array. Unordered data.
```python
# prints as {'key': 'value'}

s = {
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1
}
del s['date']
s['shares'] = 75
s['shares']

keys = s.keys()
items = d.items()  # dict to tuple
t = dict(items) # tuple to dict

# search key
if key in d:
    # YES
else:
    # NO

# get value, providing default if key not found
name = d.get(key, default)

```

# Lists. Ordered data.
```python
# prints as ['','']
records = [] # empty list
records.append(('GOOG', 100, 490.10)) # add element

```

# Sets. Unordered collection of unique items.
```python
# prints as { 'IBM','AAPL','MSFT' }
names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']
unique = set(names)
'IBM' in names

names.add('CAT')        # Add an item
names.remove('YHOO')    # Remove an item

s1 | s2                 # Set union
s1 & s2                 # Set intersection
s1 - s2                 # Set difference
```

#
```python


```
