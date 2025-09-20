
"""Tests for the functions in template_dev_ops_project/main.py."""

from template_dev_ops_project.main import add, multiply


def test_add():
    # check if 2 + 3 = 5
    assert add(2, 3) == 5


def test_multiply():
    # check if 2 * 3 = 6
    assert multiply(2, 3) == 6

def test_subtract():
    """Test that subtract() correctly subtracts numbers."""
    from template_dev_ops_project.main import subtract
    assert subtract(5, 3) == 2

def test_division():
    """Test that subtract() correctly subtracts numbers."""
    from template_dev_ops_project.main import division
    assert division(6, 3) == 2
