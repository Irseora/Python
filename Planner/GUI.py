from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkfont

import saveLoad as sl
from containers import *

class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1200x800')

        # Fonts
        self.titlesFont = tkfont.Font(family = 'Vibur', size = 24)
        self.smallerTitlesFont = tkfont.Font(family = 'Vibur', size = 16)
        self.normalFont = tkfont.Font(family = 'Sour Gummy Light', size = 12)
        
        # Colors
        self.color1 = '#d9cad0'
        self.color2 = 'thistle'
        self.color1Border = '#998d92'
        self.color2Border = '#aaa0b0'

        self.LoadData()

        self.InitLeft()
        self.InitMiddle()
        self.InitRight()

        self.root.mainloop()


    def LoadData(self):
        data = sl.ReadJSON('data.json')
        self.tasks = sl.LoadTasks(data)
        self.events = sl.LoadEvents(data)
        self.deadlines = sl.LoadDeadlines(data)


    def InitLeft(self):
        self.leftFrame = Frame(self.root, width = 300, height = 800, bg = self.color2, highlightbackground = self.color2Border, highlightthickness = 1)

        Label(self.leftFrame, text = 'ToDo:', font = self.titlesFont, bg = self.color2).grid(row = 0, column = 0, padx = 110 , pady = 10, sticky = 'ew')
        
        self.InitTodoListFrame()
        self.leftFrame.grid_rowconfigure(1, weight = 1)     # Make row 1 take up as much space as possible, to float entry to bottom

        self.InitNewTaskFrame()

        self.leftFrame.grid(row = 0, column = 0, sticky = 'nsew')
        self.leftFrame.grid_propagate(False)    # Don't resize frame to widgets
        
    def InitTodoListFrame(self):
        self.todoListFrame = Frame(self.leftFrame, bg = self.color2)

        self.taskNr = 0
        for task in self.tasks:
            self.CreateTask(task, self.taskNr)
            self.taskNr += 1

        self.todoListFrame.grid(row = 1, column = 0, sticky = 'nsew')

    def InitNewTaskFrame(self):
        self.newTaskFrame = Frame(self.leftFrame, bg = self.color2)

        Label(self.newTaskFrame, text = "New Task:", font = self.smallerTitlesFont, bg = self.color2).grid(row = 0, column = 0, sticky = 'w', padx = 10)
        
        self.newTaskText = ""
        self.newTaskEntry = Entry(self.newTaskFrame, width = 23, bg = self.color1, font = self.normalFont)
        self.newTaskEntry.grid(row = 1, column = 0, pady = 10, padx = 10, sticky = "sw")

        Button(self.newTaskFrame, text = "+", command = self.AddTask, bg = self.color1).grid(row = 1, column = 1, sticky = "e", padx = 5)

        self.newTaskFrame.grid(row = 3, column = 0, sticky = 'nsew')



    def InitMiddle(self):
        self.middleFrame = Frame(self.root, width = 680, height = 800, bg = self.color1, highlightbackground = self.color1Border, highlightthickness = 1)

        Label(self.middleFrame, text = "Timeblock:", font = self.titlesFont, bg = self.color1).grid(row = 0, column = 0, padx = 240, pady = 10, sticky = 'ew')

        self.InitTimeblockFrame()
        
        # TODO: Event adder
        self.newEventButton = Button(self.middleFrame, text = "New Event", font = self.smallerTitlesFont, bg = self.color2, command = self.AddEvent)
        self.newEventButton.grid(row = 2, column = 0, sticky = 'ns', pady = 10)

        self.middleFrame.grid(row = 0, column = 1, sticky = 'nsew')
        self.middleFrame.grid_propagate(False)    # Don't resize frame to widgets

    def InitTimeblockFrame(self):
        self.timeblockFrame = Frame(self.middleFrame, width = 680, height = 700, bg = self.color1)
        self.timeblockFrame.grid_columnconfigure((2,4,6,8,10,12,14), weight = 1, uniform = 'column')    # Uniformly distribute space between columns

        # Weekdays
        weekdays = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]
        for i in range(7):
            Label(self.timeblockFrame, text = weekdays[i], font = self.smallerTitlesFont, bg = self.color1).grid(row = 0, column = (i+1) * 2, sticky = 'ew')

        # Separators
        ttk.Separator(self.timeblockFrame, orient = HORIZONTAL).grid(row = 1, column = 0, columnspan = 18, sticky = 'ew')
        for i in range(1, 14, 2):
            ttk.Separator(self.timeblockFrame, orient = VERTICAL).grid(row = 0, column = i, rowspan = 20, sticky = 'ns')

        # Timeslots
        for i in range(6, 23):
            if (i < 13): text = f'{i} AM'
            else: text = f'{i-12} PM'
            Label(self.timeblockFrame, text = text, font = self.normalFont, bg = self.color1).grid(row = i-4, column = 0, sticky = 'e', pady = 4)

        self.InitEvents()
        self.timeblockFrame.grid(row = 1, column = 0, sticky = 'nsew')

    def InitEvents(self):
        for event in self.events:
            self.CreateEvent(event)
        


    def InitRight(self):
        self.rightFrame = Frame(self.root, width = 220, height = 800, bg = self.color2, highlightbackground = self.color2Border, highlightthickness = 1)

        Label(self.rightFrame, text = "Deadlines:", font = self.titlesFont, bg = self.color2).grid(row = 0, column = 0, padx = 50, pady = 10, sticky = 'ew')
        
        self.InitDeadlinesFrame()

        # TODO: New deadlines frame & button

        self.rightFrame.grid(row = 0, column = 3, sticky = 'nsew')
        self.rightFrame.grid_propagate(False)   # Don't resize frame to widgets

    def InitDeadlinesFrame(self):
        self.deadlinesFrame = Frame(self.rightFrame, width = 220, height = 600, bg = self.color2)

        self.deadlineNr = 0
        for deadline in self.deadlines:
            self.CreateDeadline(deadline, self.deadlineNr)
            self.deadlineNr += 1

        self.deadlinesFrame.grid(row = 1, column = 0, sticky = 'nsew')


    # --------------------------------------------------


    def AddTask(self):
        text = self.newTaskEntry.get()

        if (len(text) != 0):
            self.taskNr += 1
            task = Task(0, text)
            self.tasks.append(task)
            self.CreateTask(task, self.taskNr)

            self.newTaskEntry.delete(0, 'end')

    def AddEvent(self):
        print('A')

    def AddDeadline(self):
        print('B')



    def CreateTask(self, task, rowNr):
        checkButton = Checkbutton(self.todoListFrame, text = task.text, variable = task.done, onvalue = 1, offvalue = 0, bg = self.color2, font = self.normalFont)
        if task.done: checkButton.select()

        checkButton.grid(row = rowNr, column = 0, sticky = 'w')
        # TODO: delete task button

    def CreateEvent(self, event):
        block = Frame(self.timeblockFrame, bg = self.color2, highlightbackground = self.color2Border, highlightthickness = 1)

        Label(block, text = event.text, font = self.normalFont, bg = self.color2, wraplength = 100, justify = LEFT).grid(row = 0, column = 0, sticky = 'ew')

        block.grid(row = event.startTime - 4, column = (event.day + 1) * 2, rowspan = event.endTime - event.startTime + 1, sticky = 'nesw')

    def CreateDeadline(self, deadline, rowNr):
        labelText = deadline.dateString + '\n' + deadline.text + '\n'
        Label(self.deadlinesFrame, text = labelText, font = self.normalFont, bg = self.color2, wraplength = 100, justify = LEFT).grid(row = rowNr, column = 0, sticky = 'ew')