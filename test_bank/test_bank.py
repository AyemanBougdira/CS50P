import pytest

from bank import value


def test_value():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0
    assert value("How you doing ?") == 20
    assert value("what's happening ?") == 100
