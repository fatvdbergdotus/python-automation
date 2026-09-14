import cv2
import numpy as np

# adding watermark to image
image = cv2.imread("giraffe.jpeg")
background_image = cv2.imread("safari.jpeg")

# get dimensions of the images
image_height, image_width = image.shape[:2]
background_height, background_width = background_image.shape[:2]

# resize background to match image size
background_image = cv2.resize(background_image, (image_width, image_height))

# determine the color of the top-left pixel of the background image and convert them to numbers
image_pixel_color = image[0][0].tolist()
print(image_pixel_color)

# replace pixels in the image that match the background color with the corresponding pixels from the new background
for i in range(image_width):
    for j in range(image_height):
        pixel = image[j, i]
        if np.any(pixel == [1,255,0]):
            image[j, i] = background_image[j, i]

# save the modified image with the new background
cv2.imwrite("giraffe_with_new_background.jpeg", image)