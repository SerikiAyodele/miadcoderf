from random import randint



playAgain = "yes"

while playAgain == "yes":
    print("DRAGON REALM\n")
    safe = randint(1, 2)
    
    print("Which cave do you want to enter? 1 or 2")

    choice = int(input())

    print("\nYou approach the cave...")

    if choice == safe:
        print("You are safe")
    else:
        print("It is dark and spooky...")
        print("A large dragon jumps out in front of you! He opens his jaws and...")
        print("Gobbles you down in one bite!")

    print("Do you want to play again? (yes or no)")
    playAgain = input()
