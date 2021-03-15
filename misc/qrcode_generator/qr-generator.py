#!/usr/bin/env python3

# Import dependencies
import qrcode
import sys

# Define variables
input_data = sys.argv[1]
img_name = str(sys.argv[2]) + ".png"

# Create qrcode instance
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)

# Build and write QR image file
img = qr.make_image(fill='black', back_color='white')
img.save(img_name)
