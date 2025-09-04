import qrcode
from PIL import Image

#  QR Object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# data for qr code
qr.add_data("# link that you want to convert in qr")
qr.make(fit=True)

# change color 
img = qr.make_image(fill_color = "green" , back_color="white")

img.save("Portfolio.png")