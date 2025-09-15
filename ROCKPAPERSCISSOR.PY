import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def rock_paper_scissors():
    player_score = 0
    computer_score = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter 'rock', 'paper', or 'scissors' to play, or 'quit' to stop.")
    
    while True:
        player_choice = input("Your choice: ").lower()
        
        if player_choice == "quit":
            break
        
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        winner = get_winner(player_choice, computer_choice)
        
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
            
        print(f"Score: You {player_score}, Computer {computer_score}")
    
    print("Final Score:")
    print(f"You: {player_score}, Computer: {computer_score}")
    if player_score > computer_score:
        print("You are the champion!")
    elif computer_score > player_score:
        print("Computer is the champion!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    rock_paper_scissors()