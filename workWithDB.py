import os
import datetime
from shutil import rmtree
from shutil import copytree


def createDB():
    name = input("Enter name of data base: ")
    os.mkdir(name)
    os.chdir(name)
    open("students_0.txt", "w").close()
    open("variants_0.txt", "w").close()
    open("generatedTable.txt", "w").close()
    open("generatedTableForTeacher.txt", "w").close()
    os.chdir("..")


def deleteDB():
    name = input("Enter name of data base: ")
    if input("Are you sure? - (Y/N) \n-> ") in ["Y", "y"]:
        try:
            rmtree(name)
        except FileNotFoundError:
            print(f"No such file or directory: '{name}'")
        else:
            print("Deleted")
    else:
        print("Not deleted")


def createBackup():
    base = input("Enter database to save: ")
    try:
        os.chdir(base)
    except FileNotFoundError:
        print(f"No such database '{base}'")
        return

    os.chdir("..")
    try:
        copytree(base, f"Backups/{base}|{datetime.datetime.now().strftime('%d.%m.%Y_%H.%M')}")
    except FileExistsError:
        copytree(base, f"Backups/{base}|{datetime.datetime.now().strftime('%d.%m.%Y_%H.%M')}_1")


def resetBackup():
    base = input("Enter backup to reset: ")
    os.chdir("Backups")
    try:
        copytree(base, f"../{base}")
    except FileExistsError:
        print(f"File '{base}' already exists")

    os.chdir("..")

