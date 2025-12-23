# SSrename

SSrename is a Python CLI tool that automatically renames screenshots using **OCR-first text extraction** with an **AI-based fallback** for images that lack sufficient readable text.

It is designed to work fully **offline**, using local models, and supports both **directories** and **individual image files**.

---

##  Features

- OCR-first filename generation using EasyOCR
- Automatic AI fallback using a local Vision-Language Model (BLIP)
- Adaptive OCR thresholds based on screenshot type (code, chat, document, empty)
- Works on both directories and single image paths
- Safe preview mode with `--dry-run`
- Collision-safe renaming
- Customizable filename length
- Multiple CLI flags for control and debugging

---

##  How It Works

For each image:

1. Extract text using **EasyOCR**
2. Detect screenshot type (code / chat / document / empty)
3. Check if OCR text meets the required word threshold
4. If insufficient → generate a caption using **BLIP**
5. Clean and rank keywords
6. Generate a meaningful filename
7. Preview or apply the rename safely

---

##  Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/SSrename.git
cd SSrename
```
### 2. Create and activate a virtual environment
```bash
conda create -n ssrename python=3.11
conda activate ssrename
```
### 3. Install the package
```bash
pip install -e .
```

---

##  Usage

### Rename all screenshots in a directory (dry run)
```bash
ssrename screenshots/ --dry-run
```
### Rename a single image
```bash
ssrename path/to/image.png --dry-run
```
### Limit processing to first N images
```bash
ssrename screenshots/ --limit 5 --dry-run
```
### Show how names are generated
```bash
ssrename screenshots/ --verbose
```
### OCR only (disable AI fallback)
```bash
ssrename screenshots/ --ocr-only
```
### AI only (skip OCR)
```bash
ssrename screenshots/ --ai-only
```
### Control filename length
```bash
ssrename screenshots/ --max-words 3
```
