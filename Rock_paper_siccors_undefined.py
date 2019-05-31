# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if user_choice == "r" and computer_choice == "p":
    print("I chose Rock. Computer chose paper")
    print("I lose the game.")
elif user_choice  == "r" and computer_choice == "s":
    print("I chose Rock. Computer chose Scissors.")
    print("I won the game!")
elif user_choice == "r" and computer_choice == "r":
    print("I chose rock. Computer chose rock.")
    print("It's a draw retry!")
 
elif user_choice == "p" and computer_choice == "r":
    print("I chose paper. Computer chose rock.")
    print("Sweet I won the game!")
else:  
    print("Game complete.")
    