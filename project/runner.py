import pytest

from _test import test_runner

def create_runner(x: int = 0, y: int = 0, orientation: str = "N"):
    '''
    creates a runner corresponding to the input parameters. The types for the arguments are given as type hints. You should set the default values \
    for the parameters such that the runner will start from the (0,0) coordinate and face North by default. You do not need to check the validity of the input for now. \
    In particular, you can assume that the orientation is one of the 4 given directions, i.e., "N", "E", "W", "S".
    '''
    runner = (x, y, orientation)
    return runner

def get_x(runner):
    # returns the x-coordinate for the input runner. Here the input runner is the same type you use for the output of the create_runner() function.
    return runner[0]


def get_y(runner):
    # returns the y-coordinate for the input runner. Here the input runner is the same type you use for the output of the create_runner() function.
    return runner[1]

def get_orientation(runner):
    #  returns the orientation for the input runner. Here the input runner is the same type you use for the output of the create_runner() function.
    return runner[2]

def get_orientation_index(runner):
    point = ["N", "E", "S", "W"]
    orientation_index = get_orientation(runner)
    return point.index(orientation_index)


def turn(runner, direction: str):
    # ''' -- turn the runner to either "Left" or "Right", the function will return the runner after the turn. The runner's position should not change, \
    # but the runner's orientation will change according to the direction of the turn. For example, if the runner is currently facing north ("N"), \
    # turn(runner, "Left") must return a runner at the same position and facing west ("W").
    # '''
    
    point = ["N", "E", "S", "W"]

    

    current_index = get_orientation_index(runner)
    if direction == "Right":
        new_index = (current_index + 1) % len(point)
    elif direction == "Left":
        new_index = (current_index - 1) % len(point)
    else:
        raise ValueError("Invalid direction: Use 'Left' or 'Right'.")
    
    runner = (get_x(runner), get_y(runner), point[new_index])

    return runner

def forward(runner):
    # ''' - move the runner forward 1 cell, the function will return the runner after the move. The runner's orientation will be the same, \
    # but the position will change according to the runner's orientation. For example, if the runner (at position (5, 2)) \
    # in the figure above is facing "N" and moving forward, they will be in position (5, 3).
    # '''
    where = get_orientation_index(runner) # supposdly youre going to check if its 1 or 3 the y will change else x will change
    y = get_y(runner)
    x = get_x(runner)
    point = ["N", "E", "S", "W"]
    

    if where == 0:
        y += 1
        # orientation = "N"

    if where == 1:
        x += 1
        # orientation = "W"

    if where == 2:
        y -= 1
        # orientation = "S"

    if where == 3:
        x -= 1
        # orientation = "E"
    # return (x, y, orientation)
    runner = (x, y, point[where])
    return runner


# '''
# BY THIS STAGE you should have a module named runner.py containing the above functions. You can create some validate your implementation by creating a runner \
# , calling the movement functions (i.e., turn(runner) and forward(runner)) and checking their position and orientation (with get_x(runner), \
# get_y(runner), and get_orientation(runner)).
# '''

# # Test Case 1: Moving from the origin with different directions
# runner1 = create_runner(0, 0, "W")  # Create a runner facing West
# runner1 = turn(runner1, "Right")    # Turn right (facing North)
# print(forward(runner1))  # Expected: (0, 1, "N") Moving North

# # Test Case 2: Turn right twice, then move
# runner2 = create_runner(0, 0, "W")  # Create a runner facing West
# runner2 = turn(runner2, "Right")    # Turn right (facing North)
# runner2 = turn(runner2, "Right")    # Turn right (facing East)
# print(forward(runner2))  # Expected: (1, 0, "E") Moving East

# # Test Case 3: Turn left twice, then move
# runner3 = create_runner(0, 0, "W")  # Create a runner facing West
# runner3 = turn(runner3, "Left")     # Turn left (facing South)
# runner3 = turn(runner3, "Left")     # Turn left (facing East)
# print(forward(runner3))  # Expected: (1, 0, "E") Moving East

# # Test Case 4: Turn right and left, then move
# runner4 = create_runner(0, 0, "N")  # Create a runner facing North
# runner4 = turn(runner4, "Right")    # Turn right (facing East)
# runner4 = turn(runner4, "Left")     # Turn left (facing North)
# print(forward(runner4))  # Expected: (0, 1, "N") Moving North

# # Test Case 5: Start facing East and move forward
# runner5 = create_runner(0, 0, "E")  # Create a runner facing East
# print(forward(runner5))  # Expected: (1, 0, "E") Moving East

runner6 = create_runner(75,-78, "W")
runner6 = turn(runner6, "Left")
print(forward(runner6))  # Expected: (75, -79, "S") Moving South


runner6 = turn(runner6, "Left")
print(forward(runner6))  # Expected: (76, -79, "E") Moving East


runner7 = create_runner(-75,78, "S")
runner7 = turn(runner7, "Right")    # Turn right (facing west)
print(forward(runner7)) # Expected: (-76, 78, "E") Moving East


runner7 = turn(runner7, "Right")    # Turn right (facing north)
print(forward(runner7)) # Expected: (-77, 79, "E") Moving East

