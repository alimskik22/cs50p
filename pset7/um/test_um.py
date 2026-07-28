import pytest
from um import count


def test_single():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1



def test_multiple():
    assert count("um um um") == 3
    assert count("Um, thanks, um.") == 2


def test_not_substring():
    assert count("yummy") == 0
    assert count("umbrella") == 0


def test_punctuation():
    assert count("(um)") == 1
    assert count("um? um! um.") == 3


