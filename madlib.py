import random




def play_round():
    score = 0 
    round_score = 0
    turn = 1
    overall_score = 0
    while overall_score < 100:
        choice = input("Do you want to roll or bank?: ")
        choice = choice.title()
        if choice == "Roll":
            dice_value = random.randint(1,6)
            print(f"You rolled a {dice_value}")
            if dice_value == 1:
                print("Since you rolled a 1, you get a zero for this round.")
                round_score = 0
            else: 
                round_score = round_score + dice_value
                print(f"Your round score is {round_score}")
                print(f"Your total score is {overall_score}")
                
                
        elif choice == "Bank":
                    overall_score = overall_score + round_score
                    print(f"Your total score is {overall_score}")
                    round_score = 0
                    
        
                
        else:
            print("Game over!")
play_round()
