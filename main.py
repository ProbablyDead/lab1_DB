import workWithDB
import workWithInfo


def listening():
    while 1:
        try:
            command = input("-> ")
            if command == "1":
                workWithDB.createDB()
            elif command == "2":
                workWithDB.deleteDB()
            elif command == "3":
                workWithInfo.addStudent()
            elif command == "4":
                workWithInfo.addVariant()
            elif command == "5":
                workWithInfo.addStudentsFromFile()
            elif command == "6":
                workWithInfo.addVariantsFromFile()
    ###############################
            elif command == "e":
                print("Bye!")
                break
            elif command == "i":
                printInfo()
            else:
                print("Wrong command")
        except KeyboardInterrupt:
            print("\nBye!")
            break


def printInfo():
    print("Here the list of commands:" +
          "\n\t1 - add DB" +
          "\n\t2 - delete DB" +
          "\n\t3 - add student" +
          "\n\t4 - add variant" +
          "\n\t5 - add students from file" +
          "\n\t6 - add variants from file" +
          "\n\tType \'e\' to exit" +
          "\n\tType \'i\' to get info")


if __name__ == '__main__':
    printInfo()
    listening()
