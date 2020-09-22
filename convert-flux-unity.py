'''
Convert to flux unitiess
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
#import seaborn as sns
import sys
import argparse
import os
from colour import Color

parser = argparse.ArgumentParser(
    description="""Write wave and magnitude of a spectrum""")

parser.add_argument("source", type=str,
                    default="star",
                    help="Name of source, taken the prefix ")
parser.add_argument("--savefile", action="store_true",
                    help="Save ascii file showing the magnitude")

parser.add_argument("--debug", action="store_true",
                    help="Print out verbose debugging info about each line in region file")

args = parser.parse_args()
file_ = args.source + ".sed"

x = np.loadtxt(file_, delimiter = None, skiprows = 0, usecols = None, 
               unpack = False, dtype = np.dtype([('Wl', '|f8'), ('Flux', 'f8')]))

wl = x['Wl']
m = x['Flux']
f = (10**(-(m+2.41)/2.5)) / wl**2


if args.savefile:
    asciifile = file_.replace(".sed", 
                    ".dat")
    file=open(asciifile,'w') #create file  
    for x,y in zip(wl, f):  
       file.write('%f  %s\n'%(x,y))     #assume you separate columns by tabs  
    file.close()     #close file  
