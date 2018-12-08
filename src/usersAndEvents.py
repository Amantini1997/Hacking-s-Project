
import csv
import datetime
from collections import deque

class User():

    def __init__(self, name, password, gender, age, profession, location, desc, groups):

        self.id = getId('user_profile_id')
        self.name = name
        self.password = password
        self.gender = gender
        self.age = age
        self.profession = profession
        self.location = location
        self.desc = desc
        self.groups = groups

class Event():

    def __init__(self, name, desc, start, end, status, location, limit):
        now = datetime.datetime.now()
        self.now = now.strftime("%Y-%m-%d %H:%M")
        self.id = getId('events.csv')
        self.name = name
        self.desc = desc
        self.start = start
        self.end = end
        self.status = status
        self.location = location
        self.limit = limit

def addUser(user):
    filename = 'user_profile_id'

    with open(filename, 'w', newline = '') as theFile:
        writer = csv.writer(theFile, delimiter = ',')
        writer.writerow([user.id], [user.name], [userl.password], [user.gender], [user.age], [user.profession], [user.location], [user.desc], [user.groups])

def getId(filename):

    reader = getData(filename)

    d = deque(reader, maxlen = 1)
    last = d.pop()
    user_id = last[0]

    return user_id + 1

def getData(filename):
    with open(filename) as theFile:
        reader = csv.reader(theFile, delimiter = ',')
        next(reader)

        return reader

def addEvent(event):

    filename = 'events.csv'

    with open(filename, 'w', newline = '') as theFile:
        writer = csv.writer(theFile, delimiter = ',')
        writer.writerow([event.id], [event.name], [event.desc], [event.start], [event.end], [event.now], ["created_by"], [event.status], [event.location], [event.limit])

def checkUsernameAndPassword(username, password):

    filename = 'user_profile_id'
    reader = getData(filename)

    success = False

    for r in reader:
        if username = r[1] and password == r[2]:
            success = True

    return success
