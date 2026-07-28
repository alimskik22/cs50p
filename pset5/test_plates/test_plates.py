from plates import is_valid


def test_is_valid():
    assert is_valid("SSS222") == True
    assert is_valid("SS") == True
    assert is_valid("S") == False
    assert is_valid("123SS") == False
    assert is_valid("SS12S") == False
    assert is_valid("SSSSSSSSS") == False
    assert is_valid("SS01") == False
    assert is_valid("11111") == False
    assert is_valid("SS!!!") == False

