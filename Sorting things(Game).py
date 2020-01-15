from random import randint

numbers = []

reply = []

level_increaser = 0
level = 1
best_level = level

quits = False

try:
    file = open("bestlevel.txt", "r")
    best_level = int(file.read())
    file.close()
except:
    best_level = level


print("Sorting game by Emeka")

print("e.g Sort the numbers below")
print("5")
print("1")
print("8")

print("\nNumber 1: 1")
print("Number 2: 5")
print("Number 3: 8")
print("Sorted!")

while True:
    print("\n\nLEVEL " + str(level) + "\t\tBEST LEVEL: " + str(best_level))

    for i in range(3 + level_increaser):
        numbers.append(randint(1, 9))

    print("Sort the numbers below:      (Type 'I am done' to quit!)")

    for i in range(3 + level_increaser):
        print(numbers[i])

    print("")

    for i in range(3 + level_increaser):
        play = input("Number " + str(i+1) + ": ")
        if play == "i am done" or play == "I AM DONE"  or play == "I am done" :
            quits = True
            break
        try:
            reply.append(int(play))
        except:
            print("Enter a number next time")
            break
        
    if quits == True:
            break
    
    numbers.sort()

    
    
    l = randint(1, 3)

    if reply == numbers:
        print("Sorted!")
        print("You win")
        level += 1
        level_increaser += 1

        if level > best_level:
            best_level = level
            file = open("bestlevel.txt", "w")
            file.write(str(best_level))
            file.close()


    else:
        if l == 1:
            print("Bad luck. Try again")
        elif l == 2:
            print("You lost. Don't give up")
        else:
            print("Opps. It's not over until its over")
    
    numbers = []
    reply = []

print("\nlol.. You're tired already")
print("bye")
print("take care")
