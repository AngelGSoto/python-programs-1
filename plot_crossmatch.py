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
c1 = SkyCoord(splusra, splusdec, unit=(u.hourangle, u.deg))
RA = c1.ra.degree.reshape(len(c1.ra.degree),)
DEC = c1.dec.degree.reshape(len(c1.dec.degree),)
imX = np.empty((len(c1), 2), dtype=np.float64)
imX[:, 0] = RA
imX[:, 1] = DEC

# get standard stars ##HASH catalog
# standards_data = fetch_sdss_S82standards() ## HASH PN
stara=ascii.read("ra-pne-HASH.txt")  
stadec=ascii.read("dec-pne-HASH.txt")
c2 = SkyCoord(stara, stadec, unit=(u.hourangle, u.deg))
RA1 = c2.ra.degree.reshape(len(c2.ra.degree),)
DEC1 = c2.dec.degree.reshape(len(c2.dec.degree),)
stX = np.empty((len(c2), 2), dtype=np.float64)
stX[:, 0] = RA1
stX[:, 1] = DEC1
#HAST cata

# crossmatch catalogs
max_radius = 3600. / 3600.0  # 1 arcsec
dist, ind = crossmatch_angular(imX, stX, max_radius)
#dist, ind = crossmatch_angular(c1, c2, max_radius)
match = ~np.isinf(dist)

dist_match = dist[match]
dist_match *= 3600

ax = plt.axes()
hist(dist_match, bins='knuth', ax=ax,
     histtype='stepfilled', ec='k', fc='#AAAAAA')
ax.set_xlabel('radius of match (arcsec)')
ax.set_ylabel('N(r, r+dr)')
ax.text(0.95, 0.95,
        "Total objects: %i\nNumber with match: %i" % (stX.shape[0],
                                                      np.sum(match)),
        ha='right', va='top', transform=ax.transAxes)
ax.set_xlim(0, 3600)

plt.savefig("number-macht-jplus-hash.jpg")
