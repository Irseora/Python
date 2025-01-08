class Task:
    def __init__(self, done, text):
        self.done = done
        self.text = text

    def toDict(self):
        return {
            'done': self.done,
            'text': self.text
        }

class Event:
    def __init__(self, date, day, startTime, endTime, text):
        self.date = date
        self.day = day
        self.startTime = startTime
        self.endTime = endTime
        self.text = text

    def toDict(self):
        return {
            'date': self.date.strftime('%d-%m-%Y'),
            'startTime': self.startTime,
            'endTime': self.endTime,
            'text': self.text
        }

class Deadline:
    def __init__(self, date, dateString, text):
        self.date = date
        self.dateString = dateString
        self.text = text

    def toDict(self):
        return {
            'date': self.date.strftime('%d-%m-%Y'),
            'text': self.text
        }