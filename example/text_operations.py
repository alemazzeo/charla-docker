from typing import Dict


def count_words(text: str) -> Dict[str, int]:
    words: Dict[str, int] = {}
    for word in text.split():
        word = word.lower()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words
