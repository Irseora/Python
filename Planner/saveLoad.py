import json
import datetime as dt
from containers import *

def ReadJSON(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data

def LoadTasks(data):
    tasks = []
    for task in data['tasks']:
        temp = Task(task['done'], task['text'])
        tasks.append(temp)
    return tasks

def LoadEvents(data):
    events = []
    for event in data['events']:
        date = dt.datetime.strptime(event['date'], '%d-%m-%Y').date()
        day = date.weekday()

        # Check if event is this week
        dateWeekNr = date.strftime('%V')    # Get date's week number
        currentWeekNr = dt.date.today().strftime('%V')  # Get current week number
        if dateWeekNr == currentWeekNr:
            temp = Event(date, day, event['startTime'], event['endTime'], event['text'])
            events.append(temp)
        
    return events

def LoadDeadlines(data):
    deadlines = []
    for deadline in data['deadlines']:
        date = dt.datetime.strptime(deadline['date'], '%d-%m-%Y').date()

        # Check if deadline has passed
        if date >= dt.date.today():
            temp = Deadline(date, deadline['date'], deadline['text'])
            deadlines.append(temp)
        
    return deadlines

def Save(data, path):
    with open(path, 'w') as file:
        json.dump(data, file, indent = 4)