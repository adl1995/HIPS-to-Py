**An overview of Hierarchical progressive surveys (HiPS) and the HEALPix framework**
------------------------------------------------------

HiPS utilizes the HEALPix framework and uses it for mapping a sphere (in this case, part of a sky) and compiles / transforms it into [tiles](#hips-tiles) and [pixels](#hips-pixels). Of course, this is in context of astronomical data. HiPS emphasizes on usability thus it tries abstract the scientific details while preserving them. This can be further built upon for statistical analysis of large datasets. Thus, first a brief overview of HEALPix is given below before moving onto HiPS.

### Introduction to HEALPix
HEALPix, an acronym of 'Hierarchical Equal Area isoLatitude Pixelization of a sphere', is a framework for discretizing high resolution data. The software is available in C, C++, Fortran90, IDL, Java, and Python. It extends a data structure (with a library), for each language. The main features provided by the software are:

* Pixel manipulation
* Spherical Harmonics Transforms
* Visualization
* Input / Output (supports FITS files)

In a nutshell, the pixelization procedure subdivides a spherical sphere in which each pixel is equidistant from the origin - meaning it covers the same surface area. This produces a HEALPix grid, whose interesting property is that pixels are distributed on lines of constant latitude. Due to this iso-latitude distribution of pixels the complexity for computing integrals over each harmonics is N<sup>1/2</sup>.

HEALPix provides a standard format on how to store data in FITS files.  There are numerous software packages that can work with HEALPix data. For this project, ``healpy`` will be used which is built on the HEALPix C++ package. But there are others, e.g. in Aladin Lite. The main functionality needed for this project is HEALPix pixel index to sky coordinate transformation (back and forth), and one or two methods to list HEALPix pixels in a given region of the sky (e.g. ``query_disc`` from ``healpy``).

#### Pixel numbering schemes
HEALPix provides two numbering schemes for pixels, namely the **RING scheme** and **NESTED scheme**.
##### 

 - **RING scheme**
In this scheme the pixels are counted down from north to south along each iso-latitude ring.
 - **NESTED scheme**
 This scheme arranges the pixels into 12 tree structures with respect to their base-resolution pixels.

### Introduction to HiPS

HiPS is the hierarchical tiling mechanism which allows one to access, visualize and browse seamlessly image, catalogue and cube data. The original HiPS paper can be found [here](https://arxiv.org/pdf/1505.02291.pdf).

### HiPS working
The multi-resolution representation of original images provides the basis for visualizing data in a progressive way as the pixels that are required for a given view can be accessed through pre-computed HEALPix maps, and the nested pixel numbering scheme provides a simple hierarchical indexing system that encodes pixel inheritance across different orders.

HiPS scheme groups pixels into different tiles. The general relationship between tiles and pixels is that a tile with ``n-tile`` pixels along each side forms a HEALPix mesh of order k<sup>tile</sup>. Tiles store map information from HEALPix. These tiles are presented as square arrays and it is possible to store them in different file formats. The files are organized into different directories. Here tiles are used as files and tile orders are used for grouping data in directories - all following a naming convention. For more information on the method on file storage, [this](http://aladin.unistra.fr/hips/hipsdoc.pdf) document can be viewed, written by Pierre Fernique.

### HiPS pixels
Using the header ``hips_pixel_bitpix`` the HiPS pixels are stored in BITPIX code. ``hips_pixel_bitpix`` refers to the data type used to store the FITS tile (a value of 8 means 8-bits integers, -32 means simple floating points, -64 double precision floating points).

This is usually the same value as the BITPIX value of the original images (described in keyword data_pixel_bitpix), but might be different, notably for HiPS built from heterogeneous origins.

The BITPIX value is always present in the HiPS FITS tiles.
### HiPS tiles
As it is cumbersome to transfer each pixel (essentially a file), so HiPS scheme groups pixels into different tiles. The general relationship between the tiles and pixels is that a tile with *n*-tile pixels along each
side forms a HEALPix mesh of order of *k*-tile.

### HiPS images

The way HiPS represents images is by resampling them onto a HEALPix grid at the maximum desired order, say k<sup>max</sup>. Then it generates tile images for tile orders. When mosaicking / stitching images, the angular resolution is taken into account. There are various methods for filling the data region when stitching images and dealing with background difference. The k<sup>max</sup> chosen earlier determines minimum pixel size which is near to the angular pixel size or the resolution of original data.

Next important thing is whether to emphasize on ``display quality`` or ``photometric accuracy``, which depends on our use case. Image encoding can be done either in **FITS**, **PNG**, or **JPG** file format. For most cases it is enough to only generate FITS and PNG files. The lowest order pixel values correspond to a large area of the sky. The HiPS indexing structure takes care of mapping correct tiles onto a display.

HiPS generation for huge amounts of data such as the Hubble Space Telescope requires planning of system growth.

### HiPS catalogues

A HiPS catalogue contains the RA / DEC coordinates stored in a TSV file. The data is ASCII tab separated and is organized in various directories the same way as HiPS images.

### Google Summer of Code project

I have been selected for creating this package along with two mentors, [Christoph Deil](https://github.com/cdeil) and  [Thomas Boch](https://github.com/tboch). My GSoC application can be found [here](https://github.com/adl1995/HIPS-to-Py/blob/master/documents/application.md). The goal of this project is to design and create a Python client for Hierarchical Progressive Surveys (HiPS). The library will extend a low and high level API for exploring and creating WCS / HEALPix images. Currently, there are some clients built using HiPS, such as Aladin and Aladin Lite, but they are written in Java and JavaScript, respectively. After the trivial functionality is complete, additional features such as measuring fluxes and overplotting multi-wavelength data will also be added. The code repository for this project can be found [here](https://github.com/hipspy/hips).  If anyone has any questions or suggestions regarding the package, they are encouraged to open issues. If you want to help us build the package or add extra features onto it, please upon up a pull request.

The coding period is about to start. My future blog posts will be based around this topic.

