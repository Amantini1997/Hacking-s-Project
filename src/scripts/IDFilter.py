import csv

ID_column = []
search_term = raw_input()
search_results = []
search_index = 0
search_indexes = []

with open('../event.csv', "rb") as e:
    r = csv.reader(e)
    for row in r:
        ID_column.append(row[0])

    for ID in ID_column:
        if ID.find(search_term) > -1:
            search_index = ID_column.index(ID)
            search_indexes.append(search_index)

with open('../event.csv', "rb") as e:
    r = csv.reader(e)
    n = 0
    for row in r:
        if n in search_indexes:
            search_results.append(row)
        n += 1
    print "We have found the following events with this ID:"
    for row in search_results:
        print row[1]
