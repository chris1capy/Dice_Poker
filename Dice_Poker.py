import random

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


def print_dice_list(dice_list):

    # Prints all the dices from privided list, using print_dice() function

    for dice in dice_list:
        print_dice(dice)

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




while True:
    
    print("Welcome to The Dice Poker game! The rules originate from video game The Witcher 2: Assassins of Kings.")

    players_set = {
                "Player 1" : [0,0,0,0,0],
                "Player 2" : [0,0,0,0,0]
               }

    input("Person pressing the Enter key will be the Player 1. The game decide which person will go first. Press Enter when you ready!")

    current_player = pick_starting_player()
    print(current_player + " will be the first to roll!")
    input("Press Enter when you're ready to roll!")

    turn = 1

    while turn == 1:

        roll_all_dices(players_set[current_player])
        print_dice_list(players_set[current_player])

        roll_choosen_dices(reroll_choice(), players_set[current_player])
        print_dice_list(players_set[current_player])

        if current_player == "Player 1":
            current_player = "Player 2"
        else:
            current_player = "Player 1"

        print("Now is " + current_player + " Turn!")

        turn += 1

    while turn == 2:

        input("Press Enter when you're ready to roll!")

        roll_all_dices(players_set[current_player])
        print_dice_list(players_set[current_player])

        roll_choosen_dices(reroll_choice(), players_set[current_player])
        print_dice_list(players_set[current_player])

        turn += 1

    print("That concludes the game! Compare your configurations to see which player won!")
    print("For a reminder, there are your dices side by side.")

    print("Player 1 dices.")
    print_dice_list(players_set["Player 1"])

    print("Player 2 dices.")
    print_dice_list(players_set["Player 2"])

    break

input('Press Enter to exit...')

'''
roll_all_dices(placeholder_list)
print_dice_list(placeholder_list)

    
roll_choosen_dices(reroll_choice(), placeholder_list)
    '''