def print_dice(dice_list):
    
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

list_of_dices = [1,5,6]

for x in list_of_dices:
    print_dice(x)

input('Press Enter to exit...')