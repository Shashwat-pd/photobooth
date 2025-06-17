from PIL import Image
import os
from vars import SAVE_DIR, DURATION

def gif():
    images = [
        Image.open(os.path.join(SAVE_DIR, f"photo_{i}.png"))
        for i in range(1, 5)
    ]

    gif_path = os.path.join(SAVE_DIR, "photobooth.gif")

    images[0].save(
        gif_path,
        save_all=True,
        append_images=images[1:],
        optimize=True,
        duration=DURATION, 
        loop=0
    )

    print(f" GIF saved at: {gif_path}")


