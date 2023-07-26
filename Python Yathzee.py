import random 

def roll_dice(current_dice_rolls, dice_to_roll):
    new_dice_rolls = current_dice_rolls.copy()
    for i in dice_to_roll:
        new_dice_rolls[i] = random.randint(1, 6)
    return new_dice_rolls

    new_dice_rolls = roll_dice(current_dice_rolls, dice_to_roll)
    print(new_dice_rolls)

roll_dice([4, 4, 6, 4, 6], [1, 2, 4])

def convert_user_input_to_dice_indices(user_input: str) -> list:
    if user_input == "":
        return []
    else:
        dice_indices = [int(dice[1:]) - 1 for dice in user_input.split()]
        return dice_indices
    
convert_user_input_to_dice_indices("D4 D1")
convert_user_input_to_dice_indices("")

x = [3, 6, 1]
x.sort()
x

def calculate_score(current_dice_rolls):
    current_dice_rolls.sort()
    len_set = len(set(current_dice_rolls))
    freq_el = max(set(current_dice_rolls), key = current_dice_rolls.count)
    
    if len_set == 3:
      return 3 * freq_el
    if len_set == 2 and current_dice_rolls[0] == current_dice_rolls[3]:
      return 4 * freq_el
    if len_set == 2 and current_dice_rolls[0] != current_dice_rolls[3]:
      return 25
    if len_set == 1:
      return 50
    if current_dice_rolls[0] == 1 and current_dice_rolls[1] == 2 and current_dice_rolls[2] == 3 and current_dice_rolls[3] == 4 and current_dice_rolls[4] == 5 or current_dice_rolls[0] == 2 and current_dice_rolls[1] == 3 and current_dice_rolls[2] == 4 and current_dice_rolls[3] == 5 and current_dice_rolls[4] == 6:
      return 40
    for index in range(len(current_dice_rolls)):
       slice_to_check = current_dice_rolls[index:index + 4]
       if slice_to_check == [1, 2, 3, 4] or [2, 3, 4, 5] or [3, 4, 5, 6]:
          return 30
       
calculate_score([2, 3, 2, 2, 5])
calculate_score([3, 3, 3, 6, 6])

print(calculate_score([2, 3, 2, 2, 5]) == 6)
print(calculate_score([3, 3, 3, 6, 3]) == 12)
print(calculate_score([3, 3, 3, 2, 2]) == 25)
print(calculate_score([1, 2, 3, 4, 1]) == 30)
print(calculate_score([2, 3, 4, 5, 6]) == 40)
print(calculate_score([3, 3, 3, 3, 3]) == 50)

print(calculate_score([2, 3, 2, 2, 5]))
print(calculate_score([3, 3, 3, 6, 3]))
print(calculate_score([3, 3, 3, 2, 2]))
print(calculate_score([1, 2, 3, 4, 1]))
print(calculate_score([2, 3, 4, 5, 6]))
print(calculate_score([3, 3, 3, 3, 3]))

print("The game of Yahtzee begins!")

user_choice_info = 'When prompted to choose which dice to roll, please write the' \
' letter "D" followed by the number of the dice you want to roll.' \
' If you want to roll multiple dice, separate your choices with white space.' \
' For example, write "D1 D2 D5" if you want to roll dice 1, 2 and 5' \
' Alternatively, press enter without writing anything to skip the turn.'

print("")
print(user_choice_info)    


run_game = True
while run_game:
    
    # During the first roll of the round, the user has no choice but to roll all 5 dice
    current_dice_rolls = roll_dice([], [0, 1, 2, 3, 4])
    print("")
    print("Your current dice rolls: " + str(current_dice_rolls))
    
    # Once the dice were rolled the first time, the user will have the option to select dice
    # and roll them again two more times.
    for i in range(2):
        
        # Here we get the user's choice regarding which dice to roll
        user_choice = input('Please choose which dice you want to roll again: ')
        dice_to_roll = convert_user_input_to_dice_indices(user_choice)
        current_dice_rolls = roll_dice(current_dice_rolls, dice_to_roll)
        print("Your current dice rolls: " + str(current_dice_rolls))
    
    # Once all three dice rolls were completed, we print the score
    current_score = calculate_score(current_dice_rolls)
    print("Your score for this round is: " + str(current_score))
    
    # After the round is finished, we ask the user if they want to play again
    continue_game = input("Do you want to play again? (yes/no)")
    while continue_game not in ["yes", "no"]:
        print('Invalid option. Please write "yes" or "no"')
        continue_game = input("Do you want to play again? (yes/no)")
    
    # If user chose no, we set run_game to False which will exit the loop and finish running the game
    if continue_game == "no":
        run_game = False
    
    

