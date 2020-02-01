import scipy
from scipy import ndimage


def medianBlur(image, size=5):
    return scipy.ndimage.filters.median_filter(image, size)


def minErosion(image, size=5):
    return scipy.ndimage.filters.minimum_filter(image, size)


def maxDilation(image, size=5):
    return scipy.ndimage.filters.maximum_filter(image, size)


def makeItRadioactiveGreen(mask, img):
    img[mask == 255] = [0, 255, 0] * img[mask == 255]
    a = mask != 255
    img[a] = 255 - img[a]
    return img


def makeItGreen(mask, img):
    img[mask == 255] = [0, 255, 0] * img[mask == 255]
    return img
