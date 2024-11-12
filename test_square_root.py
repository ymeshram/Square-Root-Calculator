import pytest
from square_root import square_root

def test_square_root_positive():
    assert square_root(4) == 2.0

def test_square_root_negative():
    with pytest.raises(ValueError):
           square_root(-4)
