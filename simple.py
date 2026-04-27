import random
while True:
    start = input("You stand at the entrance of a cave, you remembering nothing. Your choices are: explore outside or explore inside the cave. Make sure to spell everything correctly \n> ")
    if start.lower() == "explore inside the cave":
            input2 = (random.choice(["you see 2 gnomes playing chess what do you want to do options, talk, run to the next room","you see a split were do you go options right left","theres nothing there"]))
            choice1 = input(input2)
            break
    elif start.lower() == "explore outside":
        
        break
    else:
        print ("invalid choise try again")
