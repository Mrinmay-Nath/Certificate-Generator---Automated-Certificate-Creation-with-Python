import cv2
import matplotlib.pyplot as plt

def click_event(event):
    if event.button == 1:  # Left mouse button.
        coordinates = (int(event.xdata), int(event.ydata))
        print(f"(x-coordinate (horizontal position from the left): {coordinates[0]}, y-coordinate (vertical position from the top): {coordinates[1]})")

img = cv2.imread('certificate-template.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert color from BGR to RGB.

# Calculate the middle point
height, width, _ = img.shape
middle_point = (width // 2, height // 2)

print(f"Middle point of the image: (x-coordinate (horizontal position from the left): {middle_point[0]}, y-coordinate (vertical position from the top): {middle_point[1]})")

fig, ax = plt.subplots()
ax.imshow(img)
fig.canvas.mpl_connect('button_press_event', click_event)

plt.show()