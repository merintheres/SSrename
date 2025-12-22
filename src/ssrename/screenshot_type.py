class ScreenshotTypeDetector:
    def detect(self, text: str) -> str:
        text = text.lower()

        if any(k in text for k in ["def ", "class ", "import ", "{", "}", ";"]):
            return "code"

        if any(k in text for k in ["sent", "seen", "typing", "online", "message"]):
            return "chat"

        if len(text.split()) > 30:
            return "document"

        if not text.strip():
            return "empty"

        return "generic"
