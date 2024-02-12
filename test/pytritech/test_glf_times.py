""" Test the fast cfg read method"""

import os
from pytritech.glftimes import glf_times

def test_glf(get_data):
    glf_path = os.path.join(get_data, "test_tritech.glf")
    assert os.path.exists(glf_path)

    start, end = glf_times(glf_path)
    assert start.hour == 16
    assert end.hour == 16