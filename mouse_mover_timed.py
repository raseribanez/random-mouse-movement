# Ben Woodfield  20/01/2019
# Set a timer for how long you want random mouse movements to run for (minutes)
# Detects users screen resolution nd stays within these paramaters

import pyautogui, random, time

# Find the resolution of the users screen
x01, y01 = pyautogui.size()
print("Detected screen resolution of ",x01," X ",y01)
print("X =", x01)
print("Y =", y01)
print("\n\n\n")

# Ask the user how many minutes to run the program for
amount=int(input("How long in minutes do you want this to run for? \nPlease use a whole number with 1 being the lowest (1 minute)\n>>> " ))
print("To kill the program before the timer ends use CTRL+C")

# Create random coordinates within users screen size and move mouse there
# Do it continuosly for the time sated
t_end = time.time() + 60 * amount
while time.time() < t_end:
    for x in range(10):
        x02 = random.randint (0, x01)
        y02 = random.randint (0, y01)
        pyautogui.moveTo(x02, y02)
     
    
