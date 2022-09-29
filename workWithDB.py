import os
from shutil import rmtree


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
