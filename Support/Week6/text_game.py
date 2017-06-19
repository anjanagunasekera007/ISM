"""
A simple text-based adventure game called: Creepy House.

Available commands include:
    go <compass direction>
    take <object>
    quit
"""
import sys
# current location: hallway, lounge or bedroom
state = "pathway"

# the object that the player is carrying around (or "nothing").
carrying = "nothing"


#####################################################
# Functions for describing the current location


# def describe_bedroom():
#     print("You are in a bedroom.")
#     print("You can see an aquarium and two cricket bats.")

def describe_helipad():
    print("You are at a helipad.")
    print("You see the helicopter waiting there to pick you up and carry you back to civilization the door is open")


def describe_pathway():
    print("You are on a pathway.")
    print("the pathway is damaged from years of exposure to natural elements and barely visible. \n  There is a dagger witha decorated hilt and a decorated compass across your path")


def describe_cave():
    print("You are in a dark cave\nIt is almost black and you can hear bats screeching inside and the howling of the wind, "
          "There is a lamp near your feet. You hear a roar a lion emerges from the cave and preapres to attack.")
    if(carrying=="dagger"):
        print("The lion pounces at you....!!!")
        # sys.exit(34)
    else:
        print("The lion pounces at you\n If only you had a weapon....!!! \n You remember all those times you bragged about being a vegetarian aint gonna save you8 from being meat...!!!")
        state="lion"
        print("Game over")
        sys.exit()
def describe_cave2():
    print("You are in a dark cave\nIt is almost black and you can hear bats screeching inside and the howling of the wind, "
          "There is a lamp near your feet. The dusty remains of the lion blows in the wind towards the inside of the cave")

def describe_forest():
    print("You are in dark forest with giant trees \nIt is thousands of years old. It is alomost impossible to see the sky")
    if (carrying == "compass"):
        print(
            "You wander in to the forest \n Its dark the path you came suddenly disappears\nGood thing you picked up that compass....!!!\n You came east so you have to go west back to the pathway\n"
            "You take out the compass and go west the pathway is there")
    else:
        print(
            "You wander in to the forest \n Its dark the path you came suddenly disappears\n There is no path and no where else to go you are Lost....!!!"
            "If only you had that compass....!!!")
        state = "forest"
        sys.exit()
        print("Game over")
def describe_lake():
    print("You are near a lake \nThe water is black as the night you can see  a dim light shining in the middle of the lake you see a boat with an oar")

def attacklion():
    print(" You hit the lion with the " + str(carrying) + " The lion crumbles in to dust")
    describe_cave2()
# def describe_whirpool():
#     print("You wade in to the lake suddenly you feel a tug on your feet...!!! \n A giant whirpool appears and sucks you in...!!! \n As you get sucked in you realize ' THIS IS THE END....!!!'")

def printmap():
    print("                                 ====== MAP ======                      ")
    print("                                   |----------|                         ")
    print("                                   | Clearing |                         ")
    print("                                   |          |                         ")
    print("                                      |-   -|                           ")
    print("                                      |-   -|                           ")
    print("                                      |-   -|                           ")
    print("                                      /\/\/\/\                          ")
    print("                                      |-   -|                          *")
    print("                                      |-   -|                          *")
    print("                                      |-   -|                          *")
    print("                                    |---   --- |        *(---------****  ")
    print("                                    |---   --- |        *(---------****  ")
    print(" **********                         |---   --- |        *(---------****  ")
    print(" (  (  (  (  \   _____________      |---   ---|         *(---------****  ")
    print(" (  (  (  (   \ (              )    |--     --|       ___|               ")
    print(" (  (  (  (          Cave      -------  PATH   ------|         Forest    ")
    print(" (  ( Lake (  (                -------  WAY    ------|                   ")
    print(" (  (  (  (   / (_____________ )      |      |---   --- *(---------****  ")
    print(" (  (  (  (  /                        |------|          *(---------****  ")
    print("                                                        *(---------****  ")
    print("                                                        *(---------****  ")

def printinventory():
    if(carrying=="nothing"):
        print(" You are not carrying anything ")
    else:
        print(carrying)


def describe():
    """Print a description of the current location."""
    if state == "pathway":
        describe_pathway()
    elif state == "cave":
        describe_cave()
    elif state == "helipad":
        describe_helipad()
    elif state == "forest":
        describe_forest()
    elif state == "lake":
        describe_lake()
    # elif state == "whirpool":
    #     describe_whirpool()
    else:
        print("ERROR: unknown location: " + str(state))


#######################################################
# Functions for moving between locations

def move_cave(direction):
    if direction == "west":
        return "lake"
    elif direction == "east":
        return "pathway"
    return ""

def move_lake(direction):
    if direction == "west":
        return "whirpool"
    if direction == "east":
        return "cave"
    return ""

def move_pathway(direction):
    if direction == "west":
        return "cave"
    elif direction == "east" and carrying == "aquarium":
        return "outside"
    elif direction == "east":
        return "forest"
    elif direction == "north":
        return "helipad"
    return ""


def move_helipad(direction):
    if direction == "north":
        return "HELICOPTER"
    if direction == "south":
        return "pathway"
    return ""

def move_forest(direction):
    if direction == "west":
        return "pathway"
    if direction == "east":
        return "YOUR LOST"
    return ""


def move_cmd(direction):
    """Attempt to move in the given direction.

    This updates the 'state' variable to the new location,
    or leaves it unchanged and prints a warning if the move was not valid.
    :param direction: a compass direction, "north", "east", "south", or "west".
    :return: None
    """
    global state
    if state == "pathway":
        new_state = move_pathway(direction)
    elif state == "cave":
        new_state = move_cave(direction)
    elif state == "lake":
        new_state = move_lake(direction)
    elif state == "forest":
        new_state = move_forest(direction)
    elif state == "helipad":
        new_state = move_helipad(direction)
    else:
        print("WARNING: move_cmd sees unknown state: " + state)
        new_state = ""
    # now check to see if it was a valid move
    if new_state == "":
        print("You cannot go " + str(direction) + " from here.")
    else:
        state = new_state


#########################################################
def take_cmd(obj):
    """Try to pick up the given object.
    Most objects can only be picked up when in the correct room.
    """
    global carrying
    if obj == "boat" and state == "lake":
        print("You drop " + carrying + " and pick up an oar and get in the boat.")
        carrying = obj
    elif obj == "lamp" and state == "cave":
        print("You drop " + carrying + " and pick up the lamp and stare in to the cave you see a distant light probably sunlight")
        carrying = obj
    elif obj == "dagger" and state == "pathway":
        print("You drop " + carrying + " and pick up the dagger, you notice that the hinge is rotatable")
        carrying = obj
    elif obj == "compass" and state == "pathway":
        print("You drop " + carrying + " and pick up the Compass, It weighs a lot")
        carrying = obj
    else:
        print("You cannot pick that up!")

def rotate_cmd(obj):
      """Try to pick up the given object.
      Most objects can only be picked up when in the correct room.
      """
      global carrying
      if obj == "dagger" and state == "pathway":
          print("You roatate the hilt and it turns and elonagates to a mighty sword.")
          carrying = obj
#########################################################
# The main loop that processes the player's input commands.
def main():
    for turn in range(20, 0, -1):
        print("")
        describe()
        cmd = input("Enter your command " + str(turn) + "> ")
        if cmd == "quit":
            print("You gave in so easily :-(")
            break
        elif cmd.startswith("go "):
            where = cmd[3:]
            move_cmd(where)
            if state == "whirpool":
                print("You wade in to the lake suddenly you feel a tug on your feet...!!! \n A giant whirpool appears and sucks you in...!!! \n As you get sucked in you realize ' THIS IS THE END....!!!'")
                break
            if state == "HELICOPTER":
                print("You go to the helicopter and get in. The pilot lifts the helicopter and pull away from the helipad and head towards civilization. You won the challange....!!!")
                break
            if state == "lion":
                print("")
                break
        elif cmd.startswith("take "):
            obj_name = cmd[5:]
            take_cmd(obj_name)
        elif cmd.startswith("rotate "):
            obj_name = cmd[7:]
            rotate_cmd(obj_name)
        elif cmd.startswith("turn "):
            obj_name = cmd[5:]
            rotate_cmd(obj_name)
        elif cmd=="map":
            # obj_name = cmd[5:]
            printmap()
        elif cmd=="inventory":
            # obj_name = cmd[5:]
            printinventory()
        elif cmd=="attack":
            # obj_name = cmd[5:]
            atacklion()
        else:
            print("I do not understand '" + cmd + "'.  Try go/take/quit")
    print("Game over")


if __name__ == "__main__":
    main()
