#!/bin/python3
# encoding: utf-8

import pytesseract as tesseract
import os.path
import re
from PIL import Image, ImageEnhance, ImageFilter

def img_to_string(img_obj):
    """
    Convert the image to grayscale, extract string from the grayscale image,
    split the string by new line character, return an empty list if no string found.
    """
    obj = img_obj.convert("L")
    enh = ImageEnhance.Contrast(obj).enhance(1.3).filter(ImageFilter.EDGE_ENHANCE)
    enh.show()
    raw_str = tesseract.image_to_string(enh)
    raw_str = raw_str and re.split("[\n|\r|\r\n]+", raw_str) or []
    return raw_str

def color_invert(img_obj):
    return ImageOps.invert(enh)



if __name__ == '__main__':
    f1 = os.path.expanduser('~/Desktop/123.png')
    f2 = os.path.expanduser('~/Desktop/2.png')
    # print(img_to_string(Image.open(f1)))
    print(img_to_string(Image.open(f2)))