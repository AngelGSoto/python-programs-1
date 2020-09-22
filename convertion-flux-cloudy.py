'''
The flux meassured at the Earth 
'''
from __future__ import print_function
import numpy as np
import glob
import json
import argparse
import matplotlib.pyplot as plt
import seaborn as sns
import sys


parser = argparse.ArgumentParser(
    description="""Tranformation of the flux from CLOUDY""")

parser.add_argument("source", type=str,
                    default="BB1_L3_T100_",
                    help="Name of source, taken the prefix ")

parser.add_argument("--debug", action="store_true",
                    help="Print out verbose debugging info about each line in region file")

cmd_args = parser.parse_args()
file_ = cmd_args.source + "output_SED.dat"

wll = []
flux = []
f = open(file_, 'r')
header1 = f.readline()
for line in f:
    line = line.strip()
    columns = line.split()
    try:
        wl = float(columns[0])
    except ValueError:
        continue
    #fl = float(columns[6])
    #fl = ((float(columns[6])*(4.0*np.pi*(8.e16)**2))/(4.0*np.pi*(1.54e22)**2))/wl  #5
    fl = ((float(columns[6])*(4.0*np.pi*(8.e16)**2))/(4.0*np.pi*(3.08e22)**2))/wl  #10
    #fl = ((float(columns[6])*(4.0*np.pi*(8.e16)**2))/(4.0*np.pi*(4.62e22)**2))/wl  #15
    #fl = ((float(columns[6])*(4.0*np.pi*(8.e16)**2))/(4.0*np.pi*(6.16e22)**2))/wl  #20
    if wl>=2000 and wl<=15000:
        wll.append(wl)
        flux.append(fl)
wll, flux = zip(*sorted(zip(wll, flux)))
asciifile = file_.replace("output_SED.dat", "output_SED.dat.tere_E0") #en reality are 10kpc :(
file=open(asciifile,'w') #create file  
for x,y in zip(wll, flux):
    file.write('%f %s\n'%(x,y))     #assume you separate columns by tabs  
file.close()     #close file   
# plt.xlim(3.e3, 10.e3)
# plt.yscale('log')
# #plt.ylim(1e-16, 1e-11)
# plt.plot(wll, flux)

# plt.show()
