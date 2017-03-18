**HiPS to Py**
===================


Student information
-
###Personal details###
* **Name**: Adeel Ahmad
* **Email**: adeelahmadadl1995@gmail.com
* **GitHub**: adl1995
* **IRC**: adl1995
* **Timezone**: UTC +05:00
* **Blog**: -- 

###Academic details###
* **University**: National University of Computer and Emerging Sciences, Islamabad
* **Degree**: Computer Science 
* **Graduation year**: 2018 

Project abstract
---------------------
Implement a Python client for HiPS. Currently, such clients exist, such a Aladin and Aladin Lite, but they written in JavaScript. The end goal (?) is to implement a Python module for viewing astronomical figures. ... 

Project summary
----------------------
Hierarchical progressive surveys (HiPS) utilize the HEALPix framework and use it for mapping a sphere (in our case, part of a sky) and compiles / transforms it into tiles and pixels. HiPS emphasizes on usability thus it tries to abstract the scientific details (while preserving them). This can be further built upon for statistical analysis for large datasets. For this project, a HiPS Python client is to be implemented which will enable users to view / explore astronomical figures. HiPS data is stored in the form of catalogues (TSV, FITS), or tiles (PNG, JPEG). In the context of this project only the tiles are to be retrieved and stitched together to get the final output. Listed below are the current HiPS clients:

* Aladin Desktop
* Aladin Lite (CDS)
* MIZAR
* ESAsky
* JUDO2 

The goal of this project would be to create another HiPS client under Astropy/HiPS. However, this would run purely on Python. The possible dependencies for this software would be:

* Python >= 3.5
*  Astropy
* Healpy
* Numpy
* Retransform

Benefits
-
The first thing that a user does when trying out a new software is to look at its documentation. It reveals how well managed and organized the software is. If the information is presented in a neat manner, the time to get it running is reduced considerably. In my opinion, a software should provide two branches of documentation, one that is more 'user-friendly' and the other that is more focused towards 'developers'. Of course, numerous softwares already provide this through popup annotations.

Work done
- 
mention Lydoc, Grako, Sphinx, test suite oll-core, gridly.
Deliverables
-

Plans
-

Communication
---------------------

Qualification
-----------------

