""" Read a GLF and print out some useful information
Example usage:
    python glfinfo.py <path to glf file>
"""

import os
from xml.etree import ElementTree
from pytritech.glf import GLF


def indent(elem, level=0):
    i = "\n" + level * "  "
    j = "\n" + (level - 1) * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="glfinfo",
        description="Print out data from a Tritech GLF file",
        epilog="SMRU St Andrews",
    )

    parser.add_argument("filename")
    args = parser.parse_args()

    assert os.path.exists(args.filename)

    with GLF(args.filename) as glf:
        start_date = glf.images[0].header.time
        end_date = glf.images[-1].header.time
        print("Date range:", start_date, "->", end_date)
        print("Sonar IDs:", glf.sonar_ids)
        nice = indent(glf.config)
        print(ElementTree.dump(nice))
        image_data, image_size = glf.extract_image(glf.images[0])
        print("Image Size", image_size)

 

