# random-mouse-movement
a short collection of programs that simulate mouse movement to prevent things like screen lock

I recommend using mouse_mover_timed

In short, this whole idea came from a problem I had yesterday. I was downloading and installing a huge file, I left the computer on in the back room, but every time it locked or went to sleep, the processes stopped.

So rather than editing the whole setup of my power and sleep settings I wanted to write a short program to move the mouse around and stop the computer going idle and locking up.

I just wanted to simulate some mouse movement, regularly.

The programs included here have 2 methods of doing this.

*Ask the user how many times to move the mouse (not efficient at all)
*Ask the user how long to keep moving the mouse around for (much better)

Along the way I learnt some little tricks with the pyautogui module.

I added a feature that detects the users screen resolution, and creates random coordinates within those paramaters so this will work for ANY screen size.

What you will need? 
* Python3 (https://www.python.org/) 
* Pyautogui (pip install pyautogui, or go here for the download and the documentation too https://pypi.org/project/PyAutoGUI/)

PLANS AND IMPROVEMENTS? 
I am looking at using something like py2exe to create a package that removes the requirement of installing Python and pyautogui so the end user (if they are a Windows user) can just run it as a .exe file
