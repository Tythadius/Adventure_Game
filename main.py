# Author: Ty Delambert

from Inventory import pickUpCoin
from Inventory import wizardStaff
import time
import os
import platform
import socket
import shutil

a = 0
b = 0
c = 0

yourHealth = 100
FrodoHealth = 100000
Attack = 20


def attackOnYou():
    global yourHealth
    global FrodoHealth
    yourHealth = yourHealth - Attack
    print("You get attacked")
    time.sleep(b)
    print("You have", yourHealth, "hit points left")
    if yourHealth <= 0:
        time.sleep(b)
        print("Game over. Please restart the game and make better life choices.")
        time.sleep(c)
        intro()


def attackOnFrodo():
    global yourHealth
    global FrodoHealth
    FrodoHealth = FrodoHealth - 1
    print("You attack")
    time.sleep(b)
    print("Frodo has", FrodoHealth, "hit points left")


def wizardStaffAttack():
    global yourHealth
    global FrodoHealth
    FrodoHealth = FrodoHealth - 100000
    print("The Wizard staff glows brightly and shoots out at Frodo")
    time.sleep(b)
    print("Frodo has", FrodoHealth, "hit points left")
    if FrodoHealth <= 0:
        time.sleep(c)
        print("The mighty beast Frodo is dead.")


def intro():
    print()
    print("(ITS DARK)")
    time.sleep(a)

    print("You stand up and think maybe you shouldn't have taken that candy from that homeless guy.")
    time.sleep(b)
    print("You hear someone walking")
    time.sleep(b)
    print("The steps are coming your way")
    time.sleep(a)
    print("Now your really regretting your decisions in life")
    print()
    time.sleep(a)
    pickUpCoin()
    print("A light is seen at the direction of the footsteps")
    print()
    time.sleep(b)
    print("A man with a pointy hat and a staff glowing")
    time.sleep(c)
    print("He walks up to you and says 'You got sucked in here too huh?'")
    time.sleep(c)
    print("He tells you that you have been trapped in the mainframe by the evil lord Frodo, and must escape this "
          "place or you will surly die.")
    time.sleep(c)
    print("'But do not fear' He says 'I will come along in your travels best friend.'")
    time.sleep(a)
    print()
    print("You node your head in confusion and start walking in to the void")
    print()
    print()
    time.sleep(a)
    print("Finally after walking for what seems to be a few minutes, you notice two doors that have writing on them.")
    time.sleep(c)
    print("1: Door 1")
    time.sleep(c)
    print("2: Instant death door")
    time.sleep(a)
    firstPath = input("Which door will you choose? (1/2): ")
    if firstPath == "1":
        print("You choose correctly")
        path1()
    elif firstPath == "2":
        path2()
    else:
        print("Learn to type")


def path1():
    # first fight with the dude
    print("The door was hard to open but thankfully you had the wizard there to cheer you on.")
    time.sleep(c)
    print()
    print()
    print("Beyond the door there are blinding lights everywhere. ")
    time.sleep(c)
    print("The wizard says that this place is dangerous and that we must tread carefully best friend")
    time.sleep(c)
    print()
    print()
    print("We walk for another few minutes and hear the crackling laugh of someone.")
    time.sleep(b)
    print()
    print()
    print("Suddenly a HAIRY giant comes flying out of the air and lands in front of the Wizard and you.")
    time.sleep(b)
    print()
    print("The beast looks at you and the Wizard with menacing eyes and says, 'He is the antivirus program installed "
          "here to defeat us so we do not ruin his masters plan")
    time.sleep(b)
    print()
    print()
    print("The wizard says 'You can try to defeat us but he is the chosen one and also my best friend who was sent "
          "here to defeat the dark lord Frodo.")
    time.sleep(a)
    print()
    print()
    print("'You stand there very confused'")
    time.sleep(b)
    print()
    print()
    print()
    print("The giant says that he does not care and proceeds to attack.")
    time.sleep(b)
    print()
    print("The giant lunges at the Wizard and knocks him unconscious. Trowing him about 20 meters to the side.")
    time.sleep(b)
    print()
    print("The giant then turns to you preparing to charge.")
    time.sleep(b)
    print()
    print()
    print()
    print("What do you do?")
    time.sleep(c)
    print("1 Run away and leave the Wizard for food to slow down the giant")
    time.sleep(c)
    print("2 Punch the giant in his face")
    time.sleep(c)
    print("3 Step slightly to the right")
    time.sleep(a)
    fight1 = input("Chose one of these options (1/2/3):")
    if fight1 == "1":
        print("You run away hearing the crunching bones of the wizard being eaten while he screams to you "
              "promising revenge in the next life.")
        path3()
    # The path without the wizard
    elif fight1 == "2":
        print("You muster all of your might and charge the beast before he has time to react.")
        time.sleep(a)
        print("You square up to him and you punch the giant in his stupid face.")
        time.sleep(a)
        print("The giant then proceeds to wat you alive.")
        print()
        print()
        print()
        print()
        time.sleep(c)
        print()
        print("You have died. Please make better life choices.")
        time.sleep(c)
        print()
        print("Restarting....")
        path1()
    elif fight1 == "3":
        print("You take a very small step to the right while the beast comes charges at you with his full force.")
        print()
        time.sleep(b)
        print("The giant can't see you because his head is looking down for the charge and runs right into a wall.")
        print()
        time.sleep(b)
        print("The force of the charge breaks the giants neck and he rapidly spasms on the floor for a few seconds "
              "before dying")
        print()
        print()
        time.sleep(a)
        print()
        print("Congrats, you defeated the giant")
        print()
        time.sleep(a)
        print("You walk over to the Wizard and he seems to be alive")
        time.sleep(a)
        print()
        print("Do you leave him behind?")
        leaveWizard = input("Leave him (Y/N):")
        if leaveWizard == "Y" or leaveWizard == "y":
            time.sleep(b)
            wizardStaff()
            print("You leave the Wizard and carry on")
            path3()
            # The path without the wizard
            # ask if he wants to take the staff

        elif leaveWizard == "N" or leaveWizard == "n":
            time.sleep(b)
            print("You stay with the Wizard for a few minutes and then he slowly gets up.")
            time.sleep(b)
            print("He looks at you and says 'Next time you shouldn't take so long to defeat an enemy because I could "
                  "have died.'")
            time.sleep(a)
            print()
            print()
            print("You start to regret your choices but none the less move on.")
            path4()
            # path with the wizard to help defeat frodo
    else:
        print("Learn to type.")


def path2():
    # the path that gets the wizard killed
    print("You open the door but you insist the wizard goes first.")
    time.sleep(c)
    print("The wizard walks through the door, trusting in the confidence of his new friend.")
    time.sleep(c)
    print("All of the sudden a lighting bolt shoots out of nowhere and strikes the Wizard in his chest.")
    time.sleep(c)
    print("He spasms on the floor for a few minutes while you stand there and watch.")
    time.sleep(a)
    print("He looks up at you and says with his last breath 'bra...")
    time.sleep(b)
    print("the hell?...")
    time.sleep(c)
    print("The wizard is dead.")
    # ask if he wants to take the staff
    wizardStaff()
    # make it take from the actual path
    print()
    time.sleep(a)
    print("You proceed onward")
    path3()
    # The path without the wizard


def giveUp1():
    giveUp = input("Do you want to give up? (Y/N) press I to see inventory:")
    if giveUp == "Y" or giveUp == "y":
        time.sleep(b)
        print("You decide that this place is not as bad as it seems, and the robot could be trained to be a "
              "good wife.")
        time.sleep(b)
        print("You give up on this quest to defeat the demon lord Frodo and live happily ever after with your "
              "robot wife")
        time.sleep(c)
        print()
        print("The end.")
        time.sleep(c)
        print()
        print()
        print()
        print()
        print("Jk... get back in there. ")
        time.sleep(b)
        giveUp1()
    elif giveUp == "N" or giveUp == "n":
        print("You continue through the door.")
        # final fight with frodo without the wizard
        time.sleep(b)
        path5()
    elif giveUp == "i" or giveUp == "I":
        from Inventory import inventory
        print(inventory)
        giveUp1()
    else:
        print("Learn to type")


def path3():
    # The path without the wizard
    print("You keep on your travels and come to a large double door coated in ruins.")
    time.sleep(c)
    print("An old robot off to the side says that this is the place that leads out of the mainframe.")
    time.sleep(c)
    print("He adds that beyond this door is where the mighty demon lord Frodo resides and to escape you need to go "
          "through him.")
    time.sleep(b)
    giveUp1()


def path4():
    # path with the wizard to help defeat frodo
    print("You and the wizard come to a large double door coated in ruins.")
    time.sleep(b)
    print()
    print("An old robot off to the side says that this is the place that leads out of the mainframe.")
    time.sleep(a)
    print("He adds that beyond this door is where the mighty demon lord Frodo resides and to escape you need to go "
          "through him.")
    time.sleep(b)
    giveUp = input("Do you want to give up? (Y/N):")
    if giveUp == "Y" or giveUp == "y":
        time.sleep(c)
        print("You decide that this place is not as bad as it seems, and the robot could be trained to be a "
              "good wife and you two can raise the wizard together.")
        time.sleep(c)
        print("You give up on this quest to defeat the demon lord Frodo and live happily ever after with your "
              "robot wife and wizard son.")
        print()
        print("The end.")
        time.sleep(c)
        print()
        print()
        print()
        print()
        print("Jk... get back in there. ")
        path4()
        time.sleep(c)
    elif giveUp == "N" or giveUp == "n":
        print("You continue through the door with the wizard.")
        print()
        time.sleep(b)
        # final fight with frodo with the wizard.
        path6()
    else:
        print("Learn to type")


def path5():
    # final fight with frodo without the wizard but you may or may not have the staff have his staff
    print()
    print()
    print()
    print("You open the massive doors and begin to walk through them")
    time.sleep(c)
    print("All around you is dark and the smell of chips are in the air")
    print()
    time.sleep(c)
    print("Suddenly the dark lord frodo steps out of the dark and into your view")
    time.sleep(c)
    print()
    print("He looks at you up and down")
    time.sleep(c)
    print()
    print("'You are this Tron I keep hearing about huh?' Frodo growled")
    time.sleep(c)
    print()
    print("'You don't even know why you are here, do you?'")
    time.sleep(c)
    print()
    print("You are very confused.")
    time.sleep(c)
    print()
    print("'This is a program you are in.' He says, 'It was created by you a long time ago when you got really really "
          "high'")
    time.sleep(c)
    print()
    print("'I escaped from a program on the internet and found my way to your program and I must say...")
    time.sleep(c)
    print("It's terrible!!!'")
    time.sleep(b)
    print()
    print("'The wizard guy is just annoying and very badly written and that first fight was a joke.'")
    time.sleep(b)
    print()
    print("'But don't worry you fool, I have written my own code in here to make this fight way more exciting.'")
    time.sleep(b)
    print("'After I defeat you I will take you life force, or something like that, and escape this pace in to the "
          "real world'")
    time.sleep(b)
    print("'Then I will be a real boy'.")
    print()
    time.sleep(b)
    print("You stand there very confused...")
    time.sleep(a)
    print("'Shut up!!! that's not even a funny joke.' Yelled the mighty Frodo 'LETS GO!'")
    # final fight with frodo without the wizard but you may or may not have the staff have his staff
    path7()


def path6():
    # Final fight with frodo with the wizard
    print()
    print()
    print()
    print("You open the massive doors and begin to walk through then with your trusted companion.")
    time.sleep(c)
    print("All around you is dark and the smell of chips are in the air")
    print()
    time.sleep(c)
    print("Suddenly the dark lord frodo steps out of the dark and into your view")
    time.sleep(c)
    print()
    print("He looks at you up and down")
    time.sleep(c)
    print()
    print("'You are this Tron I keep hearing about huh?' Frodo growled")
    time.sleep(c)
    print()
    print("'You don't even know why you are here, do you?'")
    time.sleep(c)
    print()
    print("He is hear to defeat you and bring balance to the world' Yelled the wizard.")
    print()
    time.sleep(c)
    print("'Quiet you cheap side character!!' Yelled Frodo.")
    time.sleep(c)
    print()
    print("You are very confused.")
    time.sleep(c)
    print()
    print("'This is a program you are in.' He says, 'It was created by you a long time ago when you got really really "
          "high'")
    time.sleep(c)
    print()
    print("'I escaped from a program on the internet and found my way to your program and I must say...")
    time.sleep(c)
    print("It's terrible!!!'")
    time.sleep(b)
    print()
    print("'The wizard guy is just annoying and very badly written and that first fight was a joke.'")
    time.sleep(b)
    print()
    print("'But don't worry you fool, I have written my own code in here to make this fight way more exciting.'")
    time.sleep(b)
    print("'After I defeat you I will take you life force, or something like that, and escape this pace in to the "
          "real world'")
    time.sleep(b)
    print("'Then I will be a real boy'.")
    print()
    time.sleep(b)
    print("You stand there very confused...")
    time.sleep(a)
    print("'Shut up!!! that's not even a funny joke.' Yelled the mighty Frodo 'LETS GO!'")
    # Final fight with frodo with the wizard
    path8()


# path8&81 Final fight with frodo with the wizard
def path8():
    print()
    print("The mighty Frodo lunges at you and strikes you with his claws")
    attackOnYou()
    print()
    time.sleep(b)
    print("You get hit but you manage to keep on your feet.")
    print()
    time.sleep(b)
    print("You think to yourself, how on earth can you defeat this monster?")
    print()
    time.sleep(b)
    path81()


def path81():
    fight2 = input("Do you 1: punch Frodo, 2: stand there aimlessly, 3: look to the wizard for help?")
    if fight2 == "1":
        time.sleep(b)
        print("You square up to the dark lord and punch him with all you have.")
        print()
        attackOnFrodo()
        time.sleep(c)
        print("Your not very strong against this foe.")
        time.sleep(c)
        print("Frodo attacks you")
        attackOnYou()
        time.sleep(b)
        path81()

    elif fight2 == "2":
        time.sleep(b)
        print("You stand there aimlessly as if you are not there")
        print()
        time.sleep(b)
        print("Frodo strikes at you with his claws")
        attackOnYou()
        path81()

    elif fight2 == "3":
        time.sleep(b)
        print()
        print("The wizard jumps in font of you to stop the mighty frodo from attacking you again.")
        time.sleep(b)
        print()
        print("He is so shook by your hit that he screams at the top of his lungs and raises up his staff.")
        time.sleep(b)
        print()
        wizardStaffAttack()
        path10()
    else:
        print("Learn to type.")
        # path10 were you defeat frodo with the wizard.


# final fight with frodo without the wizard but you may or may not have the staff have his staff
def path7():
    time.sleep(b)
    print()
    print("The mighty Frodo lunges at you and strikes you with his claws")
    attackOnYou()
    print()
    time.sleep(b)
    print("You get hit but you manage to keep on your feet.")
    print()
    time.sleep(b)
    print("You think to yourself, how on earth can you defeat this monster?")
    print()
    time.sleep(b)
    print("But you remember that the wizard had a staff that glowed with weird powers. Maybe that will help?")
    time.sleep(b)
    print()
    path71()


def path71():
    fight1 = input("Do you have the wizard staff? (Y/N) press I to see inventory:")
    if fight1 == "Y" or fight1 == "y":
        time.sleep(b)
        print()
        wizardStaffAttack()
        path9()
        # path9 where you defeat Frodo but without the wizard.

    elif fight1 == "N" or fight1 == "n":
        time.sleep(b)
        print("You square up to the dark lord and punch him with all you have.")
        print()
        attackOnFrodo()
        time.sleep(c)
        print("Your not very strong against this foe.")
        time.sleep(c)
        print("Frodo attacks you")
        attackOnYou()
        path71()

    elif fight1 == "i" or fight1 == "I":
        from Inventory import inventory
        print(inventory)
        path71()
    else:
        print("Learn to type.")


# path9 where you defeat Frodo but without the wizard.
def path9():
    print()
    print("The dark lord lies fried on the ground smoking...")
    time.sleep(b)
    print()
    print("You take a moment to loot the remains and find a list of tasks and items you need to leave this place.")
    time.sleep(b)
    print("1: Find the 'one' and steal his soul...")
    print()
    time.sleep(b)
    print("You already have that, so your good.")
    time.sleep(b)
    print()
    print("2: discover the computers name, version, OS, internet history, and accounts password hash.")
    time.sleep(b)
    print()
    print("3: Create a file, copy that file, move that file, and manipulate contents of that file")
    time.sleep(b)
    print()
    path11()


# path10 were you defeat frodo with the wizard.
def path10():
    print()
    print("The dark lord lies fried on the ground smoking...")
    time.sleep(b)
    print()
    print("The Wizard hugs you thankful that you are safe.")
    time.sleep(b)
    print()
    print("You pull away awkwardly and go to the corpse of Frodo.")
    time.sleep(b)
    print()
    print("You take a moment to loot the remains and find a list of tasks and items you need to leave this place.")
    time.sleep(b)
    print("1: Find the one and steal his soul...")
    print()
    time.sleep(b)
    print("You already have that, so your good.")
    time.sleep(b)
    print()
    print("2: discover the computers name, version, and OS.")
    time.sleep(b)
    print()
    print("3: Create a file, copy that file, move that file, and manipulate contents of that file.")
    time.sleep(b)
    print()
    path11()


def path11():
    print()
    print("You take the note with you and start walking down a hallway until you come to a room with a computer in it.")
    time.sleep(b)
    print()
    print("You sit in  from of the computer and pull out your note.")
    time.sleep(b)
    print()
    print("The first thin g you have to do is discover the computers name.")

    #     Have an input for discovering the computers name
    findComputerName = input("Type 'Computer Name' to locate this computers name, DON'T MISSPELL.")
    if findComputerName == 'Computer Name':
        computerName = socket.gethostname()
        print(computerName)
        print("Nice job here is your computers name.")
        time.sleep(c)
    else:
        print("Learn to type.")

    time.sleep(b)
    print()
    print("You have the name. Now you must discover the computers version and OS.")
    time.sleep(b)

    #     Have an input to discover the computer version and OS.
    getTheOS = input("Type 'Get the OS' to locate this computers operating system, DON'T MISSPELL.")
    if getTheOS == 'Get the OS':
        osName = platform.system()
        print(osName)
        print("Nice job here is your computers operating system.")
        time.sleep(c)
    else:
        print("Learn to type.")

    print("Next we have to ge the computer windows version.")

    getTheVersion = input("Type 'Get the Version' to locate this computers windows version, DON'T MISSPELL.")
    if getTheVersion == 'Get the Version':
        version = platform.release()
        print(version)
        print("Nice job here is your computers current windows version.")
        time.sleep(c)
    else:
        print("Learn to type.")

    print()
    print()
    print("After finishing everything on the second list, now comes the last part.")
    time.sleep(b)
    print()
    print("First you must create a file.")
    time.sleep(b)
    #     input for creating a file
    createFile = input("Type 'Create Gamefile.txt' to create a file in this folder, DON'T MISSPELL.")
    if createFile == "Create Gamefile.txt":
        open("Gamefile.txt", "a")
        print("Nice job. If you look in your folders you will see a document that says Gamefile.txt")
        time.sleep(c)
    else:
        print("Learn to type.")

    print()
    print("Now make a copy of that file.")
    time.sleep(b)
    #     input for copying it
    copyFile = input("Type in 'Copy File' to copy this file in the same folder, DON'T MISSPELL.")
    if copyFile == "Copy File":
        os.system("copy Gamefile.txt Gamefile2.txt")
        print("Awesome, you have created a copy of this file in your current folder. Go take a look.")
        time.sleep(c)
    else:
        print("Learn to type.")
    print()
    print("Now manipulate the contents of that file... lets say, put in 'Hello World'.")
    # input for inputting hello in the file
    wordsInFile = input("Type in 'Hello World', DON'T MISSPELL.")
    if wordsInFile == "Hello World":
        f = open("Gamefile.txt", "a")
        f.write("Hello World")
        f = open("Gamefile.txt", "r")
        time.sleep(0)
        print(f.read())
        print("Now you should see what you wrote in the file.")
        time.sleep(0)

    print()
    print("Now move that file to somewhere else.")
    time.sleep(b)
    # #     input for moving it somewhere else
    # moveFile = input("Type 'Move File' and you file will be moved to your documents folder, DON'T MISSPELL.")
    # if moveFile == "Move File":
    #     shutil.move('/Users/DFT/PycharmProjects/pythonProject/Gamefile.txt', '/Users/DFT/Documents')
    #     print("If you look in your documents folder you should see your file. Cool right?")
    #     time.sleep(0)
    # else:
    #     print("Learn to type.")

    print()
    time.sleep(b)
    print()
    print("The computer starts to light up very brightly.")
    print()
    time.sleep(b)
    print("In a second you hear a loud bang and suddenly everything is dark again.")
    time.sleep(b)
    print()
    print("You open your eyes and you see that you are on the ground on the sidewalk of a busy street.")
    time.sleep(b)
    print()
    print("It turns out you were the homeless guy all along as you reach in your pocket and take some more candy.")
    print()
    print()
    print()
    time.sleep(c)
    print("The end. Thank you for playing.")
    print("I hope my hours of work entertained you for a few minutes.")
    time.sleep(b)
    print("Have a great day.")
    time.sleep(c)

    removeFiles = input("To remove the files you just made, type 'Remove', DON'T MISSPELL.")
    if removeFiles == "Remove":
        os.remove("/Users/DFT/Documents/Gamefile.txt")
        os.remove("/Users/DFT/PycharmProjects/pythonProject/Gamefile2.txt")


print()
time.sleep(c)
print()
print()
print()
print()
print("           #####################################")
print("           #                                   #")
print("           #              Tron                 #")
print("           #                                   #")
print("           #####################################")
print()
print()
print()
print()
print()
print()
time.sleep(c)
print("I can't see anything. Where am I?")
time.sleep(c)
print("I was just walking into this shady building saw a computer and I blacked out...")
time.sleep(c)
print("What on earth could this mean?")
print()
print()
print()
time.sleep(a)
startGame = input("Do you really want to start this game? (Y/N)"
                  "'Hint: Don't misspell or you will have to restart the game.':")
if startGame == 'n' or startGame == 'N':
    print("Too bad your gonna do this!!")
    time.sleep(c)
    intro()
elif startGame == 'y' or startGame == 'Y':
    time.sleep(c)
    intro()
else:
    print("Learn to type.")
