from bank import value


def test_value():
    assert value("Hello") == 0
    assert value("hey") == 20
    assert value("yo") == 100
