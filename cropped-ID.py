import cv2
import os
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image


# Path to the image that needs to be cropped
img_path = 'uncropped-img\ID_example1.jpg'


# x = x coordinate of top-left vertice (O1) of the area that's supposed to be cropped
# y = y coordinate of top-left vertice (O1) of the area that's supposed to be cropped
# width = width of area that's supposed to be cut
# height = height of area that's supposed to be cut
#   O1------O2
#   |        |
#   O3------O4
def crop_img(img_path, x, y, width, height):
    img = cv2.imread(img_path)

    cropped_img = img[y:y+height, x:x+width]
    # included in the cropping: x to x+height
    # included in the cropping: y to y+height
    return cropped_img


uncropped_img = "uncropped-img\ID_example1.jpg"
x, y = 50, 130
width, height = 1000, 95


cropped_img = crop_img(uncropped_img, x, y, width, height)


output_dir = './results-cropped-img'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# If the output folder doesn't exist, this will create it


# READING THE IMAGE -------------------------------------------------------

ocr = PaddleOCR(use_angle_cls=True, lang="en")
result = ocr.ocr(cropped_img, cls=True)


for idx, res in enumerate(result):
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in res]
    txts = [line[1][0] for line in res]
    scores = [line[1][1] for line in res]
    
    output_filename = os.path.join(output_dir, f'ID{idx+1}_name_result.jpg')
    
    im_show = draw_ocr(cropped_img, boxes, txts, scores, font_path='./font/Roboto-Medium.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save(output_filename)


scanned_image = os.path.basename(img_path)
for idx, res in enumerate(result):
    print(f"\n\n****EXTRACTED DATA RESULTS FOR IMAGE: {scanned_image}****\n")
    for line in res:
        print(line)
    print("\n")