import random
from os import system, name


def return_dice_rows(dice_num):

    # Return dice string components as a list, that will be used in print_dice_rows()
    
    patterns = {
                'top/bot':' ------- ',
                'none':'|       |',
                "one":'|   *   |',
                'two':'| *   * |',
                'one_right':'|     * |',
                'one_left':'| *     |'
                }
    
    dices = {
             1:['top/bot','none','one','none','top/bot'],
             2:['top/bot','none','two','none','top/bot'],
             3:['top/bot','one_left','one','one_right','top/bot'],
             4:['top/bot','two','none','two','top/bot'],
             5:['top/bot','two','one','two','top/bot'],
             6:['top/bot','two','two','two','top/bot']
             }
    

    component_list = []

    for dice in dices[dice_num]:
        component_list.append(patterns[dice])
    
    return component_list

def print_dice_rows(dice_list):

    # Prints the dices in a compact and easy to display row


    # Stores each individial dice components as vertical reprezentation.

    dice_dict = {
                 0 : "",
                 1 : "",
                 2 : "",
                 3 : "",
                 4 : ""
                 }
    
    # For each of the dices, it adds a one component to a separate string

    for dice in dice_list:

        dice_row = return_dice_rows(dice)

        for num in range(0,5):
            dice_dict[num] = dice_dict[num] + dice_row[num] + "  "

    # Prints concatenated individual visual componets in one line

    for num in range(0,5):
        print(dice_dict[num])

    print()

def pick_starting_player():

    # Given that there will be 2 players for now, it will pick a random one to be the first to roll the dice.

    player_num_starting = random.randint(1,2)

    # Return a string indicating which player will be the first to start the game.

    if player_num_starting == 1:
        return "Player 1"
    else:
        return "Player 2"

def roll_all_dices(dice_list):

    dice_index = 0

    for dice in dice_list:
        dice_list[dice_index] = random.randint(1,6)
        dice_index += 1

def roll_choosen_dices(player_pick, dice_list):
    for pick in player_pick:
        dice_list[pick] = random.randint(1,6)


def reroll_choice():

    # Asks a player to pick dices to roll again. Return list of correct choices that are not repeating.


    player_choice = input("Which dices would you like to roll again? (Type a number/s. Separate multiple choices using spaces): ").split(" ")

    player_choice_int = []

    # Creates list of integers from list of strings, sifting out wrong choices.

    for choice in player_choice:
        if not (choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5"):
            pass
        else:                
            player_choice_int.append(int(choice))

    unique_player_choice = []

    # Converts list of integers to a set, removing duplicates, then back to the list.

    for unique in set(player_choice_int):
          unique_player_choice.append(unique-1)
    
    return unique_player_choice

def roll_combination_check(given_list):

    combined_value = 0

    combination = {"" : 0}

    numbers_dict = {
                1 : 0,
                2 : 0,
                3 : 0,
                4 : 0,
                5 : 0,
                6 : 0
                }

    for dice in given_list:
        numbers_dict[dice] += 1
        combined_value += dice

    roll_value_list = []

    for num in range(1,7):
        if numbers_dict[num] == 0:
            pass
        else:
            roll_value_list = roll_value_list + [numbers_dict[num]]

    roll_value_list.sort()

    if roll_value_list == [5]:
        combination = {"Five-of-a-kind" : 8}

    elif roll_value_list == [1,4]:
        combination = {"Four-of-a-kind" : 7}

    elif roll_value_list == [2,3]:
        combination = {"Full House" : 6}

    elif roll_value_list == [1,1,1,1,1] and numbers_dict[6] == 1 and numbers_dict[1] == 0:
        combination = {"Six-high strait" : 5}

    elif roll_value_list == [1,1,1,1,1] and numbers_dict[6] == 0 and numbers_dict[1] == 1:
        combination = {"Five-high strait" : 4}

    elif roll_value_list == [1,1,3]:
        combination = {"Three-of-a-kind" : 3}

    elif roll_value_list == [1,2,2]:
        combination = {"Two pairs" : 2}

    elif roll_value_list == [1,1,1,2]:
        combination = {"One Pair" : 1}

    else:
        pass
    
    print(roll_value_list)
    return [combination,combined_value]

def clear():
    
    #https://www.geeksforgeeks.org/clear-screen-python/

    # Windows
    if name == 'nt':
        _ = system('cls')
 
    # MacOS or Linux
    else:
        _ = system('clear')

def change_name(players_name_dict, player_name_code):

    print(player_name_code + " you can choose your nickname that will be displayed during the game.")

    nickname = input("Your nickname (you can leave it empty if you just want to be called '{}'): ".format(player_name_code))
    players_name_dict[player_name_code] = nickname

    clear()

    if players_name_dict[player_name_code] != "":
        print(player_name_code + " will now be called " + players_name_dict[player_name_code] + ".\n")
    else:
        players_name_dict[player_name_code] = player_name_code
        print(player_name_code + " will remain called " + players_name_dict[player_name_code] + ".\n")

    if player_name_code == "Player 1":
        player_name_code = "Player 2"
    else:
        player_name_code = "Player 1"

    print("Now, " + player_name_code + " you can choose your nickname too.")
    
    nickname = input("Your nickname (you can leave it empty if you just want to be called '{}'): ".format(player_name_code))

    players_name_dict[player_name_code] = nickname

    clear()
    if players_name_dict[player_name_code] != "":
        print(player_name_code + " will now be called " + players_name_dict[player_name_code] + ".\n")
    else:
        players_name_dict[player_name_code] = player_name_code
        print(player_name_code + " will remain called " + players_name_dict[player_name_code] + ".\n")
    

# A string to be placed on top of the dices, to help players choose dices to roll
dice_number_help = "   [1]        [2]        [3]        [4]        [5]   "




#Game logic

while True:

    clear()
    
    print("Welcome to The Dice Poker game! The rules originate from video game The Witcher 2: Assassins of Kings.\n\n\n")

    players_dice_dict = {
                "Player 1" : [0,0,0,0,0],
                "Player 2" : [0,0,0,0,0]
               }
    
    players_name_dict = {
                "Player 1" : "",
                "Player 2" : ""
               }
    
    players_score_dict = {
                "Player 1" : {},
                "Player 2" : {}
               }

    print("Person pressing the Enter key will be the Player 1. The game decide which person will go first.")
    input("Press Enter when you ready!")

    clear()

    current_player = pick_starting_player()
    print(current_player + " will be the first to roll!\n")

    change_name(players_name_dict, current_player)

    input("{} press Enter when you're ready to roll!".format(players_name_dict[current_player]))

    turn = 1

    while turn == 1:

        roll_all_dices(players_dice_dict[current_player])

        clear()

        print(players_name_dict[current_player] + " Dices.")
        print()
        print(dice_number_help)
        print()
        print_dice_rows(players_dice_dict[current_player])

        roll_choosen_dices(reroll_choice(), players_dice_dict[current_player])

        clear()

        print(players_name_dict[current_player] + " Dices.")
        print()
        print_dice_rows(players_dice_dict[current_player])

        if current_player == "Player 1":
            current_player = "Player 2"
        else:
            current_player = "Player 1"

        turn += 1

    while turn == 2:

        print("Now is " + players_name_dict[current_player] + " Turn!")

        input("{} press Enter when you're ready to roll!".format(players_name_dict[current_player]))
        clear()

        roll_all_dices(players_dice_dict[current_player])

        print(players_name_dict[current_player] + " Dices.")
        print()
        
        print(dice_number_help)
        print()

        print_dice_rows(players_dice_dict[current_player])

        roll_choosen_dices(reroll_choice(), players_dice_dict[current_player])

        clear()


        print(players_name_dict[current_player] + " Dices.")
        print()
        print_dice_rows(players_dice_dict[current_player])


        turn += 1

    print("That concludes the game! Compare your configurations to see which player won!")

    input("Press Enter to go to the end screen...")

    clear()

    print("For a reminder, there are your dices configurations side by side.")

    print(players_name_dict["Player 1"] + " Dices.")
    print_dice_rows(players_dice_dict["Player 1"])

    print(players_name_dict["Player 2"] + " Dices.")
    print_dice_rows(players_dice_dict["Player 2"])

    break

input('Press Enter to exit...')




'''
def print_dice(dice_list):

    # Prints dices one by one, refering to their coresponding numbers from the list used as an argument
    
    patterns = {
                'top/bot':' -------',
                'none':'|       |',
                "one":'|   *   |',
                'two':'| *   * |',
                'one_right':'|     * |',
                'one_left':'| *     |'
                }
    
    dices = {
             1:['top/bot','none','one','none','top/bot'],
             2:['top/bot','none','two','none','top/bot'],
             3:['top/bot','one_left','one','one_right','top/bot'],
             4:['top/bot','two','none','two','top/bot'],
             5:['top/bot','two','one','two','top/bot'],
             6:['top/bot','two','two','two','top/bot']
             }
    
    for dice in dices[dice_list]:
        print(patterns[dice])

'''

'''
def print_dice_rows(dice_list):

    # Prints all the dices from privided list, using print_dice() function

    for dice in dice_list:
        print_dice(dice)

'''