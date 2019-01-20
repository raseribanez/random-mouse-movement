# Ben Woodfield 20/01/2019
# moves mouse in a random location as many times as the user decides
# detects users resolution then always stays within those paramaters

import pyautogui, random, sys

count = 0

# Find the resolution of the users screen
x01, y01 = pyautogui.size()
print("Detected screen resolution of ",x01," X ",y01)
print("X =", x01)
print("Y =", y01)
print("\n")

# Ask user how many times to move the mouse
amount=int(input("How many random mouse movements do you want? \nPlease enter a whole number \n>>> "))

# Create random coordinates within users screen resolution and move mouse there
while (count <= amount):
    for x in range(10):
        x02 = random.randint (0, x01)
        y02 = random.randint (0, y01)
        pyautogui.moveTo(x02, y02)
        count = count+1



