def intro():
    intro_art = r'''
    .=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
    |                     ______                     |
    |                  .-"      "-.                  |
    |                 /            \                 |
    |     _          |              |          _     |
    |    ( \         |,  .-.  .-.  ,|         / )    |
    |     > "=._     | )(__/  \__)( |     _.=" <     |
    |    (_/"=._"=._ |/     /\     \| _.="_.="\_)    |
    |           "=._"(_     ^^     _)"_.="           |
    |               "=\__|IIIIII|__/="               |
    |              _.="| \IIIIII/ |"=._              |
    |    _     _.="_.="\          /"=._"=._     _    |
    |   ( \_.="_.="     `--------`     "=._"=._/ )   |
    |    > _.="                            "=._ <    |
    |   (_/                                    \_)   |
    |                                                |
    '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='''
    print('Welcome to Open Ocean')
    print(intro_art)

    print("You wake up on the beach of an island, all you remember is your name, and that you're a pirate")
    name = input("What is your name: ")
    global coins
    coins = 100
    print("To your right, you see what looks to be a bustling village. On your left, you see a dense forest")

    print()

def village():
    print("The village is packed. You want to explore but you don't know where to get started so you ask a man closeby")
    print("You must be an traveler he says. He tells you to check out the tavern or the port ")
    print()
    nextmove = input("Where do you want to go (Tavern/Port): ")
    nextmove = nextmove.title()
    if nextmove == "Tavern":
        print("You head to the tavern...")
        print("In the tavern, you have 3 options. You can either buy a drink, ask for information, or leave")
        
        for i in range(100):
            bar_decision = input("What do you want to do (Drink/Info/Leave)")
            bar_decision = bar_decision.title()
            if bar_decision == "Info":
                print("Inside the tavern, you ask the barkeeper for some information")
                print("You learn your on LaRosa island in the West Sea.")
            elif bar_decision == "Drink":
                global coins
                if coins > 10:
                    print("You decide to buy a drink for 10 coins")
                    coins = coins - 10
                    print(f"You now have {coins} coins")
                elif coins <= 10:
                    print("You don't have enough to buy a drink")
            elif bar_decision == "Leave":
                print("You exit the tavern and head towards the port")
                print()
                print("You go to the port in search of a boat for your pirate adventure")
                print("After looking around at the boat prices, you realize that you don't have enough to buy a boat")
                print("Fortunately, you are a pirate, so the law don't apply to you. You choose to steal a boat when nobody is looking")
                print("You set sail into the open ocean. You hear the village folk yelling at you from the port as you sail away")
                break
                
    if nextmove == "Port":
        print()
        print("You go to the port in search of a boat for your pirate adventure")
        print("After looking around at the boat prices, you realize that you don't have enough to buy a boat")
        print("Fortunately, you are a pirate, so the law don't apply to you. You choose to steal a boat when nobody is looking")
        print("You set sail into the open ocean. You hear the village folk yelling at you from the port as you sail away")



def forest():
    print("You enter the forest and it is ominously quiet. Only the sound of bug wings fluttering and "
          "the ocean waves crashing on the shore in the distance fill the air.")
    print()
    print("There is four ways you can go, left on a overgrown stone path, right towards a cave, forwards towards"
          "a distant bay, or backwards out of the forest")
    right_count = 0
    for i in range(100):
        print()
        way = input("What direction should you go? (left, right, forwards, or backwards): ")
        
        way2 = way.title()
        if way2 == "Left":
            print()
            print("You follow the overgrown trail and it leads to a cliff hanging over the ocean."
                  " While its a nice view, theres nothing else to do here.")
            print("You make your way back towards where you started...")
            continue
        elif way2 == "Right":
            right_count = right_count + 1
            if right_count < 2 :
                print()
                print("You head off towards  the cave...")
                print("Inside the cave, you stumble upon a treasure chest and find 50 gold coins! Its your lucky day")
                global coins
                coins = coins + 50
                print(f"You now have {coins} coins!")
                print("After exploring the cave, you make your way back towards where you started...")
            
                
            elif right_count > 1:
                print("You've already been here. Theres nothing else to find")

        elif way2 == "Forwards":
            print()
            print("You make your way towards the bay")
            print("At the bay, you find an abandoned boat. It looks a little out of shape, but it should be ready to sail")
            sail = input("Do you want to sail? (Yes/No): ")
            setsail = sail.title()
            if setsail == "Yes":
                print("You decide to set sail. This is the start of your adventure on the open ocean...")
                break
            elif setsail == "No":
                print("There's nothing else to do here, so you decide to head back")

        elif way2 == "Backwards":
            print("You decide to leave the forest and go towards the village instead...")
            village()
            break

        else:
            print("Invalid direction. Please try again")



def choice1():
        for i in range(100):
            location = input("Where should you go first? (Forest/Village): ")
            direction = location.title()

            if direction == "Forest":
                print("You decide to go explore the ominous forest...")
                forest()
                break
                
            elif direction == "Village":
                print("You decide to walk towards the town...")
                village()
                break
            else:
                print("You can only go to the forest or the village")
                continue
intro()        
choice1()