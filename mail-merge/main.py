# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    starting_letter = letter_file.read()

for name in names:
    formatted_name = name.strip()
    with open(f"./Output/ReadyToSend/{formatted_name}_letter.txt", 'w') as output_file:
        merge_letter = starting_letter.replace(PLACEHOLDER, formatted_name)
        output_file.write(merge_letter)