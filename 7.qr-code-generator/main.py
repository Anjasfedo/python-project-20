import qrcode
import os

def generateQrCode(text):
    # Create a QRCode object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add the input text to the QRCode
    qr.add_data(text)
    
    # Generate the QRCode with fit=True
    qr.make(fit=True)
    
    # Create an image from the QRCode with specified colors
    img = qr.make_image(fill_color="black", back_color="white")

    # Specify the save directory (absolute path) and create it if it doesn't exist
    save_directory = os.path.abspath("images")
    os.makedirs(save_directory, exist_ok=True)
    
    # Specify the image path and save the QRCode image
    img_path = os.path.join(save_directory, "QRImage.png")
    img.save(img_path)
    
    # Print the path where the QRCode is saved
    print(f"QR Code saved at: {img_path}")

# Take user input for the URL
url = input("> Enter the URL: ")    

# Generate and save the QRCode
generateQrCode(text=url)
