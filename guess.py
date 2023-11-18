
def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '-' for letter in word)
