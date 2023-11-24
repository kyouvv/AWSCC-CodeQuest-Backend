player1 = input("Player 1: ").lower()
player2 = input("Player 2: ").lower()

if player1 == player2:
    print("Its a tie")

elif player1 == "rock" and player2 == "paper":
    print("Player 2 wins")

elif player2 == "rock" and player1 == "paper":
    print("Player 1 wins")

elif player1 == "scissors" and player2 == "paper":
    print("Player 1 wins")

elif player2 == "scissors" and player1 == "paper":
    print("Player 2 wins")

elif player1 == "rock" and player2 == "scissors":
    print("Player 1 wins")

elif player2 == "rock" and player1 == "scissors":
    print("Player 2 wins")