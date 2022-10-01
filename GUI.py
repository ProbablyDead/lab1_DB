from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import scrolledtext
import workWithDB
from workWithTables import *
from workWithDB import *
from os import listdir


def openBase(base):
    path = f"DataBases/{base}"
    window = Tk()
    window.title(base)
    window.config(bg="gray35")
    window.geometry('%dx%d+%d+%d' % (window.winfo_screenwidth(), window.winfo_screenheight(), 0, 0))

    def update():
        window.destroy()
        openBase(base)

    def generateTables_OBR():
        generateTables(base)
        update()

    # STUDENTS

    Label(window, text="ID-Student", font=("Arial Bold", 17), bg="gray35", fg="red").place(x=150, y=2)

    students = scrolledtext.ScrolledText(window, width=50, height=61, bg="gray")
    stf = ""
    for line in os.listdir(path):
        if line[0] == "s":
            stf = open(f"{path}/{line}", "rt")

    students.insert(INSERT, stf.read())
    students.place(x=10, y=30)
    students.config(state="disabled")

    stf.close()

    # VARIANTS

    Label(window, text="ID-Variant", font=("Arial Bold", 17), bg="gray35", fg="red").place(x=470, y=2)

    variants = scrolledtext.ScrolledText(window, width=30, height=61, bg="gray")
    vaf = ""
    for line in os.listdir(path):
        if line[0] == "v":
            vaf = open(f"{path}/{line}", "rt")

    variants.insert(INSERT, vaf.read())
    variants.place(x=400, y=30)
    variants.config(state="disabled")

    vaf.close()

    # GENERATE BUTTON

    generate = Button(window, text="Generate", command=generateTables_OBR, bg="gray35", borderwidth=3,
                      height=5, width=10, font=("Arial Bold", 17), fg="red")
    generate.place(relx=0.5, rely=0.5, anchor=CENTER)

    # CLOSE BUTTON

    home = Button(window, text="Close", command=window.destroy, bg="gray35", borderwidth=3,
                  height=5, width=10, font=("Arial Bold", 17))
    home.place(relx=0.5, rely=0.9 + 0.011, anchor='center')

    # IDES

    Label(window, text="ID(stud)-ID(var)", font=("Arial Bold", 17), bg="gray35", fg="red").place(x=855, y=2)

    ides = scrolledtext.ScrolledText(window, width=30, height=61, bg="gray")
    idf = open(f"{path}/generatedTable.txt", "rt")

    ides.insert(INSERT, idf.read())
    ides.place(x=805, y=30)
    ides.config(state="disabled")

    idf.close()

    # FOR TEACHER

    Label(window, text="Student-Variant", font=("Arial Bold", 17), bg="gray35", fg="red").place(x=1170, y=2)

    fort = scrolledtext.ScrolledText(window, width=50, height=61, bg="gray")
    tf = open(f"{path}/generatedTableForTeacher.txt", "rt")

    fort.insert(INSERT, tf.read())
    fort.place(x=1055, y=30)
    fort.config(state="disabled")

    tf.close()

    ###### DEFENITIONS

    def OBR_addStudent():
        pass

    def OBR_addStudentsFromFile():
        pass

    def OBR_addVariant():
        pass

    def OBR_addVariantsFromDirectory():
        pass

    def OBR_deleteStudent():
        pass

    def OBR_deleteVariant():
        pass

    def OBR_changeStudent():
        pass

    def OBR_changeVariant():
        pass

    def OBR_showStudent():
        pass

    def OBR_showVariant():
        pass

    ###### MENU

    mainmenu = Menu(window)

    # ADD

    add = Menu(mainmenu)
    whichStud = Menu(add)
    whichStud.add_command(label="By one", command=OBR_addStudent)
    whichStud.add_command(label="From file", command=OBR_addStudentsFromFile)
    add.add_cascade(label='Student', menu=whichStud)
    whichVar = Menu(add)
    whichVar.add_command(label="By one", command=OBR_addVariant)
    whichVar.add_command(label="From directory", command=OBR_addVariantsFromDirectory)
    add.add_cascade(label='Variant', menu=whichVar)

    mainmenu.add_cascade(label="Add", menu=add)

    # DELETE

    deleteS = Menu(mainmenu)
    deleteS.add_command(label='Student', command=OBR_deleteStudent)
    deleteS.add_command(label='Variant', command=OBR_deleteVariant)
    mainmenu.add_cascade(label='Delete', menu=deleteS)

    # CHANGE

    change = Menu(mainmenu)
    change.add_command(label='Student', command=OBR_changeStudent)
    change.add_command(label='Variant', command=OBR_changeVariant)
    mainmenu.add_cascade(label='Change', menu=change)

    # SHOW

    show = Menu(mainmenu)
    show.add_command(label='Student', command=OBR_showStudent)
    show.add_command(label='Variant', command=OBR_showVariant)
    mainmenu.add_cascade(label='Show by ID', menu=show)

    window.config(menu=mainmenu)

    window.mainloop()


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
        # window.destroy()
        openBase(base)

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
