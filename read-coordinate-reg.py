from __future__ import print_function
import numpy as np
import json
import os
from astropy.io import fits
from astropy import wcs
from astropy.wcs import WCS
from astropy import coordinates as coord
from astropy import units as u 
import argparse
import sys


#position = "halpha-emitter.reg"
position = "HII-region.reg"

ra, dec = [], []
f = open(position, 'r')
header1 = f.readline()
header2 = f.readline()
header3 = f.readline()
for line in f:
    line = line.strip()
    columns = line.split()
    coor = line.split("(")[-1].split(")")[0]
    try:
        ra1, dec1 = coor.split(",")[0:2]
    except ValueError:
        continue
    coor_degree = coord.SkyCoord(ra1, dec1, unit=(u.hourangle, u.degree))
    ra.append(coor_degree.ra.degree)
    dec.append(coor_degree.dec.degree)

asciifile = "HII-region-galaxy.txt"
file=open(asciifile,'w') #create file  
for x,y in zip(ra, dec):  
    file.write('%f %f\n'%(x,y))     #assume you separate columns by tabs  
file.close()     #close file  

   
