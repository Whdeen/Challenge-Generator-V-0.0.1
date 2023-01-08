# Imports the Random Module (used for randomization)
import random
# -------------------------------------------------------------


# Introduction & Explaination
def welcome():
    print("Hello, thank you for using this program!")
    print("If you didn't know, this is a program that generates a challenge for you but with a twist!")
    print("The challenges are in different categories which you can select.")
    print("The categories include: Coding, Game Development, and Gaming.")
# -------------------------------------------------------------------------------------------------------------

# Choosing the Category
def choose():
    cat = input("Please choose the category you want the challenge in: ( C for Coding, GD for Game Development, and G for Gaming ) ")
    cat.upper()
    if cat.upper() == "C":
        coding()
    elif cat.upper() == "GD":
        gamedev()
    elif cat.upper() == "G":
        gaming()
    else:
        print("Sorry try again.")
        choose()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# The Coding Category
def coding():
    Coding = ["Code a fully functional calculater","Code a program that makes a fully randomized and unique id","Code a website that allows users to submit videos and view them","Code a traditional game like Rock, Paper, Scissors or any other traditional game"]
    print(random.choices(Coding))
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# The Game Development Category
def gamedev():
    GameDev = ["Make a 2D Platformer game using Pixel Art in 1 day","Make a 3D open world game in 2 Days","Make a 2D Puzzle Game in 2 Days","Make a 3D RPG game in 1 week","Make a Topdown 2D game using Unreal Engine in 1 week",]
    print(random.choices(GameDev))
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gaming Category
def gaming():
    print("Currently available game/s: Fortnite")
    print("More games coming soon")
    print("Your challenge is: ")
    fortchall = ["Win a game with only 1 gun","Win a game with only white weapons","Win a game but your only way of movement is sneaking","Win a game without jumping or mantling","Win a game but you can only kill 3 times"]
    print(random.choices(fortchall))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Initiation
welcome()
choose()
#---------------------------------------------------------------------------------------------------------------------------

# End
print("Thank you so much for using this program :-) Please leave any form of feedback on the Parallel discord server.")
print("-Whdeen")
#------------------------------------------------------------------------------------------------------------------------------

