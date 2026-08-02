from seasons import convert
from datetime import date


def test_convert():
    assert convert(date(2000, 1, 1)).endswith("minutes")
