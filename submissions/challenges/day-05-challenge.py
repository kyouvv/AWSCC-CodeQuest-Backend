import random

choices = ["rock", "paper", "scissor"]
winningCombinations = {
    "rock": "scissor",
    "paper": "rock",
    "scissor": "paper"
}

playerChoice = input("Rock, Paper or Scissor? ").lower()
computerChoice = random.choice(choices)

if playerChoice == computerChoice:
    print(f"Computer chose {computerChoice}.")
    print("Its a tie.")


elif winningCombinations[playerChoice] == computerChoice:
    print(f"Computer chose {computerChoice}.")
    print("Player wins.")

else:
    print(f"Computer chose {computerChoice}.")
    print("Computer wins.")
