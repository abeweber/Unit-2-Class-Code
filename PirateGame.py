intro_art = r'''.=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
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

print("What are you:")
print(f"1. Pirate\n2. Marine\n")
role = int(input("> " ))

if role == 1:
    print("You are a pirate! Discover new islands and find treasure. Don't let the marines catch you.")

elif role == 2:
    print("You are a marine! Catch pirates and keep peace on the sea.")

else: 
    print("You can only be a pirate or a marine.")