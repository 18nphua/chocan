import pytest
from unittest.mock import patch
from valid import read_int, read_float, read_string, read_y_or_n

# Chocolate Support Group themed test inputs
def test_read_int():
    with patch('builtins.input', side_effect=['Cocoa123', '45']):
        assert read_int("How many chocolates have you eaten?") == 45

def test_read_float():
    with patch('builtins.input', side_effect=['ChocolateInfinity', '3.14']):
        assert read_float("Enter the weight of your largest chocolate in kg: ") == 3.14

def test_read_string():
    with patch('builtins.input', side_effect=['', 'DarkChocolate']):
        assert read_string("What is your favorite chocolate type?") == "DarkChocolate"

def test_read_y_or_n():
    with patch('builtins.input', side_effect=['maybe', 'yes']):
        assert read_y_or_n("Do you support fair trade chocolates? (y/n): ") == 'y'

def test_read_int_negative():
    with patch('builtins.input', side_effect=['-5']):
        assert read_int("How many chocolates did you give away?") == -5

def test_read_float_zero():
    with patch('builtins.input', side_effect=['0.0']):
        assert read_float("Enter the weight of your smallest chocolate in kg: ") == 0.0

def test_read_string_with_space():
    with patch('builtins.input', side_effect=['Milk Chocolate']):
        assert read_string("Name a chocolate you tried recently: ") == "Milk Chocolate"

def test_read_y_or_n_no():
    with patch('builtins.input', side_effect=['no']):
        assert read_y_or_n("Did you skip chocolate this week? (y/n): ") == 'n'

if __name__ == "__main__":
    pytest.main()
