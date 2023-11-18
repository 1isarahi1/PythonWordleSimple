import os


current_directory = os.getcwd()
print("Current Directory:", current_directory)

def load_words(filename):
    if not os.path.isfile(filename):
        print(f"Error: The file {filename} was not found in the current directory.")
        return []
    with open(filename, 'r') as file:
        return [word for line in file for word in line.split() if len(word) == 4]
