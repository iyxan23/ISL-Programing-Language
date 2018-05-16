import os
import platform

def startcompile(cmand, variabelstr, variabelnum, hist):
    cmand = cmand.strip()
    hist.append(cmand)
    
    # vv All The command is here! vv

    command = cmand.split()
    if command == []:
        console()
    if command[0] == "write":
        nomor1 = 0
        nomor2 = 0
        if command[1] in variabelstr:
            print(variabelstr[command[1]])
        elif command[1] in variabelnum:
            print(variabelnum[command[1]])
        elif command[1] == "math":
            try:
                nomor1 = int(command[2])
                nomor2 = int(command[4])
            except:
                command.remove("write")
                if command[1] in variabelnum:
                    nomor1 = variabelnum[command[1]]
                    nomor2 = int(command[4])
                if command[3] in variabelnum:
                    nomor1 = variabelnum[command[3]]
                    nomor1 = int(command[2])
                if command[1] not in variabelnum or command[3] not in variabelnum:
                    if command[2] == "+":
                        hasil = nomor1 + nomor2
                        print(hasil)
                    elif command[2] == "-":
                        hasil = nomor1 - nomor2
                        print(hasil)
                    elif command[2] == "*":
                        hasil = nomor1 * nomor2
                        print(hasil)
                    elif command[2] == "/":
                        hasil = nomor1 / nomor2
                        print(hasil)
                else:
                    print("Please input a number")
            else:
                if command[3] == "+":
                    hasil = nomor1 + nomor2
                    print(hasil)
                elif command[3] == "-":
                    hasil = nomor1 - nomor2
                    print(hasil)
                elif command[3] == "*":
                    hasil = nomor1 * nomor2
                    print(hasil)
                elif command[3] == "/":
                    hasil = nomor1 / nomor2
                    print(hasil)
                else:
                    print("Something Went Wrong..")
        else:
            text = cmand.replace("write", "", 1)
            text = text.replace("`", "")
            text = text.strip()
            print(text)
    elif command[0] == "clear":
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
    elif command[0] == "varstr":
        try:
            frmat = "varstr" + " " + command[1]
        except IndexError:
            print("You are not writing the variable name")
        else:
            if command[2] == "=":
                cmandd = cmand.replace("varstr", "")
                cmandd = cmandd.replace("=", "")
                cmandd = cmandd.replace(command[1], "")
                cmandd = cmandd.strip()
                print("Creating Variable named \""+command[1]+"\"....")
                variabelstr["$"+command[1]] = cmandd
                print("Succes! ")
            else:
                print("Something Went Wrong...")
    elif command[0] == "varnum":
        try:
            num = int(command[3])
        except ValueError:
            print("Please enter an a number")
        else:
            if command[2] == "=":
                print("Creating Variable named \""+command[1]+"\"....")
                variabelnum["$"+command[1]] = num
                print("Succes! ")
            else:
                print("Something Went Wrong...")
    elif command[0] == "math":
        try:
            nomor1 = int(command[1])
            nomor2 = int(command[3])
        except:
            if command[1] in variabelnum:
                nomor1 = variabelnum[command[1]]
            if command[3] in variabelnum:
                nomor2 = variabelnum[command[3]]
            if command[1] in variabelnum or command[3]:
                if command[2] == "+":
                    hasil = nomor1 + nomor2
                    print(hasil)
                elif command[2] == "-":
                    hasil = nomor1 - nomor2
                    print(hasil)
                elif command[2] == "*":
                    hasil = nomor1 * nomor2
                    print(hasil)
                elif command[2] == "/":
                    hasil = nomor1 / nomor2
                    print(hasil)
                else:
                    print("Something Went Wrong..")
            else:
                print("Please input a number")
        else:
            if command[2] == "+":
                hasil = nomor1 + nomor2
                print(hasil)
            elif command[2] == "-":
                hasil = nomor1 - nomor2
                print(hasil)
            elif command[2] == "*":
                hasil = nomor1 * nomor2
                print(hasil)
            elif command[2] == "/":
                hasil = nomor1 / nomor2
                print(hasil)
            else:
                print("Something Went Wrong..")
    elif command[0] == "debug_var":
        print(variabelstr)
        print(variabelnum)
    elif command[0] == "history":
        try:
            if command[1] == "clear":
                hist = []
                print("Succes")
        except IndexError:
            for i in hist:
                print("==================")
                print(i)
            print("==================")
    elif command[0] == "inpt":
        if command[1] == "=":
            try:
                test = command[2]
            except IndexError:
                print("Please input the variable")
            else:
                variabelstr[command[2]] = input()
        else:
            test = input()
    elif command[0] == "quit":
        quit()
    elif command[0] == "color":
        try:
            test = command[1]
        except IndexError:
            print("Please type the color name")
        else:
            if platform.system() == "Windows":
                if command[1] == "red":
                    os.system("color 04")
                elif command[1] == "blue":
                    os.system("color 01")
                elif command[1] == "green":
                    os.system("color 02")
                elif command[1] == "aqua":
                    os.system("color 03")
                elif command[1] == "purple":
                    os.system("color 05")
                elif command[1] == "yellow":
                    os.system("color 06")
                elif command[1] == "white":
                    os.system("color 07")
                elif command[1] == "gray":
                    os.system("color 08")
                elif command[1] == "lblue":
                    os.system("color 09")
                elif command[1] == "lgreen":
                    os.system("color 0a")
                elif command[1] == "laqua":
                    os.system("color 0b")
                elif command[1] == "lred":
                    os.system("color 0c")
                elif command[1] == "lpurple":
                    os.system("color 0d")
                elif command[1] == "lyellow":
                    os.system("color 0e")
                elif command[1] == "bwhite":
                    os.system("color 0f")
                else:
                    print("There is no color named", command[1])
            else:
                print("This Feature only work in Windows.")
            
    else:
        print("There is no command named \"" + command[0] + "\".") 
    print("\n")


def console():
    variabstr = {}
    variabnum = {}
    h = []
    l = True
    while l:
        variabstr["!OWNER!"] = "Ihsan"
        variabstr["!COPYRIGHT!"] = "(c) Copyright KomixApix Software"
        variabstr["!VERSI!"] = 1.0
        variabstr["!OS-NAME!"] = platform.system()
        command = input("[ISL-Console@"+platform.system()+"]#> ")
        if command == "stop":
            l = False
            break
        else:
            startcompile(command, variabstr, variabnum, h)
    print("ISL-Console is Stopped")
    input("Press enter to exit.. ")


def main():
    print("====================================>")
    print("ISL Programing Language v 1.0")
    print("Running on", platform.system())
    print("Made By Ihsan (c) KomixApix Software")
    print("====================================>")
    print("\n")
    console()

if __name__ == "__main__":
    main()
