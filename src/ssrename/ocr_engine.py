import easyocr

class OCREngine:
    _reader = None
    
    def __init__(self):
        if OCREngine._reader is None:
            OCREngine._reader = easyocr.Reader(["en"], gpu=False)
        self.reader = OCREngine._reader

    def extract_text(self, image_path):
        results = self.reader.readtext(str(image_path))
        return " ".join(text.lower() for _, text, _ in results)
