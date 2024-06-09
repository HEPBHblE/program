import pytest
from punctuation import punctuation

def test_strip_punctuation_ru():
    assert punctuation("Привет, мир!") == "Привет мир"
    assert punctuation("Как дела?") == "Как дела"
    assert punctuation("Это тестовый текст.") == "Это тестовый текст"
    assert punctuation("Никаких знаков!") == "Никаких знаков"
    assert punctuation("") == ""

if __name__ == "__main__":
    pytest.main()
