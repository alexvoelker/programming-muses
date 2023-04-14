import json
import random

NUMBER_TERMS_GENERATED = 2000
NUMBER_WORDS_IN_TERM = 3
OUTPUT_TO_FILE = False
OUTPUT_FILE_NAME = "random_word_output.txt"

# Obtain the list of english words

# Use json file
# with open("words_dictionary.json", 'r') as word_file_readable:
#     word_json = json.load(word_file_readable)
#     word_list = [word for word in word_json.keys()]

# Use txt file
with open("word_list.txt", "r") as word_list_file:
    word_list = word_list_file.read().split("\n")


# Obtain word combinations for potential business ideas
word_combos = []
for term in range(NUMBER_TERMS_GENERATED):
    term_list = []
    for word in range(NUMBER_WORDS_IN_TERM):
        term_list.append(random.choice(word_list))
    word_combos += [term_list]


if not OUTPUT_TO_FILE:
    # Print out the word_combos list
    for i in range(NUMBER_TERMS_GENERATED):
        print(f"{i + 1}: ", end="")
        for j in range(NUMBER_WORDS_IN_TERM):
            print(f"{word_combos[i][j]}, " if j < NUMBER_WORDS_IN_TERM - 1 else f"{word_combos[i][j]}\n", end="")
else:
    with open(f"{OUTPUT_FILE_NAME}", 'w') as file_output:
        for i in range(NUMBER_TERMS_GENERATED):
            file_output.write(f"{i + 1}: ")
            for j in range(NUMBER_WORDS_IN_TERM):
                file_output.write(f"{word_combos[i][j]}, " if j < NUMBER_WORDS_IN_TERM - 1 else f"{word_combos[i][j]}\n")
    print(f"Output successfully written to file: '{OUTPUT_FILE_NAME}'")
