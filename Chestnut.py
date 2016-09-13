ValidInput=False
while ValidInput==False:
    try:
        filename = input(" Please enter the path and name of the *.txt file: ")
        f = open(filename, "r")
        print(f.read(1))
        print(f.read())
        f.close()

    except FileExistsError:
        print("Sorry File Does Not Exist")
    except PermissionError:
        print(" Sorry You do Not have Permisison to Access the File")
    except FileNotFoundError:
        print(" Sorry file does not exist")

    #f = open("test.txt", "r")
    #myList = []
    #for line in f:
        #myList.append(line)
    #print(myList)
 print("Hi Morris")
