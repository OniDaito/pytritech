# pytritech
This site contains the project documentation for the `pytritech` library - an interface to the [Tritech](https://www.tritech.co.uk/) GLF file format.

 This project is part of the [WATER Group](https://smru-water.wp.st-andrews.ac.uk/) research project at [SMRU](http://www.smru.st-andrews.ac.uk/), [University of St Andrews](https://www.st-andrews.ac.uk/).


## Table Of Contents

1. [How-To Guides](how-to-guides.md) - Specific how-tos on various things.
2. [Reference](reference.md) - An API reference.


## Requirements and Setup

To use this library in your own python program we recommend including it as part of a python virtual environment.

    pip install pytritech

or, directly from this repository

    pipt install https://github.com/onidaito/pytritech.git


## Basic Usage

Once installed, you can begin to read pytritech files as follows:

    from pytritech.glf import GLF 
    import os
    
    assert os.path.exists(glf_path)
    
    with GLF(glf_path) as glf:
        image_data, image_size = glf.extract_image(glf.images[20])


## Roadmap (or things we haven't implemented yet)

As of version 1.0.0, only the status and image records can be read. Records such as serial, analog video, V4 or generic are not yet supported. In addition, this library is only concerned with GLF files, not controlling the Tritech sonar itself.

In the future, we hope to add support for these remaining record types, but no timeline has been set.


The documentation follows the best practice for
project documentation as described by Daniele Procida
in the [Diátaxis documentation framework](https://diataxis.fr/)
and consists of four separate parts:
