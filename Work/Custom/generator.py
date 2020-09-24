# x = countdown(5)
# x.__next__()

def countdown(n):
    # Added a print statement
    print('Counting down from', n)  # executed only on first c.__next__()
    while n > 0:
        print('Before yield', n)
        yield n                     # every iteration exits here, returning n
        print('After yield', n)     # new iterations start here
        n -= 1
        print('After --', n)

# for line in filematch('Data/portfolio.csv', 'IBM'):
#        print(line, end='')


def filematch(filename, substr):
    print('Start')
    with open(filename, 'r') as f:
        print('Opened files')
        for line in f:
            print('Checking substr in line')
            if substr in line:
                print('Found substr, yield is next')
                yield line
                print('After yield')
