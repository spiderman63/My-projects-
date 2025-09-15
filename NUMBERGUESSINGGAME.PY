import random

def cosmic_number_quest():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    score = 0
    
    print("Welcome to the Cosmic Number Quest!")
    print("The Oracle has chosen a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to uncover it. Each attempt reveals a clue!")
    print(f"Clue: The number is {'even' if secret_number % 2 == 0 else 'odd'} and "
          f"{'is' if secret_number % 3 == 0 else 'is not'} divisible by 3.")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}: Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("The Oracle only accepts numbers between 1 and 100!")
                continue
                
            if guess > secret_number:
                print(f"Too high! The number is smaller than {guess}.")
            elif guess < secret_number:
                print(f"Too low! The number is larger than {guess}.")
            else:
                score = (max_attempts - attempts + 1) * 10
                print(f"Victory! You've cracked the Oracle's code in {attempts} attempts!")
                print(f"Your score: {score}")
                return
        except ValueError:
            print("The Oracle demands a valid number!")
    
    print(f"The Oracle's number was {secret_number}. Better luck next time!")

if __name__ == "__main__":
    cosmic_number_quest()