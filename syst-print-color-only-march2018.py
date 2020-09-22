'''
Read the table from SPLUS EDR table to make the colour-colour diagrams
'''
from __future__ import print_function
import numpy as np
from astropy.io import fits
import os
import glob
import json
import matplotlib.pyplot as plt
import pandas as pd
import StringIO
from astropy.table import Table
import seaborn as sns
import sys
from scipy.optimize import fsolve

def findIntersection(m, y, m1, y1, x0):
    x = np.linspace(-10.0, 15.5, 200)
    return fsolve(lambda x : (m*x + y) - (m1*x + y1), x0)


tab = Table.read("sys-candidate-march2018.tab", format="ascii.tab")


number = tab['Id']
Field = tab['Field']

#Color
x1 = tab['J0515'] - tab['J0861']
y1 = tab['J0515'] - tab['J0660']

x11 = tab['J0515_petro'] - tab['J0861_petro']
y11 = tab['J0515_petro'] - tab['J0660_petro']

x111 = tab['J0515_aper'] - tab['J0861_aper']
y111 = tab['J0515_aper'] - tab['J0660_aper']
    
#Color
x2 = tab['zSDSS'] - tab['gSDSS']
y2 = tab['zSDSS'] - tab['J0660']

x22 = tab['zSDSS_petro'] - tab['gSDSS_petro']
y22 = tab['zSDSS_petro'] - tab['J0660_petro']

x222 = tab['zSDSS_aper'] - tab['gSDSS_aper']
y222 = tab['zSDSS_aper'] - tab['J0660_aper']

#Color
x3 = tab['J0660'] - tab['rSDSS']
y3 = tab['J0660'] - tab['gSDSS']

x33 = tab['J0660_petro'] - tab['rSDSS_petro']
y33 = tab['J0660_petro'] - tab['gSDSS_petro']

x333 = tab['J0660_aper'] - tab['rSDSS_aper']
y333 = tab['J0660_aper'] - tab['gSDSS_aper']

#Color
x4 = tab['J0660'] - tab['rSDSS']
y4 = tab['gSDSS'] - tab['J0515']

x44 = tab['J0660_petro'] - tab['rSDSS_petro']
y44 = tab['gSDSS_petro'] - tab['J0515_petro']

x444 = tab['J0660_aper'] - tab['rSDSS_aper']
y444 = tab['gSDSS_aper'] - tab['J0515_aper']
    
#Color
x5 = tab['gSDSS'] - tab['iSDSS']
y5 = tab['J0410'] - tab['J0660']

x55 = tab['gSDSS_petro'] - tab['iSDSS_petro']
y55 = tab['J0410_petro'] - tab['J0660_petro']

x555 = tab['gSDSS_aper'] - tab['iSDSS_aper']
y555 = tab['J0410_aper'] - tab['J0660_aper']

#Color Vironen
x6 = tab['rSDSS'] - tab['iSDSS']
y6 = tab['rSDSS'] - tab['J0660']

x66 = tab['rSDSS_petro'] - tab['iSDSS_petro']
y66 = tab['rSDSS_petro'] - tab['J0660_petro']

x666 = tab['rSDSS_aper'] - tab['iSDSS_aper']
y666 = tab['rSDSS_aper'] - tab['J0660_aper']


table = Table([tab["Field"], tab["Id"], y6 , x6,  y66, x66, y666, x666, y1, x1, y11, x11, y111, x111, y2, x2, y22, x22, y222, x222, y4, x4, y44, x44, y444, x444, y5, x5, y55, x55,  y555, x555], names=("Field", "Id",  "(r-J0660)_auto", "(r-i)_auto", "(r-J0660)_petro", "(r-i)_petro", "(r-J0660)_aper", "(r-i)_aper", "(J0515-J0660)_auto", "(J0515-J0861)_auto", "(J0515-J0660)_petro", "(J0515-J0861)_petro", "(J0515-J0660)_aper", "(J0515-J0861)_aper", "(z-J0660)_auto", "(z-g)_auto", "(z-J0660)_petro", "(z-g)_petro", "(z-J0660)_aper", "(z-g)_aper", "(g-J0515)_auto", "(J0660-r)_auto", "(g-J0515)_petro", "(J0660-r)_petro", "(g-J0515)_aper", "(J0660-r)_aper", "(J0410-J0660)_auto", "(g-i)_auto", "(J0410-J0660)_petro", "(g-i)_petro", "(J0410-J0660)_aper", "(g-i)_aper"), meta={'name': 'first table'})  

#Saving resultated table

asciifile = "SySt-calor-candidates-splus_dr1-marz18.tab"
table.write(asciifile, format="ascii.tab")
