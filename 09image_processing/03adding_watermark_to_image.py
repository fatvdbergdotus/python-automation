import cv2

# adding watermark to image
image = cv2.imread("elfs.jpeg")
watermark_image = cv2.imread("watermark.png")

# get dimensions of the image
image_height, image_width = image.shape[:2]
watermark_height, watermark_width = watermark_image.shape[:2]

# set position for watermark (bottom-right corner)
x_offset = image_width - watermark_width
y_offset = image_height - watermark_height

# add somewhat transparent watermark to image
alpha = 0.5
image[y_offset:y_offset+watermark_height, x_offset:x_offset+watermark_width] = cv2.addWeighted(
    image[y_offset:y_offset+watermark_height, x_offset:x_offset+watermark_width], 1 - alpha,
    watermark_image, alpha, 0
)

# save the result
cv2.imwrite("elfs_with_watermark.jpeg", image)