'''
Reddenered the spectra from CLOUDY 
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

curve="../F04_CURVE_3.1.dat"
R=3.1

#spectrum
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
    fl = ((float(columns[6])*(4.0*np.pi*(8.e16)**2))/(4.0*np.pi*(3.08e22)**2))/wl  #10 kpc
    if wl>=2000 and wl<=15000:
        wll.append(wl)
        flux.append(fl)
#Ordered lambda and flux 
wll, flux = zip(*sorted(zip(wll, flux)))

#Readding the extiction curve of 
ext=np.loadtxt(curve)

wl_ext  = 10000/ext[:,0] # in angstroms
ext_val= 1+ext[:,1]/R  # in A_l/A_V
ord=np.argsort(wl_ext)
wl_ext = wl_ext.take(ord)
ext_val = ext_val.take(ord)

#Interpolating the extintion curve to the lambda of the spectrum
ext_val_inter_lamspectrum = np.interp(wll, wl_ext, ext_val)
#Iterating over the desired E(B-V) range and saving the reddened spectra
E = [0.1, 0.2]

for i in range(2):
    av=R*E[i]
    cor=ext_val_inter_lamspectrum*av
    #Fluxes are being multiplied by "0.12" to correct for the errors in the convertion
    specflu_red=np.array(flux)*0.12*10**(-0.4*cor)
    
    #Save the new files
    asciifile = file_.replace("output_SED.dat", "output_SED.dat.tere_E"+str(E[i])) 
    file=open(asciifile,'w') #create file  
    for x,y in zip(wll, specflu_red):
        file.write('%f %s\n'%(x,y))     #assume you separate columns by tabs  
    file.close()     #close file   



