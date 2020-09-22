'''
Convert file.json to .ascci of PN spectrum from PN gallery
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import argparse

parser = argparse.ArgumentParser(
    description="""Write wave and flux of a spectrum""")

parser.add_argument("source", type=str,
                    default="_axper_20111004_014",
                    help="Name of blue source, taken the prefix ")

parser.add_argument("--debug", action="store_true",
                    help="Print out verbose debugging info about each line in region file")

wl, flux = [], []
args = parser.parse_args()
file_list = args.source + ".json"

with open(file_list) as f:
    data = json.load(f)

for data_ in data:
    wl.append(data_['x'])
    flux.append(data_['y'])

asciifile = file_list.replace(".json", ".dat")
file=open(asciifile,'w') #create file  
for x,y in zip(np.array(wl, dtype=float), np.array(flux, dtype=float)):  
    file.write('%f  %s\n'%(x,y))     #assume you separate columns by tabs  
file.close()     #close file  

        
