# Day 6: Functions, Code Blocks, and While Loops
# Maze Project
# URL: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# To get out of the maze, the robot should move along right (or left) wall until it reaches the goal. This gives two cases:
# Case 1: If there is no wall on the right, keep turning and moving until the robot has a wall on its right side.
# Case 2: If there is a wall on the right, the robot should continue moving forward from the position it starts.

while not at_goal():
    while right_is_clear():
        turn_right()
        if not wall_in_front():
            while not wall_in_front():
                move()

    while wall_on_right():
        if front_is_clear():
            move()
        elif wall_in_front():
            turn_left()
#(this satisfies 2 in 3 robo bugs)

# Refined Version (Mam's version):
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()

# 3 Robo Bugs fixed
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
