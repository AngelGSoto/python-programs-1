'''
Transform the sexagecimal system to decimal system the equatorial coordinate
'''
from __future__ import print_function, division
from PyAstronomy import pyasl
import numpy as np

list_=[]
f = open("Belist", 'r') 
header1 = f.readline()
for line in f:
    line = line.strip()
    columns = line.split()
    list_.append(line)
#asciifile = "Belist-sdss.txt"
asciifile = "Belist-LAMOST.txt"
iii=[ii for ii in range(len(list_))]
for x, i in zip(iii, list_):
    ra, dec = pyasl.coordsSexaToDeg(i)
    #print(x, ra, dec)
    print(ra, dec, '2.0')
    
    
      
   
