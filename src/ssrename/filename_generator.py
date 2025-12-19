import re

class FilenameGenerator:
    def __init__(self, max_words=5):
        self.max_words = max_words
        self.stopwords = {
            "a", "an", "the", "of", "and", "to", "in",
            "on", "for", "with", "is", "this", "that",
            "screenshot", "image", "picture", "photo",
            "ss", "img", "it", "as", "at", "by", "be", "are"
        }

    def generate(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        words = text.split()
        words = [w for w in words if w not in self.stopwords]
        words = words[:self.max_words]

        if not words:
            return "image"

        return "_".join(words)
