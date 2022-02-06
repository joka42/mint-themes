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

def shade(bgr_color, factor):
    hsv = cv2.cvtColor(color_to_npArray(bgr_color), cv2.COLOR_BGR2HSV)
    value = int(hsv[0][0][2] * factor)
    if value > 255:
        value = 255
    hsv[0][0][2] = value
    shaded_color_array = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return tuple(shaded_color_array[0][0])

def saturate(bgr_color, factor):
    hsv = cv2.cvtColor(color_to_npArray(bgr_color), cv2.COLOR_BGR2HSV)
    value = int(hsv[0][0][1] * factor)
    if value > 255:
        value = 255
    hsv[0][0][1] = value
    shaded_color_array = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return tuple(shaded_color_array[0][0])

image = np.zeros((2, 4, 3), np.uint8)

default_color = "Tela"
base_color = hex_to_bgr(y_hex_colors1.get(default_color))

image [1][0] = hex_to_bgr(y_hex_colors1.get(default_color))
image [1][1] = hex_to_bgr(y_hex_colors2.get(default_color))
image [1][2] = hex_to_bgr(y_hex_colors3.get(default_color))
image [1][3] = hex_to_bgr(y_hex_colors4.get(default_color))


colors = (base_color, 
          saturate(shade(base_color, 0.94), 0.95), 
          saturate(base_color, 0.78), 
          shade(base_color, 0.76))

for i, color in enumerate(colors):
    image[0][i] = color
    print(i, bgr_to_hex(color))

width = 400
height = 200

image = cv2.resize(image, (width, height), interpolation = cv2.INTER_AREA)
cv2.imwrite("out/palette.png", image)