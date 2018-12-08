import csv

size_limit_column = []
search_term = raw_input()
search_results = []
columns = []
search_index = 0
search_indexes = []

with open('../event.csv', "rb") as e:
    r = csv.reader(e)
    for row in r:
        size_limit_column.append(row[9])

    for size_limit in size_limit_column:
        if size_limit.find(search_term) > -1:
            search_index = size_limit_column.index(size_limit)
            search_indexes.append(search_index)


with open('../event.csv', "rb") as e:
    r = csv.reader(e)
    n = 0
    for row in r:
        if n in search_indexes:
            search_results.append(row)
        n += 1
    print "The event(s) with this size are:"
    for row in search_results:
        print row[1]
