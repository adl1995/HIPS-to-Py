#!/usr/bin/env python
"""
Example script to fetch a HiPS image tile (PNG, JPG, FITS), display them using Matplotlib, store locally, and display from files.

We use the Crab nebula and DSSColor survey as an example.

Author: Adeel Ahmad
"""

from PIL import Image
from io import BytesIO

import healpy as hp
import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np

# Rule followed: Tile N in order K -> NorderK / DirD / NpixN{.ext}
survey = '2MASS6X/2MASS6X_H'
geocentric_coords = np.array([0.93085172744576927, 0.35906913416283726, 0.067708333333333329])
order = 7
theta, phi = hp.vec2ang(np.array(geocentric_coords))
nside = hp.order2nside(order)
npixel = hp.ang2pix(nside, theta, phi)[0]
directory = np.around(int(npixel), decimals=-(len(str(npixel)) - 1))
ext = 'fits'

# t = Time('2016-03-20 4:30:00')
# print(get_sun(t))
# Returns a GCRS frame

# Coordinates for the Crab Nebula
# c = SkyCoord(ra=5.5755472222222*u.degree, dec=22.014472222222*u.degree, frame='icrs')
# c = c.galactic
# print(c)
# How to convert this to GCRS?

# base_url = 'http://alasky.u-strasbg.fr/' + survey \
#            + '/Norder' + str(order) + '/Dir' + str(directory) + '/Npix' + str(npixel) + '.jpg'

base_url = 'http://cade.irap.omp.eu/documents/Ancillary/4Aladin/AKARI_WideS/Norder3/Dir0/Npix346.' + ext
print('Choose a library for retreiving HiPS data: \n1. URLlib\n2. Requests')
choice = input('Enter your choice: ')

if (choice is '1'):
    import urllib.request

    data = urllib.request.urlopen(base_url).read()
elif (choice is '2'):
    import requests

    data = requests.get(base_url).content
else:
    print('Invalid choice')

# decode and store image locally
if ext is 'fits':
	hdu_list = fits.open(BytesIO(data))
	tile = np.array(hdu_list[0].data)
	hdu = fits.PrimaryHDU(hdu_list[0].data)
	hdulist = fits.HDUList([hdu])
	hdulist.writeto('image.fits', clobber=True)
	hdulist.close()
else:
	tile = np.array(Image.open(BytesIO(data)))
	im = Image.fromarray(tile)
	im.save('image.'+ext)

# display images directly from server
plt.imshow(tile)
plt.show()

# display images from files
if ext is 'fits':
	hdulist = fits.open('image.'+ext)
	tile = (np.array(hdu_list[0].data))
else:
	tile = Image.open('image.'+ext)

plt.imshow(tile)
plt.show()
