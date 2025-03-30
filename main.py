import qrcode

# Your GitHub homepage URL
github_url = "https://github.com/yourusername"

# Generate the QR code
qr = qrcode.make(github_url)

# Save the image
qr.save("github_qr_code.png")

print("QR Code generated and saved as github_qr_code.png")
