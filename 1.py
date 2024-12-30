print("welcome to the traasure hunt")
print("you are in a forest serching for treasure.")

treasure_found = False
while not treasure_found:
    choice = input("do you wanna go left or right (left/right) ")

    if choice == "left":
        print("you stombelt upon a cave")
        choice = input("do you dare to enter it (yes/no) ")
        if choice == "yes":
            print("you faund a hidden trasure u won")
            treasure_found = True
        else:
            print("you chose to stay outside")
    elif choice == "right":
        choice = input("you stumbelt acros a river do you wanna swim acros the river or follow it (swim/follow) ")
        if choice == "swim":
            print("you swimd acros the river but faund no trasure")
        else:
            print("follow the river, you find a bridge leading to a mysterious temple.")
            choice = input("Do you cross the bridge? (yes/no)")
            if choice == "yes":
                 print("In the temple, you find the hidden treasure! Your quest is complete!")
                 treasure_found = True
            else:
                  print("you decide not to cross. The river path stretches endlessly before you.") 

    else:
        print("you are now lost in the forest, you decide to stop and rest. maybe try another path next time.")
            
        














