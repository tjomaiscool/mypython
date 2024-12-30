import random
wins = 0
loses = 0
variants = ["rock", "scisors", "paper"]
while True:
    pc_choice = random.choice(variants)
    player_choice = input("chose rock paper or scisors ").lower()
    if player_choice not in variants:
        print(f"try again {player_choice} is not correct")
        continue
    print(f"i chose {pc_choice}")

    if player_choice == pc_choice:
        print("tie")

    elif (player_choice == "rock" and pc_choice == "paper") or \
          (player_choice == "sicers" and pc_choice == "paper") or \
           (player_choice == "paper" and pc_choice == "rock"):
                wins = wins + 1
                print(f"you won. in toltal u won {wins} times ")
                
    else:
        loses = loses + 1
        print(f"you lost. in toltal u lost {loses} times ")
            
    print("overall score is:", wins, ":", loses)
