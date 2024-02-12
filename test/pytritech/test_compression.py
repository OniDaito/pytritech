""" A small test to see how compressed GLF files are 
and how well the isal_zlib works."""

import os
from pytritech.glf import GLF


def test_glf(get_data):
    """ Check that the GLF files are actually compressed."""
    glf_path = os.path.join(get_data, "test_tritech.glf")
    assert os.path.exists(glf_path)

    with GLF(glf_path) as glf:
        image_rec = glf.images[20]
        assert(image_rec.compression_type == 0)
        exp_size = (image_rec.bearing_end - image_rec.bearing_start) * (image_rec.range_end - image_rec.range_start)
        assert(exp_size > image_rec.image_data_size)