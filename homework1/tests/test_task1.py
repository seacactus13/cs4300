import sys
import os
sys.path.insert(0, os.path.abspath("../src"))

import task1

def test_task1_output(capsys):
    task1.main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"
