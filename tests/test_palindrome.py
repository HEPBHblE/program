import pytest
from palindrome import palindrome

def test_is_palindrome():
    assert palindrome("madam") == True
    assert palindrome("racecar") == True
    assert palindrome("hello") == False
    assert palindrome("step on no pets") == True
    assert palindrome("palindrome") == False

if __name__ == "__main__":
    pytest.main()
