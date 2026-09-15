import cv2

# Blur faces in a video using OpenCV
video = cv2.VideoCapture("smile.mp4")
success, frame = video.read()
height = int(video.get(4))
width = int(video.get(3))

giraffe_pic = cv2.imread("giraffe.jpeg")

face_cascade = cv2.CascadeClassifier("faces.xml")

output = cv2.VideoWriter("output_smile.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 30, (width, height))
output2 = cv2.VideoWriter("output_smile2.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 30, (width, height))
output3 = cv2.VideoWriter("output_smile3.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 30, (width, height))

# Process each frame of the video and blur detected faces
while success:
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    frame2 = frame.copy()
    frame3 = frame.copy()

    for (x, y, w, h) in faces:
        # Extract the face region from the frame
        face = frame[y:y+h, x:x+w]
        face2 = frame2[y:y+h, x:x+w]
        face3 = frame3[y:y+h, x:x+w]

        # Apply Gaussian blur to the face region
        face = cv2.GaussianBlur(face, (99, 99), 30)

        # Apply censuring to the face region (black)
        face2[:] = 0

        # Apply giraffe picture to the face region
        face3[:] = cv2.resize(giraffe_pic, (w, h))

        # Replace the original face region with the blurred/black version
        frame[y:y+h, x:x+w] = face
        frame2[y:y+h, x:x+w] = face2
        frame3[y:y+h, x:x+w] = face3

    output.write(frame)
    output2.write(frame2)
    output3.write(frame3)
    success, frame = video.read()

output.release()
output2.release()
output3.release()
video.release()