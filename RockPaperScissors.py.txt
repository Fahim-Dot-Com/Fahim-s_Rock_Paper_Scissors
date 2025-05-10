import fahims_rock_paper_scissors as random  # This is my simple custom module

#This is the code for your move

def get_user_choice():
    choice = input("Enter Rock, Paper, or Scissors: ").strip().lower()
    if choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Try again.")
        return get_user_choice()
    return choice
#This code is for the computers move and will tell you whether won or not

def get_computer_decision():
    return random.custom_choice(['rock', 'paper', 'scissors'])

def whos_the_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win, Fahim!"
    else:
        return "Computer wins!"

#This code right here is for starting the game.

def play_game():
    print("Welcome to Rock, Paper, Scissors, Fahim!")
    user_choice = get_user_choice()
    computer_choice = get_computer_decision()
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = whos_the_winner(user_choice, computer_choice)
    print(f"\n{result}")

if __name__ == "__main__":
    play_game()
