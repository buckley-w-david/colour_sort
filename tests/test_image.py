import numpy as np
from PIL import Image
import pytest
from colour_sort.image import as_sorted
from colour_sort import misc


IMAGE_SIZE = 4096


def test_as_sorted_brightness(image: Image.Image) -> None:
    output = as_sorted(image, 'brightness')

    pic = np.reshape(np.array(output), (IMAGE_SIZE*IMAGE_SIZE, 3))
    structured_pic = np.core.records.fromarrays(pic.transpose(),
                                                names='r, g, b',
                                                formats='u1, u1, u1')

    unique = np.unique(structured_pic)

    assert unique.shape == structured_pic.shape


def test_as_sorted_rgb(image: Image.Image) -> None:
    output = as_sorted(image, 'rgb')

    pic = np.reshape(np.array(output), (IMAGE_SIZE*IMAGE_SIZE, 3))
    structured_pic = np.core.records.fromarrays(pic.transpose(),
                                                names='r, g, b',
                                                formats='u1, u1, u1')

    unique = np.unique(structured_pic)

    assert unique.shape == structured_pic.shape


def test_as_sorted_unknown(image: Image.Image) -> None:
    with pytest.raises(ValueError):
        as_sorted(image, 'unknown')
