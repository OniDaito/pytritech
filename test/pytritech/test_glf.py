""" Tests for the GLF data."""

import os
import pytz
import datetime
from PIL import Image, ImageChops
from pytritech.glf import GLF
from pytritech.util.time import EpochGem
from pyinstrument import Profiler

def test_glf(get_data):
    """ Basic tests on the GLF files: read a glf and extract a PIL image."""
    glf_path = os.path.join(get_data, "test_tritech.glf")
    assert os.path.exists(glf_path)

    with GLF(glf_path) as glf:
        image_data, image_size = glf.extract_image(glf.images[20])
        image = Image.frombuffer('L', image_size, image_data, 'raw', 'L', 0, 1)
        image = image.transpose(Image.Transpose.ROTATE_180)
        image.save('result.png')

        start_date = glf.images[0].header.time
        end_date  = glf.images[-1].header.time

        assert(glf.images[0].header.device_id == 1194)

        assert start_date.hour == 16
        assert start_date.minute == 10
        assert end_date.hour == 16
        assert end_date.minute == 10

        profiler = Profiler()
        profiler.start()
        image_data, image_size = glf.extract_image(glf.images[20])
        profiler.stop()
        html = profiler.output_html()
        with open("profiler.html", "w") as f:
            f.write(html)

        image = Image.frombuffer('L', image_size, image_data, 'raw', 'L', 0, 1)
        image = image.transpose(Image.Transpose.ROTATE_180)
        
        test_image = os.path.join(get_data, "result.png")
        test_image = Image.open(test_image)
        diff = ImageChops.difference(image, test_image)

        if diff.getbbox():
            assert(False)

        start_date = glf.images[0].header.time
        end_date  = glf.images[-1].header.time

        assert start_date.hour == 16
        assert start_date.minute == 10
        assert end_date.hour == 16
        assert end_date.minute == 10

        start_date_cfg = float(glf.config.find("logHeader/creationTime").text)
        end_date_cfg = float(glf.config.find("logTerminator/closeTime").text)

        bst = pytz.timezone("Europe/London")
        utc = pytz.timezone("UTC")

        tseconds = int(start_date_cfg)
        tmillis = int((start_date_cfg - tseconds) * 1000)
        start_date_cfg = bst.localize(EpochGem() + datetime.timedelta(seconds=tseconds, milliseconds=tmillis))
        start_date_cfg = start_date_cfg.astimezone(utc)

        tseconds = int(end_date_cfg)
        tmillis = int((end_date_cfg - tseconds) * 1000)
        end_date_cfg = bst.localize(EpochGem() + datetime.timedelta(seconds=tseconds, milliseconds=tmillis))
        end_date_cfg = end_date_cfg.astimezone(utc)


        assert start_date.hour == start_date_cfg.hour
        assert start_date.minute == start_date_cfg.minute
        assert start_date.second == start_date_cfg.second

        assert end_date.hour == end_date_cfg.hour
        assert end_date.minute == end_date_cfg.minute
        assert end_date.second == end_date_cfg.second

  