import util_functions
import pytest
import math
from io import StringIO
from testfixtures import TempDirectory

""" this file contains all unit tests """
# pytest


def test_multiply_two_numbers():
    assert util_functions.multiply_two_numbers(3, 5) == 15
    assert util_functions.multiply_two_numbers(7, 5) == 35
    assert util_functions.multiply_two_numbers(True, 5) == 5
    assert util_functions.multiply_two_numbers([3, 6, 'joe'], 2) == [3, 6, 'joe', 3, 6, 'joe']
    with pytest.raises(TypeError) as exception_info:
        util_functions.multiply_two_numbers(None, 2)
    assert exception_info.type is TypeError
    with pytest.raises(TypeError) as exception_info2:
        util_functions.multiply_two_numbers('joe', 'bob')
    assert exception_info2.type is TypeError
    assert util_functions.multiply_two_numbers('joe', 3) == 'joejoejoe'
    assert util_functions.multiply_two_numbers(True, False) == 0


def test_string_is_int():
    num_str = '45'
    num_str2 = '45.6'
    assert util_functions.string_is_int(num_str2) is False
    assert util_functions.string_is_int(False) is True
    assert util_functions.string_is_int(num_str) is True
    assert util_functions.string_is_int('') is False
    assert util_functions.string_is_int(23) is True
    assert util_functions.string_is_int(45.9) is True
    assert util_functions.string_is_int([23, 'joe', None, False, '45']) is False
    assert util_functions.string_is_int(['45']) is False
    assert util_functions.string_is_int(id(['45'])) is True


def test_convert_string_to_numerical():
    simple_dict = {'name': 'joe', 'hp': 100, 'exp': 23}

    assert util_functions.convert_string_to_numerical(4.5) == 4
    assert util_functions.convert_string_to_numerical('4.5') == 4.5
    assert util_functions.convert_string_to_numerical(simple_dict) is None
    assert util_functions.convert_string_to_numerical('') is None
    with pytest.raises(TypeError) as exception_info:
        util_functions.convert_string_to_numerical()
    assert exception_info.type is TypeError
    assert util_functions.convert_string_to_numerical('0') == 0
    assert util_functions.convert_string_to_numerical('0.0') == 0.0
    assert util_functions.convert_string_to_numerical(True) == 1
    assert util_functions.convert_string_to_numerical(None) is None
    assert util_functions.convert_string_to_numerical(TypeError) is None
    assert util_functions.convert_string_to_numerical(math.pi) == 3
    assert util_functions.convert_string_to_numerical(str(math.pi)) == math.pi
    assert util_functions.convert_string_to_numerical(str(10/3)) == 10/3
    assert util_functions.convert_string_to_numerical(3 or 7) == 3
    assert util_functions.convert_string_to_numerical(3 and 7) == 7


def test_enter_first_name(capfd, monkeypatch):
    test_string = 'joe'
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
    assert util_functions.enter_first_name() == 'joe'
    out, err = capfd.readouterr()
    assert out == f'Please enter your first name: '

    test_string = 'joe8'
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
    assert util_functions.enter_first_name() is None
    out, err = capfd.readouterr()
    assert out == f'Please enter your first name: The name \'{test_string}\' is not valid.\n'


def test_extract_file_contents(capfd):
    with TempDirectory() as tempdir:
        temp_file = 'test.txt'
        test_line = b'Hello'
        tempdir.write(temp_file, test_line)
        file_path = tempdir.path + '\\' + temp_file
        util_functions.extract_file_content(file_path)
    out, err = capfd.readouterr()
    assert out == f'file content : Hello\n'

    missing_file = 'missing_file.txt'
    with pytest.raises(FileNotFoundError) as file_error:
        util_functions.extract_file_content(missing_file)
    assert file_error.type is FileNotFoundError