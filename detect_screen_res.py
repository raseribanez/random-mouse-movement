# Ben Woodfield 20/01/2019
# Detect your current screen resolution

import pyautogui

# Find the resolution of the users screen
x01, y01 = pyautogui.size()
print("Detected screen resolution of", x01,"X",y01)
print("X=", x01)
print("Y=", y01)
