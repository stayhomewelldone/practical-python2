# report.py
#
# Exercise 2.4
import csv
import sys
prices = {}

def read_portfolio(filename):
    'Reads the content of a file'
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            portfolio.append(record)
    print(portfolio)
    return portfolio

def read_prices(file):
    'Reads the prices of a file'
    with open(file, 'r') as f:
        rows = csv.reader(f)
        try:
            for number, row in enumerate(rows):
                prices[row[0]] = row[1]
        except IndexError:
            print('Indexerror on line',number)
    return prices

def calculate_portfolio(port, prices):
    'Calculate the current value of the portfolio'
    portvalue = 0.0
    pricevalue = 0.0
    for stocks in port:
        portvalue += int(stocks['shares']) * float(stocks['price'])
        pricevalue += float(prices[stocks['name']]) * int(stocks['shares'])
    return (pricevalue - portvalue)

def make_report(portfile,pricefile):
    report = []
    'Make a report containing tuples'
    for stocks in portfile:
        report.append((stocks['name'], int(stocks['shares']), float(pricefile[stocks['name']]), float(stocks['price']) - float(pricefile[stocks['name']])))

    return report

if len(sys.argv) == 3:
    
    portfile = sys.argv[1]
    pricesfile = sys.argv[2]
else:
    portfile = 'Data/portfolio.csv'
    pricesfile = 'Data/prices.csv'
portfolio = read_portfolio(portfile)
prices = read_prices(pricesfile)
print(calculate_portfolio(portfolio, prices))
report = make_report(portfolio,prices)
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('_' * 10 + ' ')*len(headers) )
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {'$'+str(price):>10s} {change:>10.2f}')
headers = ('Name', 'Shares', 'Price', 'Change')
