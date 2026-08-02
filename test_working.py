import pytest
from working import convert


def test_regular_times():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_mixed_formats():
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"


def test_midnight_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:30 AM to 12:30 PM") == "00:30 to 12:30"


def test_invalid_hours():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9 AM to 13 PM")


def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9 AM to 5:99 PM")


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
