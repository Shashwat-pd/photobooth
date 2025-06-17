from datetime import datetime

RUN_ID = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

SAVE_DIR = f"photos/{RUN_ID}"
DELAY = 3 
PHOTO_COUNT = 4
FRAME_SIZE = (1280, 720)
DURATION = 500 #gif duration per photo in ms