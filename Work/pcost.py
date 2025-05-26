# pcost.py
#
# Exercise 1.27
import csv
import sys
def portfolio_cost(filename):
    'Calculates the whole value of the portfolio'
    total_cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for line in rows:
            try:
                total_cost += int(line[1]) * float(line[2])
            except ValueError:
                print("Couldn't parse", line)
        return float(total_cost)


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost {cost}')

