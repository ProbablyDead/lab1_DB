import os


def addStudent(name, db):
    os.chdir(f"DataBases/{db}")

    table = ""
    table2 = ""
    i = 0

    for line in os.listdir():
        if line[0] == "s":
            table = open(line, "a")
            table2 = open(line, "rt")
            i = int(line[(line.find("_") + 1):line.find(".")])
            break

    num = i
    text = table2.read()

    if str(num) in text:
        while str(num) in text:
            num += 1

    if name in text:
        table.close()
        table2.close()
        os.chdir("..")
        os.chdir("..")
        return "1"
    else:
        table.write(f"{num}-{name}\n")
        os.rename(f"students_{i}.txt", f"students_{i + 1}.txt")

    table.close()
    table2.close()
    os.chdir("..")
    os.chdir("..")


def addVariant(name, db):
    os.chdir(f"DataBases/{db}")

    table = ""
    table2 = ""
    i = 0

    for line in os.listdir():
        if line[0] == "v":
            table = open(line, "a")
            table2 = open(line, "rt")
            i = int(line[(line.find("_") + 1):line.find(".")])
            break

    num = i
    text = table2.read()

    if str(num) in text:
        while str(num) in text:
            num += 1


    if name in text:
        table2.close()
        table.close()
        os.chdir("..")
        os.chdir("..")
        return "1"
    else:
        table.write(f"{num}-{name}\n")
        os.rename(f"variants_{i}.txt", f"variants_{i + 1}.txt")

    table2.close()
    table.close()
    os.chdir("..")
    os.chdir("..")


def addStudentsFromFile(filename, base):
    try:
        students = open(filename, "rt")
    except FileNotFoundError:
        return "1"

    os.chdir(f"DataBases/{base}")

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
                pass
            else:
                num = i
                if str(num) in lns:
                    while str(num) in lns:
                        num += 1
                table.write(f"{num}-{line}")
                i += 1

    os.rename(f"students_{sv}.txt", f"students_{i}.txt")

    os.chdir("..")
    os.chdir("..")
    students.close()
    table.close()
    table2.close()


def addVariantsFromDir(dirname, base):
    try:
        variants = os.listdir(dirname)
    except FileNotFoundError:
        return "1"
    except NotADirectoryError:
        return "1"

    os.chdir(f"DataBases/{base}")


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
            num = i
            if str(num) in lns:
                while str(num) in lns:
                    num += 1
            table.write(f"{num}-{line}\n")
            i += 1
    os.rename(f"variants_{sv}.txt", f"variants_{i}.txt")

    table2.close()
    os.chdir("..")
    os.chdir("..")
    table.close()


def deleteStudent(name, db):
    os.chdir(f"DataBases/{db}")

    table = ""
    i = 0
    filename = ""

    for line in os.listdir():
        if line[0] == "s":
            table = open(line, "rt")
            filename = line
            i = int(line[(line.find("_") + 1):line.find(".")])
            break

    buf = table.readlines()
    g = 0
    f = 0
    for line in buf:
        if name in line:
            buf.pop(g)
            f = 1
            break
        g += 1
    table.close()

    if f == 0:
        os.chdir("..")
        os.chdir("..")
        return "1"

    table = open(filename, "wt")

    table.writelines(buf)
    table.close()

    os.rename(filename, f"students_{i-1}.txt")
    os.chdir("..")
    os.chdir("..")


def deleteVariant(name, db):
    os.chdir(f"DataBases/{db}")

    table = ""
    i = 0
    filename = ""

    for line in os.listdir():
        if line[0] == "v":
            table = open(line, "rt")
            filename = line
            i = int(line[(line.find("_") + 1):line.find(".")])
            break

    buf = table.readlines()
    g = 0
    f = 0
    for line in buf:
        if name in line:
            buf.pop(g)
            f = 1
            break
        g += 1
    table.close()

    if f == 0:
        os.chdir("..")
        os.chdir("..")
        return "1"

    table = open(filename, "wt")

    table.writelines(buf)
    table.close()

    os.rename(filename, f"variants_{i - 1}.txt")
    os.chdir("..")
    os.chdir("..")


def changeStudent(name1, name2, base):
    os.chdir(f"DataBases/{base}")

    table = ""
    filename = ""

    for line in os.listdir():
        if line[0] == "s":
            table = open(line, "rt")
            filename = line
            break

    ttt = table.read()

    if ttt.find(name1) == -1:
        table.close()
        os.chdir("..")
        os.chdir("..")
        return "1"

    if ttt.find(name2) != -1:
        table.close()
        os.chdir("..")
        os.chdir("..")
        return "2"

    buf = ttt.replace(name1, name2, 1)
    table.close()

    table = open(filename, "wt")
    table.write(buf)

    table.close()
    os.chdir("..")
    os.chdir("..")


def changeVariant(name1, name2, base):
    os.chdir(f"DataBases/{base}")

    table = ""
    filename = ""

    for line in os.listdir():
        if line[0] == "v":
            table = open(line, "rt")
            filename = line
            break

    ttt = table.read()

    if ttt.find(name1) == -1:
        table.close()
        os.chdir("..")
        os.chdir("..")
        return "1"

    if ttt.find(name2) != -1:
        table.close()
        os.chdir("..")
        os.chdir("..")
        return "2"

    buf = ttt.replace(name1, name2, 1)
    table.close()

    table = open(filename, "wt")
    table.write(buf)

    table.close()
    os.chdir("..")
    os.chdir("..")


def showStudent(ide, base):
    os.chdir(f"DataBases/{base}")

    table = ""

    for line in os.listdir():
        if line[0] == "s":
            table = open(line, "rt")
            break

    buf = table.readlines()
    table.close()
    f = 0
    for line in buf:
        if ide in line:
            os.chdir("..")
            os.chdir("..")
            return line[(line.find("-")+1):-1]

    if f == 0:
        os.chdir("..")
        os.chdir("..")
        return "!"

    os.chdir("..")
    os.chdir("..")


def showVariant(ide, base):
    os.chdir(f"DataBases/{base}")

    table = ""

    for line in os.listdir():
        if line[0] == "v":
            table = open(line, "rt")
            break

    buf = table.readlines()
    table.close()
    f = 0
    for line in buf:
        if ide in line:
            os.chdir("..")
            os.chdir("..")
            return line[(line.find("-") + 1):-1]

    if f == 0:
        os.chdir("..")
        os.chdir("..")
        return "!"

    os.chdir("..")
    os.chdir("..")
