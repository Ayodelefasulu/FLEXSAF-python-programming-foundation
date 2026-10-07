#!/usr/bin/env python3

from score_utils import calculate_average
import unittest

def test_calculate_average():
    assert calculate_average([]) == None

def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20

def test_calculate_average():
    assert calculate_average([100]) == 100

if __name__ == "__main__":
    unittest.main()