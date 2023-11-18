import random
import sys

from Game import calculate_score, print_final_report
from StringDatabase import load_words
from guess import display_word




def play_game(words):
    total_score = 0
    games_report = []  # List to hold report data for each game
    if not words:  # Check if the words list is empty
        print("No words available to play.")
        return

    while True:
        chosen_word = random.choice(words)
        guessed_letters = set()
        bad_guesses = 0
        attempts = 0
        gave_up = False
        current_guess_display = display_word(chosen_word, guessed_letters)

        print("++")
        print("++The Great Guessing Game")
        print("++")

        while current_guess_display != chosen_word:
            print("Current guess:", current_guess_display)
            print("Letters guessed:", ', '.join(sorted(guessed_letters)))

            choice = input("\nChoose an option:\n(g) Guess the word\n(l) Guess a letter\n(t) Tell me and give up \n(q) Quit\n> ").strip().lower()

            if choice == 'g':  # Guess the entire word
                guess = input("Enter your guess for the word: ").strip().lower()
                if guess == chosen_word:
                    print("Correct! You guessed the word.")
                    break  # Move to the next word
                else:
                    print("Incorrect guess for the word.")
                    attempts += 1

            elif choice == 'l':  # Guess a letter
                letter = input("Guess a letter: ").strip().lower()
                if len(letter) == 1 and letter.isalpha():
                    if letter not in guessed_letters:
                        guessed_letters.add(letter)
                        if letter in chosen_word:
                            print(f"Correct! The letter '{letter}' is in the word.")
                        else:
                            print(f"Incorrect. The letter '{letter}' is not in the word.")
                            attempts += 1
                    else:
                        print(f"You have already guessed the letter '{letter}'. Try a different one.")
                    # Add a prompt for the user to press any key to continue
                    
                    input("Press any key to continue...")
                    # Update the current guess display here, after the letter has been added to guessed_letters
                    current_guess_display = display_word(chosen_word, guessed_letters)

                else:
                    print("Please enter a single alphabetical character.")

            if choice == 't':  # Tell me and give up
                gave_up = True
                print(f"You gave up. The word was: {chosen_word}")
                break  # Exit while loop to calculate the score for this round

            if choice == 'q':  # Quit the game
                print("Quitting the game.")
                print_final_report(games_report)
                return  # End the game session

        # Calculate the score for this round and update the total score and games report
        game_score = calculate_score(chosen_word, guessed_letters, attempts, gave_up)
        total_score += game_score
        games_report.append({
            'word': chosen_word,
            'status': 'Success' if not gave_up else 'Gave up',
            'bad_guesses': attempts,
            'missed_letters': len([letter for letter in chosen_word if letter not in guessed_letters]),
            'score': game_score
        })

def play_game_test(words):
    total_score = 0
    games_report = []  # List to hold report data for each game
    if not words:  # Check if the words list is empty
        print("No words available to play.")
        return

    while True:
        chosen_word = random.choice(words)
        guessed_letters = set()
        bad_guesses = 0
        attempts = 0
        gave_up = False
        current_guess_display = display_word(chosen_word, guessed_letters)

        print("++")
        print("++The Great Guessing Game")
        print("++")

        print("Current Word (for testing):", chosen_word)  # For testing purposes
        
        while current_guess_display != chosen_word:
            print("Current guess:", current_guess_display)
            print("Letters guessed:", ', '.join(sorted(guessed_letters)))

            choice = input("\nChoose an option:\n(g) Guess the word\n(l) Guess a letter\n(t) Tell me and give up \n(q) Quit\n> ").strip().lower()

            if choice == 'g':  # Guess the entire word
                guess = input("Enter your guess for the word: ").strip().lower()
                if guess == chosen_word:
                    print("Correct! You guessed the word.")
                    break  # Move to the next word
                else:
                    print("Incorrect guess for the word.")
                    attempts += 1

            elif choice == 'l':  # Guess a letter
                letter = input("Guess a letter: ").strip().lower()
                if len(letter) == 1 and letter.isalpha():
                    if letter not in guessed_letters:
                        guessed_letters.add(letter)
                        if letter in chosen_word:
                            print(f"Correct! The letter '{letter}' is in the word.")
                        else:
                            print(f"Incorrect. The letter '{letter}' is not in the word.")
                            attempts += 1
                    else:
                        print(f"You have already guessed the letter '{letter}'. Try a different one.")
                    # Add a prompt for the user to press any key to continue
                    
                    input("Press any key to continue...")
                    # Update the current guess display here, after the letter has been added to guessed_letters
                    current_guess_display = display_word(chosen_word, guessed_letters)

                else:
                    print("Please enter a single alphabetical character.")

            if choice == 't':  # Tell me and give up
                gave_up = True
                print(f"You gave up. The word was: {chosen_word}")
                break  # Exit while loop to calculate the score for this round

            if choice == 'q':  # Quit the game
                print("Quitting the game.")
                print_final_report(games_report)
                return  # End the game session

        # Calculate the score for this round and update the total score and games report
        game_score = calculate_score(chosen_word, guessed_letters, attempts, gave_up)
        total_score += game_score
        games_report.append({
            'word': chosen_word,
            'status': 'Success' if not gave_up else 'Gave up',
            'bad_guesses': attempts,
            'missed_letters': len([letter for letter in chosen_word if letter not in guessed_letters]),
            'score': game_score
        })


if __name__ == "__main__":
    # Check if a command line argument was provided
    if len(sys.argv) != 2:
        print("Usage: python words.py [play|test]")
        sys.exit(1)
    
    mode = sys.argv[1]  # Get the mode from command line
    words = load_words("four_letters.txt")  # Load the list of words
    
    if not words:
        print("Error: Could not load words.")
        sys.exit(1)
    
    if mode == "play":
        play_game(words)
    elif mode == "test":
        play_game_test(words)
    else:
        print("Invalid mode. Please choose 'play' or 'test'.")
        sys.exit(1)