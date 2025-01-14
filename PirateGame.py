
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

    print("You wake up on the beach of an island, you don't remember any of what happened before you woke up")
    print("To your right, you see what looks to be a bustling village. On your left, you see a dense forest")

    print()




def forest():
    print("You enter the forest and it is ominously quiet. Only the sound of bug wings fluttering and "
          "the ocean waves crashing on the shore in the distance fill the air.")
    print()
    print("There is four ways you can go, left on a overgrown stone path, right towards a cave, forwards towards"
          "a distant bay, or backwards out of the forest")
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
        if way2 == "Right":
            print()
            print("You head off towards  the cave...")
            print("Inside the cave, you stumble upon a treasure chest and find 50 gold coins! Its your lucky day")
            coins = 100 + 50
            print("After exploring the cave, you make your way back towards where you started...")
            print(f"You have {coins} coins!")

        if way2 == "Forwards":
            print()
            print("You make your way towards the bay")
            print("At the bay, you find an abandoned boat. It looks a little out of shape, but it should be ready to sail")
            sail = input("Do you want to sail? (Yes/No): ")
            setsail = sail.title()
            if setsail == "Yes":
                print("You decide to set sail. This is the start of your adventure on the open ocean...")
            elif setsail == "No":
                print("There's nothing else to do here, so you decide to head back")

            if way2 == "Backwards":
                print("You decide to leave the forest and go towards the village instead...")


        
def choice1():
        for i in range(100):
            location = input("Where should you go first? (Forest/Village): ")
            direction = location.title()

            if direction == "Forest":
                print("You decide to go explore the ominous forest...")
                forest()
                
            elif direction == "Village":
                print("You decide to walk towards the town...")
                break
            else:
                print("You can only go to the forest or the village")
                continue
intro()        
choice1()

