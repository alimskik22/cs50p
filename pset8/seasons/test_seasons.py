from seasons import minutes_since, to_words
from datetime import date

def test_minutes_since():
    today = date(2026, 7, 23)
    assert minutes_since(today, date(2008, 10, 22)) == 9335520


def test_to_words():
    assert to_words(9335520) == "Nine million, three hundred thirty-five thousand, five hundred twenty minutes"

