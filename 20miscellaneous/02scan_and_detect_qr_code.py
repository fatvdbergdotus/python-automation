import cv2
# pip install opencv-python

import webbrowser

image = cv2.imread("qr.png")

# Initialize the QR code detector and detect the QR code in the image
detector = cv2.QRCodeDetector()
url, bbox, pixels = detector.detectAndDecode(image)
if url:
    print(f"QR Code data: {url}")
else:
    print("QR Code not detected")

# The 'pixels' variable contains the pixel data of the detected QR code region
# Display the pixel data of the detected QR code region if available
#if pixels is not None:
#    cv2.imshow("QR Code", pixels)
#    cv2.waitKey(0)
    cv2.destroyAllWindows()

webbrowser.open(url)

