**HiPS to Py**
==============

> * Organization: OpenAstronomy
> * Suborganization: Astropy

Student information
-------------------

### Personal details ###
* **Name**: Adeel Ahmad
* **Email**: adeelahmadadl1995@gmail.com
* **GitHub handle**: adl1995
* **IRC (#OpenAstronomy)**: adl1995
* **Timezone**: UTC +05:00
* **Blog**: http://adl1995.github.io/

### Academic details ###
* **University**: National University of Computer and Emerging Sciences, Islamabad
* **Degree**: Computer Science
* **Graduation year**: 2018

Background
------

In my previous semester, I enrolled myself in Digital Image Processing course. During the tenure of this course I implemented filters (Gaussian, Sobel, Prewitt, Laplacian), edge detectors (Canny, Marr Hildreth), morphological operators (Convex hulling, Erosion, Dilation), object detectors (Generalized Hough transform, simple convolution), and seam carvers. These were implemented purely in Python, making no use external libraries other than ``Numpy`` and ``Matplotlib``. This attenuated my interest in Computer Vision and I have been an active researcher in the domain since then. I have showcased these project on my [GitHub profile](https://github.com/adl1995). The most interesting algorithm I implemented was [Generalized Hough Tranfrom](https://github.com/adl1995/generalised-hough-transform). I was amazed as to how something as simple as an equation of line could lead to detection of objects in images. Although the 'HiPS to Py' project involves Computer Vision concepts at a brief level mostly related with affine transformation, it would still benefit from my knowledge of the domain.

Apart from this, I have also been a PHP web developer for almost two years, and I have worked on multitude of projects ranging for SaaS to e-commerce websites. I work remotely on [Upwork](https://www.upwork.com/freelancers/~018e56b8591046f889) and [Fiverr](https://www.fiverr.com/adl1995). My clients are either IT organizations or independent contractors. I have also worked on web automation and data scraping using ``Selenium`` and ``BeautifulSoup``. Although these skills are not required for this organization and have no direct links in my project, it shows that I am persistent and hard-working. The skills that I acquire are through self learning and consistency. Currently, I am building an application using [Google Application Engine](https://github.com/adl1995/zoho-portal).

I started collaborating with Open Source organizations for only about a month ago, and my experience has been excellent so far. The mentors have been very kind, welcoming and have provided assistance along the way. Given my background in Computer Vision and being good at problem solving, I firmly believe this prestigious organization and its users will benefit by the HiPS client for Python. It would also provide me with a working ground knowledge on Astronomy.

During the tenure of this project, I hope to improve my skills with tools like  ``Jupyter``, ``Pytest``, ``Sphinx``, and ``Git``. It will also provide me with a professional level overview on how to write applications, make plans, organize projects, working remotely with other developers, and design a good API.

Project Details
---------------

### Mentors ###
> * [Christoph Deil](https://github.com/cdeil)
> * [Thomas Boch](https://github.com/tboch)

### Abstract ###
> Design and create a Python client for Hierarchical Progressive Surveys (HiPS). The library extend a Low and High level API for exploring or creating WCS / HEALPix images. Currently, there are clients built using HiPS, such as Aladin and Aladin Lite, but they are written in Java and JavaScript, respectively. The goal of this project is that for a given World Coordinate System and image size (nx, ny), create a NumPy array containing the image by fetching tiles and projecting them onto an image array. After this features like measuring fluxes and overplotting multi-wavelength data are to be added. If everything goes well, I wish to work on HiPS catalogues as well. An optional feature is to create a GUI viewer.

### Detailed description ###
Hierarchical progressive surveys (HiPS) utilizes the HEALPix framework for mapping a sphere (in our case, part of a sky) and compiles / transforms it into tiles and pixels. For this project, a HiPS Python client is to be implemented which will enable users to create WCS and HEALPix images. Functionality for exploring HiPS information / metadata will also be available.

The goal of this project would be to create a new HiPS client under ``tboch/hips``. The **main dependencies** for this software include:

* [Python](https://www.python.org/) >= 3.5
* [NumPy](http://www.numpy.org/)
* [Astropy](http://docs.astropy.org/en/stable/)
* [Healpy](http://healpy.readthedocs.io/)

Some other **possible dependencies** for tile drawing include:
* [Reproject](http://reproject.readthedocs.io/en/stable/)
* [SciPy](https://docs.scipy.org/doc/scipy/reference/tutorial/ndimage.html#interpolation-functions)

#### The HEALPix framework ####

This project will involve the HEALPix 'Hierarchical Equal Area isoLatitude Pixelization of a sphere' framework for discretizing high resolution data. This framework has implementations in many languages and extends a data structure (with a library) for each language. The main features provided by this software are:

  * Pixel manipulation
  * Spherical Harmonics Transforms
  * Visualization
  * Input / Output (supports FITS files)

In a nutshell, the pixelization procedure subdivides a spherical sphere in which each pixel is equidistant from the origin - meaning it covers the same surface area. This produces a HEALPix grid. The framework provides two numbering schemes for pixels, namely **RING scheme** and **NESTED scheme**. It provides three coordinate systems, namely **Celestial** (HiPS default), **Galactic**, and **Ecliptic**.

Some alternative tools to HEALPix are Hierarchical Triangular Mesh (HTM) and Tessellated Octahedral Adaptive Subdivision Transform (TOAST).

HiPS uses the Celestial coordinate system by default. Also, HiPS does not support the Ecliptic coordinate system.

#### HiPS working ####
The multi-resolution representation of original images provides the basis for visualizing data in a progressive way as the pixels that are required for a given view can be accessed through pre-computed HEALPix maps, and the nested pixel numbering scheme provides a simple hierarchical indexing system that encodes pixel inheritance across different orders.

HiPS scheme groups pixels in different tiles. The general relationship between tiles and pixels is that a tile with n-tile pixels along each side forms a HEALPix mesh of order k<sup>tile</sup>. Tiles store map information from HEALPix. These tiles are presented as square arrays and it is possible to store them in different file formats. The files are organized in different directories. Here, tiles are used as files and tile orders are used for grouping data in directories - all following a naming convention. For more information on the method of storing files, [this](http://aladin.unistra.fr/hips/hipsdoc.pdf) document can be viewed, written by Pierre Fernique.

#### HiPS images & catalogues ####
HiPS generates tile images for tile orders. When mosaicking / stitching images, the angular resolution is taken into account. Next important thing to consider is whether to emphasize on ``display quality`` or ``photometric accuracy``, which depends on our use case. Image encoding can be done either in **FITS**, **PNG**, or **JPG** file format. For most cases it is enough to only generate FITS and PNG files. The lowest order pixel values correspond to a large area of the sky.

#### Drawing HiPS tiles ####
To draw HiPS tiles, affine transformation is used. For displaying a HiPS tile, first the best order is chosen to fit the display. Properties such as maximum order and coordinate system (either ICRS or Galactic) are read from a file. The four corners of an image are mapped onto the display using affine transformation.

##### Approach #####
For a world coordinate system and an image with dimensions ``(x * y)``, I will create a NumPy array with the image information by fetching tiles and projecting them onto this image array. Some lower-level functionality like fetching tiles will also be available.

The repository where the code will reside is already set up (https://github.com/tboch/hips). I will create Pull Requests for the code I write, which will be verified by the mentors. The project will be set up by the mentors as well.

## Benefits ##
HiPS addresses the challenge of big data in astronomy. It describes data in a multi-resolution manner, so it effectively creates an ease in its access. It can also be utilized for data sharing and interoperability. HiPS provides a means for conserving scientific details of astronomical data. MOC maps generated using HiPS facilitate the comparison of sky region between different data sets, and can be used to establish regions of intersection between multiple surveys. It also helps to avoid complex queries on the database.

Current progress
---------
The repository for the current work done lies on GitHub (https://github.com/adl1995/HIPS-to-Py). This includes notes from the HiPS paper, and a package called ``hips-tools``. Apart from it includes numerous test scripts I wrote.

Firstly, there's a Python script which fetches HiPS tiles and displays them using ``Matplotlib``. The calculation of ``Norder``, ``Npixels``, and ``Nside`` was done using ``Healpy``. The retrieved image was then bytes decoded using the ``BytesIO`` library.

Another script I wrote retrieved a HiPS tile in JPG format and wrote it as a FITS map. This was achieved using Astropy's ``astropy.writeto`` method. The transformation / mapping of Geocentric coordinates onto a HiPS pixel was achieved using this
```python
theta, phi = hp.vec2ang(geocentric_coords)
```
Utilizing ``theta`` and ``phi`` the pixel number was found
```python
npixel = hp.ang2pix(nside, theta, phi)
```
After going through all conversions and successfully writing a FITS map, I then loaded it using ``astropy.io.fits.open`` function.

As multiple tiles have to be fetched for time efficiency, concurrency has to be achieved. So, I wrote a script utilizing Python's ``threading`` library. The elapsed time was calculated using ``time``. For fetching the tiles ``urllib``, ``grequests``, ``aiohttp``, ``asyncio`` were used.

For fetching 10 tiles, it took the following mentioned time (in seconds):
```python
Elapsed Time URLLib (without concurrency): 3.5430831909179688
Elapsed Time URLLib (with concurrency): 0.388397216796875
Elapsed Time URLLib (with aiohttp): 0.3900480270385742
Elapsed Time GRequests: 1.6238431930541992
```

Similarly, for fetching 100 tiles, it took:
```python
Elapsed Time URLLib (without concurrency): 37.7027428150177
Elapsed Time URLLib (with concurrency): 5.575664043426514
Elapsed Time URLLib (with aiohttp): 2.4697625637054443
Elapsed Time GRequests: 4.273705244064331
```

The pros of ``grequests`` is that it takes less time when large number of requests have to be sent. But, ``urllib`` (with threading) gives a better response time when requests are numerous.

Using ``aiohttp`` with ``asyncio`` seems to be the best option. Its response time is almost 50% less than ``grequests``.

Apart from this, I downloaded the Aladin desktop application and examined its various functionalities. It offers a tool for enabling HEALPix grid on the currently displayed image. This helped me better understand how to the grid gets divided at different zoom levels, and the relation between order and pixel numbers.

Also, I have familiarized myself with how to do code formating, write test cases and documentation using the [regions](https://github.com/astropy/regions) package.

Communication
-------------
After a brief discussion with the mentors, the decision is to write progress report at the end of each day outlining the following
* Amount of work done.
* Ask question(s) / gain assistance concerning a feature that is causing hindrance in progress (if needed).
* Schedule for next day.
* Weekly hangouts where to assess status and make a plan for the next week (with 1 hour time investment for me to prepare a Google doc with questions and notes, and then a ~1 hour call with the mentors)
* Daily summary, questions, and next day plans should be sent through email, and mentors will reply with feedback (with ~ 5 minute time investment for each)

Interaction will be mainly through GitHub or Skype chat.


Method for publishing code
-----------------------
Keeping in view the above mentioned communication structure, at least one, usually several small pull requests per week (ideally, getting work merged by the end of the week) will be made in the ``tboch/hips`` repository.


Deliverables
---------
The work will revolve around writing a high and low level API. The high level API will provide functionality such as creating WCS and HEALPix images. The current API document is available at [https://github.com/tboch/hips/blob/master/notes/API-proposal.md](https://github.com/tboch/hips/blob/master/notes/API-proposal.md)
Lower level functionality includes implementing in-memory and on-disk cache, in addition to basic input / output of HiPS tiles.

Another major part of the project involves writing test cases, docstrings, and high-level documentation. The `Sphinx` documentation generator will be used for this purpose. 

The current algorithm for drawing tiles lies here: [https://docs.google.com/document/d/1ooKTeaosHv6Bnovwfk2LOpvxi_PHLGgacz0uLnMtB38/edit?usp=sharing](https://docs.google.com/document/d/1ooKTeaosHv6Bnovwfk2LOpvxi_PHLGgacz0uLnMtB38/edit?usp=sharing)

Development environment
---------
My current development environment includes pip, Jupyer, IPython, PyCharm, and Sublime.

## Timeline ##

| Time Period        | Plan           |
| ------------- | ------------- |
| May 04, 2017 - May 30, 2017 **(Community Bonding Period)**      |   <ul><li>Discuss with mentors on which Python package to use for GUI implementation, for example ``PyQt`` (optional).</li><li>Discuss on what pattern should be followed for extracting documentation using an automated tool ``Sphinx``.</li><li>Iteratively publish code through pull requests.</li><li>Write high level documentation.</li></ul>|
| | **Part 1 starts** |
| May 30, 2017 - June 15, 2017 ( 2 weeks ) | <ul><li>Add functionality to fetch HiPS tiles.</li><li>Iteratively publish code through pull requests.</li></ul> |
| June 16, 2017 - June 30, 2017 ( 2 weeks ) | <ul><li>Functionality for drawing HiPS tiles using various techniques.</li><li>Iteratively publish code through pull requests.</li></ul>|
| | **Part 1 completed**<br />**Part 2 starts** |
| July 01, 2017 - July 14, 2017 ( 2 weeks ) | <ul><li>Link the implemented part with GU interface (optional).</li><li>Add helper functions for drawing catalogues.</li></ul> |
| July 15, 2017 - July 28, 2017 ( 2 weeks ) | <ul><li>Add optimizations, write test cases.</li><li>Add support for HiPS catalogues (to be discussed).</li></ul> |
| | **Part 2 completed** |
| August 21, 2017 - August 29, 2017 **(Students Submit Code and Evaluations)** | <ul><li>Clean up code.</li><li>Improve documentation.</li><li>Add further test cases.</li><li>Code refactoring (if required).</li><li>Resolve merge conflicts (if any).</li></ul> |
| August 29, 2017 - September 05, 2017 | Mentors submit final student evaluations. |
| September 06, 2017 | Results Announced. |

## Availability ##

My final exams end on May 20<sup>th</sup>. So, I will have ample time for the community bonding period. After that, I will be free during the whole summer i.e. almost three months. I do not have any other commitments, so I can focus all my attention to GSoC.


