"""
Functional test for the application homepage
"""
from main import calc
def test_calc():
    response = calc(2,3)
    assert response == 5