def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logged
def add(x, y):
    print('Calculating')
    return x + y

add(3,4)


