import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image


def main():
    NZ_img_bgr = cv.imread("New_Zealand_Boat.jpg", 1)
    NZ_img_rgb = cv.cvtColor(NZ_img_bgr, cv.COLOR_BGR2RGB)

    img_cropped = NZ_img_rgb[200:400, 300:600]
    plt.imshow(img_cropped)
    plt.show()

    img_resized = cv.resize(img_cropped, None, fx=2, fy=2)
    plt.imshow(img_resized)
    plt.show()

    height = 50
    width = 100
    wxh = (width, height)

    img_resized = cv.resize(img_cropped, wxh)
    plt.imshow(img_resized)
    plt.show()

    img_flip_hor = cv.flip(img_cropped, 1)
    plt.imshow(img_flip_hor)
    plt.show()

if __name__ == "__main__":
    main()
