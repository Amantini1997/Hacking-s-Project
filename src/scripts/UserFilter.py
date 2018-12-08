import csv

name_column = []
search_term = raw_input()
search_results = []
search_index = 0
search_indexes = []

with open('../user_profile_id.csv', "rb") as e:
    r = csv.reader(e)
    for row in r:
        name_column.append(row[1])

    for name in name_column:
        if name.find(search_term) > -1:
            search_index = name_column.index(name)
            search_indexes.append(search_index)

with open('../user_profile_id.csv', "rb") as e:
    r = csv.reader(e)
    n = 0
    for row in r:
        if n in search_indexes:
            search_results.append(row)
        n += 1
    print "We have found the following users:"
    for row in search_results:
        print row[1]
