from tkinter import *
from tkinter import messagebox

class MyGUI:

    def __init__(self):
        self.root = Tk()

        # Menu bar
        self.menubar = Menu(self.root)

        # Create File menu
        self.filemenu = Menu(self.menubar, tearoff = 0)
        self.filemenu.add_command(label = "Close", command = self.OnClosing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label = "Close Without Question", command = exit)

        # Create Action menu
        self.actionmenu = Menu(self.menubar, tearoff = 0)
        self.actionmenu.add_command(label = "Show Message", command = self.ShowMessage)

        # Add menus to menubar
        self.menubar.add_cascade(menu = self.filemenu, label = "File")
        self.menubar.add_cascade(menu = self.actionmenu, label = "Action")

        # Add menubar to window
        self.root.config(menu = self.menubar)

        # -------------------------------------------------------------------------------------------------------------------

        self.label = Label(self.root, text = "Your message:", font = ('Arial', 18))
        self.label.pack(padx = 10, pady = 10)

        self.textbox = Text(self.root, height = 5, font = ('Arial', 16))
        self.textbox.bind("<KeyPress>", self.Shortcut)
        self.textbox.pack(padx = 10, pady = 10)

        self.checkState = IntVar()
        self.check = Checkbutton(self.root, text = "Show Messagebox", font = ('Arial', 16), variable = self.checkState)
        self.check.pack(padx = 10, pady = 10)

        self.button = Button(self.root, text = "Show Message", font = ('Arial', 18), command = self.ShowMessage)
        self.button.pack(padx = 10, pady = 10)

        self.clearbutton = Button(self.root, text = "Clear", font = ('Arial', 18), command = self.Clear)
        self.clearbutton.pack(padx = 10, pady = 10)

        # -------------------------------------------------------------------------------------------------------------------

        self.root.protocol("WM_DELETE_WINDOW", self.OnClosing)
        self.root.mainloop()

    def ShowMessage(self):
        if (self.checkState.get()):
            messagebox.showinfo(title = "Message", message = self.textbox.get('1.0', END))
        else:
            print(self.textbox.get('1.0', END))

    def Shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            self.ShowMessage()

    def OnClosing(self):
        if messagebox.askyesno(title = "Quit?", message = "Do you really want to quit?"):
            self.root.destroy()

    def Clear(self):
        self.textbox.delete('1.0', END)