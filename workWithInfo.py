import os


def addStudent():
    name = input("Input student's full name: ")
    db = input("Input database: ")

    try:
        os.chdir(db)
    except FileNotFoundError:
        print("No such database")
        return

    table = ""
    table2 = ""
    i = 0

    for line in os.listdir():
        if line[0] == "s":
            table = open(line, "a")
            table2 = open(line, "rt")
            i = int(line[(line.find("_") + 1):line.find(".")])
            break

    if name in table2.read():
        print(f"Student '{name}' already is")
    else:
        table.write(f"{i}-{name}\n")
        os.rename(f"students_{i}.txt", f"students_{i + 1}.txt")

    table.close()
    table2.close()
    os.chdir("..")


def addVariant():
    name = input("Input variant's name: ")
    db = input("Input database: ")

    try:
        os.chdir(db)
    except FileNotFoundError:
        print("No such database")
        return

    table = ""
    table2 = ""
    i = 0

    for line in os.listdir():
        if line[0] == "v":
            table = open(line, "a")
            table2 = open(line, "rt")
            i = int(line[(line.find("_") + 1):line.find(".")])
            break

    if name in table2.read():
        print(f"Variant '{name}' already in database")
    else:
        table.write(f"{i}-{name}\n")
        os.rename(f"variants_{i}.txt", f"variants_{i + 1}.txt")

    table2.close()
    table.close()
    os.chdir("..")


def addStudentsFromFile():
    filename = input("Input path to file with students name: ")
    base = input("Input name of database: ")
    try:
        students = open(filename, "rt")
    except FileNotFoundError:
        print(f"No such file: '{filename}'")
        return

    try:
        os.chdir(base)
    except FileNotFoundError:
        print(f"No such database: '{base}'")
        return

    table = ""
    table2 = ""
    i = 0

    for line in os.listdir():
        if line[0] == "s":
            table = open(line, "a")
            table2 = open(line, "rt")
            i = int(line[(line.find("_") + 1):line.find(".")])
            break

    sv = i
    lns = table2.read()

    for line in students.readlines():
        if line != "\n":
            if line in lns:
                print(f"Student '{line[:len(line)-1]}' already in database")
            else:
                table.write(f"{i}-{line}")
                i += 1

    os.rename(f"students_{sv}.txt", f"students_{i}.txt")

    os.chdir("..")
    students.close()
    table.close()
    table2.close()


def addVariantsFromFile():
    dirname = input("Input path to directory with variants: ")
    base = input("Input name of database: ")
    try:
        variants = os.listdir(dirname)
    except FileNotFoundError:
        print(f"No such directory: '{dirname}'")
        return
    except NotADirectoryError:
        print(f"Not a directory: '{dirname}'")
        return

    try:
        os.chdir(base)
    except FileNotFoundError:
        print(f"No such database: '{base}'")
        return

    i = 0
    table = ""
    table2 = ""

    for line in os.listdir():
        if line[0] == "v":
            table = open(line, "a")
            table2 = open(line, "rt")
            i = int(line[(line.find("_") + 1):line.find(".")])
            break

    sv = i
    lns = table2.read()

    for line in variants:
        if line in lns:
            print(f"Variant '{line[:len(line)-1]}' already in database")
        else:
            table.write(f"{i}-{line}\n")
            i += 1

    os.rename(f"variants_{sv}.txt", f"variants_{i}.txt")

    table2.close()
    os.chdir("..")
    table.close()

