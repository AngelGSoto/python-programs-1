# Author: Jake VanderPlas <vanderplas@astro.washington.edu>
# License: BSD
#   The figure is an example from astroML: see http://astroML.github.com
import os                    #
import sys                   #I madified the program
from time import time        #

import numpy as np
from matplotlib import pyplot as plt

from astroML.datasets import fetch_imaging_sample, fetch_sdss_S82standards
from astroML.crossmatch import crossmatch_angular
from astroML.plotting import hist
from astropy.io import ascii
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.table import Table, Column

# get imaging data
# image_data = fetch_imaging_sample() ## splus
splusra=ascii.read("ra.txt")  
splusdec=ascii.read("dec.txt")

print()
