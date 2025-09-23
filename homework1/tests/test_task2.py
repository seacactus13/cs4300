import sys
import os
sys.path.insert(0, os.path.abspath("../src"))

import task2

def test_data_types():
    integer_var, float_var, string_var, bool_var = task2.demonstrate_data_types()

    assert isinstance(integer_var, int)
    assert isinstance(float_var, float)
    assert isinstance(string_var, str)
    assert isinstance(bool_var, bool)

    assert integer_var == 42
    assert float_var == 3.14
    assert string_var == "Python"
    assert bool_var is True
