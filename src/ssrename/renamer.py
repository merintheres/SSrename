from pathlib import Path
from ssrename.image_loader import ImageLoader
from ssrename.safety import SafetyManager
from rich.console import Console

class ScreenshotRenamer:
    def __init__(self, path: Path, dry_run: bool):
        self.path = path
        self.dry_run = dry_run
        self.console = Console()

    def run(self):
        self._validate_path()
        images = ImageLoader(self.path).load_images()
        SafetyManager(self.console).preview(images, self.dry_run)

    def _validate_path(self):
        if not self.path.exists() or not self.path.is_dir():
            raise ValueError("Provided path is not a valid directory")
