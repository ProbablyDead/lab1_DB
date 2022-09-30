import os
import datetime
from shutil import rmtree
from shutil import copytree


def createDB(name):
    os.chdir("DataBases")
    os.mkdir(name)
    os.chdir(name)
    open("students_0.txt", "w").close()
    open("variants_0.txt", "w").close()
    open("generatedTable.txt", "w").close()
    open("generatedTableForTeacher.txt", "w").close()
    os.chdir("..")
    os.chdir("..")


def deleteDB(name):
    os.chdir("DataBases")
    rmtree(name)
    os.chdir("..")


def createBackup(base):
    try:
        copytree(f"DataBases/{base}", f"Backups/{base}|{datetime.datetime.now().strftime('%d.%m.%Y_%H.%M')}")
    except FileExistsError:
        copytree(f"DataBases/{base}", f"Backups/{base}|{datetime.datetime.now().strftime('%d.%m.%Y_%H.%M')}_1")


def resetBackup(base):
    os.chdir("Backups")
    copytree(base, f"../DataBases/{base}")
    os.chdir("..")

