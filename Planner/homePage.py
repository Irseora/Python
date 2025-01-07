from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkfont

import json

import datetime as dt

# self.checkList[0].cget("text")

class HomePage:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1200x800")

        # Open JSON for reading
        with open('data.json', 'r') as file:
            self.data = json.load(file)

        # Fonts
        self.titlesFont = tkfont.Font(family = "Vibur", size = 24)
        self.smallerTitlesFont = tkfont.Font(family = "Vibur", size = 16)
        self.normalFont = tkfont.Font(family = "Sour Gummy Light", size = 12)

        # Colors
        self.color1 = '#d9cad0'
        self.color2 = 'thistle'
        self.color2Border = '#aaa0b0'

        #region ToDo Section (Left)
        # ------------------------------------------------------------------------------------------------------------------------
        self.leftFrame = Frame(self.root, width = 300, height = 800, bg = self.color2)
        self.todoListFrame = Frame(self.leftFrame, bg = self.color2)

        Label(self.leftFrame, text = "ToDo:", font = self.titlesFont, bg = self.color2).grid(row = 0, column = 0, padx = 110 , pady = 10, sticky = 'ew')

        # Load todo list
        self.checkList = []
        self.taskVars = []
        self.LoadTodo()

        # Task adder
        self.leftFrame.grid_rowconfigure(1, weight = 1) # Make row 1 take up as much space as possible, to float entry to bottom
        self.newTaskFrame = Frame(self.leftFrame, bg = self.color2)

        Label(self.newTaskFrame, text = "New Task:", font = self.smallerTitlesFont, bg = self.color2).grid(row = 0, column = 0, sticky = 'w', padx = 10)

        self.newTaskText = ""
        self.newTaskEntry = Entry(self.newTaskFrame, width = 23, bg = self.color1, font = self.normalFont)
        self.newTaskEntry.grid(row = 1, column = 0, pady = 10, padx = 10, sticky = "sw")

        Button(self.newTaskFrame, text = "+", command = self.AddTask, bg = self.color1).grid(row = 1, column = 1, sticky = "e", padx = 5)

        # Render frames
        self.newTaskFrame.grid(row = 3, column = 0, sticky = 'nsew')
        self.todoListFrame.grid(row = 1, column = 0, sticky = 'nsew')
        self.leftFrame.grid(row = 0, column = 0, sticky = 'nsew')
        self.leftFrame.grid_propagate(False)    # Don't resize frame to widgets
        #endregion ---------------------------------------------------------------------------------------------------------------

        ttk.Separator(self.root, orient = VERTICAL).grid(column = 1, row = 0, rowspan = 3, sticky = 'ns')

        #region Timeblock Section (Middle)
        # ------------------------------------------------------------------------------------------------------------------------
        self.middleFrame = Frame(self.root, width = 680, height = 800, bg = self.color1)

        Label(self.middleFrame, text = "Timeblock:", font = self.titlesFont, bg = self.color1).grid(row = 0, column = 0, padx = 240, pady = 10, sticky = 'ew')

        self.timeblockFrame = Frame(self.middleFrame, width = 680, height = 700, bg = self.color1)
        self.timeblockFrame.grid_columnconfigure((2,4,6,8,10,12,14), weight = 1, uniform = 'column')

        # Weekday columns
        Label(self.timeblockFrame, text = "Monday", font = self.smallerTitlesFont, bg = self.color1).grid(row = 0, column = 2, sticky = 'ew')
        Label(self.timeblockFrame, text = "Tuesday", font = self.smallerTitlesFont, bg = self.color1).grid(row = 0, column = 4, sticky = 'ew')
        Label(self.timeblockFrame, text = "Wednesday", font = self.smallerTitlesFont, bg = self.color1).grid(row = 0, column = 6, sticky = 'ew')
        Label(self.timeblockFrame, text = "Thursday", font = self.smallerTitlesFont, bg = self.color1).grid(row = 0, column = 8, sticky = 'ew')
        Label(self.timeblockFrame, text = "Friday", font = self.smallerTitlesFont, bg = self.color1).grid(row = 0, column = 10, sticky = 'ew')
        Label(self.timeblockFrame, text = "Saturday", font = self.smallerTitlesFont, bg = self.color1).grid(row = 0, column = 12, sticky = 'ew')
        Label(self.timeblockFrame, text = "Sunday", font = self.smallerTitlesFont, bg = self.color1).grid(row = 0, column = 14, sticky = 'ew')

        # Weekday separators
        ttk.Separator(self.timeblockFrame, orient = HORIZONTAL).grid(row = 1, column = 0, columnspan = 18, sticky = 'ew')
        ttk.Separator(self.timeblockFrame, orient = VERTICAL).grid(row = 0, column = 1, rowspan = 20, sticky = 'ns')
        ttk.Separator(self.timeblockFrame, orient = VERTICAL).grid(row = 0, column = 3, rowspan = 20, sticky = 'ns')
        ttk.Separator(self.timeblockFrame, orient = VERTICAL).grid(row = 0, column = 5, rowspan = 20, sticky = 'ns')
        ttk.Separator(self.timeblockFrame, orient = VERTICAL).grid(row = 0, column = 7, rowspan = 20, sticky = 'ns')
        ttk.Separator(self.timeblockFrame, orient = VERTICAL).grid(row = 0, column = 9, rowspan = 20, sticky = 'ns')
        ttk.Separator(self.timeblockFrame, orient = VERTICAL).grid(row = 0, column = 11, rowspan = 20, sticky = 'ns')
        ttk.Separator(self.timeblockFrame, orient = VERTICAL).grid(row = 0, column = 13, rowspan = 20, sticky = 'ns')

        # Timeslots
        for i in range(6, 23):
            if (i < 13): text = f"{i} AM"
            else: text = f"{i-12} PM"
            Label(self.timeblockFrame, text = text, font = self.normalFont, bg = self.color1).grid(row = i-4, column = 0, sticky = 'e', pady = 4)

        # Load timeblock
        self.eventsList = []
        self.eventFramesList = []
        self.LoadTimeblock()

        # Event adder
        self.newEventButton = Button(self.middleFrame, text = "New Event", font = self.smallerTitlesFont, bg = self.color2, command = self.AddEvent)
        self.newEventButton.grid(row = 2, column = 0, sticky = 'ns', pady = 10)

        # Render section
        self.timeblockFrame.grid(row = 1, column = 0, sticky = 'nsew')
        self.middleFrame.grid(row = 0, column = 2, sticky = 'nsew')
        self.middleFrame.grid_propagate(False)  # Don't resize frame to widgets
        #endregion ---------------------------------------------------------------------------------------------------------------

        ttk.Separator(self.root, orient = VERTICAL).grid(row = 0, column = 3, rowspan = 3, sticky = 'ns')

        #region Deadlines Section (Right)
        # ------------------------------------------------------------------------------------------------------------------------
        self.rightFrame = Frame(self.root, width = 220, height = 800, bg = self.color2)

        Label(self.rightFrame, text = "Deadlines:", font = self.titlesFont, bg = self.color2).grid(row = 0, column = 0, padx = 50, pady = 10, sticky = 'ew')

        # Render section
        self.rightFrame.grid(row = 0, column = 4, sticky = 'nsew')
        self.rightFrame.grid_propagate(False)   # Don't resize frame to widgets
        #endregion ---------------------------------------------------------------------------------------------------------------

        self.root.protocol("WM_DELETE_WINDOW", self.SaveAndClose)
        self.root.mainloop()

    def LoadTodo(self):
        """Load & render todo list from JSON file"""
        for task in self.data['todo']:
            self.taskVars.append(IntVar())
            checkBtn = Checkbutton(self.todoListFrame, text = task['text'], variable = self.taskVars[task['id']], onvalue = 1, offvalue = 0, bg = self.color2, font = self.normalFont)
            if task['done']:
                checkBtn.select()

            self.checkList.append(checkBtn)
            checkBtn.grid(row = task['id'], column = 0, sticky = 'w')

    def LoadTimeblock(self):
        """Load & render timeblock from JSON file"""
        for entry in self.data['timeblock']:
            # Check if it's this week
            date = dt.datetime.strptime(entry['date'], '%d-%m-%Y').date()
            dateWeekNr = date.strftime('%V')
            currentWeekNr = dt.date.today().strftime('%V')
            if dateWeekNr == currentWeekNr:
                event = MyEvent(date, entry['start'], entry['end'], entry['text'])
                block = Frame(self.timeblockFrame, bg = self.color2, highlightbackground = self.color2Border, highlightthickness = 1)
                Label(block, text = entry['text'], font = self.normalFont, bg = self.color2, wraplength = 100, justify = LEFT).grid(row = 0, column = 0, sticky = 'ew')

                block.grid(row = event.startTime - 4, column = (event.day + 1) * 2, rowspan = event.endTime - event.startTime + 1, sticky = "nesw")

                self.eventsList.append(event)
                self.eventFramesList.append(block)

    def LoadDeadlines(self):
        """Load & render deadlines from JSON file"""


    def AddTask(self):
        """Add a new task to the todo list"""
        id = len(self.checkList)
        text = self.newTaskEntry.get()
        self.taskVars.append(IntVar())

        checkBtn = Checkbutton(self.todoListFrame, text = text, variable = self.taskVars[id], onvalue = 1, offvalue = 0, bg = self.color2, font = self.normalFont)
        self.checkList.append(checkBtn)
        checkBtn.grid(row = id, column = 0, sticky = 'w')

        self.newTaskEntry.delete(0, 'end')

    def AddEvent(self):
        """Add a new event to the timeblock"""
        id = len(self.eventsList)

        newWindow = Toplevel(self.root)
        newWindow.geometry('500x200')
        newWindow.configure(bg = self.color1)

        Label(newWindow, text = 'Date (dd-mm-yyyy):', font = self.normalFont, bg = self.color1).grid(row = 0, column = 0, sticky = 'w')
        


    def SaveAndClose(self):
        # TODO: save everything

        self.root.destroy()

class MyEvent:
    """Class for representing events

    Attributes:
    date : str
        String representing a date
    day : int
        Number representing a day of the week (0-7)
    startTime : int
        Number representing starting hour (6-23)
    endTime : int
        Number representing ending hour (6-23)
    text : str
    """

    def __init__(self, date, startTime, endTime, text):
        self.date = date
        self.day = self.date.weekday()
        self.startTime = startTime
        self.endTime = endTime
        self.text = text