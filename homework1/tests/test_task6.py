import sys
import os
sys.path.insert(0, os.path.abspath("../src"))

import task6

def test_count_words_in_file():
    # Adjust the path if your file is in src/
    filepath = os.path.join(os.path.dirname(__file__), "../src/task6_read_me.txt")
    word_count = task6.count_words_in_file(filepath)
    
    # Count manually or trust the file above: 124 words
    assert word_count == 125
