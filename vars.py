from datetime import datetime

RUN_ID = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

SAVE_DIR = f"photos/{RUN_ID}"
DELAY = 1 
PHOTO_COUNT = 4
FRAME_SIZE = (1280, 720)