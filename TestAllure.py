import pytest
import allure

@pytest.mark.parametrize("test_input,expected", [
    ("3*5", 15),
    ("2*4", 8),
    ("6*9", 54),
])
def test_eval(test_input, expected):
    allure.attach("Ruber")
    assert eval(test_input) == expected