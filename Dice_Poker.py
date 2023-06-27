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
    

dices_list_test = [1,5,6,6,3]

print_dice_list(dices_list_test)

input('Press Enter to exit...')