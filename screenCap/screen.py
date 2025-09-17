import cv2
import numpy as np
import mss
import pygetwindow as gw

# Set the name of the window you want to capture
WINDOW_TITLE = "Guilty Gear -Strive-"  # Replace with your game window's title

# Find the window
window = None
for w in gw.getWindowsWithTitle(WINDOW_TITLE):
    if w.visible:
        window = w
        break

if not window:
    raise Exception(f"Window titled '{WINDOW_TITLE}' not found or not visible.")

# Get window's position and size
left, top = window.left, window.top
width, height = window.width, window.height

region = {
    "top": top,
    "left": left,
    "width": width,
    "height": height
}

# Use mss to capture that region
with mss.mss() as sct:
    while True:
        screenshot = sct.grab(region)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        cv2.imshow("Window Capture", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cv2.destroyAllWindows()