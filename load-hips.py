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