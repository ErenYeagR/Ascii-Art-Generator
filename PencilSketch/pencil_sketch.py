import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont

# Characters used for Mapping to Pixels
Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}

def get_data(mode):
    font = ImageFont.truetype("fonts/arial.ttf", size=20)
    scale = 2
    char_list = Character[mode]
    return char_list, font, scale

# Making Background Black or White
bg = "white"
# bg = "black"
if bg == "white":
    bg_code = 255
elif bg == "black":
    bg_code = 0

# Getting the character List, Font and Scaling characters for square Pixels
char_list, font, scale = get_data("complex")
num_chars = len(char_list)
num_cols = 300

image = cv2.imread("./PencilSketch/Input/Input3.jpg")  # Reading Input Image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

inverted_gray_image = 255-gray_image  # Making the Pencil Sketch of Input Image
blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

inverted_blurred_image = 255-blurred_image
pencil_sketch_image = cv2.divide(
    gray_image, inverted_blurred_image, scale=256.0)
image = pencil_sketch_image

height, width = image.shape  # Extracting height and width from Image

cell_w = width / num_cols   # Defining height and width of each cell==pixel
cell_h = scale * cell_w
num_rows = int(height / cell_h)

char_width, char_height = font.getsize("A") # Calculating Height and Width of the output Image
out_width = char_width * num_cols
out_height = scale * char_height * num_rows

out_image = Image.new("L", (out_width, out_height), bg_code)    # Making a new Image using PIL
draw = ImageDraw.Draw(out_image)

# Mapping
for i in range(num_rows):
    min_h = min(int((i + 1) * cell_h), height)
    row_pix = int(i * cell_h)
    line = "".join([char_list[
        min(int(
            np.mean(image[row_pix:min_h, int(j*cell_w)
                    :min(int((j + 1) * cell_w), width)]) / 255 * num_chars
        ), num_chars - 1)]
        for j in range(num_cols)]) + "\n"

    draw.text((0, i * char_height), line, fill=255-bg_code, font=font)

if bg == "white":
    cropped_image = ImageOps.invert(out_image).getbbox()
elif bg == "black":
    cropped_image = out_image.getbbox()

# Saving the new Image
out_image = out_image.crop(cropped_image)
out_image.save("./PencilSketch/Output/Output3.jpg")
