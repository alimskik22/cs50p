from twttr import shorten


def test_shorten():
    assert shorten("Alima") == "lm"
    assert shorten("alimskik22") == "lmskk22"
    assert shorten("alima!") == "lm!"
