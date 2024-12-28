from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkfont

import json

# self.checkList[0].cget("text")

class HomePage:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1200x800")

        # Fonts
        titlesFont = tkfont.Font(family = "Vibur", size = 24)

        #region ToDo Section (Left)
        # ------------------------------------------------------------------------------------------------------------------------
        self.leftFrame = Frame(self.root, width = 300, height = 800)
        self.todoListFrame = Frame(self.leftFrame, highlightbackground = "red", highlightthickness = 1)

        Label(self.leftFrame, text = "ToDo:", font = titlesFont).grid(row = 0, column = 0, padx = 110 , pady = 10, sticky = 'ew')

        # Load todo list
        self.checkList = []
        self.taskVars = []
        self.LoadTodo()

        # Task adder
        self.leftFrame.grid_rowconfigure(1, weight = 1) # Make row 1 take up as much space as possible, to float entry to bottom
        self.newTaskFrame = Frame(self.leftFrame, highlightbackground = "blue", highlightthickness = 1)

        Label(self.newTaskFrame, text = "NEW TASK:").grid(row = 0, column = 0, sticky = 'w')

        self.newTaskText = ""
        self.newTaskEntry = Entry(self.newTaskFrame, width = 45)
        self.newTaskEntry.grid(row = 1, column = 0, sticky = "sw")

        Button(self.newTaskFrame, text = "+", command = self.AddTask).grid(row = 1, column = 1, sticky = "e")

        # Render frames
        self.newTaskFrame.grid(row = 3, column = 0, sticky = 'nsew')
        self.todoListFrame.grid(row = 1, column = 0, sticky = 'nsew')
        self.leftFrame.grid(row = 0, column = 0, sticky = 'nsew')
        self.leftFrame.grid_propagate(False)    # Don't resize frame to widgets
        #endregion ---------------------------------------------------------------------------------------------------------------

        ttk.Separator(self.root, orient = VERTICAL).grid(column = 1, row = 0, rowspan = 3, sticky = 'ns')

        #region Timeblock Section (Middle)
        # ------------------------------------------------------------------------------------------------------------------------
        self.middleFrame = Frame(self.root, width = 600, height = 800)

        Label(self.middleFrame, text = "Timeblock:", font = titlesFont).grid(row = 0, column = 0, padx = 240, pady = 10, sticky = 'ew')

        # Render section
        self.middleFrame.grid(row = 0, column = 2, sticky = 'nsew')
        self.middleFrame.grid_propagate(False)  # Don't resize frame to widgets
        #endregion ---------------------------------------------------------------------------------------------------------------

        ttk.Separator(self.root, orient = VERTICAL).grid(column = 3, row = 0, rowspan = 3, sticky = 'ns')

        #region Misc Section (Right)
        # ------------------------------------------------------------------------------------------------------------------------
        self.rightFrame = Frame(self.root, width = 300, height = 800)


        # Render section
        self.rightFrame.grid(row = 0, column = 4, sticky = 'nsew')
        self.rightFrame.grid_propagate(False)   # Don't resize frame to widgets
        #endregion ---------------------------------------------------------------------------------------------------------------

        self.root.mainloop()

    def LoadTodo(self):
        """Load & render todo list from JSON file"""
        with open('data.json', 'r') as file:
            data = json.load(file)

        for task in data['todo']:
            self.taskVars.append(IntVar())

            checkBtn = Checkbutton(self.todoListFrame, text = task['text'], variable = self.taskVars[task['id']], onvalue = 1, offvalue = 0)
            if task['done']: checkBtn.select()
            self.checkList.append(checkBtn)
            checkBtn.grid(row = task['id'], column = 0, sticky = 'w')

    def AddTask(self):
        """Add a new task to the todo list"""
        id = len(self.checkList)
        text = self.newTaskEntry.get()
        self.taskVars.append(IntVar())

        checkBtn = Checkbutton(self.todoListFrame, text = text, variable = self.taskVars[id], onvalue = 1, offvalue = 0)
        self.checkList.append(checkBtn)
        checkBtn.grid(row = id, column = 0, sticky = 'w')

        self.newTaskEntry.delete(0, 'end')