import os
from random import randint


def generateTables():
    base = input("Enter database: ")
    os.chdir("DataBases")

    try:
        os.chdir(base)
    except FileExistsError:
        print(f"File '{base}' already exists")
        return

    studentsFile = ""
    variantsFile = ""

    for line in os.listdir():
        if line[0] == "s":
            studentsFile = open(line, "rt")
        if line[0] == "v":
            variantsFile = open(line, "rt")

    students = studentsFile.readlines()
    variants = variantsFile.readlines()
    variantsCount = len(variants)

    studentsFile.close()
    variantsFile.close()

    tableID = open("generatedTable.txt", "wt")
    tableForTeacher = open("generatedTableForTeacher.txt", "wt")

    variantsID = []
    variantsNames = []

    for line in variants:
        variantsID.append(line[:line.find("-")])
        variantsNames.append(line[(line.find("-")+1):])

    for line in students:
        ide = line[:line.find("-")]
        name = line[(line.find("-")+1):-1]
        index = randint(0, variantsCount - 1)

        tableID.write(f"{ide}-{variantsID[index]}\n")
        tableForTeacher.write(f"{name}-{variantsNames[index]}")

    tableID.close()
    tableForTeacher.close()
    os.chdir("..")
    os.chdir("..")
