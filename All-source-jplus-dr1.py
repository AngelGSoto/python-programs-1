'''
Read the file from J-PLUS IDR table to make the colour-colour diagrams
'''
from __future__ import print_function
import numpy as np
from astropy.io import fits
import os
import glob
import json
import matplotlib.pyplot as plt
import pandas as pd
#import StringIO
from astropy.table import Table
import seaborn as sns
import sys
from scipy.optimize import fsolve
import colours


def findIntersection(m, y, m1, y1, x0):
    x = np.linspace(-10.0, 15.5, 200)
    return fsolve(lambda x : (m*x + y) - (m1*x + y1), x0)

#The equation the represent the criteria
def findIntersection(m, y, m1, y1, x0):
    x = np.linspace(-10.0, 15.5, 200)
    return fsolve(lambda x : (m*x + y) - (m1*x + y1), x0)


#Halpha emitters find to metodogy suggest by Carlinhos
#tab_np = Table.read("ha-emitter-j660-r_iso_v1.tab", format="ascii.tab")
label_pne = ['TK 1', "Kn J1857.7+3931", "KnPa J1848.6+4151", "Jacoby 1"]

#Halpha emitters find will whole the criteria
tab_np = Table.read("10725_wmask.tab", format="ascii.tab")
tab_np_hast = Table.read("11081-macht-true.tab", format="ascii.tab")
tab_np_hast_s = Table.read("../../../S-PLUS/math-splus-hash.tab", format="ascii.tab")
#Field and number of the objects
number_np = tab_np['Number']

# number_sym = tab_sym['Id']
# Field_sym = tab_sym['Field']

#Calor ISO GAUSS
#Color vironen
x_np_ISO_GAUSS_0 = tab_np['rSDSS_ISO_GAUSS'][0] - tab_np['iSDSS_ISO_GAUSS'][0]
y_np_ISO_GAUSS_0 = tab_np['rSDSS_ISO_GAUSS'][0] - tab_np['J0660_ISO_GAUSS'][0]

#Color
x1_np_ISO_GAUSS_0 = tab_np['J0515_ISO_GAUSS'][0] - tab_np['J0861_ISO_GAUSS'][0]
y1_np_ISO_GAUSS_0 = tab_np['J0515_ISO_GAUSS'][0] - tab_np['J0660_ISO_GAUSS'][0]

#Color
x2_np_ISO_GAUSS_0 = tab_np['zSDSS_ISO_GAUSS'][0] - tab_np['gSDSS_ISO_GAUSS'][0]
y2_np_ISO_GAUSS_0 = tab_np['zSDSS_ISO_GAUSS'][0] - tab_np['J0660_ISO_GAUSS'][0]

#Color
x3_np_ISO_GAUSS_0 = tab_np['J0660_ISO_GAUSS'][0] - tab_np['rSDSS_ISO_GAUSS'][0]
y3_np_ISO_GAUSS_0 = tab_np['J0660_ISO_GAUSS'][0] - tab_np['gSDSS_ISO_GAUSS'][0]

#Color
x4_np_ISO_GAUSS_0 = tab_np['J0660_ISO_GAUSS'][0] - tab_np['rSDSS_ISO_GAUSS'][0]
y4_np_ISO_GAUSS_0 = tab_np['gSDSS_ISO_GAUSS'][0] - tab_np['J0515_ISO_GAUSS'][0]

    
#Color
x5_np_ISO_GAUSS_0 = tab_np['gSDSS_ISO_GAUSS'][0] - tab_np['iSDSS_ISO_GAUSS'][0]
y5_np_ISO_GAUSS_0 = tab_np['J0410_ISO_GAUSS'][0] - tab_np['J0660_ISO_GAUSS'][0]

#Calor ISO GAUSS
#Color vironen
x_np_ISO_GAUSS_1 = tab_np['rSDSS_ISO_GAUSS'][1] - tab_np['iSDSS_ISO_GAUSS'][1]
y_np_ISO_GAUSS_1 = tab_np['rSDSS_ISO_GAUSS'][1] - tab_np['J0660_ISO_GAUSS'][1]

#Color
x1_np_ISO_GAUSS_1 = tab_np['J0515_ISO_GAUSS'][1] - tab_np['J0861_ISO_GAUSS'][1]
y1_np_ISO_GAUSS_1 = tab_np['J0515_ISO_GAUSS'][1] - tab_np['J0660_ISO_GAUSS'][1]

#Color
x2_np_ISO_GAUSS_1 = tab_np['zSDSS_ISO_GAUSS'][1] - tab_np['gSDSS_ISO_GAUSS'][1]
y2_np_ISO_GAUSS_1 = tab_np['zSDSS_ISO_GAUSS'][1] - tab_np['J0660_ISO_GAUSS'][1]

#Color
x3_np_ISO_GAUSS_1 = tab_np['J0660_ISO_GAUSS'][1] - tab_np['rSDSS_ISO_GAUSS'][1]
y3_np_ISO_GAUSS_1 = tab_np['J0660_ISO_GAUSS'][1] - tab_np['gSDSS_ISO_GAUSS'][1]

#Color
x4_np_ISO_GAUSS_1 = tab_np['J0660_ISO_GAUSS'][1] - tab_np['rSDSS_ISO_GAUSS'][1]
y4_np_ISO_GAUSS_1 = tab_np['gSDSS_ISO_GAUSS'][1] - tab_np['J0515_ISO_GAUSS'][1]

    
#Color
x5_np_ISO_GAUSS_1 = tab_np['gSDSS_ISO_GAUSS'][1] - tab_np['iSDSS_ISO_GAUSS'][1]
y5_np_ISO_GAUSS_1 = tab_np['J0410_ISO_GAUSS'][1] - tab_np['J0660_ISO_GAUSS'][1]

#Calor ISO GAUSS
#Color vironen
x_np_ISO_GAUSS_2 = tab_np['rSDSS_ISO_GAUSS'][2] - tab_np['iSDSS_ISO_GAUSS'][2]
y_np_ISO_GAUSS_2 = tab_np['rSDSS_ISO_GAUSS'][2] - tab_np['J0660_ISO_GAUSS'][2]

#Color
x1_np_ISO_GAUSS_2 = tab_np['J0515_ISO_GAUSS'][2] - tab_np['J0861_ISO_GAUSS'][2]
y1_np_ISO_GAUSS_2 = tab_np['J0515_ISO_GAUSS'][2] - tab_np['J0660_ISO_GAUSS'][2]

#Color
x2_np_ISO_GAUSS_2 = tab_np['zSDSS_ISO_GAUSS'][2] - tab_np['gSDSS_ISO_GAUSS'][2]
y2_np_ISO_GAUSS_2 = tab_np['zSDSS_ISO_GAUSS'][2] - tab_np['J0660_ISO_GAUSS'][2]

#Color
x3_np_ISO_GAUSS_2 = tab_np['J0660_ISO_GAUSS'][2] - tab_np['rSDSS_ISO_GAUSS'][2]
y3_np_ISO_GAUSS_2 = tab_np['J0660_ISO_GAUSS'][2] - tab_np['gSDSS_ISO_GAUSS'][2]

#Color
x4_np_ISO_GAUSS_2 = tab_np['J0660_ISO_GAUSS'][2] - tab_np['rSDSS_ISO_GAUSS'][2]
y4_np_ISO_GAUSS_2 = tab_np['gSDSS_ISO_GAUSS'][2] - tab_np['J0515_ISO_GAUSS'][2]

    
#Color
x5_np_ISO_GAUSS_2 = tab_np['gSDSS_ISO_GAUSS'][2] - tab_np['iSDSS_ISO_GAUSS'][2]
y5_np_ISO_GAUSS_2 = tab_np['J0410_ISO_GAUSS'][2] - tab_np['J0660_ISO_GAUSS'][2]


#Calor ISO GAUSS
#Color vironen
x_np_ISO_GAUSS_3 = tab_np['rSDSS_ISO_GAUSS'][3] - tab_np['iSDSS_ISO_GAUSS'][3]
y_np_ISO_GAUSS_3 = tab_np['rSDSS_ISO_GAUSS'][3] - tab_np['J0660_ISO_GAUSS'][3]

#Color
x1_np_ISO_GAUSS_3 = tab_np['J0515_ISO_GAUSS'][3] - tab_np['J0861_ISO_GAUSS'][3]
y1_np_ISO_GAUSS_3 = tab_np['J0515_ISO_GAUSS'][3] - tab_np['J0660_ISO_GAUSS'][3]

#Color
x2_np_ISO_GAUSS_3 = tab_np['zSDSS_ISO_GAUSS'][3] - tab_np['gSDSS_ISO_GAUSS'][3]
y2_np_ISO_GAUSS_3 = tab_np['zSDSS_ISO_GAUSS'][3] - tab_np['J0660_ISO_GAUSS'][3]

#Color
x3_np_ISO_GAUSS_3 = tab_np['J0660_ISO_GAUSS'][3] - tab_np['rSDSS_ISO_GAUSS'][3]
y3_np_ISO_GAUSS_3 = tab_np['J0660_ISO_GAUSS'][3] - tab_np['gSDSS_ISO_GAUSS'][3]

#Color
x4_np_ISO_GAUSS_3 = tab_np['J0660_ISO_GAUSS'][3] - tab_np['rSDSS_ISO_GAUSS'][3]
y4_np_ISO_GAUSS_3 = tab_np['gSDSS_ISO_GAUSS'][3] - tab_np['J0515_ISO_GAUSS'][3]

    
#Color
x5_np_ISO_GAUSS_3 = tab_np['gSDSS_ISO_GAUSS'][3] - tab_np['iSDSS_ISO_GAUSS'][3]
y5_np_ISO_GAUSS_3 = tab_np['J0410_ISO_GAUSS'][3] - tab_np['J0660_ISO_GAUSS'][3]

##################################################################
##################################################################
#Cross macthing ith HASt#########################################
##################################################################
##################################################################
#Calor ISO GAUSS
#Color vironen
x_np_hast_ISO_GAUSS = tab_np_hast['rSDSS_ISO_GAUSS'] - tab_np_hast['iSDSS_ISO_GAUSS']
y_np_hast_ISO_GAUSS = tab_np_hast['rSDSS_ISO_GAUSS'] - tab_np_hast['J0660_ISO_GAUSS']

#Color
x1_np_hast_ISO_GAUSS = tab_np_hast['J0515_ISO_GAUSS'] - tab_np_hast['J0861_ISO_GAUSS']
y1_np_hast_ISO_GAUSS = tab_np_hast['J0515_ISO_GAUSS'] - tab_np_hast['J0660_ISO_GAUSS']

#Color
x2_np_hast_ISO_GAUSS = tab_np_hast['zSDSS_ISO_GAUSS'] - tab_np_hast['gSDSS_ISO_GAUSS']
y2_np_hast_ISO_GAUSS = tab_np_hast['zSDSS_ISO_GAUSS'] - tab_np_hast['J0660_ISO_GAUSS']

#Color
x3_np_hast_ISO_GAUSS = tab_np_hast['J0660_ISO_GAUSS'] - tab_np_hast['rSDSS_ISO_GAUSS']
y3_np_hast_ISO_GAUSS = tab_np_hast['J0660_ISO_GAUSS'] - tab_np_hast['gSDSS_ISO_GAUSS']

#Color
x4_np_hast_ISO_GAUSS = tab_np_hast['J0660_ISO_GAUSS'] - tab_np_hast['rSDSS_ISO_GAUSS']
y4_np_hast_ISO_GAUSS = tab_np_hast['gSDSS_ISO_GAUSS'] - tab_np_hast['J0515_ISO_GAUSS']

    
#Color
x5_np_hast_ISO_GAUSS = tab_np_hast['gSDSS_ISO_GAUSS'] - tab_np_hast['iSDSS_ISO_GAUSS']
y5_np_hast_ISO_GAUSS = tab_np_hast['J0410_ISO_GAUSS'] - tab_np_hast['J0660_ISO_GAUSS']

##################################################################
##################################################################
#Cross macthing ith HASt SPLUS#########################################
##################################################################
##################################################################
#Calor ISO GAUSS
#Color vironen
x_np_hast_ISO_GAUSS_s = tab_np_hast_s['rSDSS_ISO_GAUSS'] - tab_np_hast_s['iSDSS_ISO_GAUSS']
y_np_hast_ISO_GAUSS_s = tab_np_hast_s['rSDSS_ISO_GAUSS'] - tab_np_hast_s['J0660_ISO_GAUSS']

#Color
x1_np_hast_ISO_GAUSS_s = tab_np_hast_s['J0515_ISO_GAUSS'] - tab_np_hast_s['J0861_ISO_GAUSS']
y1_np_hast_ISO_GAUSS_s = tab_np_hast_s['J0515_ISO_GAUSS'] - tab_np_hast_s['J0660_ISO_GAUSS']

#Color
x2_np_hast_ISO_GAUSS_s = tab_np_hast_s['zSDSS_ISO_GAUSS'] - tab_np_hast_s['gSDSS_ISO_GAUSS']
y2_np_hast_ISO_GAUSS_s = tab_np_hast_s['zSDSS_ISO_GAUSS'] - tab_np_hast_s['J0660_ISO_GAUSS']

#Color
x3_np_hast_ISO_GAUSS_s = tab_np_hast_s['J0660_ISO_GAUSS'] - tab_np_hast_s['rSDSS_ISO_GAUSS']
y3_np_hast_ISO_GAUSS_s = tab_np_hast_s['J0660_ISO_GAUSS'] - tab_np_hast_s['gSDSS_ISO_GAUSS']

#Color
x4_np_hast_ISO_GAUSS_s = tab_np_hast_s['J0660_ISO_GAUSS'] - tab_np_hast_s['rSDSS_ISO_GAUSS']
y4_np_hast_ISO_GAUSS_s = tab_np_hast_s['gSDSS_ISO_GAUSS'] - tab_np_hast_s['J0515_ISO_GAUSS']

    
#Color
x5_np_hast_ISO_GAUSS_s = tab_np_hast_s['gSDSS_ISO_GAUSS'] - tab_np_hast_s['iSDSS_ISO_GAUSS']
y5_np_hast_ISO_GAUSS_s = tab_np_hast_s['J0410_ISO_GAUSS'] - tab_np_hast_s['J0660_ISO_GAUSS']


#########################################################
#ERROR ##################################################
#########################################################
#Calor ISO GAUSS
#Color vironen
x_np_ISO_GAUSS_0_err = np.sqrt(tab_np['rSDSS_ISO_GAUSS_err'][0]**2 + tab_np['iSDSS_ISO_GAUSS_err'][0]**2)
y_np_ISO_GAUSS_0_err = np.sqrt(tab_np['rSDSS_ISO_GAUSS_err'][0]**2 + tab_np['J0660_ISO_GAUSS_err'][0]**2)

#Color
x1_np_ISO_GAUSS_0_err = np.sqrt(tab_np['J0515_ISO_GAUSS_err'][0]**2 + float(tab_np['J0861_ISO_GAUSS_err'][0])**2)
y1_np_ISO_GAUSS_0_err = np.sqrt(tab_np['J0515_ISO_GAUSS_err'][0]**2 + tab_np['J0660_ISO_GAUSS_err'][0]**2)

#Color
x2_np_ISO_GAUSS_0_err = np.sqrt(tab_np['zSDSS_ISO_GAUSS_err'][0]**2 + tab_np['gSDSS_ISO_GAUSS_err'][0]**2)
y2_np_ISO_GAUSS_0_err = np.sqrt(tab_np['zSDSS_ISO_GAUSS_err'][0]**2 + tab_np['J0660_ISO_GAUSS_err'][0]**2)

#Color
x3_np_ISO_GAUSS_0_err = np.sqrt(tab_np['J0660_ISO_GAUSS_err'][0]**2 + tab_np['rSDSS_ISO_GAUSS_err'][0]**2)
y3_np_ISO_GAUSS_0_err = np.sqrt(tab_np['J0660_ISO_GAUSS_err'][0]**2 + tab_np['gSDSS_ISO_GAUSS_err'][0]**2)

#Color
x4_np_ISO_GAUSS_0_err = np.sqrt(tab_np['J0660_ISO_GAUSS_err'][0]**2 + tab_np['rSDSS_ISO_GAUSS_err'][0]**2)
y4_np_ISO_GAUSS_0_err = np.sqrt(tab_np['gSDSS_ISO_GAUSS_err'][0]**2 + tab_np['J0515_ISO_GAUSS_err'][0]**2)

    
#Color
x5_np_ISO_GAUSS_0_err = np.sqrt(tab_np['gSDSS_ISO_GAUSS_err'][0]**2 + tab_np['iSDSS_ISO_GAUSS_err'][0]**2)
y5_np_ISO_GAUSS_0_err = np.sqrt(tab_np['J0410_ISO_GAUSS_err'][0]**2 + tab_np['J0660_ISO_GAUSS_err'][0]**2)

#Calor ISO GAUSS
#Color vironen
x_np_ISO_GAUSS_1_err = np.sqrt(tab_np['rSDSS_ISO_GAUSS_err'][1]**2 + tab_np['iSDSS_ISO_GAUSS_err'][1]**2)
y_np_ISO_GAUSS_1_err = np.sqrt(tab_np['rSDSS_ISO_GAUSS_err'][1]**2 + tab_np['J0660_ISO_GAUSS_err'][1]**2)

#Color
x1_np_ISO_GAUSS_1_err = np.sqrt(tab_np['J0515_ISO_GAUSS_err'][1]**2 + float(tab_np['J0861_ISO_GAUSS_err'][1])**2)
y1_np_ISO_GAUSS_1_err = np.sqrt(tab_np['J0515_ISO_GAUSS_err'][1]**2 + tab_np['J0660_ISO_GAUSS_err'][1]**2)

#Color
x2_np_ISO_GAUSS_1_err = np.sqrt(tab_np['zSDSS_ISO_GAUSS_err'][1]**2 + tab_np['gSDSS_ISO_GAUSS_err'][1]**2)
y2_np_ISO_GAUSS_1_err = np.sqrt(tab_np['zSDSS_ISO_GAUSS_err'][1]**2 + tab_np['J0660_ISO_GAUSS_err'][1]**2)

#Color
x3_np_ISO_GAUSS_1_err = np.sqrt(tab_np['J0660_ISO_GAUSS_err'][1]**2 + tab_np['rSDSS_ISO_GAUSS_err'][1]**2)
y3_np_ISO_GAUSS_1_err = np.sqrt(tab_np['J0660_ISO_GAUSS_err'][1]**2 + tab_np['gSDSS_ISO_GAUSS_err'][1]**2)

#Color
x4_np_ISO_GAUSS_1_err = np.sqrt(tab_np['J0660_ISO_GAUSS_err'][1]**2 + tab_np['rSDSS_ISO_GAUSS_err'][1]**2)
y4_np_ISO_GAUSS_1_err = np.sqrt(tab_np['gSDSS_ISO_GAUSS_err'][1]**2 + tab_np['J0515_ISO_GAUSS_err'][1]**2)

    
#Color
x5_np_ISO_GAUSS_1_err = np.sqrt(tab_np['gSDSS_ISO_GAUSS_err'][1]**2 + tab_np['iSDSS_ISO_GAUSS_err'][1]**2)
y5_np_ISO_GAUSS_1_err = np.sqrt(tab_np['J0410_ISO_GAUSS_err'][1]**2 + tab_np['J0660_ISO_GAUSS_err'][1]**2)

#Calor ISO GAUSS
#Color vironen
x_np_ISO_GAUSS_2_err = np.sqrt(tab_np['rSDSS_ISO_GAUSS_err'][2]**2 + tab_np['iSDSS_ISO_GAUSS_err'][2]**2)
y_np_ISO_GAUSS_2_err = np.sqrt(tab_np['rSDSS_ISO_GAUSS_err'][2]**2 + tab_np['J0660_ISO_GAUSS_err'][2]**2)

#Color
x1_np_ISO_GAUSS_2_err = np.sqrt(tab_np['J0515_ISO_GAUSS_err'][2]**2 + float(tab_np['J0861_ISO_GAUSS_err'][2])**2)
y1_np_ISO_GAUSS_2_err = np.sqrt(tab_np['J0515_ISO_GAUSS_err'][2]**2 + tab_np['J0660_ISO_GAUSS_err'][2]**2)

#Color
x2_np_ISO_GAUSS_2_err = np.sqrt(tab_np['zSDSS_ISO_GAUSS_err'][2]**2 + tab_np['gSDSS_ISO_GAUSS_err'][2]**2)
y2_np_ISO_GAUSS_2_err = np.sqrt(tab_np['zSDSS_ISO_GAUSS_err'][2]**2 + tab_np['J0660_ISO_GAUSS_err'][2]**2)

#Color
x3_np_ISO_GAUSS_2_err = np.sqrt(tab_np['J0660_ISO_GAUSS_err'][2]**2 + tab_np['rSDSS_ISO_GAUSS_err'][2]**2)
y3_np_ISO_GAUSS_2_err = np.sqrt(tab_np['J0660_ISO_GAUSS_err'][2]**2 + tab_np['gSDSS_ISO_GAUSS_err'][2]**2)

#Color
x4_np_ISO_GAUSS_2_err = np.sqrt(tab_np['J0660_ISO_GAUSS_err'][2]**2 + tab_np['rSDSS_ISO_GAUSS_err'][2]**2)
y4_np_ISO_GAUSS_2_err = np.sqrt(tab_np['gSDSS_ISO_GAUSS_err'][2]**2 + tab_np['J0515_ISO_GAUSS_err'][2]**2)

    
#Color
x5_np_ISO_GAUSS_2_err = np.sqrt(tab_np['gSDSS_ISO_GAUSS_err'][2]**2 + tab_np['iSDSS_ISO_GAUSS_err'][2]**2)
y5_np_ISO_GAUSS_2_err = np.sqrt(tab_np['J0410_ISO_GAUSS_err'][2]**2 + tab_np['J0660_ISO_GAUSS_err'][2]**2)


#Calor ISO GAUSS
#Color vironen
x_np_ISO_GAUSS_3_err = np.sqrt(tab_np['rSDSS_ISO_GAUSS_err'][3]**2 + tab_np['iSDSS_ISO_GAUSS_err'][3]**2)
y_np_ISO_GAUSS_3_err = np.sqrt(tab_np['rSDSS_ISO_GAUSS_err'][3]**2 + tab_np['J0660_ISO_GAUSS_err'][3]**2)

#Color
x1_np_ISO_GAUSS_3_err = np.sqrt(tab_np['J0515_ISO_GAUSS_err'][3]**2 + 0.0**2)
y1_np_ISO_GAUSS_3_err = np.sqrt(tab_np['J0515_ISO_GAUSS_err'][3]**2 + tab_np['J0660_ISO_GAUSS_err'][3]**2)

#Color
x2_np_ISO_GAUSS_3_err = np.sqrt(tab_np['zSDSS_ISO_GAUSS_err'][3]**2 + tab_np['gSDSS_ISO_GAUSS_err'][3]**2)
y2_np_ISO_GAUSS_3_err = np.sqrt(tab_np['zSDSS_ISO_GAUSS_err'][3]**2 + tab_np['J0660_ISO_GAUSS_err'][3]**2)

#Color
x3_np_ISO_GAUSS_3_err = np.sqrt(tab_np['J0660_ISO_GAUSS_err'][3]**2 + tab_np['rSDSS_ISO_GAUSS_err'][3]**2)
y3_np_ISO_GAUSS_3_err = np.sqrt(tab_np['J0660_ISO_GAUSS_err'][3]**2 + tab_np['gSDSS_ISO_GAUSS_err'][3]**2)

#Color
x4_np_ISO_GAUSS_3_err = np.sqrt(tab_np['J0660_ISO_GAUSS_err'][3]**2 + tab_np['rSDSS_ISO_GAUSS_err'][3]**2)
y4_np_ISO_GAUSS_3_err = np.sqrt(tab_np['gSDSS_ISO_GAUSS_err'][3]**2 + tab_np['J0515_ISO_GAUSS_err'][3]**2)

    
#Color
x5_np_ISO_GAUSS_3_err = np.sqrt(tab_np['gSDSS_ISO_GAUSS_err'][3]**2 + tab_np['iSDSS_ISO_GAUSS_err'][3]**2)
y5_np_ISO_GAUSS_3_err = np.sqrt(tab_np['J0410_ISO_GAUSS_err'][3]**2 + tab_np['J0660_ISO_GAUSS_err'][3]**2)

##################################################################
##################################################################
#Cross macthing ith HASt#########################################
##################################################################
##################################################################
#Color vironen
x_np_hast_ISO_GAUSS_err = np.sqrt(tab_np_hast['rSDSS_ISO_GAUSS_err']**2 + tab_np_hast['iSDSS_ISO_GAUSS_err']**2)
y_np_hast_ISO_GAUSS_err = np.sqrt(tab_np_hast['rSDSS_ISO_GAUSS_err']**2 + tab_np_hast['J0660_ISO_GAUSS_err']**2)

#Color
x1_np_hast_ISO_GAUSS_err =  np.sqrt(tab_np_hast['J0515_ISO_GAUSS_err']**2 + 0.0**2)
y1_np_hast_ISO_GAUSS_err =  np.sqrt(tab_np_hast['J0515_ISO_GAUSS_err']**2 + tab_np_hast['J0660_ISO_GAUSS_err']**2)

#Color
x2_np_hast_ISO_GAUSS_err =  np.sqrt(tab_np_hast['zSDSS_ISO_GAUSS_err']**2 + tab_np_hast['gSDSS_ISO_GAUSS_err']**2)
y2_np_hast_ISO_GAUSS_err =  np.sqrt(tab_np_hast['zSDSS_ISO_GAUSS_err']**2 + tab_np_hast['J0660_ISO_GAUSS_err']**2)

#Color
x3_np_hast_ISO_GAUSS_err = np.sqrt(tab_np_hast['J0660_ISO_GAUSS_err']**2 + tab_np_hast['rSDSS_ISO_GAUSS_err']**2)
y3_np_hast_ISO_GAUSS_err = np.sqrt(tab_np_hast['J0660_ISO_GAUSS_err']**2 + tab_np_hast['gSDSS_ISO_GAUSS_err']**2)

#Color
x4_np_hast_ISO_GAUSS_err = np.sqrt(tab_np_hast['J0660_ISO_GAUSS_err']**2 + tab_np_hast['rSDSS_ISO_GAUSS_err']**2)
y4_np_hast_ISO_GAUSS_err = np.sqrt(tab_np_hast['gSDSS_ISO_GAUSS_err']**2 + tab_np_hast['J0515_ISO_GAUSS_err']**2)

    
#Color
x5_np_hast_ISO_GAUSS_err = np.sqrt(tab_np_hast['gSDSS_ISO_GAUSS_err']**2 + tab_np_hast['iSDSS_ISO_GAUSS_err']**2)
y5_np_hast_ISO_GAUSS_err = np.sqrt(tab_np_hast['J0410_ISO_GAUSS_err']**2 + tab_np_hast['J0660_ISO_GAUSS_err']**2)

##################################################################
##################################################################
#Cross macthing ith HASt SPLUS#########################################
##################################################################
##################################################################
#Color vironen
x_np_hast_ISO_GAUSS_err_s = np.sqrt(tab_np_hast_s['rSDSS_ISO_GAUSS_err']**2 + tab_np_hast_s['iSDSS_ISO_GAUSS_err']**2)
y_np_hast_ISO_GAUSS_err_s = np.sqrt(tab_np_hast_s['rSDSS_ISO_GAUSS_err']**2 + tab_np_hast_s['J0660_ISO_GAUSS_err']**2)

#Color
x1_np_hast_ISO_GAUSS_err_s =  np.sqrt(tab_np_hast_s['J0515_ISO_GAUSS_err']**2 + tab_np_hast_s['J0861_ISO_GAUSS_err']**2)
y1_np_hast_ISO_GAUSS_err_s =  np.sqrt(tab_np_hast_s['J0515_ISO_GAUSS_err']**2 + tab_np_hast_s['J0660_ISO_GAUSS_err']**2)

#Color
x2_np_hast_ISO_GAUSS_err_s =  np.sqrt(tab_np_hast_s['zSDSS_ISO_GAUSS_err']**2 + tab_np_hast_s['gSDSS_ISO_GAUSS_err']**2)
y2_np_hast_ISO_GAUSS_err_s =  np.sqrt(tab_np_hast_s['zSDSS_ISO_GAUSS_err']**2 + tab_np_hast_s['J0660_ISO_GAUSS_err']**2)

#Color
x3_np_hast_ISO_GAUSS_err_s = np.sqrt(tab_np_hast_s['J0660_ISO_GAUSS_err']**2 + tab_np_hast_s['rSDSS_ISO_GAUSS_err']**2)
y3_np_hast_ISO_GAUSS_err_s = np.sqrt(tab_np_hast_s['J0660_ISO_GAUSS_err']**2 + tab_np_hast_s['gSDSS_ISO_GAUSS_err']**2)

#Color
x4_np_hast_ISO_GAUSS_err_s = np.sqrt(tab_np_hast_s['J0660_ISO_GAUSS_err']**2 + tab_np_hast_s['rSDSS_ISO_GAUSS_err']**2)
y4_np_hast_ISO_GAUSS_err_s = np.sqrt(tab_np_hast_s['gSDSS_ISO_GAUSS_err']**2 + tab_np_hast_s['J0515_ISO_GAUSS_err']**2)

    
#Color
x5_np_hast_ISO_GAUSS_err_s = np.sqrt(tab_np_hast_s['gSDSS_ISO_GAUSS_err']**2 + tab_np_hast_s['iSDSS_ISO_GAUSS_err']**2)
y5_np_hast_ISO_GAUSS_err_s = np.sqrt(tab_np_hast_s['J0410_ISO_GAUSS_err']**2 + tab_np_hast_s['J0660_ISO_GAUSS_err']**2)

def source_label(ax, txt, x, y, dx=6, dy=1.5):
    ax.annotate(txt, (x, y), (dx, dy),
                    textcoords='offset points', verticalalignment='center',
                    fontsize=9, alpha=0.9)
def source_label_hash(ax, txt, x, y, number, dx=6, dy=1.5):
    mask = tab_np_hast['Number'] == number
    ax.annotate(txt, (x[mask], y[mask]), (dx, dy),
                    textcoords='offset points', verticalalignment='center',
                    fontsize=9, alpha=0.9)
def source_label_hash_s(ax, txt, x, y,  dx=-2, dy=10):
    ax.annotate(txt, (float(x), float(y)), (dx, dy),
                    textcoords='offset points', verticalalignment='center',
                    fontsize=9, alpha=0.9,)


true_mask = tab_np_hast['Number'] == 5598
possible_mask = (tab_np_hast['Number'] != 5598) & (tab_np_hast['Number'] != 6034)
likely_mask = tab_np_hast['Number'] == 6034


# ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             )
#Halpha emitters find to metodogy suggest by Carlinhos
#tab_np = Table.read("ha-emitter-j660-r_iso_v1.tab", format="ascii.tab")


#Definition to make of plots
current_palette = sns.color_palette()
sns.palplot(current_palette)
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111)
ax.set_xlim(xmin=-3.7,xmax=3.7)
ax.set_ylim(ymin=-1.8,ymax=2.8)
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.xlabel('$r - i$', size =22)
plt.ylabel('$r - J0660$', size =22)
ax.scatter(x_np_ISO_GAUSS_0, y_np_ISO_GAUSS_0, c=sns.xkcd_rgb['true blue'], alpha=0.8, marker ='o', s=80, zorder=10.0, label='J-PLUS PN candidate')
ax.scatter(x_np_ISO_GAUSS_3, y_np_ISO_GAUSS_3, c='green', alpha=0.9, marker ='o', s=80, zorder=100.0, label='J-PLUS Known PN')
ax.scatter(x_np_ISO_GAUSS_1, y_np_ISO_GAUSS_1, c='gray', alpha=0.9, marker ='D', s=80, zorder=10.0, label='J-PLUS Known HII region')
ax.scatter(x_np_ISO_GAUSS_2, y_np_ISO_GAUSS_2, c='red', alpha=0.9, marker ='D', s=80, zorder=10.0, label='J-PLUS Known HII galaxy')

ax.scatter(x_np_hast_ISO_GAUSS[true_mask], y_np_hast_ISO_GAUSS[true_mask], c=sns.xkcd_rgb['dark purple'], alpha=0.9, marker ='o', s=80, zorder=10.0, label='J-PLUS tHASH PN')
ax.scatter(x_np_hast_ISO_GAUSS[likely_mask], y_np_hast_ISO_GAUSS[likely_mask], c=sns.xkcd_rgb['reddish brown'], alpha=0.8, marker ='o', s=80, zorder=10.0, label='J-PLUS lHASH PN')
ax.scatter(x_np_hast_ISO_GAUSS[possible_mask], y_np_hast_ISO_GAUSS[possible_mask], c='orange', alpha=0.8, marker ='o', s=80, zorder=10.0, label='J-PLUS pHASH PN')
ax.scatter(x_np_hast_ISO_GAUSS_s, y_np_hast_ISO_GAUSS_s, c=sns.xkcd_rgb['dark pink'], alpha=0.7, marker ='o', s=80, zorder=10.0, label='S-PLUS pHASH PN')

ax.errorbar(x_np_ISO_GAUSS_0, y_np_ISO_GAUSS_0, xerr=x_np_ISO_GAUSS_0_err, yerr=x_np_ISO_GAUSS_0_err,  marker='.', fmt='b.', alpha=0.8, markersize=8, capsize=8,)
ax.errorbar(x_np_ISO_GAUSS_3, y_np_ISO_GAUSS_3, xerr=x_np_ISO_GAUSS_3_err, yerr=y_np_ISO_GAUSS_3_err, marker='.', fmt='g.', alpha=0.4, markersize=8, capsize=8)
ax.errorbar(x_np_ISO_GAUSS_1, y_np_ISO_GAUSS_1, xerr=x_np_ISO_GAUSS_1_err, yerr=y_np_ISO_GAUSS_1_err, marker='.', fmt='k.', alpha=0.1,  markersize=8, capsize=8,)
ax.errorbar(x_np_ISO_GAUSS_2, y_np_ISO_GAUSS_2, xerr=x_np_ISO_GAUSS_2_err, yerr=y_np_ISO_GAUSS_2_err, marker='.', fmt='r.', alpha=0.1, markersize=8, capsize=8,)

ax.errorbar(x_np_hast_ISO_GAUSS[true_mask], y_np_hast_ISO_GAUSS[true_mask], xerr=x_np_hast_ISO_GAUSS_err[true_mask], yerr=y_np_hast_ISO_GAUSS_err[true_mask], marker='.', fmt='.', alpha=0.9, color="purple", markersize=8, capsize=8, label=None)
ax.errorbar(x_np_hast_ISO_GAUSS[possible_mask], y_np_hast_ISO_GAUSS[possible_mask], xerr=x_np_hast_ISO_GAUSS_err[possible_mask], yerr=y_np_hast_ISO_GAUSS_err[possible_mask], marker='.', fmt='.', alpha=0.9, color="orange", markersize=8, capsize=8, label=None)
ax.errorbar(x_np_hast_ISO_GAUSS[likely_mask], y_np_hast_ISO_GAUSS[likely_mask], xerr=x_np_hast_ISO_GAUSS_err[likely_mask], yerr=y_np_hast_ISO_GAUSS_err[likely_mask], marker='.', fmt='.', alpha=0.9, color="brown", markersize=8, capsize=8, label=None)

ax.errorbar(x_np_hast_ISO_GAUSS_s, y_np_hast_ISO_GAUSS_s, xerr=x_np_hast_ISO_GAUSS_err_s, yerr=y_np_hast_ISO_GAUSS_err_s, marker='.', fmt='.', alpha=0.9, color="pink", markersize=8, capsize=8, label=None)


# for cap in caps:
#     cap.set_markeredgewidth(1)

result = findIntersection(0.43, 0.65, -6.8, -1.3, 0.0)
result_y = 8.0*result + 4.50

x_new = np.linspace(-15.0, result, 200)
x_new2 = np.linspace(-15.0, result, 200)
y0 =  0.43*x_new + 0.65
yy = -6.8*x_new2 - 1.3
ax.plot(x_new, y0, color='k', linestyle='-')
ax.plot(x_new2, yy , color='k', linestyle='-')

# Region of the simbiotic stars
result1 = findIntersection(-220, +40.4, 0.39, 0.73, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(result1, 15.5, 200)
y_s = -220*x_new_s + 40.4
yy_s = 0.39*x_new2_s + 0.73

ax.plot(x_new_s, y_s, color='r', linestyle='--')
ax.plot(x_new2_s, yy_s , color='r', linestyle='--')

source_label(ax, "", x_np_ISO_GAUSS_0, y_np_ISO_GAUSS_0, dx=7)
source_label(ax, "PN Sp 4-1", x_np_ISO_GAUSS_3, y_np_ISO_GAUSS_3, dx=-52)
source_label(ax, "[HLG90] 55", x_np_ISO_GAUSS_1, y_np_ISO_GAUSS_1, dx=-60)
source_label(ax, "LEDA 101538", x_np_ISO_GAUSS_2, y_np_ISO_GAUSS_2, dx=-68)
source_label_hash(ax, "TK 1", x_np_hast_ISO_GAUSS, y_np_hast_ISO_GAUSS, 6034, dx=6, dy=6)
source_label_hash(ax, "Kn J1857.7+3931", x_np_hast_ISO_GAUSS, y_np_hast_ISO_GAUSS, 3014, dx=-75, dy=-13)
source_label_hash(ax, "KnPa J1848.6+4151", x_np_hast_ISO_GAUSS, y_np_hast_ISO_GAUSS, 45492, dy=10)
source_label_hash(ax, "Jacoby 1", x_np_hast_ISO_GAUSS, y_np_hast_ISO_GAUSS, 5598, dx=-45, dy=-1)
source_label_hash_s(ax, "Fr 2-21", x_np_hast_ISO_GAUSS_s, y_np_hast_ISO_GAUSS_s, dx=-36, dy=8)

plt.text(0.05, 0.92, 'hPN zone',
     transform=ax.transAxes, fontsize='x-large')
ax.minorticks_on()

plt.text(0.78, 0.92, 'SySt Zone',
         transform=ax.transAxes, color="red", fontsize='x-large')
ax.minorticks_on()

#ax1.grid(which='minor')#, lw=0.3)
ax.legend(scatterpoints=1, ncol=2, fontsize=12.3, loc="lower right", **lgd_kws)
ax.grid()
#sns.despine(bottom=True)
plt.tight_layout()
pltfile = 'Fig1-IDR-JPLUS-vironen_ISO_GAUSS.pdf'
save_path = '../../../../../Dropbox/JPAS/paper-phot/'
file_save = os.path.join(save_path, pltfile)
plt.savefig(file_save)

'''
J0515 - J0861 vs J0515 - J0660
'''
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax1 = fig.add_subplot(111)
ax1.set_xlim(xmin=-3.0,xmax=6.4)
ax1.set_ylim(ymin=-3.7,ymax=5.7)
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.xlabel('$J0515 - J0861$', size = 22)
plt.ylabel('$J0515 - J0660$', size = 22)
ax1.scatter(x1_np_ISO_GAUSS_0, y1_np_ISO_GAUSS_0, c='blue', alpha=0.8, marker ='o', s=80, cmap=plt.cm.hot, zorder=100.0, label='J-PLUS PN candidate')
ax1.scatter(x1_np_ISO_GAUSS_3, y1_np_ISO_GAUSS_3, c='green', alpha=0.8, marker ='o', s=80, cmap=plt.cm.hot, zorder=10.0, label='J-PLUS Known PN')
ax1.scatter(x1_np_ISO_GAUSS_1, y1_np_ISO_GAUSS_1, c='gray', alpha=0.9, marker ='D', s=80, cmap=plt.cm.hot, zorder=10.0, label='J-PLUS Known HII region')
ax1.scatter(x1_np_ISO_GAUSS_2, y1_np_ISO_GAUSS_2, c='red', alpha=0.9, marker ='D', s=80, cmap=plt.cm.hot, zorder=10.0, label='J-PLUS Known HII galaxy')
ax1.scatter(x1_np_hast_ISO_GAUSS[true_mask], y1_np_hast_ISO_GAUSS[true_mask], c=sns.xkcd_rgb['dark purple'], alpha=0.9, marker ='o', s=80, zorder=10.0, label='J-PLUS tHASH PN')
ax1.scatter(x1_np_hast_ISO_GAUSS[likely_mask], y1_np_hast_ISO_GAUSS[likely_mask], c=sns.xkcd_rgb['reddish brown'], alpha=0.8, marker ='o', s=80, zorder=10.0, label='J-PLUS lHASH PN')
ax1.scatter(x1_np_hast_ISO_GAUSS[possible_mask], y1_np_hast_ISO_GAUSS[possible_mask], c='orange', alpha=0.8, marker ='o', s=80, zorder=10.0, label='J-PLUS pHASH PN')
ax1.scatter(x1_np_hast_ISO_GAUSS_s, y1_np_hast_ISO_GAUSS_s, c=sns.xkcd_rgb['dark pink'], alpha=0.7, marker ='o', s=80, zorder=10.0, label='S-PLUS pHASH PN')


ax1.errorbar(x1_np_ISO_GAUSS_0, y1_np_ISO_GAUSS_0, xerr=x1_np_ISO_GAUSS_0_err, yerr=x1_np_ISO_GAUSS_0_err,  marker='.', fmt='b.', alpha=0.8, markersize=8, capsize=8,)
ax1.errorbar(x1_np_ISO_GAUSS_3, y1_np_ISO_GAUSS_3, xerr=x1_np_ISO_GAUSS_3_err, yerr=y1_np_ISO_GAUSS_3_err, marker='.', fmt='g.', alpha=0.8, markersize=8, capsize=8)
ax1.errorbar(x1_np_ISO_GAUSS_1, y1_np_ISO_GAUSS_1, xerr=x1_np_ISO_GAUSS_1_err, yerr=y1_np_ISO_GAUSS_1_err, marker='.', fmt='k.', alpha=0.6,  markersize=8, capsize=8,)
ax1.errorbar(x1_np_ISO_GAUSS_2, y1_np_ISO_GAUSS_2, xerr=x1_np_ISO_GAUSS_2_err, yerr=y1_np_ISO_GAUSS_2_err, marker='.', fmt='r.', alpha=0.6, markersize=8, capsize=8,)

ax1.errorbar(x1_np_hast_ISO_GAUSS[true_mask], y1_np_hast_ISO_GAUSS[true_mask], xerr=x1_np_hast_ISO_GAUSS_err[true_mask], yerr=y1_np_hast_ISO_GAUSS_err[true_mask], marker='.', fmt='.', alpha=0.9, color="purple", markersize=8, capsize=8, label=None)
ax1.errorbar(x1_np_hast_ISO_GAUSS[possible_mask], y1_np_hast_ISO_GAUSS[possible_mask], xerr=x1_np_hast_ISO_GAUSS_err[possible_mask], yerr=y1_np_hast_ISO_GAUSS_err[possible_mask], marker='.', fmt='.', alpha=0.9, color="orange", markersize=8, capsize=8, label=None)
ax1.errorbar(x1_np_hast_ISO_GAUSS[likely_mask], y1_np_hast_ISO_GAUSS[likely_mask], xerr=x1_np_hast_ISO_GAUSS_err[likely_mask], yerr=y1_np_hast_ISO_GAUSS_err[likely_mask], marker='.', fmt='.', alpha=0.9, color="brown", markersize=8, capsize=8, label=None)

ax1.errorbar(x1_np_hast_ISO_GAUSS_s, y1_np_hast_ISO_GAUSS_s, xerr=x1_np_hast_ISO_GAUSS_err_s, yerr=y1_np_hast_ISO_GAUSS_err_s, marker='.', fmt='.', alpha=0.9, color="pink", markersize=8, capsize=8, label=None)
# Region where are located the PNe
result = findIntersection(2.7, 2.15, 0.0, 0.22058956, 0.0)
result_y = 2.7*result + 2.15

x_new = np.linspace(result, 15.5, 200)
x_new2 = np.linspace(-10.0, result, 200)
x_new3 = np.linspace(-10.0, result, 200)
y = 2.7*x_new + 2.15
yy = 0.0*x_new2 + 0.22058956

ax1.plot(x_new, y, color='k', linestyle='-')
ax1.plot(x_new2, yy , color='k', linestyle='-')

# Region of the simbiotic stars
result1 = findIntersection(5.5, -6.45, 0.98, -0.16, 0.0)
x_new_s = np.linspace(result1, 15.5, 200)
x_new2_s = np.linspace(result1, 15.5, 200)
y_s = 5.5*x_new_s - 6.45
yy_s = 0.98*x_new2_s - 0.16

ax1.plot(x_new_s, y_s, color='r', linestyle='--')
ax1.plot(x_new2_s, yy_s , color='r', linestyle='--')

source_label(ax1, "", x1_np_ISO_GAUSS_0, y1_np_ISO_GAUSS_0, dx=-45)
source_label(ax1, "PN Sp 4-1", x1_np_ISO_GAUSS_3, y1_np_ISO_GAUSS_3, dx=-55)
source_label(ax1, "[HLG90] 55", x1_np_ISO_GAUSS_1, y1_np_ISO_GAUSS_1, dx=-62)
source_label(ax1, "LEDA 101538", x1_np_ISO_GAUSS_2, y1_np_ISO_GAUSS_2, dx=-69)
source_label_hash(ax1, "TK 1", x1_np_hast_ISO_GAUSS, y1_np_hast_ISO_GAUSS, 6034, dx=4, dy=-10)
source_label_hash(ax1, "Kn J1857.7+3931", x1_np_hast_ISO_GAUSS, y1_np_hast_ISO_GAUSS, 3014, dx=-50, dy=13)
source_label_hash(ax1, "KnPa J1848.6+4151", x1_np_hast_ISO_GAUSS, y1_np_hast_ISO_GAUSS, 45492, dy=10)
source_label_hash(ax1, "Jacoby 1", x1_np_hast_ISO_GAUSS, y1_np_hast_ISO_GAUSS, 5598, dx=-42, dy=6)
source_label_hash_s(ax1, "Fr 2-21", x1_np_hast_ISO_GAUSS_s, y1_np_hast_ISO_GAUSS_s, dx=-36, dy=-7)

plt.text(0.05, 0.91, 'hPN zone',
         transform=ax1.transAxes, fontsize='x-large')
plt.text(0.65, 0.91, 'SySt Zone',
         transform=ax1.transAxes, color="red", fontsize='x-large')
ax1.minorticks_on()

ax1.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax1.legend(scatterpoints=1, ncol=2, fontsize=12.3, loc="lower right", **lgd_kws)
ax1.grid()
plt.tight_layout()
pltfile = 'Fig2-IDR-JPLUS-J0515_ISO_GAUSS.pdf'
save_path = '../../../../../Dropbox/JPAS/paper-phot/'
file_save = os.path.join(save_path, pltfile)
plt.savefig(file_save)

plt.clf()
###########################################################
#############################################################
'''
z - g vs z - J0660
'''
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax2 = fig.add_subplot(111)
ax2.set_xlim(xmin=-5.9,xmax=3.9)
ax2.set_ylim(ymin=-5.5,ymax=5.0)
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.xlabel('$z - g$', size =22)
plt.ylabel('$z - J0660$', size =22)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax2.scatter(x2_np_ISO_GAUSS_0, y2_np_ISO_GAUSS_0, c='blue', alpha=0.8, marker ='o', s=80, cmap=plt.cm.hot, zorder=100.0, label='J-PLUS PN candidate')
ax2.scatter(x2_np_ISO_GAUSS_3, y2_np_ISO_GAUSS_3, c='green', alpha=0.8, marker ='o', s=80, cmap=plt.cm.hot, zorder=10.0, label='J-PLUS Known PN')
ax2.scatter(x2_np_ISO_GAUSS_1, y2_np_ISO_GAUSS_1, c='gray', alpha=0.9, marker ='D', s=80, cmap=plt.cm.hot, zorder=10.0, label='J-PLUS Known HII region')
ax2.scatter(x2_np_ISO_GAUSS_2, y2_np_ISO_GAUSS_2, c='red', alpha=0.9, marker ='D', s=80, cmap=plt.cm.hot, zorder=10.0, label='J-PLUS Known HII galaxy')

ax2.scatter(x2_np_hast_ISO_GAUSS[true_mask], y2_np_hast_ISO_GAUSS[true_mask], c=sns.xkcd_rgb['dark purple'], alpha=0.9, marker ='o', s=80, zorder=10.0, label='J-PLUS tHASH PN')
ax2.scatter(x2_np_hast_ISO_GAUSS[likely_mask], y2_np_hast_ISO_GAUSS[likely_mask], c=sns.xkcd_rgb['reddish brown'], alpha=0.8, marker ='o', s=80, zorder=10.0, label='J-PLUS lHASH PN')
ax2.scatter(x2_np_hast_ISO_GAUSS[possible_mask], y2_np_hast_ISO_GAUSS[possible_mask], c='orange', alpha=0.8, marker ='o', s=80, zorder=10.0, label='J-PLUS pHASH PN')
ax2.scatter(x2_np_hast_ISO_GAUSS_s, y2_np_hast_ISO_GAUSS_s, c=sns.xkcd_rgb['dark pink'], alpha=0.7, marker ='o', s=80, zorder=10.0, label='S-PLUS pHASH PN')

ax2.errorbar(x2_np_ISO_GAUSS_0, y2_np_ISO_GAUSS_0, xerr=x2_np_ISO_GAUSS_0_err, yerr=x2_np_ISO_GAUSS_0_err,  marker='.', fmt='b.', alpha=0.8, markersize=8, capsize=8,)
ax2.errorbar(x2_np_ISO_GAUSS_3, y2_np_ISO_GAUSS_3, xerr=x2_np_ISO_GAUSS_3_err, yerr=y2_np_ISO_GAUSS_3_err, marker='.', fmt='g.', alpha=0.8, markersize=8, capsize=8)
ax2.errorbar(x2_np_ISO_GAUSS_1, y2_np_ISO_GAUSS_1, xerr=x2_np_ISO_GAUSS_1_err, yerr=y2_np_ISO_GAUSS_1_err, marker='.', fmt='k.', alpha=0.6,  markersize=8, capsize=8,)
ax2.errorbar(x2_np_ISO_GAUSS_2, y2_np_ISO_GAUSS_2, xerr=x2_np_ISO_GAUSS_2_err, yerr=y2_np_ISO_GAUSS_2_err, marker='.', fmt='r.', alpha=0.6, markersize=8, capsize=8,)

ax2.errorbar(x2_np_hast_ISO_GAUSS[true_mask], y2_np_hast_ISO_GAUSS[true_mask], xerr=x2_np_hast_ISO_GAUSS_err[true_mask], yerr=y2_np_hast_ISO_GAUSS_err[true_mask], marker='.', fmt='.', alpha=0.9, color="purple", markersize=8, capsize=8, label=None)
ax2.errorbar(x2_np_hast_ISO_GAUSS[possible_mask], y2_np_hast_ISO_GAUSS[possible_mask], xerr=x2_np_hast_ISO_GAUSS_err[possible_mask], yerr=y2_np_hast_ISO_GAUSS_err[possible_mask], marker='.', fmt='.', alpha=0.9, color="orange", markersize=8, capsize=8, label=None)
ax2.errorbar(x2_np_hast_ISO_GAUSS[likely_mask], y2_np_hast_ISO_GAUSS[likely_mask], xerr=x2_np_hast_ISO_GAUSS_err[likely_mask], yerr=y2_np_hast_ISO_GAUSS_err[likely_mask], marker='.', fmt='.', alpha=0.9, color="brown", markersize=8, capsize=8, label=None)

ax2.errorbar(x2_np_hast_ISO_GAUSS_s, y2_np_hast_ISO_GAUSS_s, xerr=x2_np_hast_ISO_GAUSS_err_s, yerr=y2_np_hast_ISO_GAUSS_err_s, marker='.', fmt='.', color="pink", markersize=8, capsize=8, label=None)

result = findIntersection(0.2319, 0.85, -1.3, 1.7, 0.0)
result_y = 0.2319*result + 0.85

x_new = np.linspace(result, 15.5, 200)
x_new2 = np.linspace(-10.0, result, 200)

y = 0.2319*x_new + 0.85
yy = -1.3*x_new2 +  1.7
#Mask
#mask = y >= result_y - 0.5
ax2.plot(x_new, y, color='k', linestyle='-')
ax2.plot(x_new2, yy , color='k', linestyle='-')

# Region of the simbiotic stars=>
result1 = findIntersection(-1.96, -3.15, 0.2, 0.44, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(-15.5, result1, 200)
y_s = -1.96*x_new_s - 3.15
yy_s = 0.2*x_new2_s + 0.44
ax2.plot(x_new_s, y_s, color='r', linestyle='--')
ax2.plot(x_new2_s, yy_s , color='r', linestyle='--')

source_label(ax2, "", x2_np_ISO_GAUSS_0, y2_np_ISO_GAUSS_0, dx=-42)
source_label(ax2, "PN Sp 4-1", x2_np_ISO_GAUSS_3, y2_np_ISO_GAUSS_3, dx=5, dy=7)
source_label(ax2, "[HLG90] 55", x2_np_ISO_GAUSS_1, y2_np_ISO_GAUSS_1, dy=-8)
source_label(ax2, "LEDA 101538", x2_np_ISO_GAUSS_2, y2_np_ISO_GAUSS_2, dx=7, dy=-5)
source_label_hash(ax2, "TK 1", x2_np_hast_ISO_GAUSS, y2_np_hast_ISO_GAUSS, 6034)
source_label_hash(ax2, "Kn J1857.7+3931", x2_np_hast_ISO_GAUSS, y2_np_hast_ISO_GAUSS, 3014, dx=-85, dy=-5)#, dx=-85, dy=5)
source_label_hash(ax2, "KnPa J1848.6+4151", x2_np_hast_ISO_GAUSS, y2_np_hast_ISO_GAUSS, 45492, dy=-10)
source_label_hash(ax2, "Jacoby 1", x2_np_hast_ISO_GAUSS, y2_np_hast_ISO_GAUSS, 5598, dx=4, dy=-10)#, dx=-45, dy=-5)
source_label_hash_s(ax2, "Fr 2-21", x2_np_hast_ISO_GAUSS_s, y2_np_hast_ISO_GAUSS_s, dx=-36, dy=7) 

plt.text(0.7, 0.91, 'hPN zone',
         transform=ax2.transAxes, fontsize='x-large')
plt.text(0.03, 0.85, 'SySt Zone',
         transform=ax2.transAxes, color="red", fontsize='x-large')
ax2.minorticks_on()

ax2.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax2.legend(scatterpoints=1, ncol=2, fontsize=12.3, loc="lower right", **lgd_kws)
ax2.grid()
#sns.despine(bottom=True)
plt.tight_layout()
pltfile = 'Fig3-IDR-JPLUS-z_ISO_GAUSS.pdf'
file_save = os.path.join(save_path, pltfile)
plt.savefig(file_save)
plt.clf()

#########################################################################
#########################################################################

'''
J0660 - r vs J0660 - g
'''
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax3 = fig.add_subplot(111)
ax3.set_xlim(xmin=-2.5,xmax=0.5)
ax3.set_ylim(ymin=-5.0,ymax=1.5)
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.xlabel('$J0660 - r$', size =22)
plt.ylabel('$J0660 - gSDSS$', size =22)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax3.scatter(x3_np_ISO_GAUSS_0, y3_np_ISO_GAUSS_0, c='blue', alpha=0.8, marker ='o', s=80, cmap=plt.cm.hot, zorder=100.0, label='J-PLUS PN candidate')
ax3.scatter(x3_np_ISO_GAUSS_3, y3_np_ISO_GAUSS_3, c='green', alpha=0.8, marker ='o', s=80, cmap=plt.cm.hot, zorder=10.0, label='J-PLUS Known PN')
ax3.scatter(x3_np_ISO_GAUSS_1, y3_np_ISO_GAUSS_1, c='gray', alpha=0.9, marker ='D', s=80, cmap=plt.cm.hot, zorder=10.0, label='J-PLUS Known HII region')
ax3.scatter(x3_np_ISO_GAUSS_2, y3_np_ISO_GAUSS_2, c='red', alpha=0.9, marker ='D', s=80, cmap=plt.cm.hot, zorder=10.0, label='J-PLUS Known HII galaxy')
ax3.scatter(x3_np_hast_ISO_GAUSS[true_mask], y3_np_hast_ISO_GAUSS[true_mask], c=sns.xkcd_rgb['dark purple'], alpha=0.9, marker ='o', s=80, zorder=10.0, label='J-PLUS, T HASH PNe?')
ax3.scatter(x3_np_hast_ISO_GAUSS[possible_mask], y3_np_hast_ISO_GAUSS[possible_mask], c='orange', alpha=0.8, marker ='o', s=80, zorder=10.0, label='J-PLUS, P HASH PNe?')
ax3.scatter(x3_np_hast_ISO_GAUSS[likely_mask], y3_np_hast_ISO_GAUSS[likely_mask], c=sns.xkcd_rgb['reddish brown'], alpha=0.8, marker ='o', s=80, zorder=10.0, label='J-PLUS, L HASH PNe?')
ax3.scatter(x3_np_hast_ISO_GAUSS_s, y3_np_hast_ISO_GAUSS_s, c=sns.xkcd_rgb['dark pink'], alpha=0.7, marker ='o', s=80, zorder=10.0, label='S-PLUS, P HASH PNe')

ax3.errorbar(x3_np_ISO_GAUSS_0, y3_np_ISO_GAUSS_0, xerr=x3_np_ISO_GAUSS_0_err, yerr=x3_np_ISO_GAUSS_0_err,  marker='.', fmt='b.', alpha=0.8, markersize=8, capsize=8,)
ax3.errorbar(x3_np_ISO_GAUSS_3, y3_np_ISO_GAUSS_3, xerr=x3_np_ISO_GAUSS_3_err, yerr=y3_np_ISO_GAUSS_3_err, marker='.', fmt='g.', alpha=0.8, markersize=8, capsize=8)
ax3.errorbar(x3_np_ISO_GAUSS_1, y3_np_ISO_GAUSS_1, xerr=x3_np_ISO_GAUSS_1_err, yerr=y3_np_ISO_GAUSS_1_err, marker='.', fmt='k.', alpha=0.6,  markersize=8, capsize=8,)
ax3.errorbar(x3_np_ISO_GAUSS_2, y3_np_ISO_GAUSS_2, xerr=x3_np_ISO_GAUSS_2_err, yerr=y3_np_ISO_GAUSS_2_err, marker='.', fmt='r.', alpha=0.6, markersize=8, capsize=8,)
ax3.errorbar(x3_np_hast_ISO_GAUSS, y3_np_hast_ISO_GAUSS, xerr=x3_np_hast_ISO_GAUSS_err, yerr=y3_np_hast_ISO_GAUSS_err, marker='.', fmt='.', color="orange", alpha=0.9, markersize=8, capsize=8, label=None)
ax3.errorbar(x3_np_hast_ISO_GAUSS_s, y3_np_hast_ISO_GAUSS_s, xerr=x3_np_hast_ISO_GAUSS_err_s, yerr=y3_np_hast_ISO_GAUSS_err_s, marker='.', fmt='.', color="pink", markersize=8, capsize=8, label=None)
# Region where stay the PNe
result = findIntersection(1.559, 0.58, -0.5, 0.0, 0.0)
result_y = 1.559*result + 0.58

x_new = np.linspace(-15, -0.5, 200)
x_new2 = -0.5
x_new3 = np.linspace(-10.0, 1.1, 200)
y = 1.559*x_new + 0.58
yy = 0.0*x_new2 
#Mask
#mask = y >= result_y - 0.5
ax3.plot(x_new, y, color='k', linestyle='-')
plt.axvline(x=-0.5, ymin=0.74, ymax = 1.79, color='k', linestyle='-')
#plt.axvline(x=0.1, ymin=0.18, ymax = 1.79, linewidth=2, color='k')

source_label(ax3, "PN ????", x3_np_ISO_GAUSS_0, y3_np_ISO_GAUSS_0)
source_label(ax3, "PN Sp 4-1", x3_np_ISO_GAUSS_3, y3_np_ISO_GAUSS_3)
source_label(ax3, "[HLG90] 55", x3_np_ISO_GAUSS_1, y3_np_ISO_GAUSS_1)
source_label(ax3, "LEDA 101538", x3_np_ISO_GAUSS_2, y3_np_ISO_GAUSS_2)
source_label_hash(ax3, "TK 1", x3_np_hast_ISO_GAUSS, y3_np_hast_ISO_GAUSS, 6034)
source_label_hash(ax3, "Kn J1857.7+3931", x3_np_hast_ISO_GAUSS, y3_np_hast_ISO_GAUSS, 3014, dx=-85, dy=5)
source_label_hash(ax3, "KnPa J1848.6+4151", x3_np_hast_ISO_GAUSS, y3_np_hast_ISO_GAUSS, 45492, dy=10)
source_label_hash(ax3, "Jacoby 1", x3_np_hast_ISO_GAUSS, y3_np_hast_ISO_GAUSS, 5598, dx=-45, dy=-5)

plt.text(0.05, 0.90, 'hPN zone',
         transform=ax3.transAxes, fontsize='x-large')

ax3.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax3.legend(scatterpoints=1, ncol=2, fontsize=12.3, **lgd_kws)
ax3.grid()
#sns.despine(bottom=True)
plt.tight_layout()
pltfile = 'Fig4-IDR-JPLUS-g_ISO_GAUSS.pdf'
file_save = os.path.join(save_path, pltfile)
plt.savefig(file_save)
plt.clf()

###############################################################
###############################################################
'''
J0660 - r vs g - J0515
'''
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax4 = fig.add_subplot(111)
ax4.set_xlim(xmin=-2.7,xmax=0.8)
ax4.set_ylim(ymin=-3.2,ymax=1.8)
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.xlabel('$J0660 - r$', size =22)
plt.ylabel('$g - J0515$', size =22)
ax4.scatter(x4_np_ISO_GAUSS_0, y4_np_ISO_GAUSS_0, c='blue', alpha=0.8, marker ='o', s=80, cmap=plt.cm.hot,  zorder=100.0, label='J-PLUS PN candidate')
ax4.scatter(x4_np_ISO_GAUSS_3, y4_np_ISO_GAUSS_3, c='green', alpha=0.8, marker ='o', s=80, cmap=plt.cm.hot, zorder=10.0, label='J-PLUS Known PN')
ax4.scatter(x4_np_ISO_GAUSS_1, y4_np_ISO_GAUSS_1, c='gray', alpha=0.9, marker ='D', s=80, cmap=plt.cm.hot, zorder=10.0, label='J-PLUS Known HII region')
ax4.scatter(x4_np_ISO_GAUSS_2, y4_np_ISO_GAUSS_2, c='red', alpha=0.9, marker ='D', s=80, cmap=plt.cm.hot, zorder=10.0, label='J-PLUS Known HII galaxy')
ax4.scatter(x4_np_hast_ISO_GAUSS[true_mask], y4_np_hast_ISO_GAUSS[true_mask], c=sns.xkcd_rgb['dark purple'], alpha=0.9, marker ='o', s=80, zorder=10.0, label='J-PLUS tHASH PN')
ax4.scatter(x4_np_hast_ISO_GAUSS[likely_mask], y4_np_hast_ISO_GAUSS[likely_mask], c=sns.xkcd_rgb['reddish brown'], alpha=0.8, marker ='o', s=80, zorder=10.0, label='J-PLUS lHASH PN')
ax4.scatter(x4_np_hast_ISO_GAUSS[possible_mask], y4_np_hast_ISO_GAUSS[possible_mask], c='orange', alpha=0.8, marker ='o', s=80, zorder=10.0, label='J-PLUS pHASH PN')
ax4.scatter(x4_np_hast_ISO_GAUSS_s, y4_np_hast_ISO_GAUSS_s, c=sns.xkcd_rgb['dark pink'], alpha=0.7, marker ='o', s=80, zorder=10.0, label='S-PLUS pHASH PN')

ax4.errorbar(x4_np_ISO_GAUSS_0, y4_np_ISO_GAUSS_0, xerr=x4_np_ISO_GAUSS_0_err, yerr=x4_np_ISO_GAUSS_0_err,  marker='.', fmt='b.', alpha=0.8, markersize=8, capsize=8,)
ax4.errorbar(x4_np_ISO_GAUSS_3, y4_np_ISO_GAUSS_3, xerr=x4_np_ISO_GAUSS_3_err, yerr=y4_np_ISO_GAUSS_3_err, marker='.', fmt='g.', alpha=0.8, markersize=8, capsize=8)
ax4.errorbar(x4_np_ISO_GAUSS_1, y4_np_ISO_GAUSS_1, xerr=x4_np_ISO_GAUSS_1_err, yerr=y4_np_ISO_GAUSS_1_err, marker='.', fmt='k.', alpha=0.6,  markersize=8, capsize=8,)
ax4.errorbar(x4_np_ISO_GAUSS_2, y4_np_ISO_GAUSS_2, xerr=x4_np_ISO_GAUSS_2_err, yerr=y4_np_ISO_GAUSS_2_err, marker='.', fmt='r.', alpha=0.6, markersize=8, capsize=8,)

ax4.errorbar(x4_np_hast_ISO_GAUSS[true_mask], y_np_hast_ISO_GAUSS[true_mask], xerr=x4_np_hast_ISO_GAUSS_err[true_mask], yerr=y4_np_hast_ISO_GAUSS_err[true_mask], marker='.', fmt='.', alpha=0.9, color="purple", markersize=8, capsize=8, label=None)
ax4.errorbar(x4_np_hast_ISO_GAUSS[possible_mask], y4_np_hast_ISO_GAUSS[possible_mask], xerr=x4_np_hast_ISO_GAUSS_err[possible_mask], yerr=y4_np_hast_ISO_GAUSS_err[possible_mask], marker='.', fmt='.', alpha=0.9, color="orange", markersize=8, capsize=8, label=None)
ax4.errorbar(x4_np_hast_ISO_GAUSS[likely_mask], y4_np_hast_ISO_GAUSS[likely_mask], xerr=x4_np_hast_ISO_GAUSS_err[likely_mask], yerr=y4_np_hast_ISO_GAUSS_err[likely_mask], marker='.', fmt='.', alpha=0.9, color="brown", markersize=8, capsize=8, label=None)

ax4.errorbar(x4_np_hast_ISO_GAUSS_s, y4_np_hast_ISO_GAUSS_s, xerr=x4_np_hast_ISO_GAUSS_err_s, yerr=y4_np_hast_ISO_GAUSS_err_s, marker='.', fmt='.', color="pink", markersize=8, capsize=8, label=None)

# Region where are located the PNe
result = findIntersection(0.12, -0.01, -1.1, -1.07, 0.0)
result_y = 0.12*result - 0.01

x_new = np.linspace(-15.5, result,  200)
x_new2 = np.linspace(result, 10.0, 200)
x_new3 = np.linspace(-10.0, 1.1, 200)
y = 0.12*x_new - 0.01
yy = -1.1*x_new2 - 1.07
#Mask
#mask = y >= result_y - 0.5
ax4.plot(x_new, y, color='k', linestyle='-')
ax4.plot(x_new2, yy , color='k', linestyle='-')

# Region of the simbiotic stars
result1 = findIntersection(-0.19, -0.05, -2.66, -2.2, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(-15.0, result1, 200)
y_s = -0.19*x_new_s - 0.09
yy_s = -2.66*x_new2_s - 2.2

ax4.plot(x_new_s, y_s, color='r', linestyle='--')
ax4.plot(x_new2_s, yy_s , color='r', linestyle='--')

source_label(ax4, "", x4_np_ISO_GAUSS_0, y4_np_ISO_GAUSS_0, dy=-4.5)
source_label(ax4, "PN Sp 4-1", x4_np_ISO_GAUSS_3, y4_np_ISO_GAUSS_3, dy=-4.5)
source_label(ax4, "[HLG90] 55", x4_np_ISO_GAUSS_1, y4_np_ISO_GAUSS_1, dy=-6)
source_label(ax4, "LEDA 101538", x4_np_ISO_GAUSS_2, y4_np_ISO_GAUSS_2, dy=-4.5)
source_label_hash(ax4, "TK 1", x4_np_hast_ISO_GAUSS, y4_np_hast_ISO_GAUSS, 6034)
source_label_hash(ax4, "Kn J1857.7+3931", x4_np_hast_ISO_GAUSS, y4_np_hast_ISO_GAUSS, 3014, dx=0, dy=-10)
source_label_hash(ax4, "KnPa J1848.6+4151", x4_np_hast_ISO_GAUSS, y4_np_hast_ISO_GAUSS, 45492, dx=-25, dy=20)
source_label_hash(ax4, "Jacoby 1", x4_np_hast_ISO_GAUSS, y4_np_hast_ISO_GAUSS, 5598, dx=-45, dy=-5)
source_label_hash_s(ax4, "Fr 2-21", x4_np_hast_ISO_GAUSS_s, y4_np_hast_ISO_GAUSS_s)

plt.text(0.05, 0.1, 'hPN zone',
         transform=ax4.transAxes, fontsize='x-large')
plt.text(0.05, 0.92, 'SySt Zone',
         transform=ax4.transAxes, color="red", fontsize='x-large')
ax4.minorticks_on()

ax4.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
#ax4.legend(scatterpoints=1, fontsize=15.0, loc="lower right", **lgd_kws)
ax4.grid()
#sns.despine(bottom=True)
plt.tight_layout()
pltfile = 'Fig5-IDR-JPLUS-r_ISO_GAUSS.pdf'
file_save = os.path.join(save_path, pltfile)
plt.savefig(file_save)
plt.clf()

####################################################################################
####################################################################################

'''
g - i vs J0410 - J0660
'''
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax5 = fig.add_subplot(111)
ax5.set_xlim(xmin=-3.0,xmax=5.0)
ax5.set_ylim(ymin=-2.0,ymax=6.0)

plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.xlabel('$g - i$', size=22)
plt.ylabel('$J0410 - J0660$', size =22)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax5.scatter(x5_np_ISO_GAUSS_0, y5_np_ISO_GAUSS_0, c='blue', alpha=0.8, marker ='o', s=80, cmap=plt.cm.hot, zorder=100.0, label='J-PLUS PN candidate')
ax5.scatter(x5_np_ISO_GAUSS_3, y5_np_ISO_GAUSS_3, c='green', alpha=0.8, marker ='o', s=80, cmap=plt.cm.hot, zorder=10.0, label='J-PLUS Known PN')
ax5.scatter(x5_np_ISO_GAUSS_1, y5_np_ISO_GAUSS_1, c='gray', alpha=0.9, marker ='D', s=80, cmap=plt.cm.hot, zorder=10.0,  label='J-PLUS Known HII region')
ax5.scatter(x5_np_ISO_GAUSS_2, y5_np_ISO_GAUSS_2, c='red', alpha=0.9, marker ='D', s=80, cmap=plt.cm.hot, zorder=10.0, label='J-PLUS Known HII galaxy')
ax5.scatter(x5_np_hast_ISO_GAUSS[true_mask], y5_np_hast_ISO_GAUSS[true_mask], c=sns.xkcd_rgb['dark purple'], alpha=0.9, marker ='o', s=80, zorder=10.0, label='J-PLUS tHASH PN')
ax5.scatter(x5_np_hast_ISO_GAUSS[likely_mask], y5_np_hast_ISO_GAUSS[likely_mask], c=sns.xkcd_rgb['reddish brown'], alpha=0.8, marker ='o', s=80, zorder=10.0, label='J-PLUS pHASH PN')
ax5.scatter(x5_np_hast_ISO_GAUSS[possible_mask], y5_np_hast_ISO_GAUSS[possible_mask], c='orange', alpha=0.8, marker ='o', s=80, zorder=10.0, label='J-PLUS pHASH PN')
ax5.scatter(x5_np_hast_ISO_GAUSS_s, y5_np_hast_ISO_GAUSS_s, c=sns.xkcd_rgb['dark pink'], alpha=0.7, marker ='o', s=80, zorder=10.0, label='S-PLUS pHASH PN')

ax5.errorbar(x5_np_ISO_GAUSS_0, y5_np_ISO_GAUSS_0, xerr=x5_np_ISO_GAUSS_0_err, yerr=x5_np_ISO_GAUSS_0_err,  marker='.', fmt='b.', alpha=0.8, markersize=8, capsize=8,)
ax5.errorbar(x5_np_ISO_GAUSS_3, y5_np_ISO_GAUSS_3, xerr=x5_np_ISO_GAUSS_3_err, yerr=y5_np_ISO_GAUSS_3_err, marker='.', fmt='g.', alpha=0.8, markersize=8, capsize=8)
ax5.errorbar(x5_np_ISO_GAUSS_1, y5_np_ISO_GAUSS_1, xerr=x5_np_ISO_GAUSS_1_err, yerr=y5_np_ISO_GAUSS_1_err, marker='.', fmt='k.', alpha=0.6,  markersize=8, capsize=8,)
ax5.errorbar(x5_np_ISO_GAUSS_2, y5_np_ISO_GAUSS_2, xerr=x5_np_ISO_GAUSS_2_err, yerr=y5_np_ISO_GAUSS_2_err, marker='.', fmt='r.', alpha=0.6, markersize=8, capsize=8,)

ax5.errorbar(x5_np_hast_ISO_GAUSS[true_mask], y5_np_hast_ISO_GAUSS[true_mask], xerr=x5_np_hast_ISO_GAUSS_err[true_mask], yerr=y5_np_hast_ISO_GAUSS_err[true_mask], marker='.', fmt='.', alpha=0.9, color="purple", markersize=8, capsize=8, label=None)
ax5.errorbar(x5_np_hast_ISO_GAUSS[possible_mask], y5_np_hast_ISO_GAUSS[possible_mask], xerr=x5_np_hast_ISO_GAUSS_err[possible_mask], yerr=y5_np_hast_ISO_GAUSS_err[possible_mask], marker='.', fmt='.', alpha=0.9, color="orange", markersize=8, capsize=8, label=None)
ax5.errorbar(x5_np_hast_ISO_GAUSS[likely_mask], y5_np_hast_ISO_GAUSS[likely_mask], xerr=x5_np_hast_ISO_GAUSS_err[likely_mask], yerr=y5_np_hast_ISO_GAUSS_err[likely_mask], marker='.', fmt='.', alpha=0.9, color="brown", markersize=8, capsize=8, label=None)

ax5.errorbar(x5_np_hast_ISO_GAUSS_s, y5_np_hast_ISO_GAUSS_s, xerr=x5_np_hast_ISO_GAUSS_err_s, yerr=y5_np_hast_ISO_GAUSS_err_s, marker='.', fmt='.', color="pink", markersize=8, capsize=8, label=None)


# Region where are located the PNe
result = findIntersection(8.0, 4.50, 0.8, 0.55, 0.0)
result_y = 8.0*result + 4.50

x_new = np.linspace(result, 15.5, 200)
x_new2 = np.linspace(-10.0, result, 200)
x_new3 = np.linspace(-10.0, 1.1, 200)
y =  8.0*x_new + 4.50
yy = 0.8*x_new2 + 0.55
#Mask
#mask = y >= result_y - 0.5
ax5.plot(x_new, y, color='k', linestyle='-')
ax5.plot(x_new2, yy , color='k', linestyle='-')

# Region of the simbiotic stars
result1 = findIntersection(-5.2, +10.60, 2.13, -1.43, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(result1, 15.5, 200)
y_s = -5.2*x_new_s + 10.60
yy_s = 2.13*x_new2_s - 1.43


ax5.plot(x_new_s, y_s, color='r', linestyle='--')
ax5.plot(x_new2_s, yy_s , color='r', linestyle='--')

source_label(ax5, "", x5_np_ISO_GAUSS_0, y5_np_ISO_GAUSS_0, dy=-4.5)
source_label(ax5, "PN Sp 4-1", x5_np_ISO_GAUSS_3, y5_np_ISO_GAUSS_3, dx=-50, dy=-4.5)
source_label(ax5, "[HLG90] 55", x5_np_ISO_GAUSS_1, y5_np_ISO_GAUSS_1, dx=-58, dy=-4.5)
source_label(ax5, "LEDA 101538", x5_np_ISO_GAUSS_2, y5_np_ISO_GAUSS_2, dx= -72, dy=-4.5)
source_label_hash(ax5, "TK 1", x5_np_hast_ISO_GAUSS, y5_np_hast_ISO_GAUSS, 6034, dy=-5)
source_label_hash(ax5, "Kn J1857.7+3931", x5_np_hast_ISO_GAUSS, y5_np_hast_ISO_GAUSS, 3014)#, dx=-85)
source_label_hash(ax5, "KnPa J1848.6+4151", x5_np_hast_ISO_GAUSS, y5_np_hast_ISO_GAUSS, 45492, dy=10)
source_label_hash(ax5, "Jacoby 1", x5_np_hast_ISO_GAUSS, y5_np_hast_ISO_GAUSS, 5598, dx=-46, dy=-5)
source_label_hash_s(ax5, "Fr 2-21", x5_np_hast_ISO_GAUSS_s, y5_np_hast_ISO_GAUSS_s, dx=-36, dy=8)


plt.text(0.05, 0.90, 'hPN zone',
         transform=ax5.transAxes, fontsize='x-large')

plt.text(0.55, 0.90, 'SySt Zone',
         transform=ax5.transAxes,color="red", fontsize='x-large')

ax5.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
#ax5.legend(scatterpoints=1, fontsize=15.0, loc='lower right', **lgd_kws)
ax5.grid()
#sns.despine(bottom=True)
plt.tight_layout()
pltfile = 'Fig6-IDR-JPLUS-gi_ISO_GAUSS.pdf'
file_save = os.path.join(save_path, pltfile)
plt.savefig(file_save)

