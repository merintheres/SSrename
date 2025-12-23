from pathlib import Path
from ssrename.image_loader import ImageLoader

def test_load_single_image(tmp_path):
    img = tmp_path / "test.png"
    img.write_bytes(b"fake")

    loader = ImageLoader(img)
    images = loader.load_images()

    assert images == [img]

def test_ignore_non_image(tmp_path):
    txt = tmp_path / "note.txt"
    txt.write_text("hello")

    loader = ImageLoader(txt)
    images = loader.load_images()

    assert images == []
