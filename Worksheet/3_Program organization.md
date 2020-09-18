## Key point: Functions don’t receive a copy of the input arguments.
```python
def foo(items):
    items.append(42)    # Modifies the input object

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]
```



## Right way to raise generic exception
```python
# essential part
try:
    go_do_something()
except Exception as e:
    print('Exception occured:', e)

# full notation
try:
    go_do_something()
except Exception as e:
    print('Exception occured:', e)
    raise # optional, pass error to the caller
finally:
    lock.release()  # this will ALWAYS be executed. With and without exception.

# modern notation
with open(filename) as f:
    # Use the file
    ...
# File closed
```

## Modules
```python
import sys
# get dict of all loaded modules
sys.modules.keys()
# paths
sys.path

# args list ['test.py', '1', '2', '3']
sys.argv

# export TEST="wow"
envvar = os.environ['TEST']  # 'wow'

# customize exit code
raise SystemExit
raise SystemExit(exitcode)
raise SystemExit('Informative message')
## alt
sys.exit(exitcode)

```

## Script template
```python
#!/usr/bin/env python3
# prog.py

# Import statements (libraries)
import modules

# Functions
def spam():
    ...

def blah():
    ...

# Main function
def main(argv):
    # Parse command line args, environment, etc.
    ...

if __name__ == '__main__':
    import sys
    main(sys.argv)
```

