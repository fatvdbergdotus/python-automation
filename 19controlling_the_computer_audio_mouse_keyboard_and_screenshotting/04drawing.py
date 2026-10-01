import pyautogui as py

# Open https://jspaint.app/ to draw using the mouse

# Draw a line using the mouse
def draw_line(start_x, start_y, end_x, end_y, duration=2):
    py.moveTo(start_x, start_y)
    py.mouseDown()
    py.moveTo(end_x, end_y, duration=duration)
    py.mouseUp()

# Draw a rectangle
draw_line(200, 200, 200, 400, 1) # Left vertical line of the rectangle
draw_line(200, 400, 250, 400, 1) # Bottom left horizontal line of the rectangle
draw_line(250, 390, 300, 390, 1)
draw_line(250, 410, 300, 410, 1)
draw_line(250, 390, 250, 410, 1) # Left vertical line of the small rectangle
draw_line(300, 390, 300, 410, 1) # Right vertical line of the small rectangle
draw_line(300, 400, 400, 400, 1) # Bottom right horizontal line of the rectangle
draw_line(400, 400, 400, 280, 1) # Right vertical line of the rectangle
draw_line(400, 230, 400, 200, 1) # Top right vertical line of the rectangle
draw_line(400, 200, 200, 200, 1) # Top horizontal line of the rectangle


