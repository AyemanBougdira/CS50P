import pytest

from twttr import shorten


def test_shorten():
    assert shorten("ayeman") == "ymn"
    assert shorten("Ayeman") == "ymn"
    assert shorten("Ayeman 1") == "ymn 1"
    assert shorten("Ayeman, Bougdira") == "ymn, Bgdr"
