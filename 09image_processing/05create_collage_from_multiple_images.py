import cv2
import glob
import numpy as np
import math
import os

# Create a collage from multiple images in the "collage" directory, excluding the result image itself.
collage_images = []

# Read all image files from the "collage" directory, excluding the result image itself.
for filename in glob.glob("collage/*.*"):
    if filename.lower().endswith((".jpeg", ".jpg", ".png")) and not filename.lower().endswith("collage_result.jpeg"):
        image = cv2.imread(os.path.abspath(filename))

        if image is not None:
            collage_images.append(image)

# If there are any images, create the collage.
if collage_images:
    # Get the height and width of the first image to use as the standard size for all images.
    img_height, img_width = collage_images[0].shape[:2]

    cols = math.ceil(math.sqrt(len(collage_images)))
    rows = math.ceil(len(collage_images) / cols)

    # Create an empty collage image with the calculated number of rows and columns.
    collage = np.zeros(
        (rows * img_height, cols * img_width, 3),
        dtype=np.uint8
    )

    # Place each image in the appropriate position within the collage.
    for idx, img in enumerate(collage_images):
        img = cv2.resize(img, (img_width, img_height))

        row = idx // cols
        col = idx % cols

        collage[
            row * img_height:(row + 1) * img_height,
            col * img_width:(col + 1) * img_width
        ] = img

    # Save the final collage image to the "collage" directory.
    cv2.imwrite("collage/collage_result.jpeg", collage)