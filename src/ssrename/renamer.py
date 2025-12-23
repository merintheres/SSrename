from rich.console import Console
from ssrename.image_loader import ImageLoader
from ssrename.ocr_engine import OCREngine
from ssrename.caption_model import CaptionModel
from ssrename.filename_generator import FilenameGenerator
from ssrename.safety import SafetyManager
from ssrename.screenshot_type import ScreenshotTypeDetector

class ScreenshotRenamer:
    def __init__(self, path, dry_run, limit=None, verbose=False, ocr_only=False, ai_only=False, max_words=5):
        self.path = path
        self.dry_run = dry_run
        self.limit = limit
        self.verbose = verbose
        self.ocr_only = ocr_only
        self.ai_only = ai_only

        self.console = Console()
        self.ocr = OCREngine()
        self.caption = CaptionModel()
        self.generator = FilenameGenerator(max_words=max_words)
        self.detector = ScreenshotTypeDetector()

    def run(self):
        images = ImageLoader(self.path).load_images()

        if self.limit:
            images = images[:self.limit]

        SafetyManager(self.console).preview(
            images,
            self._generate_names,
            self.dry_run,
            verbose=self.verbose
        )

    def _generate_names(self, images):
        results = []

        for img in images:
            text = self.ocr.extract_text(img)
            source = "ocr"

            stype = self.detector.detect(text)

            thresholds = {
                "code": 5,
                "chat": 8,
                "document": 12,
                "empty": 999
            }

            if len(text.split()) < thresholds.get(stype, 10):
                text = self.caption.describe(img)
                source = "caption"

            base = self.generator.generate(text, stype)

            results.append({
                "image": img,
                "filename": f"{base}{img.suffix}",
                "source": source,
                "words": len(text.split()),
                "type": stype
            })

        return results
