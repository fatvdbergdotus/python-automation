import qrcode
# py -m pip install qrcode
import cv2
# pip install opencv-python

image = "qrcode_generated.png"
url = "https://www.vdberg.us"

# generate a QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(image)


# generate multiple QR codes from file urls.txt
with open("urls.txt") as f:
    urls = f.read().splitlines()

for i, url in enumerate(urls):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"qrcode_generated_{i}.png")