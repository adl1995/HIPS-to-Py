#!/usr/bin/env python
# @Author: Adeel Ahmad

from PIL import Image
from io import BytesIO

import healpy as hp
import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.coordinates import get_sun
from astropy.time import Time

# Rule followed: Tile N in order K -> NorderK / DirD / NpixN{.ext}
survey = 'DSSColor'
geocentric_coords = np.array([0.93085172744576927, 0.35906913416283726, 0.067708333333333329])
order = 7
theta, phi = hp.vec2ang(np.array(geocentric_coords))
nside = hp.order2nside(order)
npixel = hp.ang2pix(nside, theta, phi)[0]
directory = np.around(int(npixel), decimals=-(len(str(npixel)) - 1))

# t = Time('2016-03-20 4:30:00')
# print(get_sun(t))
# Returns a GCRS frame

# Coordinates for the Crab Nebula
# c = SkyCoord(ra=5.5755472222222*u.degree, dec=22.014472222222*u.degree, frame='icrs')
# c = c.galactic
# print(c)
# How to convert this to GCRS?

import numpy
from astropy import wcs
w = wcs.WCS(naxis=2)

# Set up an "Airy's zenithal" projection
# Vector properties may be set with Python lists, or Numpy arrays
w.wcs.crpix = [-234.75, 8.3393]
w.wcs.cdelt = numpy.array([-0.066667, 0.066667])
w.wcs.crval = [0, -90]
w.wcs.ctype = ["RA---HPX", "DEC--HPX"]
w.wcs.set_pv([(2, 1, 45.0)])

res = hp.ang2pix(nside, 250.96708936, -73.49289645)
print(res)

# Some pixel coordinates of interest.
pixcrd = numpy.array([[0, 0], [24, 38], [45, 98]], numpy.float_)

# Convert pixel coordinates to world coordinates
world = w.wcs_pix2world(pixcrd, 1)
print(world)
base_url = 'http://alasky.u-strasbg.fr/DSS/' + survey \
           + '/Norder' + str(order) + '/Dir' + str(directory) + '/Npix' + str(npixel) + '.jpg'

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

tile = np.array(Image.open(BytesIO(data)))
plt.imshow(tile)
plt.show()