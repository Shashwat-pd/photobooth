from vars import SAVE_DIR, DELAY, PHOTO_COUNT, FRAME_SIZE
import os
import cv2
import time
from PIL import Image, ImageDraw, ImageFont

from frame import frame_main
from overlay_countdown import overlay_countdown
from video import gif




if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def capture_photobooth():
    cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION) 

    if not cap.isOpened():
        print("Cannot open camera")
        return

    for i in range(PHOTO_COUNT):
        print(f"Photo {i+1} in {DELAY} seconds...")

        start = time.time()
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.resize(frame, FRAME_SIZE)

            elapsed = int(time.time() - start)
            remaining = DELAY - elapsed


            frame = overlay_countdown(frame, remaining, DELAY)

            cv2.imshow("Photobooth", frame)
            if remaining <= 0:
                break
            if cv2.waitKey(1) == 27:
                break

        ret, frame = cap.read()
        
        if not ret:
            print("Failed to capture photo")
            continue
        
        preview_frame = cv2.resize(frame.copy(), FRAME_SIZE)

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
        img_pil = Image.fromarray(img).convert("RGB")  


        filename = os.path.join(SAVE_DIR, f"photo_{i+1}.png")

        img_pil.save(filename)
        print(f"Saved photo: {filename}")

        flash = cv2.add(preview_frame, 100)
        cv2.imshow("Photobooth", flash)
        cv2.waitKey(300)

    frame_main()
    gif()

    cap.release()
    cv2.destroyAllWindows()
    print("Done!")

if __name__ == "__main__":
    capture_photobooth()
