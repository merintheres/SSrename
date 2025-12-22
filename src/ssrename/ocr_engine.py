import easyocr

class OCREngine:
    def __init__(self, min_confidence=0.4):
        self.reader = easyocr.Reader(["en"], gpu=False)
        self.min_confidence = min_confidence

    def extract_text(self, image_path):
        results = self.reader.readtext(str(image_path))
        words = []

        for _, text, conf in results:
            if conf >= self.min_confidence and len(text.strip()) > 1:
                words.append(text.lower())

        return " ".join(words)
