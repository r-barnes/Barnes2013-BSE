Barnes2013-BSE
==============

This archive contains the code used in the manuscript

**Modeling of bovine spongiform encephalopathy in a two-species feedback loop**

By: Richard Barnes and Clarence Lehman

doi: [10.1016/j.epidem.2013.04.001](http://dx.doi.org/10.1016/j.epidem.2013.04.001)

To generate the figures, open a command line and type:

    ./run.sh

This will run **./one\_species\_model.py** and **./two\_species\_model.py**
with the arguments used to generate the figures in the manuscript.

The figures will then be automatically plotted with the **./plot** script.

The figures will then be automatically converted to PDF and cropped.

Please contact Richard Barnes (rbarnes@umn.edu) with any questions or comments.

Requirements
============
* Python
* Scipy
* GnuPlot
* epspdf  (from TexLive)
* pdfcrop (from TeXLive)
* This will run best on GNU/Linux systems
