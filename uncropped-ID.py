import os
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image


output_dir = './results-uncropped-img'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# If the output folder doesn't exist, this will create it


# Initializing the paddleOCR class
ocr = PaddleOCR(use_angle_cls=True, lang="en")
img_path = './uncropped-img/ID_example1.jpg'


# Actual OCR happens here
result = ocr.ocr(img_path, cls=True)


for idx, res in enumerate(result):
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in res]
    txts = [line[1][0] for line in res]
    scores = [line[1][1] for line in res]
    
    output_filename = os.path.join(output_dir, f'result_IDexample{idx+1}.jpg')
    
    im_show = draw_ocr(image, boxes, txts, scores, font_path='./font/Roboto-Medium.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save(output_filename)


# Print results in the terminal as well
for idx, res in enumerate(result):
    print(f"\n\n****EXTRACTED DATA RESULTS FOR IMAGE: {os.path.basename(img_path)}****\n")
    for line in res:
        print(line)
    print("\n")