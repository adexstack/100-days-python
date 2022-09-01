# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

TO_REPLACE = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("Input\Letters\starting_letter.txt") as starting_letter:
    starting_letter = starting_letter.read()
    for name in names_list:
        stripped_name = name.strip()
        with open(f"./Output/ReadyToSend/{stripped_name}_letter.txt", 'w', encoding='utf8') as completed_letter:
            completed_letter.write(starting_letter.replace(TO_REPLACE, stripped_name))
