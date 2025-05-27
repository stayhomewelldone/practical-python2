# fileparse.py
#
# Exercise 3.3
import csv
def parse_csv(filename, select =None, types=[str, int, float], has_headers=True):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        # Read the file headers (if any)
        headers = next(rows) if has_headers else []

        # If a column selector was given, find indices of the specified columns.
        #  Also narrow the set of headers used fot the resulting dictionaries. 
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
                    
        records =[]
        for row in rows:
            if not row:
                continue  # Skip rows with no data
            # Filter the row if specifc columns were selected
            if indices: 
                row = [ row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]
                record = tuple(row)
            if not types:    
                record = dict(zip(headers,row))
            records.append(record)

    return records