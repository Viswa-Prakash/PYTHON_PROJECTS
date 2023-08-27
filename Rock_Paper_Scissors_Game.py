import random 

def play_game(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("Its a tie")
    
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
            (player_choice == 'paper' and computer_choice == 'rock') or \
            (player_choice == 'scissors' and computer_choice == 'paper'):
        print("You Win")
    
    else:
        print("Computer Wins")

player_choice = input("Enter your choice (rock/paper/scissors): ")

if player_choice in ['rock', 'paper', 'scissors']:
    play_game(player_choice)

else:
    print("Invalid choice")
    

         
         