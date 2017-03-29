#!/usr/bin/env python
"""
Example script to fetch a HiPS image tile (PNG, JPG, FITS), display them using Matplotlib, store locally, and display from files.

We use the Crab nebula and DSSColor survey as an example.

Author: Adeel Ahmad
"""

from hipstools.io import image
from hipstools.info import header
from hipstools.retrieve import tiles
import matplotlib.pyplot as plt

# define metadata
survey = '/2MASS6X/2MASS6X_H'
geocentric_coords = [0.93085172744576927,
                     0.35906913416283726, 0.067708333333333329]
url = 'http://cade.irap.omp.eu'
order = 7
extension = '.jpg'

# fetch tile
data = tiles.fetch(survey, url, geocentric_coords, order,
                   package='requests', format=extension)

# store images locally
if extension is 'fits':
    image.storeFITS(data, 'image')
elif extension is 'png':
    image.storePNG(data, 'image')
else:
    image.storeJPG(data, 'image')

# load images from files
if extension is 'fits':
    tile = image.loadFITS('image')
elif extension is 'png':
    tile = image.loadPNG('image')
else:
    tile = image.loadJPG('image')

# display data type
print('Data type: ', tile.dtype)

# display header information
if extension is 'fits':
    print('Header information: ', header.headerFITS(data))

# plot image
plt.imshow(tile)
plt.show()
