import os
import platform
import socket
import shutil
import time

# # gets the computer name
# findComputerName = input("Type 'Computer Name' to locate this computers name, DON'T MISSPELL.")
# if findComputerName == 'Computer Name':
#     computerName = socket.gethostname()
#     print(computerName)
#     print("Nice job here is your computers name.")
#     time.sleep(0)
# else:
#     print("Learn to type.")


# # gets the OS
# getTheOS = input("Type 'Get the OS' to locate this computers operating system, DON'T MISSPELL.")
# if getTheOS == 'Get the OS':
#     osName = platform.system()
#     print(osName)
#     print("Nice job here is your computers operating system.")
#     time.sleep(0)
# else:
#     print("Learn to type.")



# # gets the version
# version = platform.release()
# print(version)
# getTheVersion = input("Type 'Get the Version' to locate this computers windows version, DON'T MISSPELL.")
# if getTheVersion == 'Get the Version':
#     version = platform.release()
#     print(version)
#     print("Nice job here is your computers current windows version.")
#     time.sleep(0)
# else:
#     print("Learn to type.")




# creates a file
createFile = input("Type 'Create Gamefile.txt' to create a file in this folder, DON'T MISSPELL.")
if createFile == "Create Gamefile.txt":
    open("Gamefile.txt", "a")
    print("Nice job. If you look in your folders you will see a document that says Gamefile.txt")
    time.sleep(0)
else:
    print("Learn to type.")




#  copy's file
copyFile = input("Type in 'Copy File' to copy this file in the same folder, DON'T MISSPELL.")
if copyFile == "Copy File":
    os.system("copy Gamefile.txt Gamefile2.txt")
    print("Awesome, you have created a copy of this file in your current folder. Go take a look.")
    time.sleep(0)
else:
    print("Learn to type.")



# move the file to docs folder
moveFile = input("Type 'Move File' and you file will be moved to your documents folder, DON'T MISSPELL.")
if moveFile == "Move File":
    shutil.move('/Users/DFT/PycharmProjects/pythonProject/venv/Game/Gamefile.txt', '/Users/DFT/Documents')
    print("If you look in your documents folder you should see your file. Cool right?")
    time.sleep(0)
else:
    print("Learn to type.")



# input for inputting Hello World in the file and displaying it
wordsInFile = input("Type in 'Hello Word', DON'T MISSPELL.")
if wordsInFile == "Hello World":
    f = open("Gamefile.txt", "a")
    f.write("Hello World")
    f = open("Gamefile.txt", "r")
    time.sleep(0)
    print(f.read())
    print("Now you should see what you wrote in the file.")
    time.sleep(0)



# # remove the files
removeFiles = input("To remove the files you just made, type 'Remove', DON'T MISSPELL.")
if removeFiles == "Remove":
    os.remove("/Users/DFT/Documents/Gamefile.txt")
    os.remove("Gamefile2.txt")


