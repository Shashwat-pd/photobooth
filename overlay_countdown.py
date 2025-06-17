import os
import cv2
import time
from PIL import Image, ImageDraw, ImageFont
from frame import frame_main
import numpy as np



font_path = "Poppins.ttf"
font_size = 100
font = ImageFont.truetype(font_path, font_size)

def overlay_countdown(frame, countdown, total_count):
    frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(frame_pil)

    height, width = frame.shape[:2]

    bar_height = 120
    bar_color = (234, 67, 53, 255)
    bar_top = height - bar_height

    draw.rectangle([(0, bar_top), (width, height)], fill=bar_color)


    number = str(countdown)
    bbox = font.getbbox(number)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = bar_top + (bar_height - text_height) // 2 - 30
    fill = (255, 255, 255)
    draw.text((x, y), number, font=font, fill=fill)

    return cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)
