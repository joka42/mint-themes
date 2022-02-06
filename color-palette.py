import cv2
import numpy as np

from constants import y_hex_colors1, y_hex_colors2, y_hex_colors3, y_hex_colors4

def hex_to_rgb(hex):
    h = hex.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def bgr_to_hex(bgr_color):
    return '#%02x%02x%02x' % (bgr_color[2], bgr_color[1], bgr_color[0])

def hex_to_bgr(hex):
    h = hex.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (4, 2, 0))

def color_to_npArray(color):
    color_array = np.zeros((1,1,len(color)), np.uint8)
    color_array[0][0] = color
    return color_array

def shade(bgr_color, saturate, shade):
    hsv = cv2.cvtColor(color_to_npArray(bgr_color), cv2.COLOR_BGR2HSV)
    
    saturation = int(hsv[0][0][1] * saturate)
    if saturation > 255:
        saturation = 255
    hsv[0][0][1] = saturation

    shading = int(hsv[0][0][2] * shade)
    if shading > 255:
        shading = 255
    hsv[0][0][2] = shading
    
    shaded_color_array = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return tuple(shaded_color_array[0][0])

mint_colors = y_hex_colors1.keys()

image = np.zeros((len(mint_colors) * 2, 4, 3), np.uint8)

for i, color in enumerate(mint_colors):
    image[i*2][0] = hex_to_bgr(y_hex_colors1.get(color))
    image[i*2][1] = hex_to_bgr(y_hex_colors2.get(color))
    image[i*2][2] = hex_to_bgr(y_hex_colors3.get(color))
    image[i*2][3] = hex_to_bgr(y_hex_colors4.get(color))

    base_color = hex_to_bgr(y_hex_colors1.get(color))

    generated_colors = (base_color, 
            shade(base_color, 0.95, 0.94), 
            shade(base_color, 0.78, 1.0), 
            shade(base_color, 1.0, 0.76))

    for j, generated_color in enumerate(generated_colors):
        image[i*2 + 1][j] = generated_color
        # print(i, bgr_to_hex(color))

height = len(image) * 50
width = len(image[0]) * 100

image = cv2.resize(image, (width, height), interpolation = cv2.INTER_AREA)
cv2.imwrite("out/palette.png", image)