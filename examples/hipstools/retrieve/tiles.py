#!/usr/bin/env python
"""
Fetch HiPS tile from server.

Author: Adeel Ahmad
"""

import healpy as hp
import numpy as np


def fetch(survey, url, geocentric_coords, order, **kwargs):
        # Rule followed: Tile N in order K -> NorderK / DirD / NpixN{.ext}
    theta, phi = hp.vec2ang(np.array(geocentric_coords))
    nside = hp.order2nside(order)
    npixel = hp.ang2pix(nside, theta, phi)[0]
    directory = np.around(int(npixel), decimals=-(len(str(npixel)) - 1))

    # base_url = 'http://alasky.u-strasbg.fr/' + survey \
    #            + '/Norder' + str(order) + '/Dir' + str(directory) + '/Npix' + str(npixel) + '.jpg'
    base_url = 'http://cade.irap.omp.eu/documents/Ancillary/4Aladin/AKARI_WideS/Norder3/Dir0/Npix346.' + \
        kwargs['format']

    if (kwargs['package'] is 'urllib'):
        import urllib.request

        data = urllib.request.urlopen(base_url).read()
    elif (kwargs['package'] is 'requests'):
        import requests

        data = requests.get(base_url).content

        # t = Time('2016-03-20 4:30:00')
        # print(get_sun(t))
        # Returns a GCRS frame

        # Coordinates for the Crab Nebula
        # c = SkyCoord(ra=5.5755472222222*u.degree, dec=22.014472222222*u.degree, frame='icrs')
        # c = c.galactic
        # print(c)
        # How to convert this to GCRS?

    return data
