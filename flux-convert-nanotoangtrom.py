'''
Convert the flux the erg s^-1 cm^-2 nm^-1 to erg s^-1 cm^-2 angtrom^-1
'''
from __future__ import print_function
import numpy as np
import glob
import json
import argparse
import matplotlib.pyplot as plt
import seaborn as sns
import sys

wl, flux = [], []

parser = argparse.ArgumentParser(
    description="""Write wave and flux of a spectrum""")

parser.add_argument("source", type=str,
                    default="SO397",
                    help="Name of source, taken the prefix")

parser.add_argument("--debug", action="store_true",
                    help="Print out verbose debugging info about each line in region file")

args = parser.parse_args()
file_ = args.source + ".txt"

f = open(file_, 'r')
header1 = f.readline()
header2 = f.readline()
for line in f:
    line = line.strip()
    columns = line.split()
    try:
        wl_nm = float(columns[0])
    except IndexError:
        continue
    fl_nm = float(columns[1])
    wl_ang = 10*wl_nm
    fl_ang = (wl_nm/wl_ang) * fl_nm
    if wl_ang>=2000 and wl_ang<=9939:
        wl.append(wl_ang)
        flux.append(fl_ang)

asciifile = file_.replace(".txt", ".dat")
file=open(asciifile,'w') #create file  
for x,y in zip(wl, flux):
    file.write('%f %s\n'%(x,y))     #assume you separate columns by tabs  
file.close()     #close file   
