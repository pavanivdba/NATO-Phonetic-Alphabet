import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pd.DataFrame(student_dict)
nato_data_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {}
for (index, row) in nato_data_df.iterrows():
    nato_dict[row.letter] = row.code

to_repeat = False
try:
    while not to_repeat:
        userInput = input("Enter a Word for the Phonetic values for each letter of the word:").upper()
        phonetic_dict = {}
        nonchars_list = []
        phonetic_list = [nato_dict[item] for item in list(userInput) if item in nato_dict.keys()]
        for item in list(userInput):
            if item in nato_dict.keys():
                phonetic_dict[item] = nato_dict[item]
            else:
                nonchars_list.append(item)
        if len(nonchars_list) == 0:
            print(phonetic_list)
            break
        else:
            print("Sorry, only letters in the alphabet please.")
except KeyError:
    to_repeat = True





