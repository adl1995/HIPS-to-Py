**Hierarchical progressive surveys (HiPS)**
===================

Overview
-
HiPS utilizes the HEALPix framework and uses it for mapping a sphere (in our case, part of a sky) and compiles / transforms it into tiles and pixels. Of course, this is in context of astronomical data. HiPS emphasizes on usability thus it tries abstract the scientific details (while preserving them). This can be further built upon for statistical analysis of large datasets.


**Introduction to HEALPix**
-
HEALPix, an acronym of 'Hierarchical Equal Area isoLatitude Pixelization of a sphere', is a framework for discretizing high resolution data. The software is available in C, C++, Fortran90, IDL, Java and Python. It extends a data structure (with a library), for each language. The main features provided by the software are:

* Pixel manipulation
* Spherical Harmonics Transforms
* Visualization
* Input / Output (supports FITS files)

In a nutshell, the pixelization procedure subdivides a spherical sphere in which each pixel is equidistant from the origin - meaning it covers the same surface area. This produces a HEALPix grid, whose interesting property pixels are distributed on lines on constant latitude. Due to this iso-latitude distribution of pixels the complexity for computing integrals over each harmonics is N ^ (1/2).
#### **Pixel numbering schemes** ####
HEALPix provides two numbering schemes for pixels, namely **RING scheme** and **NESTED scheme**
##### **RING scheme** #####
In this schemes the pixels are counted down from north to soutch along each iso-latitude ring.
##### **NESTED scheme** #####
 This schemes arranges the pixels in 12 tree structures with respect to base-resolution pixels.

Related tools
-
In addition to HEALPix, there are several other tools available for sky tessellation, and are used by various organizations / institutes. WorldWide Telescope (WWT) uses Hierarchical Triangular Mesh (HTM) and Tessellated Octahedral Adaptive Subdivision Transform (TOAST). Google uses a more cylindrical model.
 
**The coordinate system**
-
Before moving on to the coordinating systems used by HiPS, let's briefly go through some common measures using in astronomical studies.

##### **RA / DEC** #####
RA (right ascension) and DEC (declination) are the longitudes and latitudes of the sky. RA corresponds to east/west direction (like longitude), while Dec measures north/south directions, like latitude.

##### **WCS** #####
World coordinate system (WCS) comprises of latitude and longitude for describing a location on the Earth.

##### **FITS WCS** #####
The FITS "World Coordinate System" (WCS) standard defines keywords and usage that provide for the description of astronomical coordinate systems in a FITS image header. This is extensively used in HEALPix as it data from a FITS file.

##### **FITS** #####
Flexible Image Transport System (FITS) is a digital file format useful for storage, transmission and processing of scientific and other images, used by default by many sky tessellation softwares - in our case, HEALPix.

HEALPix header files can contain the following three letters, each depicting the coordinate system being used:

* **C**:Celestial=ICRS=RA/DEC(equatorial)=FK5 J2000 (default)
* **G**:Galactic
* **E**:Ecliptic (not mentioned in HiPS paper)

### **International Celestial Reference System** ###

ICRS is the current standard celestial reference system adopted by the International Astronomical Union (IAU). Its **origin is at the barycenter of the Solar System**, with axes that are intended to be "fixed" with respect to space - this is referred to as International Celestial Reference Frame (ICRF). ICRS coordinates are approximately the same as equatorial coordinates:

### **Fifth Fundamental Catalogue** ###

FK5 is a part of the "Catalogue of Fundamental Stars" which provides a series of six astrometric catalogues of high precision positional data for a small selection of stars to define a celestial reference frame. J2000 refers to the instant of 12pm (midday) on 1st January 2000. FK5, publish in 1991, added 3,117 new stars.

### **Galactic coordinate system** ###

The galactic coordinate system is a celestial coordinate system in spherical coordinates, with its **origin at the Sun**, the primary direction aligned with the approximate center of the Milky Way galaxy, and the fundamental plane parallel to an approximation of the galactic plane but offset to its north. GCS has its own Galactic longitude and Galactic latitude.

### **Ecliptic coordinate system** ###

A celestial coordinate system commonly used for representing the positions and orbits of Solar System objects. The system's **origin can be either the center of the Sun or the center of the Earth**, its primary direction is towards the vernal (northbound) equinox, and it has a right-handed convention.

**HiPS pixels**
-
Using the header *hips_pixel_bitpix* with the format -64, -32, 8, 16, 32, 64 (FITS convention) the pixels are stored in BITPIX code. The multi-resolution representation of the original images provides the basis for visualizing data in a progressive way as the pixels that are required for a given view can be accessed from the pre-computed HEALPix maps, and the nested pixel numbering scheme provides a simple hierarchical
indexing system that encodes pixel inheritance across the diﬀer-
ent orders.

**HiPS tiles**
-
As it is cumbersome to transfer each pixel (essentially a file), so HiPS scheme groups pixels in different tiles. The general relationship between
the tiles and pixels is that a tile with *n*-tile pixels along each
side forms a HEALPix mesh of order of *k*-tile.


**HiPS file structuring scheme**
-
In HiPS, tiles store the map information from HEALPix. These tiles are presented as square arrays and it is possible to store them in multiple file formats. Focusing on simplicity and usability, the description of arrays stored in files are straightforward with all the array positions being filled.
The files are organized in different directories. Here, tiles are used as files and tile orders are used for group data in directories - all following a naming convention. For more information on the method of storing files, view [this](http://aladin.unistra.fr/hips/hipsdoc.pdf) document, written by *Pierre Fernique*.

**HiPS images**
-
The way HiPS represents images is by resampling them on a HEALPix grid at the maximum desired order, say k<sup>max</sup>. Then it generates tile images for tile orders. When mosaicking / stitching images, the angular resolution is taken into account. There are various methods for filling the data region when stitching images and dealing with background difference. The k<sup>max</sup> chosen earlier determines minimum pixel size which is near to the angular pixel size or the resolution of original data.

Next important thing is whether to emphasize on ``display quality`` or ``photometric accuracy``, which depends on our use case. Image encoding can be done either in **FITS**, **PNG**, **JPG** file format. For most cases it is enough to only generate FITS and PNG files. The lowest order pixel values correspond to a large area of the sky. The HiPS indexing structure takes care of mapping correct tiles onto a display.

HiPS generation for huge amounts of data such as the Hubble Space Telescope requires planning of system growth.

**HiPS catalogues**
-
The same ways a tile in HiPS image survey contains a 512x512 image, a tile catalogue contains the RA / DEC coordinates stored in a TSV file. The data is ASCII tab separated and is organized in various directories the same way as HiPS images. 

**Multi-order coverage maps**
-
To define an MOC map, HEALPix pixels are considered at a given order, k. These HEALPix pixels point to a location in the sky. So, for a given data from a part of Sky, the MOC maps can be defined from them. For generating the MOC map, first the highest order values it found out for which we get the minimum pixel value. The resolution for MOC is determined by the highest order. The resolution of MOC is four times less than the k-max (maximum order) of HiPS.

**HiPS usage**

Mainly, HiPS is only used for tiles and images, however, it can be used as a container for other information related with sky. The format / content of this container can vary according to the use case. The data structures available in HiPS have so far been used for images, catalogues, and three dimensional cubes.

 *HiPS images

The way HiPS represents images is by resampling them on a HEALPix grid at the maximum desired order, say k-max. Then it generates tile images for tile orders. When mosaicking / stitching images, the angular resolution is taken into account. There are various methods available for filling the data region when stitching images and how to deal with the background difference. The k-max we chose earlier determines minimum pixel size which is near to  the angular pixel size or the resolution of the original data.

Next important thing is whether to emphasize on **display quality** or **photometric accuracy**, which depends on our use case. Image encoding can be done either in **FITS**, **PNG**, **JPG** file format. For most cases it is enough to only generate FITS and PNG files. The lowest order pixel values correspond to a large area of the sky. The HiPS indexing structure takes care of mapping correct tiles onto a display.

**Drawing HiPS tiles**
To draw HiPS tiles, affine transformation is used. For displaying a HiPS tile, first the best order is chosen to fit the display. Properties such as the maximum order and coordinate system (either ICRS or Galactic) are read from a file. The four corners of an image are mapped onto the display using affine transformation.  

Current progress
---------
I have already started conversing with Christoph Deil, who assigned me numerous tasks related with fetching HiPS tiles and displaying them using ``Matplotlib``. The calculation of ``Norder``, ``Npixels``, and ``Nside`` was done using ``Healpy``. The retrieved image was then decoded and displayed using
```python
tile = Image.open(BytesIO(data))
plt.imshow(tile)
```
There is also a different Python script that I wrote which retrieves a tile in JPG format and writes it as a FITS map. This was achieved using Astropy's ``astropy.writeto`` method. For writing the file, this code was used
```python
tile = Image.open(BytesIO(data))
hdu = fits.PrimaryHDU(tile)
hdu.writeto('tile.fits')
```
The transformation / mapping of Geocentric coordinates onto a HiPS pixel was achieved using this
```python
geocentric_coords = np.array([0.93085172744576927, 0.35906913416283726, 0.067708333333333329])
theta, phi = hp.vec2ang(geocentric_coords)
```
Utilizing ``theta`` and ``phi`` the pixel number was found
```python
npixel = hp.ang2pix(nside, theta, phi)
```
After going through all conversions and successfully writing a FITS map, I then loaded it using ``astropy.io.fits.open`` function.

Apart from this, I downloaded the Aladin desktop application and examined its various functionalities. It offers a tool for enabling HEALPix grid on the currently displayed image. This helped me better understand how to the grid gets divided at different zoom levels, and the relation between order and pixel numbers.
