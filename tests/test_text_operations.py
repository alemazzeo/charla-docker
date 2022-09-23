import ensayo.text_operations as to

SAMPLE_TEXT = "un dos tres   Cuatro cuatro   tres tres     uno"

WORDS = {"un": 1, "dos": 1, "tres": 3, "cuatro": 2, "uno": 1}


def test_count_words():
    words = to.count_words(SAMPLE_TEXT)
    assert words == WORDS
