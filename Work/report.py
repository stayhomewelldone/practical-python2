# report.py
#
# Exercise 2.4
import csv
import sys
portfolio = []
def read_portfolio(filename):
    'Reads the content of a file'
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            print(row)
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = read_portfolio('Data/portfolio.csv')
