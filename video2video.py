# This will make a Command Line ASCII Video from the Input Video

import cv2
import os
import sys
from cv2 import line
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont

# Characters used for Mapping to Pixels
Character = {
    "standard": "@%#+=-:. ",
    "complex": "$@B%8&WM#oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:," ^`'. "
}


def get_data(mode):
    scale = 2
    char_list = Character[mode]
    return char_list, scale


# Getting the character List, Font and Scaling characters for square Pixels
char_list, scale = get_data("complex")
num_chars = len(char_list)
num_cols = 100

#Reading the video file
cap = cv2.VideoCapture("inputvideo.mp4")

while True:
    # Reading Video Framewise
    ret, image = cap.read()

    # Converting Color Image to Grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Extracting height and width from Image
    height, width = image.shape

    # Defining height and width of each cell==pixel
    cell_w = width / num_cols
    cell_h = scale * cell_w
    num_rows = int(height / cell_h)

    # Mapping the Characters
    # ascii_frame=""
    for i in range(num_rows):
        min_h = min(int((i + 1) * cell_h), height)
        row_pix = int(i * cell_h)
        line = "".join([char_list[min(int(np.mean(image[row_pix:min_h, int(jcell_w):min(int((j + 1) cell_w), width)]) / 255 * num_chars), num_chars - 1)]for j in range(num_cols)]) + "\n"
        cv2.imshow("frame", image)
        sys.stdout.write(line)
    os.system('cls' if os.name == 'nt' else 'clear')
    cv2.waitKey(1)
