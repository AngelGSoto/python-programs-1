'''
Getting the PN and SyST candidtaes in S-PLUS catalog (DR1)
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from astropy.table import Table

n=17
magnitude = [[] for _ in range(n)]
pattern = "SPLUS_STRIPE82_all_fields/*photo_BPZ.cat"
file_list = glob.glob(pattern)

for file_name in file_list:
    data = np.loadtxt(file_name)
    #colums of my interest 
    magnitude[1].append(data[:,0]) #id
    magnitude[2].append(data[:,1])  #ra
    magnitude[3].append(data[:,2]) #dec
    magnitude[4].append(data[:,15])   #u
    magnitude[5].append(data[:,24]) #j0378
    magnitude[6].append(data[:,33]) #j0395
    magnitude[7].append(data[:,42]) #j0410
    magnitude[8].append(data[:,51]) #j0430
    magnitude[9].append(data[:,60])     #g
    magnitude[10].append(data[:,69]) #j0515
    magnitude[11].append(data[:,78])       #r
    magnitude[12].append(data[:,87])   #j0660
    magnitude[13].append(data[:,96])       #i
    magnitude[14].append(data[:,105])  #j0861
    magnitude[15].append(data[:,114])      #z
    magnitude[16].append(data[:,125])   #clas
    magnitude[0].append(file_name.split('82-')[-1].split('_photo')[0]) #field
     
table = Table([magnitude[0], magnitude[1], magnitude[2], magnitude[3], magnitude[4], 
           magnitude[5], magnitude[6], magnitude[7], magnitude[8], magnitude[9], magnitude[10], 
               magnitude[11], magnitude[12], magnitude[13], magnitude[14], magnitude[15], magnitude[16]], names=('Field', 'Id', 'RA', 'Dec', 'rSDSS', 'gSDSS', 'iSDSS', 'zSDSS', 'uJAVA', 'J0378', 'J0395', 'J0410', 'J0430', 'J0515', 'J0660', 'J0861', "Class"), meta={'name': 'first table'})   
    
    
#Saving resultated table

asciifile = "SPLUS_STRIPE82.tab"
table.write(asciifile, format="ascii.tab")
