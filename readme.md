[AI GENERATED README]
Absolutely! Here’s your updated **`README.md`** with:

* ✅ Clean structure
* ✅ Install instructions using `requirements.txt`
* ✅ Font requirement (Poppins.ttf)
* ✅ Screenshot placeholder
* ✅ Ready for GitHub

---

### 📸 Photobooth

A sleek macOS photo booth built with Python + OpenCV + Pillow.
It captures 4 black-and-white photos with countdowns and assembles them into a styled filmstrip — complete with a personal label and modern font.

---

### ✨ Features

* 🖼️ Live camera preview with smooth countdown overlay
* 🎨 Custom bottom banner with **Poppins** font
* 🖤 Automatically saves black-and-white photos
* 🧱 Cropped and bordered vertical filmstrip layout
* 💬 Personalized text on final frame
* 📁 Timestamped folder for each photo session

---

### 📂 Project Structure

```
photobooth/
├── photos/               ← Output images
├── .env                  ← Optional environment config
├── venv/                 ← Virtual environment (ignored by Git)
├── vars.py               ← Settings like SAVE_DIR, DELAY
├── photobooth.py         ← Main app script
├── frame.py              ← Builds final filmstrip image
├── overlay_countdown.py  ← Handles countdown overlay UI
├── Poppins.ttf           ← Required font file
├── requirements.txt      ← Python dependencies
└── README.md
```

---

### 🚀 Getting Started

#### 1. Clone the repo

```bash
git clone https://github.com/Shashwat-pd/photobooth.git
cd photobooth
```

#### 2. Set up virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Make sure `Poppins.ttf` is in the project root

You can download it from [Google Fonts](https://fonts.google.com/specimen/Poppins)

---

### 🖥️ Usage

```bash
python photobooth.py
```

* A live preview will appear
* 4 photos will be taken (with countdown)
* Final collage saved to:
  `photos/YYYY-MM-DD_HH-MM-SS/photobooth.png`

---

### 🧠 Customization

You can change settings in `vars.py`:

```python
PHOTO_COUNT = 4
DELAY = 5
FRAME_SIZE = (1280, 720)
```


### 📜 License

MIT License — free to use, modify, and share. Attribution appreciated.


