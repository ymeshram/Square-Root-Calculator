import pytest
from square_root import square_root  # Make sure this matches the name of your function file

def test_square_root_perfect_squares():
    """Test square root function with perfect squares."""
    assert square_root(1) == 1
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(16) == 4
    assert square_root(25) == 5

def test_square_root_non_perfect_squares():
    """Test square root function with non-perfect squares."""
    assert square_root(2) == pytest.approx(1.4142, rel=1e-4)
    assert square_root(3) == pytest.approx(1.7321, rel=1e-4)
    assert square_root(10) == pytest.approx(3.1623, rel=1e-4)

def test_square_root_zero():
    """Test square root function with zero."""
    assert square_root(0) == 0

def test_square_root_negative_input():
    """Test square root function with negative input."""
    with pytest.raises(ValueError):
        square_root(-1)

def test_square_root_non_numeric_input():
    """Test square root function with non-numeric input."""
    with pytest.raises(TypeError):
        square_root("string")
    with pytest.raises(TypeError):
        square_root([1, 2, 3])
    with pytest.raises(TypeError):
        square_root(None)

# If you want to run the tests directly from this file, uncomment the following lines:
# if __name__ == "__main__":
#     pytest.main()
