import main


def test_add():
    assert main.add(1, 2) == 3
    assert main.add(1,8) == 9
    assert main.add(1,8) == 12
    assert main.add(1,4) == 5
    