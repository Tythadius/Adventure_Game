# health [100]
# import time




class health:
    def __init__(self):
        self.health = 100
    def attack(self):
        self.attack = self.health - 20
        if self.health <= 0:
            # time.sleep(c)
            print("Your health is gone.")
            # time.sleep(c)
            print("Game over. This part will now restart...")
            intro()

# if attack == "y" or attack == "Y":
#     attack()


    # attack()
    # print(health)




# attack()
# print(health)
# def main_game():
#     game_status = GameStatus()
#     #...
#     # when player gets hurt
#     game_status.reduce_health()
#     # ...

# def game_over():
#     print "game over, sorry"
#     os._exit(1)