import os                    #
import sys                   #I madified the program
from time import time        #
import seaborn as sns

import numpy as np
from matplotlib import pyplot as plt

from astroML.datasets import fetch_imaging_sample, fetch_sdss_S82standards
from astroML.crossmatch import crossmatch_angular
from astroML.plotting import hist
from astropy.io import ascii
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.table import Table, Column

# get standard stars ##HASH catalog
# standards_data = fetch_sdss_S82standards() ## HASH PN
stara=ascii.read("ra-pne-HASH.txt")  
stadec=ascii.read("dec-pne-HASH.txt")
c2 = SkyCoord(stara, stadec, unit=(u.hourangle, u.deg))
RA1 = c2.ra.hour.reshape(len(c2.ra.degree),)
DEC1 = c2.dec.degree.reshape(len(c2.dec.degree),)

#Calculating longitug (l) and latitud (b)
c3 = c2.galactic
ll = c3.l.degree
bb = c3.b.degree



# ax = plt.axes()
# hist(DEC1, bins='knuth', ax=ax,
#      histtype='stepfilled', ec='k', fc='#AAAAAA')
# ax.set_xlabel('DEC (degree)')
# ax.set_ylabel('N(PNe)')
# # ax.text(0.95, 0.95,
# #         "Total objects: %i\nNumber with match: %i" % (imX.shape[0],
# #                                                       np.sum(match)),
# #         ha='right', va='top', transform=ax.transAxes)
# #ax.set_xlim(0, 2500)

# plt.savefig("distribution-hist-pn-hash.pdf")
# plt.clf()
# sys.exit()
###############################################################################################################
###############################################################################################################
fig = plt.figure()
ax1 = fig.add_subplot(111, axisbg="#eeeeee")
# ax1.set_xlim(xmin=-3.0,xmax=5.0)
# ax1.set_ylim(ymin=-2.0,ymax=6.0)
plt.tick_params(axis='x', labelsize=18) 
plt.tick_params(axis='y', labelsize=18)
plt.xlabel(r'$RA (hour)$', fontsize= 18)
plt.ylabel(r'$DEC (degree)$', fontsize= 18)
ax1.scatter(RA1, DEC1)
ax1.minorticks_on()
ax1.grid()#, lw=0.3)
ax1.legend(scatterpoints=1, ncol=1)

plt.tight_layout()
#plt.savefig('luis-JPLUS-Viironen.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.savefig('distribution-hash-pne.pdf')
plt.clf()
###################################################################
###################################################################
ax2 = fig.add_subplot(111, axisbg="#eeeeee")
# ax1.set_xlim(xmin=-3.0,xmax=5.0)
# ax1.set_ylim(ymin=-2.0,ymax=6.0)
plt.tick_params(axis='x', labelsize=18) 
plt.tick_params(axis='y', labelsize=18)
plt.xlabel(r'$l$', fontsize= 18)
plt.ylabel(r'$b$', fontsize= 18)
ax2.scatter(ll, bb, edgecolor='black',  c='xkcd:baby poop green')
ax2.minorticks_on()
ax2.grid(which='minor')#, lw=0.3)
ax2.legend(scatterpoints=1, ncol=1)

plt.tight_layout()
#plt.savefig('luis-JPLUS-Viironen.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.savefig('distribution-hash-pne-lb.pdf')
plt.clf()
