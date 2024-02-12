# How to guides

A quick overview on how to do various common operations with pytritech.


## Reading the raw image and saving as a png

Assuming you have [Pillow](https://pypi.org/project/pillow/) installed:

    from pytritech.glf import GLF
    from PIL import Image
    import os
    
    assert os.path.exists(glf_path)
    
    with GLF(glf_path) as glf:
        image_data, image_size = glf.extract_image(glf.images[20])

        image = Image.frombuffer('L', image_size, image_data, 'raw', 'L', 0, 1)
        image.save("test.png")


## Reading the time of an image

    from pytritech.glf import GLF
    from PIL import Image
    import os
    
    assert os.path.exists(glf_path)
    
    with GLF(glf_path) as glf:
        image_date_time = glf.images[0].header.time
        print(image_date_time)

## Reading the status of the sonar when an image was taken

    from pytritech.glf import GLF
    from PIL import Image
    import os
    
    assert os.path.exists(glf_path)
    
    with GLF(glf_path) as glf:
        status_rec = glf.statuses[0]
        print(status_rec)
        

## Quickly reading the time range of a GLF file.

Sometimes, it's necessary to quickly read the time range of a GLF file. This is done much quicker with the following function:

    from pytritech.glftimes import glf_times
    glf_path = os.path.join(get_data, "test_tritech.glf")
    assert os.path.exists(glf_path)
    start, end = glf_times(glf_path)