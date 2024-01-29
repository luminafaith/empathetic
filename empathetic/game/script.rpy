# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define a = Character("Anna")
# Main script for the demo!

define n = Character("You")

# NVL characters are used for the phone texting
define n_nvl = Character("You", kind=nvl)
define e_nvl = Character("Eileen", kind=nvl)
define a_nvl = Character("Anna", kind=nvl)



# The game starts here.

label start:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # Example of receiving a new message  

    #Phone conversation start
    nvl_narrator "Added Eileen to the group"
    nvl_narrator "Added Anna to the group"
    n_nvl "Hey! Welcome to the demo guys!"
    e_nvl "who's this?"
    a_nvl "Hi Eileen! I'm Anna, nice to meet you!"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
