from PIL import Image, ImageFont, ImageDraw
import socket
import random

def generateIp():
    ip = f"{random.randrange(1, 255)}.{random.randrange(1, 255)}.{random.randrange(1, 255)}.{random.randrange(1, 255)}"

    my_image = Image.open("brogle.jpg")
    x, y = my_image.size
    title_font = ImageFont.truetype("aakar-medium", 90)
    title_text = ip
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((90 / 2, y / 2), title_text, (999, 999, 999), font=title_font)
    my_image.save("result.jpg")