from ssrename.renamer import ScreenshotRenamer

class DummyOCR:
    def extract_text(self, img):
        return "short"

class DummyCaption:
    def describe(self, img):
        return "fallback caption text"

def test_fallback_used(monkeypatch, tmp_path):
    img = tmp_path / "a.png"
    img.write_bytes(b"fake")

    renamer = ScreenshotRenamer(tmp_path, dry_run=True)
    renamer.ocr = DummyOCR()
    renamer.caption = DummyCaption()

    names = renamer._generate_names([img])
    assert "fallback" in names[0]["filename"]
