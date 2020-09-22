'''
Getting the PN and SyST candidtaes in S-PLUS catalog (DR1)
'''
from __future__ import print_function
import numpy as np
import glob
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from astropy.table import Table
import argparse

n=17
magnitude = [[] for _ in range(n)]


#pattern = "SPLUS_STRIPE82_all_fields/SPLUS_STRIPE82-0004_photo_BPZ.cat"
pattern = "SPLUS_STRIPE82_all_fields/*_photo_BPZ.cat"
file_list = glob.glob(pattern)
for file_name in sorted(file_list):
    data = np.loadtxt(file_name)
    for i in data:
        magnitude[0].append(i[0]) #id
        magnitude[1].append(i[1])  #ra
        magnitude[2].append(i[2]) #dec
        magnitude[3].append(i[15])   #u
        magnitude[4].append(i[24]) #j0378
        magnitude[5].append(i[33]) #j0395
        magnitude[6].append(i[42]) #j0410
        magnitude[7].append(i[51]) #j0430
        magnitude[8].append(i[60])     #g
        magnitude[9].append(i[69]) #j0515
        magnitude[10].append(i[78])       #r
        magnitude[11].append(i[87])   #j0660
        magnitude[12].append(i[96])       #i
        magnitude[13].append(i[105])  #j0861
        magnitude[14].append(i[114])      #z
        magnitude[15].append(i[133])   #clas stars
        magnitude[16].append(file_name.split('82-')[-1].split('_photo')[0]) #field

# print(magnitude[0])
table = Table([magnitude[16], magnitude[0], magnitude[1], magnitude[2], magnitude[3], magnitude[4], magnitude[5], magnitude[6], magnitude[7], magnitude[8], magnitude[9], magnitude[10], magnitude[11], magnitude[12], magnitude[13], magnitude[14], magnitude[15]], names=('Field', 'Id', 'RA', 'Dec', 'uJAVA', 'J0378', 'J0395', 'J0410', 'J0430', 'gSDSS', 'J0515', 'rSDSS', 'J0660', 'iSDSS', 'J0861', 'zSDSS', "Class star"), meta={'name': 'first table'})   
#Saving resultated table
asciifile = "SPLUS_STRIPE82.tab"
table.write(asciifile, format="ascii.tab")


#for Field, id1, ra1, dec1, u1, j03781, j03951, j04101, j04301, g1, j05151, r1, j06601, i1, j08611, z1, clas1 in zip(field, id_, ra, dec, u, j0378, j0395, j0410, j0430, g, j0515, r, j0660, i, j0861, z, clas):
    
