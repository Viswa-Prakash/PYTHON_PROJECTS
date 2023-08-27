import random
def roll_dice():
    return random.randint(1,6)

num_rolls = int(input("Enter the number of rolls: "))

for _ in range(num_rolls):
    result = roll_dice()
    print(f"You rolled a {result}")