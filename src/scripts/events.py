import csv

location_column = []
search_term = raw_input()
search_results = []
columns = []
search_index = 0
search_indexes = []

with open('../event.csv', "rb") as e:
    r = csv.reader(e)
    for row in r:
        location_column.append(row[8])
    print location_column

    for location in location_column:
        print "Current location: ", location
        if location.find(search_term) > -1:
            print "An event has been found in ", location, "!"
            search_index = location_column.index(location)
            search_indexes.append(search_index)

        else:
            print "nothing was found"

print "Search indexes are: ", search_indexes
with open('../event.csv', "rb") as e:
    r = csv.reader(e)
    n = 0
    for row in r:
        if n in search_indexes:
            search_results.append(row)
        n += 1
    print "The event(s) in this location are:"
    for row in search_results:
        print row[1]
