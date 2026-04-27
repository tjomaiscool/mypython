import random
DIOLOG_OPTION_A = "you see 2 gnomes playing chess what do you want to do options, talk, run to the next room"
DIOLOG_OPTION_B = "you see a split were do you go options, right, left"
DIOLOG_OPTION_C = "theres nothing there do you wish to go back options, yes, mindlesly staring into solid stone"
while True:
    start = input("You stand at the entrance of a cave, you remembering nothing. Your choices are: explore outside or explore inside the cave. Make sure to spell everything correctly \n> ")
    if start.lower() == "explore inside the cave":
            input2 = (random.choice([DIOLOG_OPTION_A,DIOLOG_OPTION_B,DIOLOG_OPTION_C]))
            choice1 = input(p for p in input2 if p !=DIOLOG_OPTION_A)
            break
    elif start.lower() == "explore outside":
        
        break
    else:
        print ("invalid choise try again")
