import json
from PIL import Image, ImageDraw, ImageFont


img = Image.open("ExampleDocument_page-0001.jpg")

textbox_coordinates = (240, 210, 740, 210)

with open("data_test4.json") as json_file:
    data = json.load(json_file)

draw = ImageDraw.Draw(img)
font = ImageFont.truetype("font\Roboto-Medium.ttf", 12)

data_to_print = "Test data: {}".format(data)

draw.text(textbox_coordinates[:2], data_to_print, font=font, fill=(0,0,0))

img.save("FilledDocumentImg.jpg")


