# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas

# Load CSV
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create dictionary from DataFrame
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Get user input and convert to phonetic code
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)


try:
    word = input("Enter a word: ").upper()
    output_list = [phonetic_dict[letter] for letter in word]
except KeyError:
    print("Please enter only letters from A-Z.")
else:
    print(output_list)
