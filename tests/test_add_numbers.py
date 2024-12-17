"""Test that our add numbers module behaves as expected"""

from mypackage.add_number import add_num


def test_add_number():
    """Test that the output of the add number function is correct"""

    assert add_num(1, 2) == 3
