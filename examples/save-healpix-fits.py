#!/usr/bin/env python
"""
Example script to fetch a HiPS image tile and save it using Astropy.

The FITS image is then loaded and displayed using Matplotlib.
Author: Adeel Ahmad
"""

from PIL import Image
from io import BytesIO

import healpy as hp
import matplotlib.pyplot as plt
import numpy as np
import urllib.request
from astropy.io import fits

# Rule followed: Tile N in order K -> NorderK / DirD / NpixN{.ext}
survey = 'DSSColor'
geocentric_coords = np.array([0.93085172744576927, 0.35906913416283726, 0.067708333333333329])
order = 7
theta, phi = hp.vec2ang(np.array(geocentric_coords))
nside = hp.order2nside(order)
npixel = hp.ang2pix(nside, theta, phi)[0]
directory = np.around(int(npixel), decimals=-(len(str(npixel)) - 1))

base_url = 'http://alasky.u-strasbg.fr/DSS/' + survey \
           + '/Norder' + str(order) + '/Dir' + str(directory) + '/Npix' + str(npixel) + '.jpg'

data = urllib.request.urlopen(base_url).read()
tile = np.array(Image.open(BytesIO(data)))

hdu = fits.PrimaryHDU(tile)

hdu.writeto('tile.fits')

hdu_list = fits.open('tile.fits')

plt.imshow(hdu_list[0].data, cmap='gray')
plt.colorbar()
plt.show()
