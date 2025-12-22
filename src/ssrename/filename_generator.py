import re
from collections import Counter

class FilenameGenerator:
    def __init__(self, max_words=5):
        self.max_words = max_words

        self.common_stopwords = {
            "a", "an", "the", "of", "and", "to", "in", "on", "for",
            "with", "is", "this", "that", "it", "as", "at", "by",
            "be", "are", "was"
        }

        self.type_stopwords = {
            "chat": {
                "sent", "seen", "online", "typing", "message",
                "yesterday", "today", "am", "pm"
            },
            "code": {
                "run", "output", "input", "console", "line",
                "file", "main", "print", "return"
            },
            "document": {
                "page", "chapter", "section", "figure",
                "table", "copyright"
            }
        }

    def generate(self, text: str, stype: str = "generic") -> str:
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        words = text.split()

        stopwords = set(self.common_stopwords)
        stopwords |= self.type_stopwords.get(stype, set())

        filtered = [w for w in words if w not in stopwords and len(w) > 2]
        if not filtered:
            return "image"

        counts = Counter(filtered)

        def score(word):
            s = min(len(word), 10)
            s += counts[word] * 2
            if any(c.isdigit() for c in word):
                s += 2
            return s

        ranked = sorted(set(filtered), key=score, reverse=True)
        return "_".join(ranked[:self.max_words])
