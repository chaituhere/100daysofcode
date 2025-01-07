# Day 3: Conditional Statements, Logical Operators, Code Blocks & Scope (Global/Local Name Spacing)
# Treasure Island Project

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You jumped from your plane and landed in a deep forest...")

move = input("Do you want to go right or left?\nType 'R' for right or 'L' for left: ").upper()

if move == "R":
    print("You've reached a lake.")
    way = input("Do you want to wait for a boat or swim?\nType 'W' to wait or 'S' to swim: ").upper()

    if way == "W":
        print("A boat comes and takes you to an old temple. There are three paths.")
        print("One has a fish symbol, one has a snake, and the other has the moon.")

        path = input("Which path will you take?\nType 'F' for Fish, 'S' for Snake, or 'M' for Moon: ").upper()

        if path == "F":
            print("Oops, you fell into a pool of piranhas! GAME OVER ☠️")
        elif path == "S":
            print("Oh no, you're surrounded by snakes! GAME OVER ☠️")
        elif path == "M":
            print("Congratulations! You found the treasure! You win! 🏆")
        else:
            print("That's not a valid choice. GAME OVER ☠️")

    elif way == "S":
        print("Yikes! The crocodiles got you. GAME OVER ☠️")
    else:
        print("That's not a valid choice. GAME OVER ☠️")

elif move == "L":
    print("You fell into an old well. GAME OVER ☠️")

else:
    print("That's not a valid choice. GAME OVER ☠️")
