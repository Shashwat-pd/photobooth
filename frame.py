from PIL import Image, ImageDraw, ImageFont
from vars import SAVE_DIR
from dotenv import load_dotenv
load_dotenv()

import os


def center_crop(img, target_size):
    img_width, img_height = img.size
    target_width, target_height = target_size

    left = (img_width - target_width) // 2
    top = (img_height - target_height) // 2
    right = left + target_width
    bottom = top + target_height

    return img.crop((left, top, right, bottom))

def frame_main():
    images = [Image.open(f"{SAVE_DIR}/photo_{i}.png") for i in range(1, 5)]



    
    crop_size = (1000, 1000)   
    border = 50                
    side_border = 100          
    label_height = 150        

    images = [center_crop(img, crop_size) for img in images]


    strip_width = crop_size[0] + side_border * 2
    strip_height = crop_size[1] * len(images) + border * (len(images) - 1) + label_height 


    film_strip = Image.new('RGB', (strip_width, strip_height), color='white')


    for i, img in enumerate(images):
        y_offset = i * (crop_size[1] + border)
        film_strip.paste(img, (side_border, y_offset))




    
    draw = ImageDraw.Draw(film_strip)
    text = f"{os.getenv('MARK')} "


    max_width = strip_width - 500  
    max_height = label_height - 20


    font_path = "Poppins.ttf"
    font_size = 10
    while True:
        try:
            font = ImageFont.truetype(font_path, font_size)
        except:
            print("Font not found. Make sure Poppins.ttf is in the same directory.")
            break

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        if text_width > max_width or text_height > max_height:
            font_size -= 5  # backtrack to last good size
            font = ImageFont.truetype(font_path, font_size)
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            break

        font_size += 1


    text_x = (strip_width - text_width) // 2
    text_y = strip_height - label_height + (label_height - text_height) // 2 - 20

    draw.text((text_x, text_y), text, font=font, fill='black')



    output_path = f"{SAVE_DIR}/photobooth.png"


    film_strip.save(output_path)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    frame_main()
