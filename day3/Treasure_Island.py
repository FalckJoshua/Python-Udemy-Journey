print("Welcome to Treasure Island. Your mission is to find the treassure.")

direction = input("Do you want to go (Left) or (Right)\n")

if (direction== "Right"):
    print("Game Over, you fell and died :)")
    exit(1)
elif not direction == "Left":
    print("You did not pick a valid choice!!")
    exit(1)
    
direction = input("By turning Left you have now reached a lake, you can either (Wait) for a boat or (Swim) across\n")

if (direction == "Swim"):
    print("You attempted to swim but drowned, Game over")
    exit(1)
    
elif not direction  ==  "Wait":
    print("You did not pick a valid choice!!")
    exit(1)
else:
    print("You waited and decided to take another look around. You see three different door a (Yellow), (Red) and (Blue)")

    direction = input("Which door do you enter?\n")

    if(direction == "Red"):
        print("It was a trap you fell and died, Game over")
        exit(1)

    elif(direction == "Blue"):
        print("It was a trap you fell and died, Game over")
        exit(1)
    elif(not direction == "Yellow"):
        print("You did not pick a valid choice!!")
        exit(1)
print("You entered the Yellow door and found the treassure!!!")
print("You win!")