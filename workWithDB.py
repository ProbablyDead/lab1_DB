import os
import datetime
from shutil import rmtree
from shutil import copytree


def createDB():
    name = input("Enter name of data base: ")
    os.chdir("DataBases")
    try:
        os.mkdir(name)
    except FileExistsError:
        print(f"Database '{name}' already exist")
        return

    os.chdir(name)
    open("students_0.txt", "w").close()
    open("variants_0.txt", "w").close()
    open("generatedTable.txt", "w").close()
    open("generatedTableForTeacher.txt", "w").close()
    os.chdir("..")
    os.chdir("..")


def deleteDB():
    name = input("Enter name of data base: ")
    os.chdir("DataBases")
    if input("Are you sure? - (Y/N) \n-> ") in ["Y", "y"]:
        try:
            rmtree(name)
        except FileNotFoundError:
            print(f"No such file or directory: '{name}'")
        else:
            print("Deleted")
    else:
        print("Not deleted")
    os.chdir("..")


def createBackup():
    base = input("Enter database to save: ")
    os.chdir("DataBases")
    try:
        os.chdir(base)
    except FileNotFoundError:
        print(f"No such database '{base}'")
        return

    os.chdir("..")
    os.chdir("..")

    try:
        copytree(f"DataBases/{base}", f"Backups/{base}|{datetime.datetime.now().strftime('%d.%m.%Y_%H.%M')}")
    except FileExistsError:
        copytree(f"DataBases/{base}", f"Backups/{base}|{datetime.datetime.now().strftime('%d.%m.%Y_%H.%M')}_1")


def resetBackup():
    base = input("Enter backup to reset: ")
    os.chdir("Backups")
    try:
        copytree(base, f"../DataBases/{base}")
    except FileNotFoundError:
        print(f"No such backup '{base}'")

    os.chdir("..")

