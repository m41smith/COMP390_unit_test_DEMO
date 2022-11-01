import util_functions
import pytest

""" this file contains all unit tests """


def test_multiply_two_numbers():
    assert util_functions.multiply_two_numbers(3, 5) == 15
    assert util_functions.multiply_two_numbers(7, 5) == 35
    assert util_functions.multiply_two_numbers(True, 5) == 5
    assert util_functions.multiply_two_numbers([3, 6, 'joe'], 2) == [3, 6, 'joe', 3, 6, 'joe']
    with pytest.raises(TypeError) as exception_info:
        util_functions.multiply_two_numbers(None, 2)
    assert exception_info.type is TypeError

