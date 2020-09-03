prices = {}  # Initial empty dict

with open('Data/prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        if row == ['\n']:
            print(row)
            break

        prices[row[0]] = float(row[1])
    print(prices)
