#this is my game!!!!
import random
random_number = random.randint(1, 100)
right_answer = False
while right_answer == False:
    try:
        answer = int(input("guess the number from 1 to 100   "))
    except:
        print("i dont think this number works with our game")
        continue
    if answer > random_number:
        print("you are too high")
    elif answer < random_number:
        print("you are too low")
    else:
        print("you won")
        right_answer = True
