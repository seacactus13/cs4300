import sys
import os
sys.path.insert(0, os.path.abspath("../src"))

import task4

def test_calculate_discount_integers():
    assert task4.calculate_discount(100, 20) == 80
    assert task4.calculate_discount(50, 50) == 25

def test_calculate_discount_floats():
    assert task4.calculate_discount(59.99, 15) == 59.99 * 0.85
    assert task4.calculate_discount(200, 5.5) == 200 * 0.945
