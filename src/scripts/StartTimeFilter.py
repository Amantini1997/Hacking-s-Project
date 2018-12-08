import csv

start_time_column = []
search_results = []
search_index = 0
search_indexes = []

print "Please enter a start time in the format DD/MM/YYYY HH:MM"
search_term = raw_input()

with open('../event.csv', "rb") as e:
    r = csv.reader(e)
    for row in r:
        start_time_column.append(row[3])
    print start_time_column

    for start_time in start_time_column:
        if start_time.find(search_term) > -1:
            search_index = start_time_column.index(start_time)
            search_indexes.append(search_index)

        else:
            print "Nothing was found!"

print "Search indexes are: ", search_indexes
with open('../event.csv', "rb") as e:
    r = csv.reader(e)
    n = 0
    for row in r:
        if n in search_indexes:
            search_results.append(row)
        n += 1
    print "The event(s) starting at this time are:"
    for row in search_results:
        print row[1]
