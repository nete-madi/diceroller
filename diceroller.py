import random

print("Welcome to Dice Rolling Simulator! May your initiative be high and your damage taken be low.")
print("Dice Rolling Simulator supports the 7 standard RPG dice in the format d#, where # is the number of faces.")

def dice_roll():
    die = input("Enter the type of die you'd like to roll: ")
    while die[0] != 'd':
        die = input("Invalid input, try again: ")
    die_types_list = ["d4","d6","d8","d10","d12","d20","d100"]
    while die not in die_types_list:
        die = input("Invalid die type, try again: ")
    die_type = int(die[1:])

    die_num = input("Enter the number of d%ds you'd like to roll: " %die_type)
    while not die_num.isdigit():
        die_num = input("Invalid input, try again: ")
    die_num = int(die_num)

    for i in range(0, die_num):
            result = random.randint(1, die_type)
            print("Die %d: %d" %(i+1, result))

while True:
    dice_roll()
    exit_prompt = input("Roll again? [y/n]: ")
    if exit_prompt == 'n' or exit_prompt == 'n':
        break

