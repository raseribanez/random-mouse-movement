# Ben Woodfield 20/01/2019
# Taken from the pyautogui docs as a tool to help with finding specific resolutions
# I was going to make a clicker that avoided the toolbar for example

import pyautogui, sys

# If you want to see continuous output of mouse position
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
