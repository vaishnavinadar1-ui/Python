from plates import is_valid


def test_length():
    assert is_valid("CS") == True
    assert is_valid("CS50") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_first_two_letters():
    assert is_valid("CS50") == True
    assert is_valid("1S50") == False
    assert is_valid("C150") == False


def test_numbers():
    assert is_valid("CS50") == True
    assert is_valid("AAA222") == True
    assert is_valid("CS05") == False
    assert is_valid("AAA022") == False


def test_number_position():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False
    assert is_valid("AA22BB") == False


def test_punctuation():
    assert is_valid("PI.3") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS,50") == False
