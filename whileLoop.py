game_on = True

def runTheGame():
    global game_on  

    choice = int(input('Play the game.'))

    if choice == 1:
        print(choice)
        print(game_on)
    else: 
        game_on = False
        print(choice)
        print(game_on)


while game_on:
    runTheGame()

print('you ended the game.')
    
