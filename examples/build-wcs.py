# Set the WCS information manually by setting properties of the WCS
# object.

from __future__ import division, print_function

import numpy
from astropy import wcs
from astropy.io import fits
import matplotlib.pyplot as plt

# Create a new WCS object. The number of axes must be set
# from the start
w = wcs.WCS(naxis=2)

# Set up an "Airy's zenithal" projection
# Vector properties may be set with Python lists, or Numpy arrays
w.wcs.crpix = [-234.75, 8.3393]
w.wcs.cdelt = numpy.array([-0.066667, 0.066667])
w.wcs.crval = [0, -90]
w.wcs.ctype = ["RA---CAR", "DEC--CAR"]
w.wcs.set_pv([(2, 1, 45.0)])

print("WCS object : ", w.wcs)

# Some pixel coordinates of interest.
pixcrd = numpy.array([[0, 0], [24, 38], [45, 98]], numpy.float_)

# Convert pixel coordinates to world coordinates
world = w.wcs_pix2world(pixcrd, 1)
print(world)

# Convert the same coordinates back to pixel coordinates.
pixcrd2 = w.wcs_world2pix(world, 1)
print(pixcrd2)

# These should be the same as the original pixel coordinates, modulo
# some floating-point error.
assert numpy.max(numpy.abs(pixcrd - pixcrd2)) < 1e-6

# Now, write out the WCS object as a FITS header
header = w.to_header()

# header is an astropy.io.fits.Header object.  We can use it to create a new
# PrimaryHDU and write it to a file.
hdu = fits.PrimaryHDU(header=header)
# Save to FITS file
# hdu.writeto('test.fits')


# Creating 512x512 numpy array filled with random values 
image = numpy.random.rand(512,512)
# plt.subplot(projection=wcs)
plt.imshow(image)
plt.grid(color='white', ls='solid')
plt.xlabel('Galactic Longitude')
plt.ylabel('Galactic Latitude')
# plt.imshow(image)
plt.show()
