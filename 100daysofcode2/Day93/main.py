import time
import pyautogui

# Function to check if the dinosaur can jump
def can_jump():
    # Check for the presence of a cactus
    # Adjust the coordinates based on your screen resolution and position of the game
    pixel = pyautogui.pixel(550, 350)
    if pixel[0] == 83 and pixel[1] == 83 and pixel[2] == 83:
        return False
    return True

# Function to make the dinosaur jump
def jump():
    # Press the spacebar key to make the dinosaur jump
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')

# Main game loop
while True:
    if can_jump():
        jump()
    # Adjust the sleep time based on your screen refresh rate and game speed
    time.sleep(0.1)
