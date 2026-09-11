# install opencv version 4
# py -m pip install "opencv-python<5"
import cv2
import os

# detect humans faces in images
# load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier("faces.xml")

# load the image
image = cv2.imread('humans.jpeg')

# detect faces
faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# draw rectangles around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# save the output image
cv2.imwrite('humans_detected.jpeg', image)


# detect human faces in multiple images
for image_file in os.listdir('.'):
    if not image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
        continue
    image = cv2.imread(image_file)
    faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if len(faces) > 0:
        print(f"Detected {len(faces)} faces in {image_file}")
    else:
        print(f"No faces detected in {image_file}")
