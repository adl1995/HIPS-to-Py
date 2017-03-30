#!/usr/bin/env python
"""
Get a JPG, PNG, or FITS image header.

Returns NumPy array containing image

Author: Adeel Ahmad
"""
from astropy.io import fits
from io import BytesIO


def headerFITS(data):
    """
    Load FITS image header.
    Parameters
    ----------
    data : np array
        Array containing FITS image information
    """
    hdu_list = fits.open(BytesIO(data))
    hdu = fits.PrimaryHDU(hdu_list[0].data)
    hdulist = fits.HDUList([hdu])
    # hdulist = fits.open(filename+'.fits')
    return hdulist[0].header


def headerPNG():
    return


def headerJPG():
    return
