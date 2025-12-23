from pathlib import Path

class ImageLoader:
    def __init__(self, folder: Path):
        self.folder = folder
        self.extensions = {".png", ".jpg", ".jpeg"}

    def load_images(self):
        if self.folder.is_file():
            if self.folder.suffix.lower() in self.extensions:
                return [self.folder]
            return []

        if self.folder.is_dir():
            return [
                p for p in self.folder.iterdir()
                if p.is_file() and p.suffix.lower() in self.extensions
            ]

        return []
