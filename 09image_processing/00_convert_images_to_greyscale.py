import cv2
import os

# convert multiple images to greyscale
for filename in os.listdir('.'):
    if filename.endswith('.jpeg') and not filename.endswith('_greyscale.jpeg') and not filename.endswith('_resized.jpeg'):
        # Load the image
        image = cv2.imread(filename)

        # Convert the image to greyscale
        grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Save the greyscale image
        cv2.imwrite(f'{os.path.splitext(filename)[0]}_greyscale.jpeg', grey_image)
        print(f'Converted {filename} to greyscale.')

