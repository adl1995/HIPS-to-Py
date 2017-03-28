#!/usr/bin/env python
"""
Load a JPG, PNG, or FITS image.

Returns NumPy array containing image

Author: Adeel Ahmad
"""

from PIL import Image
from astropy.io import fits
from io import BytesIO
import numpy as np


def loadFITS(filename):
    hdulist = fits.open('output/'+filename+'.fits')
    return np.array(hdulist[0].data)


def loadJPG(filename):
    im = Image.open('output/'+filename+'.jpg')
    return np.array(im)


def loadPNG(filename):
    im = Image.open('output/'+filename+'.png')
    return np.array(im)


def storeFITS(data, filename='image'):
    hdu_list = fits.open(BytesIO(data))
    hdu = fits.PrimaryHDU(hdu_list[0].data)
    hdulist = fits.HDUList([hdu])
    hdulist.writeto('output/'+filename+'.fits', clobber=True)
    hdulist.close()


def storeJPG(data, filename='image'):
    tile = np.array(Image.open(BytesIO(data)))
    im = Image.fromarray(tile)
    im.save('output/'+filename+'.jpg')


def storePNG(data, filename='image'):
    tile = np.array(Image.open(BytesIO(data)))
    im = Image.fromarray(tile)
    im.save('output/'+filename+'.png')
