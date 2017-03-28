#!/usr/bin/env python
"""
Example script to fetch a HiPS image tile and save it using Astropy.

The FITS image is then loaded and displayed using Matplotlib.
Author: Adeel Ahmad
"""
from hipstools.io import image
from hipstools.info import header
from hipstools.retrieve import tiles
import matplotlib.pyplot as plt

# define metadata
survey = '2MASS6X/2MASS6X_H'
geocentric_coords = [0.93085172744576927,
                     0.35906913416283726, 0.067708333333333329]
url = 'http://cade.irap.omp.eu'
order = 7
extension = 'fits'

# fetch tile
data = tiles.fetch(survey, url, geocentric_coords, order,
                   package='requests', format=extension)

# store tile
image.storeFITS(data, 'fits')

# load tile
tile = image.loadFITS('image')

# display tile
plt.imshow(tile, cmap='gray')
plt.colorbar()
plt.show()
