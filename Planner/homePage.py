from tkinter import *
import tkinter.ttk

class HomePage:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("1200x800")

        # ToDo Section (left) ---------------------------------------------------------------------------
        self.todoFrame = Frame(self.root, width = 300, height = 800)

        Label(self.todoFrame, text = "TO DO:").grid(row = 0, column = 0, padx = 120 , pady = 10, sticky = 'ew')

        self.checkList = []
        self.taskVars = []

        # self.var1 = 0
        # c1 = Checkbutton(self.todoFrame, text = "AAAAAAAAAAAAAAAAAAAA", variable = self.var1, onvalue = 1, offvalue = 0)
        # c1.grid(row = 1, column = 0, sticky = 'w')


        self.todoFrame.grid(row = 0, column = 0, sticky = 'nsew')
        self.todoFrame.grid_propagate(False)

        tkinter.ttk.Separator(self.root, orient = VERTICAL).grid(column = 1, row = 0, rowspan = 3, sticky = 'ns')

        # Timeblock Section (middle) --------------------------------------------------------------------
        self.timeblockFrame = Frame(self.root, width = 600, height = 800)

        Label(self.timeblockFrame, text = "TIMEBLOCK:", padx = 270, pady = 10).grid(row = 0, column = 0, sticky = 'ew')

        self.timeblockFrame.grid(row = 0, column = 2, sticky = 'nsew')
        self.timeblockFrame.grid_propagate(False)

        tkinter.ttk.Separator(self.root, orient = VERTICAL).grid(column = 3, row = 0, rowspan = 3, sticky = 'ns')

        # Misc Section (right) --------------------------------------------------------------------------
        self.miscFrame = Frame(self.root, width = 300, height = 800)



        self.miscFrame.grid(row = 0, column = 4, sticky = 'nsew')
        self.miscFrame.grid_propagate(False)

        self.root.mainloop()

    def CreateTask(self, done, text):
        a