from pathlib import Path
from ssrename.image_loader import ImageLoader
from ssrename.safety import SafetyManager
from ssrename.filename_generator import FilenameGenerator
from rich.console import Console

class ScreenshotRenamer:
    def __init__(self, path: Path, dry_run: bool):
        self.path = path
        self.dry_run = dry_run
        self.console = Console()
        self.filename_generator = FilenameGenerator()

    def run(self):
        self._validate_path()
        images = ImageLoader(self.path).load_images()
        SafetyManager(self.console).preview(images, self._generate_names, self.dry_run)

    def _generate_names(self, images):
        names = []
        for img in images:
            base = self.filename_generator.generate(img.stem)
            names.append(f"{base}{img.suffix}")
        return names

    def _validate_path(self):
        if not self.path.exists() or not self.path.is_dir():
            raise ValueError("Provided path is not a valid directory")
