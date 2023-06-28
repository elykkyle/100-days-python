import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
alpha = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter: row.code for (index, row) in alpha.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
running = True
while running:
    word = input("Enter a word: ")
    if word == "stop tool":
        running = False
        break
    result = [alpha_dict[letter] for letter in word.upper()]

    print(result)
