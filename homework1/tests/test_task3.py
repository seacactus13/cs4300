import sys
import os
sys.path.insert(0, os.path.abspath("../src"))

import task3

def test_check_number():
    assert task3.check_number(10) == "positive"
    assert task3.check_number(-7) == "negative"
    assert task3.check_number(0) == "zero"

def test_first_n_primes():
    primes = task3.first_n_primes()
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert primes == expected

def test_sum_1_to_100():
    assert task3.sum_1_to_100() == 5050
