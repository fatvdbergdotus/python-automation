import pyautogui
# pip install pyautogui

# return the current position of the mouse
print(pyautogui.position())

# Move the mouse to the coordinates (100, 100) in 5 seconds
pyautogui.moveTo(10, 10, duration=5)

# Click the mouse at the current position
pyautogui.click()

# Double click the mouse at the current position
# pyautogui.doubleClick()

# Right click the mouse at the current position
# pyautogui.rightClick()