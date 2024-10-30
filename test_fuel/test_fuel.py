import pytest

from fuel import convert
from fuel import gauge

def test_convert():
    # Test valid fraction conversion
    assert convert("3/4") == 75.0

    # Additional test cases for `convert` function
    assert convert("1/2") == 50.0
    assert convert("1/4") == 25.0

def test_gauge():
    # Test gauge function with edge cases and valid inputs
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_error():
    # Test for ValueError
    with pytest.raises(ValueError):
        convert("5/4")

    # Test for ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

    # Test for invalid input format
    with pytest.raises(ValueError):
        convert("invalid")
    with pytest.raises(ValueError):
        convert("5")
    with pytest.raises(ValueError):
        convert("/4")
