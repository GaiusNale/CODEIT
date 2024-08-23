import random

def get_random_number(difficulty):
    if difficulty == 'easy':
        return random.randint(1, 50)
    elif difficulty == 'medium':
        return random.randint(1, 100)
    elif difficulty == 'hard':
        return random.randint(1, 200)
    else:
        print("Invalid difficulty level.")
        return None

def get_attempts(difficulty):
    if difficulty == 'easy':
        return 7
    elif difficulty == 'medium':
        return 5
    elif difficulty == 'hard':
        return 3
    else:
        print("Invalid difficulty level.")
        return None

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("Choose a difficulty level:")
    print("1. Easy (Range: 1-50, Attempts: 7)")
    print("2. Medium (Range: 1-100, Attempts: 5)")
    print("3. Hard (Range: 1-200, Attempts: 3)")
    
    difficulty_choice = input("Enter 1, 2, or 3: ").strip()
    
    if difficulty_choice == '1':
        difficulty = 'easy'
    elif difficulty_choice == '2':
        difficulty = 'medium'
    elif difficulty_choice == '3':
        difficulty = 'hard'
    else:
        print("Invalid choice, please restart the game.")
        return
    
    target_number = get_random_number(difficulty)
    attempts = get_attempts(difficulty)
    
    if target_number is None or attempts is None:
        return
    
    print(f"You have chosen {difficulty.capitalize()} mode. You have {attempts} attempts to guess the number.")
    
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess: "))
        
        if guess == target_number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < target_number:
            print("Too low!")
        else:
            print("Too high!")
    
    if guess != target_number:
        print(f"Sorry, you've run out of attempts. The correct number was {target_number}.")

if __name__ == "__main__":
    play_game()
