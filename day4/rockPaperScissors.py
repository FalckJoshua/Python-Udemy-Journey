import random

def winMessage():
    print("You are victorious big IQ!!")

def loseMessage():
    print("Computer is better player unlucky go next :)) ")

def rps_map(computerChoice):
    if (computerChoice == 1):
        return "rock"
    elif (computerChoice  == 2):
        return "paper"
    elif (computerChoice  == 3):
        return "scissors"
    else:
        return None

userChoice = input("Welcome to RPS, Enter 'rock', 'paper' or 'scissors'\n")
generateComputerCoice = rps_map(random.randint(1,3)) # 1 = rock, 2 = paper, 3 = scissors
print(f"You choose: {userChoice}")
print (f"Computer choose {generateComputerCoice}")

if (userChoice == generateComputerCoice):
    print("Draw!!")
elif(userChoice == "rock" and generateComputerCoice == "paper"):
    loseMessage()
elif(userChoice == "rock" and generateComputerCoice == "scissors"):
    winMessage()

elif(userChoice == "paper" and generateComputerCoice == "rock"):
    winMessage()
elif(userChoice == "paper" and generateComputerCoice == "scissors"):
    loseMessage()
    
elif(userChoice == "sciccors" and generateComputerCoice == "paper"):
    winMessage()
elif(userChoice == "sciccors" and generateComputerCoice == "rock"):
    loseMessage()
else:
    print("You failed to enter a valid input :o")




