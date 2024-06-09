import pytest
from correct_number import correct_number

def test_correct_number():
    assert correct_number("+7 999 123-45-67") == True
    assert correct_number("8(999)1234567") == True
    assert correct_number("89991234567") == True
    assert correct_number("+7 999 123 45 67") == True
    assert correct_number("9991234567") == False
    assert correct_number("7 999 123 45 67") == False
    assert correct_number("8 999 123 45 67") == True
    assert correct_number("8 999 123 45 6") == False
    assert correct_number("+7 (999) 123 45 67") == True
    assert correct_number("+7-999-123-45-67") == True
    assert correct_number("+7 999 123 45 678") == False

if __name__ == "__main__":
    pytest.main()
