import cv2
import os

# resize multiple images
for filename in os.listdir('.'):
    if filename.endswith('.jpeg') and not filename.endswith('_greyscale.jpeg') and not filename.endswith('_resized.jpeg'):
        # Load the image
        image = cv2.imread(filename)

        # Resize the image to 800x600
        resized_image = cv2.resize(image, (800, 600))

        # Save the resized image
        cv2.imwrite(f'{os.path.splitext(filename)[0]}_resized.jpeg', resized_image)
        print(f'Resized {filename} to 800x600.')
