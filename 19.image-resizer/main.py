from PIL import Image

def resize_image(width, height):
    image = Image.open("QRImage.png")

    print(f"Current size is: {image.size}")

    resized_image = image.resize((width, height))

    resized_image.save(f"QRImage-{width}.png")
    
width = int(input("> Input Width: " ))
height = int(input("> Input Height: "))
resize_image(width=width, height=height)
