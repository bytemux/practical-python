# general help
```python
re.<tab_key>
string_var.<tab_key>
dir(string_var)
help(string_var.replace)

# run interactive
python3 -i pcost.py
```

# strings
```python
# append work to start of thing
symbols[:0] + 'HPQ,' + symbols[0:]

```
# regex
```python
re.findall(r'\d+/\d+/\d+', text)
# Replace all occurrences of a date with replacement text
text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

```

# lists
```python
# list search
names.index('Curtis')

# remove element
names.remove('Curtis')
del names[1]

```

# files
```python
# with/as imply that file will be closed even if exception
# READ from file & close
with open('filename', 'rt') as file:
    data = file.read()

# READ from csv by line, skip header, split rows.
# NOTE: use Pandas library in prod
with open('Data/portfolio.csv', 'rt') as f:
        headers = next(f).split(',')
        headers
        for line in f:
            row = line.split(',')
            print(row)


# WRITE to file
with open('filename', 'wt') as out:
    out.write('Hello World\n')

with open('filename', 'wt') as out:
    print('Hello World', file=out)

```

# os
```python
import os
os.getcwd()
os.chdir('Work')

```

# functions
```python
# pcost.py

import csv
def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print('Bad row:', row)

    return total_cost

import sys
if len(sys.argv) == 2:   # python3.8 pcost.py Work/portfolio.csv
    print(sys.argv)
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)

```
