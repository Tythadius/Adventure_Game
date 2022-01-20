inventory = []


def addToInventory(item):
    inventory.append(item)


def printInventory():
    print("INVENTORY:")
    print(inventory)


def pickUpCoin():
    global inventory
    pickup = input("You see a worthless coin on the ground. Do you pick it up? (Y/N)? to view your inventory "
                   "click (I).")

    if pickup == "y" or pickup == "Y":
        addToInventory("Worthless coin")
        print("Congrats you got a worthless coin, do you feel better?")
        printInventory()
    elif pickup == "n" or pickup == "N":
        print("You leave the coin and continue forward.")
    elif pickup == "i" or pickup == "I":
        printInventory()
        pickUpCoin()


def wizardStaff():
    global inventory
    # when the wizard dies by a lighting bolt or if you leave him behind, ask if you want his staff.
    pickup = input("You see the wizards staff on the ground. Do you pick it up (Y/N)? to view your items you already "
                   "have click (I)")

    if pickup == "y" or pickup == "Y":
        addToInventory("Staff")
        print("You got a staff.")
        printInventory()
    elif pickup == "n" or pickup == "N":
        print("You leave the staff and continue forward.")
    elif pickup == "i" or pickup == "I":
        printInventory()
        wizardStaff()
