#!/usr/bin/env python
"""
Fetch HiPS tile from server.

Author: Adeel Ahmad
"""

import healpy as hp
import numpy as np
from astropy.coordinates import SkyCoord

"""
Transform a given angle (theta, phi) to the World Coordinate System.

"""


def ang2WCS(theta, phi, unit='radian'):
    if (unit is 'radian'):
        vector = hp.ang2vec(theta, phi)
    return vector


def fetch(survey, url, geocentric_coords, order, **kwargs):
    """
    Fetch tile from a HiPS server. Performs conversion as well.
    Parameters
    ----------
    survey : str
        Suvery where HiPS is hosted
    url : str
        URL excluding survey
    geocentric_coords : list(int)
        Contains WCS coordinates 
    order : int
        HiPS order 
    """

    # Rule followed: Tile N in order K -> NorderK / DirD / NpixN{.ext}
    nside = hp.order2nside(order)
    c = SkyCoord.from_name('crab')
    theta = (np.pi / 2) - c.dec.radian
    phi = c.ra.radian
    npixel = hp.ang2pix(nside, theta, phi)
    directory = np.around(int(npixel), decimals=-(len(str(npixel)) - 1))

    base_url = url + survey \
        + '/Norder' + str(order) + '/Dir' + str(directory) + \
        '/Npix' + str(npixel) + kwargs['format']

    # URL: Crab image
    # http://alasky.unistra.fr/DSS/DSSColor/Norder6/Dir20000/Npix24185.jpg

    # base_url = 'http://cade.irap.omp.eu/documents/Ancillary/4Aladin/AKARI_WideS/Norder3/Dir0/Npix346.' + \
    #     kwargs['format']

    if (kwargs['package'] is 'urllib'):
        import urllib.request

        data = urllib.request.urlopen(base_url).read()
    elif (kwargs['package'] is 'requests'):
        import requests

        data = requests.get(base_url).content

    print('WCS : ', ang2WCS(theta, phi))

    return data
