import qrcode

# Data to encode
data = "https://github.com/NashrahFatima28/qrcode_genrator"  # Replace with your text or URL

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Create and save image
img = qr.make_image(fill="black", back_color="white")
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'")
