from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import workWithDB
from workWithTables import *
from workWithDB import *
from os import listdir

def openBase(base):
    pass


def Home():

    # MAIN

    window = Tk()
    window.title("DataBasesHSE")
    window.config(bg="gray")
    window.geometry('%dx%d+%d+%d' % (380, 226, 100, 100))
    font = ("Arial Bold", 17)

    def update():
        window.destroy()
        Home()

    # ADD
    def createDB_OBR():
        auf = enterAdd.get()
        if auf in ["", " "]:
            messagebox.showerror("Error", "Enter name of database")
            enterAdd.delete(0, END)
            return

        if auf in listdir("DataBases"):
            messagebox.showerror("Error", f"Database '{auf}' already exist")
            enterAdd.delete(0, END)
            return
        workWithDB.createDB(auf)
        update()

    txt1 = Label(window, text="Add Database: ", font=font, bg="gray", fg="black")
    txt1.place(x=10, y=8)

    enterAdd = Entry(window, width=13, bg="gray60", fg="black", borderwidth=3, highlightbackground="gray")
    enterAdd.place(x=135, y=8)

    btn1 = Button(window, text="Ok", font=font, command=createDB_OBR, borderwidth=3,
                  highlightbackground="gray")
    btn1.place(x=263, y=6)

    # DELETE
    def deleteDB_OBR():
        auf = choose0.get()
        if auf == "Choose...":
            return
        if messagebox.askyesno("Confirmation", "Are you sure?"):
            if auf not in listdir("DataBases"):
                messagebox.showerror("Error", f"There is no such database '{auf}'")
                update()
                return
            workWithDB.deleteDB(auf)
            update()

    txt2 = Label(window, text="Delete Database: ", font=font, bg="gray", fg="black")
    txt2.place(x=10, y=50)

    buf0 = listdir("DataBases")
    buf0.pop(buf0.index(".DS_Store"))
    buf0.insert(0, "Choose...")

    choose0 = Combobox(window, width=13)
    choose0["values"] = buf0
    choose0.current(0)
    choose0.place(x=153, y=50)

    btn2 = Button(window, text="Ok", font=font, command=deleteDB_OBR, borderwidth=3,
                  highlightbackground="gray")
    btn2.place(x=298, y=47)

    # CHOOSE
    def chooseDB_OBR():
        base = choose1.get()
        if base == "Choose...":
            return
        if base not in listdir("DataBases"):
            messagebox.showerror("Error", f"There is no such database '{base}'")
            update()
            return
        openBase(base)
        update()

    txt3 = Label(window, text="Choose Database: ", font=font, bg="gray", fg="black")
    txt3.place(x=10, y=92)

    buf = listdir("DataBases")
    buf.pop(buf.index(".DS_Store"))
    buf.insert(0, "Choose...")

    choose1 = Combobox(window, width=13)
    choose1["values"] = buf
    choose1.current(0)
    choose1.place(x=165, y=92)

    btn3 = Button(window, text="Ok", font=font, command=chooseDB_OBR, borderwidth=3,
                  highlightbackground="gray")
    btn3.place(x=309, y=89)

    # CREATE BACKUP

    def createBackup_OBR():
        bku = choose2.get()
        if bku == "Choose...":
            return
        if bku not in listdir("DataBases"):
            messagebox.showerror("Error", f"There is no such database '{bku}'")
            update()
            return
        workWithDB.createBackup(bku)
        update()

    txt4 = Label(window, text="Create backup: ", font=font, bg="gray", fg="black")
    txt4.place(x=10, y=140)

    buf2 = listdir("DataBases")
    buf2.pop(buf2.index(".DS_Store"))
    buf2.insert(0, "Choose...")

    choose2 = Combobox(window, width=13)
    choose2["values"] = buf2
    choose2.current(0)
    choose2.place(x=139, y=140)

    btn4 = Button(window, text="Ok", font=font, command=createBackup_OBR, borderwidth=3,
                  highlightbackground="gray")
    btn4.place(x=284, y=137)

    # RESET BACKUP

    def resetBackup_OBR():
        rbku = choose3.get()
        if rbku == "Choose...":
            return
        if rbku not in listdir("Backups"):
            messagebox.showerror("Error", f"There is no such backup '{rbku}'")
            update()
            return
        workWithDB.resetBackup(rbku)
        update()

    txt5 = Label(window, text="Reset backup: ", font=font, bg="gray", fg="black")
    txt5.place(x=10, y=188)

    buf3 = listdir("Backups")
    buf3.pop(buf3.index(".DS_Store"))
    buf3.insert(0, "Choose...")

    choose3 = Combobox(window, width=13)
    choose3["values"] = buf3
    choose3.current(0)
    choose3.place(x=132, y=188)

    btn5 = Button(window, text="Ok", font=font, command=resetBackup_OBR, borderwidth=3,
                  highlightbackground="gray")
    btn5.place(x=277, y=185)

    window.mainloop()
