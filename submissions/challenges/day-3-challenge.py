firstQuestion = input("Would you give a man a shelter? [y/n] ").lower()

if firstQuestion == 'n':
    print('He attacked you and killed you. [Game Over]')

else:
    answer = input("Police arrived and asked you if there was a man nearby. [y/n] ").lower()

    if answer == 'n':
        print('GAME OVER')
    
    else:
        print('You Won !')

