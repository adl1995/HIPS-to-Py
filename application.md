**HiPS to Py**
==============
> Suborganization: Astropy

Student information
-------------------

### Personal details ###
* **Name**: Adeel Ahmad
* **Email**: adeelahmadadl1995@gmail.com
* **GitHub**: adl1995
* **IRC (#OpenAstronomy)**: adl1995
* **Timezone**: UTC +05:00
* **Blog**: http://adl1995.github.io/

### Academic details ###
* **University**: National University of Computer and Emerging Sciences, Islamabad
* **Degree**: Computer Science 
* **Graduation year**: 2018 

Background
------

In my previous semester, I enrolled myself in Digital Image Processing course. During the tenure of this course I implemented filters (Gaussian, Sobel, Prewitt, Laplacian), edge detectors (Canny, Marr Hildreth), morphological operators (Covex hulling, Erosion, Dilation), object detectors (Generalized Hough transform, simple convolution), and seam carvers. These were implemented purely in Python, making no use of any library other than ``Numpy`` and ``Matplotlib``. This attenuated my interest in Computer Vision and I have been an active researcher since then. I have showcased these project on my [GitHub profile](https://github.com/adl1995). The most interesting algorithm I implemented was [Generalized Hough Tranfrom](https://github.com/adl1995/generalised-hough-transform). I was amazed as to how something as simple as an equation of line could lead to detection of objects in images. Although my implementation was only scale invariant, I plan on extending this invariancy to orientation as well. Altough the 'HiPS to Py' project involves Computer Vision concepts at a brief level, building a visualization framework has been my interested for quite some time. 

Apart from this, I have also been a PHP web developer for almost two years, and I have worked on multitude of project ranging for SaaS to e-commerce websites. I work remotely on [Upwork](https://www.upwork.com/freelancers/~018e56b8591046f889) and [Fiverr](https://www.fiverr.com/adl1995). My clients are either IT organizations or independent contractors. I have also worked on web automation and data scraping using ``Selenium`` and ``BeautifulSoup``. Although these skills are not required for this organization and have no direct links in my project, it shows that I am persistent and hard-working. The skills that I acquire are through self learning and consistency. Currently I am building an application using [Google Application Engine](https://github.com/adl1995/zoho-portal).

I started collaborating with Open Source organizations for only about a month now, and my experience has been excellent so far. The mentors have been very kind, welcoming and have provided assistance along the way. Given my background in Computer Vision and being good at problem solving, I firmly believe this prestigious organization and its users will benefit by HiPS client for Python. It would also provide me with a working ground knowledge on Astronomy.

Project Details
---------------

### Mentors ###
> * [Christoph Deil](https://github.com/cdeil)
* [Thomas Boch](https://github.com/tboch)

### Abstract ###
> Design and create a Python client for Hierarchical Progressive Surveys (HiPS). This will enable users to view astronomical figures in an interactive environment, similar to Google Maps. Currently, such clients exist, such as Aladin and Aladin Lite, but they are written in Java and JavaScript, respectively. The goal of this project is to provide similar functionality using Python. The current decision is to work only with HiPS images, but if everything goes well, I wish to work on HiPS catalogues as well. 

### Detailed description ###
Hierarchical progressive surveys (HiPS) utilizes the HEALPix framework for mapping a sphere (in our case, part of a sky) and compiles / transforms it into tiles and pixels. HiPS emphasizes on usability and thus tries to abstract the scientific details (while preserving them). This can be further built upon for statistical analysis of large datasets. For this project, a HiPS Python client is to be implemented which will enable users to view / explore astronomical figures. HiPS data is stored in the form of catalogues (TSV), or tiles (PNG, JPG, FITS). In the context of this project only tiles are to be retrieved and stitched together to get the final output. Listed below are current HiPS clients:

* Aladin Desktop
* Aladin Lite (CDS)
* MIZAR
* ESAsky
* JUDO2 

The goal of this project would be to create a new HiPS client under ``astropy/hips``. However, this would run purely on Python. The possible dependencies for this software are:

* Python >= 3.5
* Astropy
* Healpy
* Numpy
* Retransform

#### The HEALPix framework ####

HEALPix, an acronym of 'Hierarchical Equal Area isoLatitude Pixelization of a sphere', is a framework for discretizing high resolution data. The software is available in C, C++, Fortran90, IDL, Java, and Python. It extends a data structure (with a library), for each language. The main features provided by this software are:

  * Pixel manipulation
  * Spherical Harmonics Transforms
  * Visualization
  * Input / Output (supports FITS files)

In a nutshell, the pixelization procedure subdivides a spherical sphere in which each pixel is equidistant from the origin - meaning it covers the same surface area. This produces a HEALPix grid, whose interesting property is that pixels are distributed on lines of constant latitude. Due to this iso-latitude distribution of pixels the complexity for computing integrals over each harmonics is N<sup>1/2</sup>.

#### Pixel numbering schemes ####

HEALPix provides two numbering schemes for pixels, namely **RING scheme** and **NESTED scheme**.
    
Some alternative tools to HEALPix are Hierarchical Triangular Mesh (HTM) and Tessellated Octahedral Adaptive Subdivision Transform (TOAST).

#### HEALPix coordinate system ####
HEALPix header files contain one of the following three letters, each depicting the coordinate system being used:

* C:Celestial=ICRS=RA/DEC(equatorial)=FK5 J2000
* G:Galactic
* E:Ecliptic

HiPS uses the Celestial coordinate system by default. Also, HiPS does not support Ecliptic coordinate system.

#### HiPS pixels ####
Using the header ``hips_pixel_bitpix`` with the format -64, -32, 8, 16, 32, 64 (FITS convention) the pixels are stored in ``BITPIX`` code. The multi-resolution representation of original images provides the basis for visualizing data in a progressive way as the pixels that are required for a given view can be accessed through pre-computed HEALPix maps, and the nested pixel numbering scheme provides a simple hierarchical indexing system that encodes pixel inheritance across different orders.

#### HiPS tiles ####
As it is cumbersome to transfer each pixel (essentially a file), HiPS scheme groups pixels in different tiles. The general relationship between tiles and pixels is that a tile with n-tile pixels along each side forms a HEALPix mesh of order of k-tile.

#### HiPS file structuring scheme ####
In HiPS, tiles store map information from HEALPix. These tiles are presented as square arrays and it is possible to store them in multiple file formats. Focusing on simplicity and usability, the description of arrays stored in files are straightforward with all the array positions being filled. The files are organized in different directories. Here, tiles are used as files and tile orders are used for grouping data in directories - all following a naming convention. For more information on the method of storing files, [this](http://aladin.unistra.fr/hips/hipsdoc.pdf) document can be viewed, written by Pierre Fernique.

#### HiPS images ####
The way HiPS represents images is by resampling them on a HEALPix grid at the maximum desired order, say k<sup>max</sup>. Then it generates tile images for tile orders. When mosaicking / stitching images, the angular resolution is taken into account. There are various methods for filling the data region when stitching images and dealing with background difference. The k<sup>max</sup> chosen earlier determines minimum pixel size which is near to the angular pixel size or the resolution of original data.

Next important thing is whether to emphasize on ``display quality`` or ``photometric accuracy``, which depends on our use case. Image encoding can be done either in **FITS**, **PNG**, **JPG** file format. For most cases it is enough to only generate FITS and PNG files. The lowest order pixel values correspond to a large area of the sky. The HiPS indexing structure takes care of mapping correct tiles onto a display.

HiPS generation for huge amounts of data such as the Hubble Space Telescope requires planning of system growth.

#### HiPS catalogues ####
The same ways a tile in HiPS image survey contains a 512x512 image, a tile catalogue contains the RA / DEC coordinates stored in a TSV file. The data is ASCII tab separated and is organized in various directories the same way as HiPS images. 

## Benefits ##
HiPS addresses the challenge of big data in astronomy. It describes data in a multi-resolution manner, so it effectively creates an ease in its access. It can also be utilized for data sharing and interoperability. HiPS provides a means for conserving scientific details of astronomical data. MOC maps generated using HiPS facilitate the comparison of sky region between different data sets, and can be used to establish regions of intersection between multiple surveys. It helps to avoid complex queries on database through the initial first response.

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

## Timeline ##

| Time Period        | Plan           |
| ------------- | ------------- |
| May 04, 2017 - May 30, 2017 **(Community Bonding Period)**      |   <ul><li>Finalize on the deliverables.</li><li>Discuss with mentors and get a final idea on how to approach the problem.<li>Discuss with mentors on which Python package to use for GUI implementation, for example ``PyQt``.</li><li>Discuss with mentors which documentation generation tool to use such as ``Sphinx`` or ``Doxygen``.</li></ul>|
| | **Part 1 starts** |
| May 30, 2017 - June 15, 2017 ( 2 weeks ) | <ul><li>Set up the developement environment, get familiar with Astropy's coding practices.</li><li>Write a skeleton layout of the algorithm / code to implement.</li></ul> |
| June 16, 2017 - June 30, 2017 ( 2 weeks ) | <ul><li>Document and write test cases for the added part.</li><li>**Update 1 : Push code so it is possible to view images on  providing coordinates.**</li></ul>|
| | **Part 1 completed**<br />**Part 2 starts** |
| July 01, 2017 - July 14, 2017 ( 2 weeks ) | <ul><li>Link the implemented part with GU interface.</li><li>Add functionality that enables user to apply filters on images for better results.</li></ul> |
| July 15, 2017 - July 28, 2017 ( 2 weeks ) | <ul><li>Add optimizations, write test cases.</li><li>Add support for HiPS catalogues (to be discussed).</li></ul> |
| | **Part 2 completed** |
| August 21, 2017 - August 29, 2017 **(Students Submit Code and Evaluations)** | <ul><li>Clean up code.</li><li>Improve documentation.</li><li>Add further test cases.</li><li>Code refactoring (if required).</li><li>Resolve merge conflicts (if any).</li></ul> |
| August 29, 2017 - September 05, 2017 | Mentors submit final student evaluations. |
| September 06, 2017 | Results Announced. |

## Availability ##

My final exams end on May 20<sup>th</sup>. So, I will have ample time for the community bonding period. After that, I will be free during the whole summer i.e. almost three months. I do not have any other commitments, so I can focus all my attention to GSoC.

