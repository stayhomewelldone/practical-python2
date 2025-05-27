# pcost.py
#
# Exercise 1.27
import csv
import sys
import report
def portfolio_cost(filename):
    'Calculates the whole value of the portfolio'
    total_cost = 0
    rows = report.read_portfolio(filename)
    for rowno, row in enumerate(rows):
        try:
            total_cost += int(row['shares']) * float(row['price'])
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')
    return float(total_cost)
def main(args):
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    cost = portfolio_cost(filename)
    print(f'Total cost {cost}')
    
if __name__ == '__main__':
    main(sys.argv)



