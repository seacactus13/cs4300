import sys
import os
sys.path.insert(0, os.path.abspath("../src"))

import task7

def test_get_status_code():
    # Use a reliable testing URL
    url = "https://httpbin.org/get"
    status = task7.get_status_code(url)
    assert status == 200
