from mss import MSS, tools
# py -m pip install mss
import time

# Take a full-screen screenshot and save it as 'screenshot.png'
with MSS() as sct:
    screenshot = sct.shot(output='screenshot.png')
    print(f'Full-screen screenshot taken: screenshot.png')

# Take a partial screenshot and save it as 'partial_screenshot.png'
with MSS() as sct:
    monitor = {"top": 100, "left": 100, "width": 500, "height": 400}
    image = sct.grab(monitor)
    tools.to_png(image.rgb, image.size, output='partial_screenshot.png')
    print(f'Partial screenshot taken: partial_screenshot.png')

# Take a screenshot of a specific monitor and save it as 'monitor_screenshot.png'
with MSS() as sct:
    monitor = sct.monitors[1]  # Change the index to select a different monitor
    image = sct.grab(monitor)
    tools.to_png(image.rgb, image.size, output='monitor_screenshot.png')
    print(f'Monitor screenshot taken: monitor_screenshot.png')

# Take a screenshot every 10 seconds and store it as 'screenshot_<timestamp>.png'
with MSS() as sct:
    while True:
        timestamp = int(time.time())
        screenshot = sct.shot(output=f'screenshot_{timestamp}.png')
        print(f'Screenshot taken: screenshot_{timestamp}.png')
        time.sleep(10)