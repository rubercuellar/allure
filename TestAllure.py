import pytest
import allure

@allure.feature("Ruber")
@pytest.mark.parametrize("test_input,expected", [
    ("3*5", 15),
    ("2*4", 8),
    ("6*9", 54),
])
@allure.title('Test: {0}')
def test_eval(test_input, expected):
    allure.attach("Ruber")
    assert eval(test_input) == expected