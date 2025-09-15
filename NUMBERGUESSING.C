#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(0));
    int secret_number = rand() % 100 + 1;
    int guess, attempts = 0, max_attempts = 10;
    int score = 0;
    
    printf("Welcome to the Cosmic Number Quest!\n");
    printf("The Oracle has chosen a number between 1 and 100.\n");
    printf("You have %d attempts to uncover it. Each attempt reveals a clue!\n", max_attempts);
    printf("Clue: The number is %s and %s divisible by 3.\n", 
           secret_number % 2 == 0 ? "even" : "odd",
           secret_number % 3 == 0 ? "is" : "is not");
    
    while (attempts < max_attempts) {
        printf("\nAttempt %d/%d: Enter your guess: ", attempts + 1, max_attempts);
        scanf("%d", &guess);
        attempts++;
        
        if (guess < 1 || guess > 100) {
            printf("The Oracle only accepts numbers between 1 and 100!\n");
            continue;
        }
        
        if (guess > secret_number) {
            printf("Too high! The number is smaller than %d.\n", guess);
        } else if (guess < secret_number) {
            printf("Too low! The number is larger than %d.\n", guess);
        } else {
            score = (max_attempts - attempts + 1) * 10;
            printf("Victory! You've cracked the Oracle's code in %d attempts!\n", attempts);
            printf("Your score: %d\n", score);
            return 0;
        }
    }
    
    printf("The Oracle's number was %d. Better luck next time!\n", secret_number);
    return 0;
}