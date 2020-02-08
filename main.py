import argparse as ap

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from src.affine import shear


if __name__ == "__main__":
    scale = 0.5

    img = np.array(Image.open('resources/meme.png'))

    shape = (img.shape * np.array([1, scale, 1])).astype(int) + [100, 100, 0]
    new = np.zeros(shape, dtype=img.dtype)

    for i, v in np.ndenumerate(img):
        # Get coordinates
        j = i[:2]

        # Translate coordinates according to an affine shear transform
        # Coordinate is in y, x while shear is expecting x, y
        j = shear(0, scale, j)
        j = j.flatten()

        # Add RGB color data
        k = np.append(j, i[2:]).astype(int)
        k = tuple(k.tolist())

        new[k] = v

    plt.imshow(new)
    plt.show()
