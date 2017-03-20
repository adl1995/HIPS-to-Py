**HiPS to Py**
=======
> Suborganization: Astropy

Student information
---------------------------

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


Project Details
--------

### Mentors ###
* [Christoph Deil](https://github.com/cdeil)
* [Thomas Boch](https://github.com/tboch)

### Abstract ###
Design and create a Python client for Hierarchical Progressive Surveys (HiPS). This will enable users to view astronomical figures in an interactive environment, similar to Google Maps. Currently, such clients exist, such as Aladin and Aladin Lite, but they are written in Java and JavaScript, respectively. The goal of this project is to provide similar functionality using Python. The current decision is to work only with HiPS images, but if everything goes well, I wish to work on HiPS catalogs as well. 

### Detailed description ###
Hierarchical progressive surveys (HiPS) utilizes the HEALPix framework and uses it for mapping a sphere (in our case, part of a sky) and then compiles / transforms it into tiles and pixels. HiPS emphasizes on usability thus it tries to abstract the scientific details (while preserving them). This can be further built upon for statistical analysis of large datasets. For this project, a HiPS Python client is to be implemented which will enable users to view / explore astronomical figures. HiPS data is stored in the form of catalogs (TSV), or tiles (PNG, JPG, FITS). In the context of this project only tiles are to be retrieved and stitched together to get the final output. Listed below are current HiPS clients:

* Aladin Desktop
* Aladin Lite (CDS)
* MIZAR
* ESAsky
* JUDO2 

The goal of this project would be to create a new HiPS client under Astropy/HiPS. However, this would run purely in Python. The possible dependencies for this software are:

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

In a nutshell, the pixelization procedure subdivides a spherical sphere in which each pixel is equidistant from the origin - meaning it covers the same surface area. This produces a HEALPix grid, whose interesting property is that pixels are distributed on lines of constant latitude. Due to this iso-latitude distribution of pixels the complexity for computing integrals over each harmonics is N ^ (1/2).

#### Pixel numbering schemes ####

HEALPix provides two numbering schemes for pixels, namely **RING scheme** and **NESTED scheme**.
    
Some alternative tools to HEALPix are Hierarchical Triangular Mesh (HTM) and Tessellated Octahedral Adaptive Subdivision Transform (TOAST).

#### HEALPix coordinate system ####
HEALPix header files contain one of the following three letters, each depicting the coordinate system being used:

* C:Celestial=ICRS=RA/DEC(equatorial)=FK5 J2000
* G:Galactic
* E:Ecliptic

HiPS uses the Celestial coordinate system, by default. Also, HiPS does not support Ecliptic coordinate system.

#### HiPS pixels ####
Using the header ``hips_pixel_bitpix`` with the format -64, -32, 8, 16, 32, 64 (FITS convention) the pixels are stored in ``BITPIX`` code. The multi-resolution representation of original images provides the basis for visualizing data in a progressive way as the pixels that are required for a given view can be accessed from pre-computed HEALPix maps, and the nested pixel numbering scheme provides a simple hierarchical indexing system that encodes pixel inheritance across different orders.

#### HiPS tiles ####
As it is cumbersome to transfer each pixel (essentially a file), HiPS scheme groups pixels in different tiles. The general relationship between tiles and pixels is a tile with n-tile pixels along each side forms a HEALPix mesh of order of k-tile.

#### HiPS file structuring scheme ####
In HiPS, tiles store map information from HEALPix. These tiles are presented as square arrays and it is possible to store them in multiple file formats. Focusing on simplicity and usability, the description of arrays stored in files are straightforward with all the array positions being filled. The files are organized in different directories. Here, tiles are used as files and tile orders are used for grouping data in directories - all following a naming convention. For more information on the method of storing files, view [this](http://aladin.unistra.fr/hips/hipsdoc.pdf) document, written by Pierre Fernique.

#### HiPS images ####
The way HiPS represents images is by resampling them on a HEALPix grid at the maximum desired order, say k-max. Then it generates tile images for tile orders. When mosaicking / stitching images, the angular resolution is taken into account. There are various methods for filling the data region when stitching images and dealing with background difference. The k-max chosen earlier determines minimum pixel size which is near to the angular pixel size or the resolution of the original data.

Next important thing is whether to emphasize on ``display quality`` or ``photometric accuracy``, which depends on our use case. Image encoding can be done either in **FITS**, **PNG**, **JPG** file format. For most cases it is enough to only generate FITS and PNG files. The lowest order pixel values correspond to a large area of the sky. The HiPS indexing structure takes care of mapping correct tiles onto a display.

### Goals ###

### Benefits ###
This package would enable...

Deliverables
-

Plans
-

Current progress
---------
I have already started conversing with Christoph, who assigned me numerous tasks related with fetching HiPS tiles and displaying them using ``Matplotlib``. The calculation of ``Norder``, ``Npixels``, and ``Nside`` was done using ``Healpy``. The retrieved image was then decoded and displayed using
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


## Timeline ##

| Time Period        | Plan           |
| ------------- | ------------- |
| April 22, 2016 - May 22, 2016 **(Community Bonding Period)**      |   <ul><li>Read documentation and get more familiar with how Fido works.</li><li>Discuss with mentors and get a final idea of how to approach the project.<li>**Get familiar with the various clients that Fido would be supporting and also understand how each client’s query is different from other clients and how to download data from each client.** This is important because later on one common query will have to be assigned to a client automatically, and downloads from that particular client will be made.</li><li>**Discuss with mentors and get a final idea of which client will serve which kinds of files and decide how the metadata of each file type will be stored in the database. Also finalize how to store metadata of any file types which are not currently supported ( maybe create an additional feature that will allow easy additions of new file types’ metadata to the database in the future ).**</li><li>Read code and get more familiar with the caching mechanism and try to get an idea of what challenges could possibly arise while implementing the new caching mechanism. This is important because query results of multiple clients will be stored in the cache.</li></ul>|
| | **Part 1 starts** |
| May 23, 2016 - May 29, 2016 ( 1 week ) | <ul><li>**Implement adding the Fido records to the database.**</li><li>Ensure that functionalities like `display_entries` etc. are working. Cross check by adding entries using specific client methods (the old way).</li><li>Document and write tests for adding while using Fido.</li><li>**Update 1 : Push code which will enable the database to accept Fido records/entries.**</li></ul> |
| May 30, 2016 -  June 12, 2016 ( 2 weeks ) | <ul><li>**Implement querying with Fido.** Ensure that the different clients are recognized correctly and correct results are returned. Cross check by using custom queries for each client.</li><li>Write tests for querying with Fido.</li><li>Document querying with Fido.</li><li>**Update 2 : Push code so that querying inside the database is successfully done using Fido attributes.**</li></ul> |
| June 13, 2016 - June 20, 2016 ( 1 week ) | <ul><li>**Implement downloading files for VSO and HEK queries after querying database.**</li><li>Ensure that the correct files from the correct clients are being downloaded by checking using the old separate download functions.</li></ul> |
| **June 21, 2016 - June 28, 2016 (Midterm Evaluations / Buffer period)** | **Mid term deliverables :**<ul><li>Querying with Fido</li><li>Adding Fido records to the database</li><li>Downloading files from VSO and HEK queries using Fido. Downloading using other clients, tests and documentation will be done after mid-term evaluations.</li><li>Continue work on downloading files using Fido.</li></ul> |
| June 28, 2016 - July 4, 2016 ( 1 week ) | <ul><li>**Implement downloading files for all other remaining clients.**</li><li>**For all supported file types, implement storing their metadata in the database. The database module already handles FITS files pretty well.**</li><li>**If needed, create a new feature/wrapper which will allow new file types’ metadata to be added easily to the database in the future.**</li><li>Cross check for every client by using the old separate download methods for downloading files.</li><li>Document and write tests for downloading files using Fido.</li><li>**Update 3 : Push code so that files from all clients can be downloaded from a Fido search result.**</li></ul> |
| July 5, 2016 - July 11, 2016 ( 1 week ) | <ul><li>**Test and ensure that all other pre-existing functionalities of the database module like `tag`, `star`, `undo` etc. are still working.**</li><li>Clean up code to make it PEP8 compliant.</li><li>Finalize Part 1 of the project after reviewing it with mentors.</li></ul> |
| | **Part 1 completed**<br />**Part 2 starts** |
| July 12, 2016 - July 25, 2016 ( 2 weeks ) | <ul><li>**Implement functionality that serializes each query result by converting them to JSON.** Make sure that the serialization and deserialization processes work correctly.</li></ul> |
| July 26, 2016 - August 8, 2016 ( 2 weeks ) | <ul><li>**Implement adding the new type of entries to the cache table in the database.**</li><li>**Implement searching through this database and check if all query results from all different clients are matching correctly.** This includes ensuring that pre-existing query results are detected correctly for every client, like VSO, HEK etc.</li><li>**Implement skipping downloading of files** in case there is a query result match in the cache.</li><li>Ensure that this “skipping” is working for all clients.</li></ul> |
| August 9, 2016 - August 15, 2016 ( 1 week ) | <ul><li>**Buffer period**</li><li>Write documentation and tests for the new caching mechanism.</li><li>**Update 4 : Push code so that the database successfully uses the new caching mechanism.**</li></ul> |
| | **Part 2 completed** |
| August 16, 2016 - August 24, 2016 **(Students Submit Code and Evaluations)** | <ul><li>Clean up code</li><li>Improve documentation</li><li>Resolve merge conflicts (if any)</li></ul> |
| August 24, 2016 - August 30, 2016 | **Mentors Submit Final Evaluations** |
| August 30, 2016 | **Results Announced** |


