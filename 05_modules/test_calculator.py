import pytest
from calculator import calculate_total, calculate_average, calculate_grade

def test_calculate_total():
    assert calculate_total([2, 2, 2]) == 6
    assert calculate_total([-2, 2, 2]) == 2
    assert calculate_total([-2, 0, 1]) == -1

def test_calculate_average():
    assert calculate_average([2, 2, 2]) == 2
    assert calculate_average([-2, 2, 2]) == pytest.approx(0.66, abs=0.01)

def test_calculate_grade():
    assert calculate_grade(73) == "A"
    assert calculate_grade(0) == "F"