""" Test the range calculation."""

import os
from pytritech.glf import GLF
from src.pytritech.util.range import calculate_range

def test_range(get_data):
    """ Basic tests on the GLF files: read a glf and extract a PIL image."""
    glf_path = os.path.join(get_data, "test_tritech.glf")
    assert os.path.exists(glf_path)

    with GLF(glf_path) as glf:
        assert(round(calculate_range(glf.images[10])) == 2)