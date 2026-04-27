while True:
    choice = input("Your choices are: explore outside or explore inside the cave.\n> ")
    if choice.lower() == "explore inside the cave":
        print("You step into the cave, the darkness swallowing you...")
        break
    elif choice.lower() == "explore outside":
        print("You walk around outside, searching for clues...")
        break
    else:
        print("That’s not a valid choice. Try again!")
