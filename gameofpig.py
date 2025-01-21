import random

def bot_play(bot_overall):
    bot_score = 0
    bot_round = 0
    turn = 1

    while bot_overall < 100:
        roll = random.randint(1, 6)
        if roll == 1:
            print("The bot rolled a 1. They get a 0 for this turn")
            bot_round = 0
            break
        else:
            print("The bot rolled a " + str(roll))
            bot_round = bot_round + roll
            print("The bot has " + str(bot_round) + " points this round")
            if bot_round <= 15:
                print("The bot will roll again")
                print()
        
        if bot_round > 15:
            bot_overall = bot_overall + bot_round
            print("The bot chose to bank")
            print("The bot's overall score is " + str(bot_overall))
            break
        
        if bot_overall >= 100:
            print("The bot wins! The bot reached 100 points before you")
            return bot_overall  
            
    return bot_overall  

def play_round():
    score = 0
    round_score = 0
    turn = 1
    overall_score = 0
    bot_overall = 0  

    while overall_score < 100 and bot_overall < 100:
        print("\nTurn " + str(turn))
        print("Your turn:")
        choice = input("Do you want to roll or bank?: ").title()

        if choice == "Roll":
            dice_value = random.randint(1, 6)
            print(f"You rolled a {dice_value}")
            if dice_value == 1:
                print("Since you rolled a 1, you get a zero for this round.")
                round_score = 0
                turn += 1
                bot_overall = bot_play(bot_overall)  
                if bot_overall >= 100: 
                    break
            else:
                round_score += dice_value
                print(f"Your round score is {round_score}")
                print(f"Your total score is {overall_score}")
        elif choice == "Bank":
            overall_score += round_score
            print(f"Your total score is {overall_score}")
            round_score = 0
            turn += 1
            bot_overall = bot_play(bot_overall)  
            

        if overall_score >= 100:
            print("You win! You reached 100 points before the bot.")
            break

        if bot_overall >= 100:
            print("The bot wins! The bot reached 100 points before you.")
            break

play_round()