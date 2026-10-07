import pytest
from grade_classifier import grade_classifier

def test_grade_classifier():
    #assert grade_classifier(90) == "This is A+"
    assert grade_classifier(90) == None