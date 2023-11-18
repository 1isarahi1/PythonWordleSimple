import os


# Letter frequencies given in the document
letter_frequencies = {
    'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70,
    'f': 2.23, 'g': 2.02, 'h': 6.09, 'i': 6.97, 'j': 0.15,
    'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51,
    'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06,
    'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97, 'z': 0.07
}

def calculate_score(chosen_word, guessed_letters, bad_guesses, gave_up):
    score = 0

    if gave_up:
        # If the user gave up, calculate the negative score
        score = -sum(letter_frequencies[letter] for letter in chosen_word)
    else:
        # If the word was guessed correctly
        # Check if any letters were guessed correctly
        if guessed_letters:
            # Sum the frequencies of letters that have not been guessed yet
            unguessed_letters = [letter for letter in chosen_word if letter not in guessed_letters]
            score = sum(letter_frequencies[letter] for letter in unguessed_letters)
        else:
            # If no letters were guessed (meaning the user guessed the word outright),
            # sum up all letter frequencies
            score = sum(letter_frequencies[letter] for letter in chosen_word)
        
        # Divide the score by the number of letters guessed to account for the difficulty
        # If all letters were guessed correctly one by one, this division should not reduce the score
        score /= max(len(guessed_letters), 1)
        
        # Deduct 10% of the score for each bad guess
        # In this case, there are no bad guesses, so no deduction
        if bad_guesses > 0:
            score *= (1 - 0.1 * bad_guesses)

    # Round the score to two decimal places
    return round(score, 2)


def print_final_report(games_report):
    # Clear the screen before printing the final report
    os.system('cls' if os.name == 'nt' else 'clear')

    print("++")
    print("++ Game Report")
    print("++")
    print(f"{'Game':<5} {'Word':<5} {'Status':<10} {'Bad Guesses':<12} {'Missed Letters':<15} {'Score':<5}")
    for index, game in enumerate(games_report, 1):
        print(f"{index:<5} {game['word']:<5} {game['status']:<10} {game['bad_guesses']:<12} {game['missed_letters']:<15} {game['score']:<5.2f}")
    final_score = sum(game['score'] for game in games_report)
    print("Final Score: {:.2f}".format(final_score))