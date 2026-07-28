from numb3rs import validate

def test_validate_true():
    assert validate("255.255.255.255") == True
    assert validate("255.0.0.0") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.234.56") == True


def test_validate_false():
    assert validate("255.") == False
    assert validate("255.0.") == False
    assert validate("255.280.479.579") == False
    assert validate("-3.-48.4790.46") == False
    assert validate("....") == False
    assert validate(".") == False
    assert validate("a.b.c.d") == False
    assert validate("#.$.#.#") == False
    

