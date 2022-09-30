import workWithDB
import workWithInfo
import workWithTables
import GUI


def listening():
    while 1:
        try:
            command = input("-> ")
            if command == "1":
                v1 = input("1 - Student\n2 - Variant\n3 - Database\n-> ")
                if v1 == "1":
                    if input("1 - from console (only 1)\n2 - from file\n-> ") == "1":
                        workWithInfo.addStudent()
                    else:
                        workWithInfo.addStudentsFromFile()
                elif v1 == "2":
                    if input("1 - from console (only 1)\n2 - from directory\n-> ") == "1":
                        workWithInfo.addVariant()
                    else:
                        workWithInfo.addVariantsFromDir()
                elif v1 == "3":
                    workWithDB.createDB()
            elif command == "2":
                v2 = input("1 - Student\n2 - Variant\n3 - Database\n-> ")
                if v2 == "1":
                    workWithInfo.deleteStudent()
                elif v2 == "2":
                    workWithInfo.deleteVariant()
                elif v2 == "3":
                    workWithDB.deleteDB()
            elif command == "3":
                if input("1 - Student\n2 - Variant\n-> ") == "1":
                    workWithInfo.changeStudent()
                else:
                    workWithInfo.changeVariant()
            elif command == "4":
                if input("1 - Student\n2 - Variant\n-> ") == "1":
                    workWithInfo.showStudent()
                else:
                    workWithInfo.showVariant()
            elif command == "5":
                if input("1 - Create\n2 - Reset\n-> ") == "1":
                    workWithDB.createBackup()
                else:
                    workWithDB.resetBackup()
            elif command == "6":
                workWithTables.generateTables()
    ###############################
            elif command in ["e", "E"]:
                print("Bye!")
                break
            elif command in ["i", "I"]:
                printInfo()
            elif not command:
                pass
            else:
                print("Wrong command")
        except KeyboardInterrupt:
            print("\nBye!")
            break


def printInfo():
    print("Here the list of commands:" +
          "\n\t1 - add ..." +
          "\n\t2 - delete ..." +
          "\n\t3 - change ... (obj1 -> obj2)" +
          "\n\t4 - show id ..." +
          "\n\t5 - backup ..." +
          "\n\t6 - generate tables ..." +
          "\n\tType \'E\' to exit" +
          "\n\tType \'I\' to get info")


if __name__ == '__main__':
    #printInfo()
    GUI.Home()
    #listening()

