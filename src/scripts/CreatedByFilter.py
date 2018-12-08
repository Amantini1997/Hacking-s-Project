import csv

created_by_column = []
search_term = raw_input()
search_results = []
search_index = 0
search_indexes = []

with open('../event.csv', "rb") as e:
    r = csv.reader(e)
    for row in r:
        created_by_column.append(row[6])

    for created_by in created_by_column:
        if created_by.find(search_term) > -1:
            search_index = created_by_column.index(created_by)
            search_indexes.append(search_index)

with open('../event.csv', "rb") as e:
    r = csv.reader(e)
    n = 0
    for row in r:
        if n in search_indexes:
            search_results.append(row)
        n += 1
    print "The event(s) created by this user are: "
    for row in search_results:
        print row[1]
