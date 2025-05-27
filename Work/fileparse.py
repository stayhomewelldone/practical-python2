# fileparse.py
#
# Exercise 3.3
import csv
def parse_csv(filename, select =None, types=[str, int, float], has_headers=True, delimiter=',',silence_errors=False ):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
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
        for rowno,row in enumerate(rows, start=1):
            try:
                if not row:
                    continue  # Skip rows with no data
                # Filter the row if specifc columns were selected
                if indices: 
                    row = [ row[index] for index in indices]
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                if headers:    
                    record = dict(zip(headers,row))
                else:
                    record = tuple(row)

                records.append(record)
            except ValueError as e:
                if silence_errors:
                    print(f'Row {rowno}: Couldn\'t convert {row}')
                    print(f'Row {rowno}: {e} ')
                continue
    return records