# report.py
#
# Exercise 2.4
import csv
import sys
from fileparse import parse_csv 

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''    
    portfolio = parse_csv(filename)
    
    return portfolio

def read_prices(file):
    'Reads the prices of a file'
    prices = dict(parse_csv(file, types=[str, float], has_headers=False))
    print(prices)
    
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

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('_' * 10 + ' ')*len(headers) )
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {'$'+str(price):>10s} {change:>10.2f}')

def portfolio_report(portfolio_filename, prices_filename):

    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    print(f'Current value of the portfolio is: {calculate_portfolio(portfolio, prices)}' )
    report = make_report(portfolio,prices)
    print_report(report)


if len(sys.argv) == 3:
    
    portfile = sys.argv[1]
    pricesfile = sys.argv[2]
else:
    portfile = 'Data/portfolio.csv'
    pricesfile = 'Data/prices.csv'

portfolio_report(portfile, pricesfile)


