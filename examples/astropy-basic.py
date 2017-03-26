#!/usr/bin/env python
"""
Example script showing Astropy's basic functionality.
"""

from astropy import units as u
from astropy.coordinates import SkyCoord

c = SkyCoord(ra=10.625 * u.degree, dec=41.2 * u.degree, frame='icrs')
c = SkyCoord(10.625, 41.2, frame='icrs', unit='deg')
c = SkyCoord('00h42m30s', '+41d12m00s', frame='icrs')
c = SkyCoord('00h42.5m', '+41d12m')
c = SkyCoord('00 42 30 +41 12 00', unit=(u.hourangle, u.deg))
c = SkyCoord('00:42.5 +41:12', unit=(u.hourangle, u.deg))

# storing multiple object in same object
c = SkyCoord(ra=[10, 11, 12, 13] * u.degree, dec=[41, -5, 42, 0] * u.degree)
print(c.shape)

# Coordinate access
c = SkyCoord(ra=10.68458 * u.degree, dec=41.26917 * u.degree)
print(c.ra)
print(c.ra.hour)
print(c.ra.hms)
print(c.dec)
print(c.dec.degree)
print(c.dec.radian)

# coverting coordinates to string
print(c.to_string('decimal'))
print(c.to_string('dms'))
print(c.to_string('hmsdms'))

# Transformation - getting coordinate in galactic frame
c_icrs = SkyCoord(ra=10.68458 * u.degree, dec=41.26917 * u.degree, frame='icrs')
c_icrs.galactic

# Representation
c = SkyCoord(x=1, y=2, z=3, unit='kpc', representation='cartesian')
print(c)
print(c.x, c.y, c.z)

c.representation = 'cylindrical'
print(c)

# Distance
c = SkyCoord(ra=10.68458 * u.degree, dec=41.26917 * u.degree, distance=770 * u.kpc)
print(c.cartesian.x)
print(c.cartesian.y)
print(c.cartesian.z)

# making use of 3D information
c1 = SkyCoord(ra=10 * u.degree, dec=9 * u.degree, distance=10 * u.pc, frame='icrs')
c2 = SkyCoord(ra=11 * u.degree, dec=10 * u.degree, distance=11.5 * u.pc, frame='icrs')
print(c1.separation_3d(c2))

# convenience methods
c1 = SkyCoord(ra=10 * u.degree, dec=9 * u.degree, frame='icrs')
c2 = SkyCoord(ra=11 * u.degree, dec=10 * u.degree, frame='fk5')
print(c1.separation(c2))  # Differing frames handled correctly  

print(SkyCoord.from_name("M42"))

from astropy.coordinates import EarthLocation

print(EarthLocation.of_site('Apache Point Observatory'))

# these method query Google Maps to retreive information
print(EarthLocation.of_address('1002 Holy Grail Court, St. Louis, MO'))
print(EarthLocation.of_address('1002 Holy Grail Court, St. Louis, MO', get_height=True))
print(EarthLocation.of_address('Danbury, CT'))
