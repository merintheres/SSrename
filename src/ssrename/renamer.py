from rich.console import Console
from ssrename.image_loader import ImageLoader
from ssrename.ocr_engine import OCREngine
from ssrename.caption_model import CaptionModel
from ssrename.filename_generator import FilenameGenerator
from ssrename.safety import SafetyManager
from ssrename.screenshot_type import ScreenshotTypeDetector

class ScreenshotRenamer:
    def __init__(self, path, dry_run):
        self.path = path
        self.dry_run = dry_run
        self.console = Console()
        self.ocr = OCREngine()
        self.caption = CaptionModel()
        self.generator = FilenameGenerator()
        self.detector = ScreenshotTypeDetector()

    def run(self):
        images = ImageLoader(self.path).load_images()
        SafetyManager(self.console).preview(
            images,
            self._generate_names,
            self.dry_run
        )

    def _generate_names(self, images):
        names = []

        thresholds = {
            "code": 5,
            "chat": 8,
            "document": 12,
            "empty": 999
        }

        for img in images:
            text = self.ocr.extract_text(img)
            stype = self.detector.detect(text)

            if len(text.split()) < thresholds.get(stype, 10):
                text = self.caption.describe(img)

            base = self.generator.generate(text, stype)
            names.append(f"{base}{img.suffix}")

        return names
