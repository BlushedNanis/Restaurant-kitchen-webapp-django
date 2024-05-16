from qrcode import make

# Creates a QR code for the clients to scan it with their phone and access the menu.
qr_image = make("https://127.0.0.1:8000")
qr_image.save("qr.png")