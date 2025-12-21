from rich.console import Console
from ssrename.image_loader import ImageLoader
from ssrename.ocr_engine import OCREngine
from ssrename.caption_model import CaptionModel
from ssrename.filename_generator import FilenameGenerator
from ssrename.safety import SafetyManager

class ScreenshotRenamer:
    def __init__(self, path, dry_run):
        self.path = path
        self.dry_run = dry_run
        self.console = Console()
        self.ocr = OCREngine()
        self.caption = None
        self.generator = FilenameGenerator()

    def run(self):
        images = ImageLoader(self.path).load_images()
        SafetyManager(self.console).preview(
            images,
            self._generate_names,
            self.dry_run
        )

    def _generate_names(self, images):
        names = []

        for img in images:
            text = self.ocr.extract_text(img).strip()

            if len(text.split()) < 10:
                if self.caption is None:
                    self.caption = CaptionModel()
                text = self.caption.describe(img)

            base = self.generator.generate(text)
            names.append(f"{base}{img.suffix}")

        return names
