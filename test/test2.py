import pytest

from hello import convert

def test_conversion():
  assert convert(1) == 149597870.7
  assert convert(10) == 1495978707

def test_error():
  with pytest.raises(TypeError):
    convert("1")


def test_float_conversion():
  assert convert(0.001) == pytest.approx(149597870.700, abs=1e-5)
