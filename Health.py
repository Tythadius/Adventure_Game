yourHealth = 100
FrodoHealth = 100
Attack = 20


def attackOnYou():
    global yourHealth
    global FrodoHealth
    yourHealth = yourHealth - Attack
    print("You get attacked")
    print("you have", yourHealth, "left")
    if yourHealth <= 0:
        # time.sleep(b)
        print("Game over. Please restart the game and make better life choices.")


def attackOnFrodo():
    global yourHealth
    global FrodoHealth
    FrodoHealth = FrodoHealth - Attack
    print("You attack")
    print("Frodo has", FrodoHealth, "left")


firstAttack = input("Do you want to attack? (Y/N): ")
if firstAttack == "Y":
    attackOnFrodo()


elif firstAttack == "N":
    attackOnYou()

secAttack = input("Do you want to attack? (Y/N): ")
if secAttack == "Y":
    attackOnFrodo()


elif secAttack == "N":
    attackOnYou()

thirdAttack = input("Do you want to attack? (Y/N): ")
if thirdAttack == "Y":
    attackOnFrodo()


elif thirdAttack == "N":
    attackOnYou()

fourthAttack = input("Do you want to attack? (Y/N): ")
if fourthAttack == "Y":
    attackOnFrodo()


elif fourthAttack == "N":
    attackOnYou()

fifthAttack = input("Do you want to attack? (Y/N): ")
if fifthAttack == "Y":
    attackOnFrodo()


elif fifthAttack == "N":
    attackOnYou()
