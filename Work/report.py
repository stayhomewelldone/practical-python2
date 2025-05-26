# report.py
#
# Exercise 2.4
import csv
import sys
portfolio = []
prices = {}

def read_portfolio(filename):
    'Reads the content of a file'
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {headers[0]: row[0], headers[1]:int(row[1]), headers[2]:float(row[2])}
            portfolio.append(holding)
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
        portvalue += stocks['shares'] * stocks['price']
        pricevalue += float(prices[stocks['name']]) * stocks['shares']
    return (pricevalue - portvalue)

def make_report(portfile,pricefile):
    report = []
    'Make a report containing tuples'
    for stocks in portfile:
        report.append((stocks['name'], stocks['shares'], float(pricefile[stocks['name']]), float(stocks['price']) - float(pricefile[stocks['name']])))

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
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')