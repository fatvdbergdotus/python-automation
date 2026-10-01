import pyautogui as py
# pip install pyautogui
import pyperclip
# pip install pyperclip

# return the current position of the mouse
print(py.position())

# Move the mouse to the coordinates (100, 100) in 5 seconds
py.moveTo(10, 10, duration=3)

# Click the mouse at the current position
py.click()

# Double click the mouse at the current position
# py.doubleClick()

# Right click the mouse at the current position
py.rightClick()

# Access the keyboard functions
# Type the text "Hello, World!" at the current cursor position
py.write("Hello, World!\n")
py.hotkey("ctrl", "a") # Select all text at the current cursor position
py.hotkey("ctrl", "c") # Copy the selected text
py.hotkey("ctrl", "v") # Paste the copied text at the current cursor position

# Access the clipboard functions (requires pyperclip)
# print(pyperclip.paste()) # Print the current clipboard content
