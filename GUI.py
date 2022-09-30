from tkinter import *
from tkinter import ttk
from workWithTables import *

OPTIONS = [
"Jan",
"Feb",
"Mar"
]


def start():
    window = Tk()
    window.title("DataBasesHSE")
    window.config(bg="white")
    window.geometry('800x600')

    variable = StringVar(window)
    variable.set(OPTIONS[0])

    but = OptionMenu(window, variable, *OPTIONS)
    but.pack()



    window.mainloop()
