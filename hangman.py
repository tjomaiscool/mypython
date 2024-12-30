import random
words = ["Tree" ,"Ocean" ,"Book" ,"Apple" ,"Cat"]
word = random.choice(words)
hangman_word = ["_"] * len(word)
tries = 6
used_leters = []
print(f"lets play some hang man you have 6 tryes")
while tries > 0:
    letter = input (hangman_word)
    if letter in used_leters:
        print(f"{used_leters} has alredy been used")
        continue
    if letter in word:
    #TODO: successfull logic
        continue
    else:
        tries -= 1
        used_leters.append(letter)
        print(f"{letter} is not in the word. you have {tries} tries left")
        continue
