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
tab_np = Table.read("SPLUS_HYDRA_master_catalogue_iDR2_december_2019-aper-PN.tab", format="ascii.tab")
tab_np_petro = Table.read("SPLUS_HYDRA_master_catalogue_iDR2_december_2019-petro-PN.tab", format="ascii.tab")
#tab_np_hast_s = Table.read("../../../S-PLUS/math-splus-hash.tab", format="ascii.tab")
#Field and number of the objects
#number_np = tab_np['Number']

# number_sym = tab_sym['Id']
# Field_sym = tab_sym['Field']

#Calor Aper 3
#Color vironen
x_np_MAG_APER_3_0_0 = tab_np['r_aper'][0] - tab_np['i_aper'][0]
y_np_MAG_APER_3_0_0 = tab_np['r_aper'][0] - tab_np['F660_aper'][0]

#Color
x1_np_MAG_APER_3_0_0 = tab_np['F515_aper'][0] - tab_np['F861_aper'][0]
y1_np_MAG_APER_3_0_0 = tab_np['F515_aper'][0] - tab_np['F660_aper'][0]

#Color
x2_np_MAG_APER_3_0_0 = tab_np['z_aper'][0] - tab_np['g_aper'][0]
y2_np_MAG_APER_3_0_0 = tab_np['z_aper'][0] - tab_np['F660_aper'][0]

#Color
x3_np_MAG_APER_3_0_0 = tab_np['F660_aper'][0] - tab_np['r_aper'][0]
y3_np_MAG_APER_3_0_0 = tab_np['F660_aper'][0] - tab_np['g_aper'][0]

#Color
x4_np_MAG_APER_3_0_0 = tab_np['F660_aper'][0] - tab_np['r_aper'][0]
y4_np_MAG_APER_3_0_0 = tab_np['g_aper'][0] - tab_np['F515_aper'][0]
    
#Color
x5_np_MAG_APER_3_0_0 = tab_np['g_aper'][0] - tab_np['i_aper'][0]
y5_np_MAG_APER_3_0_0 = tab_np['F410_aper'][0] - tab_np['F660_aper'][0]

#Calor 
#Color vironen
x_np_MAG_APER_3_0_1 = tab_np['r_aper'][1] - tab_np['i_aper'][1]
y_np_MAG_APER_3_0_1 = tab_np['r_aper'][1] - tab_np['F660_aper'][1]

#Color
x1_np_MAG_APER_3_0_1 = tab_np['F515_aper'][1] - tab_np['F861_aper'][1]
y1_np_MAG_APER_3_0_1 = tab_np['F515_aper'][1] - tab_np['F660_aper'][1]

#Color
x2_np_MAG_APER_3_0_1 = tab_np['z_aper'][1] - tab_np['g_aper'][1]
y2_np_MAG_APER_3_0_1 = tab_np['z_aper'][1] - tab_np['F660_aper'][1]

#Color
x3_np_MAG_APER_3_0_1 = tab_np['F660_aper'][1] - tab_np['r_aper'][1]
y3_np_MAG_APER_3_0_1 = tab_np['F660_aper'][1] - tab_np['g_aper'][1]

#Color
x4_np_MAG_APER_3_0_1 = tab_np['F660_aper'][1] - tab_np['r_aper'][1]
y4_np_MAG_APER_3_0_1 = tab_np['g_aper'][1] - tab_np['F515_aper'][1]

    
#Color
x5_np_MAG_APER_3_0_1 = tab_np['g_aper'][1] - tab_np['i_aper'][1]
y5_np_MAG_APER_3_0_1 = tab_np['F410_aper'][1] - tab_np['F660_aper'][1]

#Calor 
#Color vironen
x_np_MAG_APER_3_0_1 = tab_np['r_aper'][1] - tab_np['i_aper'][1]
y_np_MAG_APER_3_0_1 = tab_np['r_aper'][1] - tab_np['F660_aper'][1]

#Color
x1_np_MAG_APER_3_0_1 = tab_np['F515_aper'][1] - tab_np['F861_aper'][1]
y1_np_MAG_APER_3_0_1 = tab_np['F515_aper'][1] - tab_np['F660_aper'][1]

#Color
x2_np_MAG_APER_3_0_1 = tab_np['z_aper'][1] - tab_np['g_aper'][1]
y2_np_MAG_APER_3_0_1 = tab_np['z_aper'][1] - tab_np['F660_aper'][1]

#Color
x3_np_MAG_APER_3_0_1 = tab_np['F660_aper'][1] - tab_np['r_aper'][1]
y3_np_MAG_APER_3_0_1 = tab_np['F660_aper'][1] - tab_np['g_aper'][1]

#Color
x4_np_MAG_APER_3_0_1 = tab_np['F660_aper'][1] - tab_np['r_aper'][1]
y4_np_MAG_APER_3_0_1 = tab_np['g_aper'][1] - tab_np['F515_aper'][1]

    
#Color
x5_np_MAG_APER_3_0_1 = tab_np['g_aper'][1] - tab_np['i_aper'][1]
y5_np_MAG_APER_3_0_1 = tab_np['F410_aper'][1] - tab_np['F660_aper'][1]

#Color vironen
x_np_MAG_APER_3_0_2 = tab_np['r_aper'][2] - tab_np['i_aper'][2]
y_np_MAG_APER_3_0_2 = tab_np['r_aper'][2] - tab_np['F660_aper'][2]

#Color
x1_np_MAG_APER_3_0_2 = tab_np['F515_aper'][2] - tab_np['F861_aper'][2]
y1_np_MAG_APER_3_0_2 = tab_np['F515_aper'][2] - tab_np['F660_aper'][2]

#Color
x2_np_MAG_APER_3_0_2 = tab_np['z_aper'][2] - tab_np['g_aper'][2]
y2_np_MAG_APER_3_0_2 = tab_np['z_aper'][2] - tab_np['F660_aper'][2]

#Color
x3_np_MAG_APER_3_0_2 = tab_np['F660_aper'][2] - tab_np['r_aper'][2]
y3_np_MAG_APER_3_0_2 = tab_np['F660_aper'][2] - tab_np['g_aper'][2]

#Color
x4_np_MAG_APER_3_0_2 = tab_np['F660_aper'][2] - tab_np['r_aper'][2]
y4_np_MAG_APER_3_0_2 = tab_np['g_aper'][2] - tab_np['F515_aper'][2]

    
#Color
x5_np_MAG_APER_3_0_2 = tab_np['g_aper'][2] - tab_np['i_aper'][2]
y5_np_MAG_APER_3_0_2 = tab_np['F410_aper'][2] - tab_np['F660_aper'][2]


#########################################################################
#Calor Petro#############################################################
#########################################################################

#Color vironen
x_np_MAG_APER_petro_0_0 = tab_np_petro['r_petro'][0] - tab_np_petro['i_petro'][0]
y_np_MAG_APER_petro_0_0 = tab_np_petro['r_petro'][0] - tab_np_petro['F660_petro'][0]

#Color
x1_np_MAG_APER_petro_0_0 = tab_np_petro['F515_petro'][0] - tab_np_petro['F861_petro'][0]
y1_np_MAG_APER_petro_0_0 = tab_np_petro['F515_petro'][0] - tab_np_petro['F660_petro'][0]

#Color
x2_np_MAG_APER_petro_0_0 = tab_np_petro['z_petro'][0] - tab_np_petro['g_petro'][0]
y2_np_MAG_APER_petro_0_0 = tab_np_petro['z_petro'][0] - tab_np_petro['F660_petro'][0]

#Color
x3_np_MAG_APER_petro_0_0 = tab_np_petro['F660_petro'][0] - tab_np_petro['r_petro'][0]
y3_np_MAG_APER_petro_0_0 = tab_np_petro['F660_petro'][0] - tab_np_petro['g_petro'][0]

#Color
x4_np_MAG_APER_petro_0_0 = tab_np_petro['F660_petro'][0] - tab_np_petro['r_petro'][0]
y4_np_MAG_APER_petro_0_0 = tab_np_petro['g_petro'][0] - tab_np_petro['F515_aper'][0]

    
#Color
x5_np_MAG_APER_petro_0_0 = tab_np_petro['g_petro'][0] - tab_np_petro['i_petro'][0]
y5_np_MAG_APER_petro_0_0 = tab_np_petro['F410_petro'][0] - tab_np_petro['F660_petro'][0]

#Calor 
#Color vironen
x_np_MAG_APER_petro_0_1 = tab_np_petro['r_petro'][1] - tab_np_petro['i_petro'][1]
y_np_MAG_APER_petro_0_1 = tab_np_petro['r_petro'][1] - tab_np_petro['F660_petro'][1]

#Color
x1_np_MAG_APER_petro_0_1 = tab_np_petro['F515_petro'][1] - tab_np_petro['F861_petro'][1]
y1_np_MAG_APER_petro_0_1 = tab_np_petro['F515_petro'][1] - tab_np_petro['F660_petro'][1]

#Color
x2_np_MAG_APER_petro_0_1 = tab_np_petro['z_petro'][1] - tab_np_petro['g_petro'][1]
y2_np_MAG_APER_petro_0_1 = tab_np_petro['z_petro'][1] - tab_np_petro['F660_petro'][1]

#Color
x3_np_MAG_APER_petro_0_1 = tab_np_petro['F660_petro'][1] - tab_np_petro['r_petro'][1]
y3_np_MAG_APER_petro_0_1 = tab_np_petro['F660_petro'][1] - tab_np_petro['g_petro'][1]

#Color
x4_np_MAG_APER_petro_0_1 = tab_np_petro['F660_petro'][1] - tab_np_petro['r_petro'][1]
y4_np_MAG_APER_petro_0_1 = tab_np_petro['g_petro'][1] - tab_np_petro['F515_petro'][1]

    
#Color
x5_np_MAG_APER_petro_0_1 = tab_np_petro['g_petro'][1] - tab_np_petro['i_petro'][1]
y5_np_MAG_APER_petro_0_1 = tab_np_petro['F410_petro'][1] - tab_np_petro['F660_petro'][1]


#Color vironen
x_np_MAG_APER_petro_0_1 = tab_np_petro['r_petro'][1] - tab_np_petro['i_petro'][1]
y_np_MAG_APER_petro_0_1 = tab_np_petro['r_petro'][1] - tab_np_petro['F660_petro'][1]

#Color
x1_np_MAG_APER_petro_0_1 = tab_np_petro['F515_petro'][1] - tab_np_petro['F861_petro'][1]
y1_np_MAG_APER_petro_0_1 = tab_np_petro['F515_petro'][1] - tab_np_petro['F660_petro'][1]

#Color
x2_np_MAG_APER_petro_0_1 = tab_np_petro['z_petro'][1] - tab_np_petro['g_petro'][1]
y2_np_MAG_APER_petro_0_1 = tab_np_petro['z_petro'][1] - tab_np_petro['F660_petro'][1]

#Color
x3_np_MAG_APER_petro_0_1 = tab_np_petro['F660_petro'][1] - tab_np_petro['r_petro'][1]
y3_np_MAG_APER_petro_0_1 = tab_np_petro['F660_petro'][1] - tab_np_petro['g_petro'][1]

#Color
x4_np_MAG_APER_petro_0_1 = tab_np_petro['F660_petro'][1] - tab_np_petro['r_petro'][1]
y4_np_MAG_APER_petro_0_1 = tab_np_petro['g_petro'][1] - tab_np_petro['F515_petro'][1]

    
#Color
x5_np_MAG_APER_petro_0_1 = tab_np_petro['g_petro'][1] - tab_np_petro['i_petro'][1]
y5_np_MAG_APER_petro_0_1 = tab_np_petro['F410_petro'][1] - tab_np_petro['F660_petro'][1]

#Calor
#Color vironen
x_np_MAG_APER_petro_0_2 = tab_np_petro['r_petro'][2] - tab_np_petro['i_petro'][2]
y_np_MAG_APER_petro_0_2 = tab_np_petro['r_petro'][2] - tab_np_petro['F660_petro'][2]

#Color
x1_np_MAG_APER_petro_0_2 = tab_np_petro['F515_petro'][2] - tab_np_petro['F861_petro'][2]
y1_np_MAG_APER_petro_0_2 = tab_np_petro['F515_petro'][2] - tab_np_petro['F660_petro'][2]

#Color
x2_np_MAG_APER_petro_0_2 = tab_np_petro['z_petro'][2] - tab_np_petro['g_petro'][2]
y2_np_MAG_APER_petro_0_2 = tab_np_petro['z_petro'][2] - tab_np_petro['F660_petro'][2]

#Color
x3_np_MAG_APER_petro_0_2 = tab_np_petro['F660_petro'][2] - tab_np_petro['r_petro'][2]
y3_np_MAG_APER_petro_0_2 = tab_np_petro['F660_petro'][2] - tab_np_petro['g_petro'][2]

#Color
x4_np_MAG_APER_petro_0_2 = tab_np_petro['F660_petro'][2] - tab_np_petro['r_petro'][2]
y4_np_MAG_APER_petro_0_2 = tab_np_petro['g_petro'][2] - tab_np_petro['F515_petro'][2]

    
#Color
x5_np_MAG_APER_petro_0_2 = tab_np_petro['g_petro'][2] - tab_np_petro['i_petro'][2]
y5_np_MAG_APER_petro_0_2 = tab_np_petro['F410_petro'][2] - tab_np_petro['F660_petro'][2]

#Calor
#Color vironen
x_np_MAG_APER_petro_0_3 = tab_np_petro['r_petro'][3] - tab_np_petro['i_petro'][3]
y_np_MAG_APER_petro_0_3 = tab_np_petro['r_petro'][3] - tab_np_petro['F660_petro'][3]

#Color
x1_np_MAG_APER_petro_0_3 = tab_np_petro['F515_petro'][3] - tab_np_petro['F861_petro'][3]
y1_np_MAG_APER_petro_0_3 = tab_np_petro['F515_petro'][3] - tab_np_petro['F660_petro'][3]

#Color
x2_np_MAG_APER_petro_0_3 = tab_np_petro['z_petro'][3] - tab_np_petro['g_petro'][3]
y2_np_MAG_APER_petro_0_3 = tab_np_petro['z_petro'][3] - tab_np_petro['F660_petro'][3]

#Color
x3_np_MAG_APER_petro_0_3 = tab_np_petro['F660_petro'][3] - tab_np_petro['r_petro'][3]
y3_np_MAG_APER_petro_0_3 = tab_np_petro['F660_petro'][3] - tab_np_petro['g_petro'][3]

#Color
x4_np_MAG_APER_petro_0_3 = tab_np_petro['F660_petro'][3] - tab_np_petro['r_petro'][3]
y4_np_MAG_APER_petro_0_3 = tab_np_petro['g_petro'][3] - tab_np_petro['F515_petro'][3]

    
#Color
x5_np_MAG_APER_petro_0_3 = tab_np_petro['g_petro'][3] - tab_np_petro['i_petro'][3]
y5_np_MAG_APER_petro_0_3 = tab_np_petro['F410_petro'][3] - tab_np_petro['F660_petro'][3]


##################################################################
##################################################################
#Cross macthing ith HASt#########################################
##################################################################
##################################################################
#Calor ISO GAUSS
#Color vironen
# x_np_hast_MAG_APER_6_0 = tab_np_hast['rSDSS_MAG_APER_6_0'] - tab_np_hast['iSDSS_MAG_APER_6_0']
# y_np_hast_MAG_APER_6_0 = tab_np_hast['rSDSS_MAG_APER_6_0'] - tab_np_hast['J0660_MAG_APER_6_0']

# #Color
# x1_np_hast_MAG_APER_6_0 = tab_np_hast['J0515_MAG_APER_6_0'] - tab_np_hast['J0861_MAG_APER_6_0']
# y1_np_hast_MAG_APER_6_0 = tab_np_hast['J0515_MAG_APER_6_0'] - tab_np_hast['J0660_MAG_APER_6_0']

# #Color
# x2_np_hast_MAG_APER_6_0 = tab_np_hast['zSDSS_MAG_APER_6_0'] - tab_np_hast['gSDSS_MAG_APER_6_0']
# y2_np_hast_MAG_APER_6_0 = tab_np_hast['zSDSS_MAG_APER_6_0'] - tab_np_hast['J0660_MAG_APER_6_0']

# #Color
# x3_np_hast_MAG_APER_6_0 = tab_np_hast['J0660_MAG_APER_6_0'] - tab_np_hast['rSDSS_MAG_APER_6_0']
# y3_np_hast_MAG_APER_6_0 = tab_np_hast['J0660_MAG_APER_6_0'] - tab_np_hast['gSDSS_MAG_APER_6_0']

# #Color
# x4_np_hast_MAG_APER_6_0 = tab_np_hast['J0660_MAG_APER_6_0'] - tab_np_hast['rSDSS_MAG_APER_6_0']
# y4_np_hast_MAG_APER_6_0 = tab_np_hast['gSDSS_MAG_APER_6_0'] - tab_np_hast['J0515_MAG_APER_6_0']

    
# #Color
# x5_np_hast_MAG_APER_6_0 = tab_np_hast['gSDSS_MAG_APER_6_0'] - tab_np_hast['iSDSS_MAG_APER_6_0']
# y5_np_hast_MAG_APER_6_0 = tab_np_hast['J0410_MAG_APER_6_0'] - tab_np_hast['J0660_MAG_APER_6_0']

# ##################################################################
# ##################################################################
# #Cross macthing ith HASt SPLUS#########################################
# ##################################################################
# ##################################################################
# #Calor ISO GAUSS
# #Color vironen
# x_np_hast_ISO_GAUSS_s = tab_np_hast_s['rSDSS_ISO_GAUSS'] - tab_np_hast_s['iSDSS_ISO_GAUSS']
# y_np_hast_ISO_GAUSS_s = tab_np_hast_s['rSDSS_ISO_GAUSS'] - tab_np_hast_s['J0660_ISO_GAUSS']

# #Color
# x1_np_hast_ISO_GAUSS_s = tab_np_hast_s['J0515_ISO_GAUSS'] - tab_np_hast_s['J0861_ISO_GAUSS']
# y1_np_hast_ISO_GAUSS_s = tab_np_hast_s['J0515_ISO_GAUSS'] - tab_np_hast_s['J0660_ISO_GAUSS']

# #Color
# x2_np_hast_ISO_GAUSS_s = tab_np_hast_s['zSDSS_ISO_GAUSS'] - tab_np_hast_s['gSDSS_ISO_GAUSS']
# y2_np_hast_ISO_GAUSS_s = tab_np_hast_s['zSDSS_ISO_GAUSS'] - tab_np_hast_s['J0660_ISO_GAUSS']

# #Color
# x3_np_hast_ISO_GAUSS_s = tab_np_hast_s['J0660_ISO_GAUSS'] - tab_np_hast_s['rSDSS_ISO_GAUSS']
# y3_np_hast_ISO_GAUSS_s = tab_np_hast_s['J0660_ISO_GAUSS'] - tab_np_hast_s['gSDSS_ISO_GAUSS']

# #Color
# x4_np_hast_ISO_GAUSS_s = tab_np_hast_s['J0660_ISO_GAUSS'] - tab_np_hast_s['rSDSS_ISO_GAUSS']
# y4_np_hast_ISO_GAUSS_s = tab_np_hast_s['gSDSS_ISO_GAUSS'] - tab_np_hast_s['J0515_ISO_GAUSS']

    
# #Color
# x5_np_hast_ISO_GAUSS_s = tab_np_hast_s['gSDSS_ISO_GAUSS'] - tab_np_hast_s['iSDSS_ISO_GAUSS']
# y5_np_hast_ISO_GAUSS_s = tab_np_hast_s['J0410_ISO_GAUSS'] - tab_np_hast_s['J0660_ISO_GAUSS']


#########################################################
#ERROR ##################################################
#########################################################
#Calor ISO GAUSS
#Color vironen
x_np_MAG_APER_3_0_0_err = np.sqrt(tab_np['er_aper'][0]**2 + tab_np['ei_aper'][0]**2)
y_np_MAG_APER_3_0_0_err = np.sqrt(tab_np['er_aper'][0]**2 + tab_np['eF660_aper'][0]**2)

#Color
x1_np_MAG_APER_3_0_0_err = np.sqrt(tab_np['eF515_aper'][0]**2 + float(tab_np['eF861_aper'][0])**2)
y1_np_MAG_APER_3_0_0_err = np.sqrt(tab_np['eF515_aper'][0]**2 + tab_np['eF660_aper'][0]**2)

#Color
x2_np_MAG_APER_3_0_0_err = np.sqrt(tab_np['ez_aper'][0]**2 + tab_np['eg_aper'][0]**2)
y2_np_MAG_APER_3_0_0_err = np.sqrt(tab_np['ez_aper'][0]**2 + tab_np['eF660_aper'][0]**2)

#Color
x3_np_MAG_APER_3_0_0_err = np.sqrt(tab_np['eF660_aper'][0]**2 + tab_np['er_aper'][0]**2)
y3_np_MAG_APER_3_0_0_err = np.sqrt(tab_np['eF660_aper'][0]**2 + tab_np['eg_aper'][0]**2)

#Color
x4_np_MAG_APER_3_0_0_err = np.sqrt(tab_np['eF660_aper'][0]**2 + tab_np['er_aper'][0]**2)
y4_np_MAG_APER_3_0_0_err = np.sqrt(tab_np['eg_aper'][0]**2 + tab_np['eF515_aper'][0]**2)

    
#Color
x5_np_MAG_APER_3_0_0_err = np.sqrt(tab_np['eg_aper'][0]**2 + tab_np['ei_aper'][0]**2)
y5_np_MAG_APER_3_0_0_err = np.sqrt(tab_np['F410_aper'][0]**2 + tab_np['eF660_aper'][0]**2)

#Calor ISO GAUSS
#Color vironen
x_np_MAG_APER_3_0_1_err = np.sqrt(tab_np['er_aper'][1]**2 + tab_np['ei_aper'][1]**2)
y_np_MAG_APER_3_0_1_err = np.sqrt(tab_np['er_aper'][1]**2 + tab_np['eF660_aper'][1]**2)

#Color
x1_np_MAG_APER_3_0_1_err = np.sqrt(tab_np['eF515_aper'][1]**2 + float(tab_np['eF861_aper'][1])**2)
y1_np_MAG_APER_3_0_1_err = np.sqrt(tab_np['eF515_aper'][1]**2 + tab_np['eF660_aper'][1]**2)

#Color
x2_np_MAG_APER_3_0_1_err = np.sqrt(tab_np['ez_aper'][1]**2 + tab_np['eg_aper'][1]**2)
y2_np_MAG_APER_3_0_1_err = np.sqrt(tab_np['ez_aper'][1]**2 + tab_np['eF660_aper'][1]**2)

#Color
x3_np_MAG_APER_3_0_1_err = np.sqrt(tab_np['eF660_aper'][1]**2 + tab_np['er_aper'][1]**2)
y3_np_MAG_APER_3_0_1_err = np.sqrt(tab_np['eF660_aper'][1]**2 + tab_np['eg_aper'][1]**2)

#Color
x4_np_MAG_APER_3_0_1_err = np.sqrt(tab_np['eF660_aper'][1]**2 + tab_np['er_aper'][1]**2)
y4_np_MAG_APER_3_0_1_err = np.sqrt(tab_np['eg_aper'][1]**2 + tab_np['eF515_aper'][1]**2)

    
#Color
x5_np_MAG_APER_3_0_1_err = np.sqrt(tab_np['eg_aper'][1]**2 + tab_np['ei_aper'][1]**2)
y5_np_MAG_APER_3_0_1_err = np.sqrt(tab_np['eF410_aper'][1]**2 + tab_np['eF660_aper'][1]**2)

#Calor ISO GAUSS
#Color vironen
x_np_MAG_APER_3_0_2_err = np.sqrt(tab_np['er_aper'][2]**2 + tab_np['ei_aper'][2]**2)
y_np_MAG_APER_3_0_2_err = np.sqrt(tab_np['er_aper'][2]**2 + tab_np['eF660_aper'][2]**2)

#Color
x1_np_MAG_APER_3_0_2_err = np.sqrt(tab_np['eF515_aper'][2]**2 + float(tab_np['eF861_aper'][2])**2)
y1_np_MAG_APER_3_0_2_err = np.sqrt(tab_np['eF515_aper'][2]**2 + tab_np['eF660_aper'][2]**2)

#Color
x2_np_MAG_APER_3_0_2_err = np.sqrt(tab_np['ez_aper'][2]**2 + tab_np['eg_aper'][2]**2)
y2_np_MAG_APER_3_0_2_err = np.sqrt(tab_np['ez_aper'][2]**2 + tab_np['eF660_aper'][2]**2)

#Color
x3_np_MAG_APER_3_0_2_err = np.sqrt(tab_np['eF660_aper'][2]**2 + tab_np['er_aper'][2]**2)
y3_np_MAG_APER_3_0_2_err = np.sqrt(tab_np['eF660_aper'][2]**2 + tab_np['eg_aper'][2]**2)

#Color
x4_np_MAG_APER_3_0_2_err = np.sqrt(tab_np['eF660_aper'][2]**2 + tab_np['er_aper'][2]**2)
y4_np_MAG_APER_3_0_2_err = np.sqrt(tab_np['eg_aper'][2]**2 + tab_np['eF515_aper'][2]**2)

    
#Color
x5_np_MAG_APER_3_0_2_err = np.sqrt(tab_np['eg_aper'][2]**2 + tab_np['ei_aper'][2]**2)
y5_np_MAG_APER_3_0_2_err = np.sqrt(tab_np['eF410_aper'][2]**2 + tab_np['eF660_aper'][2]**2)


##################################################################
##################################################################
#Cross macthing ith HASt#########################################
##################################################################
##################################################################
#Color vironen
# x_np_hast_MAG_APER_6_0_err = np.sqrt(tab_np_hast['rSDSS_MAG_APER_6_0_err']**2 + tab_np_hast['iSDSS_MAG_APER_6_0_err']**2)
# y_np_hast_MAG_APER_6_0_err = np.sqrt(tab_np_hast['rSDSS_MAG_APER_6_0_err']**2 + tab_np_hast['J0660_MAG_APER_6_0_err']**2)

# #Color
# x1_np_hast_MAG_APER_6_0_err =  np.sqrt(tab_np_hast['J0515_MAG_APER_6_0_err']**2 + 0.0**2)
# y1_np_hast_MAG_APER_6_0_err =  np.sqrt(tab_np_hast['J0515_MAG_APER_6_0_err']**2 + tab_np_hast['J0660_MAG_APER_6_0_err']**2)

# #Color
# x2_np_hast_MAG_APER_6_0_err =  np.sqrt(tab_np_hast['zSDSS_MAG_APER_6_0_err']**2 + tab_np_hast['gSDSS_MAG_APER_6_0_err']**2)
# y2_np_hast_MAG_APER_6_0_err =  np.sqrt(tab_np_hast['zSDSS_MAG_APER_6_0_err']**2 + tab_np_hast['J0660_MAG_APER_6_0_err']**2)

# #Color
# x3_np_hast_MAG_APER_6_0_err = np.sqrt(tab_np_hast['J0660_MAG_APER_6_0_err']**2 + tab_np_hast['rSDSS_MAG_APER_6_0_err']**2)
# y3_np_hast_MAG_APER_6_0_err = np.sqrt(tab_np_hast['J0660_MAG_APER_6_0_err']**2 + tab_np_hast['gSDSS_MAG_APER_6_0_err']**2)

# #Color
# x4_np_hast_MAG_APER_6_0_err = np.sqrt(tab_np_hast['J0660_MAG_APER_6_0_err']**2 + tab_np_hast['rSDSS_MAG_APER_6_0_err']**2)
# y4_np_hast_MAG_APER_6_0_err = np.sqrt(tab_np_hast['gSDSS_MAG_APER_6_0_err']**2 + tab_np_hast['J0515_MAG_APER_6_0_err']**2)

    
# #Color
# x5_np_hast_MAG_APER_6_0_err = np.sqrt(tab_np_hast['gSDSS_MAG_APER_6_0_err']**2 + tab_np_hast['iSDSS_MAG_APER_6_0_err']**2)
# y5_np_hast_MAG_APER_6_0_err = np.sqrt(tab_np_hast['J0410_MAG_APER_6_0_err']**2 + tab_np_hast['J0660_MAG_APER_6_0_err']**2)

# ##################################################################
# ##################################################################
# #Cross macthing ith HASt SPLUS#########################################
# ##################################################################
# ##################################################################
# #Color vironen
# x_np_hast_ISO_GAUSS_err_s = np.sqrt(tab_np_hast_s['rSDSS_ISO_GAUSS_err']**2 + tab_np_hast_s['iSDSS_ISO_GAUSS_err']**2)
# y_np_hast_ISO_GAUSS_err_s = np.sqrt(tab_np_hast_s['rSDSS_ISO_GAUSS_err']**2 + tab_np_hast_s['J0660_ISO_GAUSS_err']**2)

# #Color
# x1_np_hast_ISO_GAUSS_err_s =  np.sqrt(tab_np_hast_s['J0515_ISO_GAUSS_err']**2 + tab_np_hast_s['J0861_ISO_GAUSS_err']**2)
# y1_np_hast_ISO_GAUSS_err_s =  np.sqrt(tab_np_hast_s['J0515_ISO_GAUSS_err']**2 + tab_np_hast_s['J0660_ISO_GAUSS_err']**2)

# #Color
# x2_np_hast_ISO_GAUSS_err_s =  np.sqrt(tab_np_hast_s['zSDSS_ISO_GAUSS_err']**2 + tab_np_hast_s['gSDSS_ISO_GAUSS_err']**2)
# y2_np_hast_ISO_GAUSS_err_s =  np.sqrt(tab_np_hast_s['zSDSS_ISO_GAUSS_err']**2 + tab_np_hast_s['J0660_ISO_GAUSS_err']**2)

# #Color
# x3_np_hast_ISO_GAUSS_err_s = np.sqrt(tab_np_hast_s['J0660_ISO_GAUSS_err']**2 + tab_np_hast_s['rSDSS_ISO_GAUSS_err']**2)
# y3_np_hast_ISO_GAUSS_err_s = np.sqrt(tab_np_hast_s['J0660_ISO_GAUSS_err']**2 + tab_np_hast_s['gSDSS_ISO_GAUSS_err']**2)

# #Color
# x4_np_hast_ISO_GAUSS_err_s = np.sqrt(tab_np_hast_s['J0660_ISO_GAUSS_err']**2 + tab_np_hast_s['rSDSS_ISO_GAUSS_err']**2)
# y4_np_hast_ISO_GAUSS_err_s = np.sqrt(tab_np_hast_s['gSDSS_ISO_GAUSS_err']**2 + tab_np_hast_s['J0515_ISO_GAUSS_err']**2)

    
# #Color
# x5_np_hast_ISO_GAUSS_err_s = np.sqrt(tab_np_hast_s['gSDSS_ISO_GAUSS_err']**2 + tab_np_hast_s['iSDSS_ISO_GAUSS_err']**2)
# y5_np_hast_ISO_GAUSS_err_s = np.sqrt(tab_np_hast_s['J0410_ISO_GAUSS_err']**2 + tab_np_hast_s['J0660_ISO_GAUSS_err']**2)

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


# true_mask = tab_np_hast['Number'] == 5598
# possible_mask = (tab_np_hast['Number'] != 5598) & (tab_np_hast['Number'] != 6034)
# likely_mask = tab_np_hast['Number'] == 6034


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
ax.set_ylim(ymin=-2.4,ymax=2.8)
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.xlabel('$r - i$', size =22)
plt.ylabel('$r - J0660$', size =22)
ax.scatter(x_np_MAG_APER_3_0_0, y_np_MAG_APER_3_0_0, c=sns.xkcd_rgb['true blue'], alpha=0.5, marker ='o', s=80,  zorder=211.0, label='PN candidate')
ax.scatter(x_np_MAG_APER_3_0_1, y_np_MAG_APER_3_0_1, c=sns.xkcd_rgb['true blue'], alpha=0.5, marker ='o', s=80, zorder=100.0)
ax.scatter(x_np_MAG_APER_3_0_2, y_np_MAG_APER_3_0_2, c=sns.xkcd_rgb['true blue'], alpha=0.5, marker ='o', s=80,  zorder=10.0)#, label='J-PLUS Blue compact galaxy')

ax.scatter(x_np_MAG_APER_petro_0_0, y_np_MAG_APER_petro_0_0, c=sns.xkcd_rgb['true blue'], alpha=0.9, marker ='o', s=80,  zorder=211.0, label='PN candidate')
ax.scatter(x_np_MAG_APER_petro_0_1, y_np_MAG_APER_petro_0_1, c=sns.xkcd_rgb['grey green'], alpha=0.9, marker ='o', s=80, zorder=100.0, label='Known PNe')
ax.scatter(x_np_MAG_APER_petro_0_2, y_np_MAG_APER_petro_0_2, c=sns.xkcd_rgb['grey green'], alpha=0.9, marker ='o', s=80,  zorder=10.0)#, label='J-PLUS Blue compact galaxy')
ax.scatter(x_np_MAG_APER_petro_0_3, y_np_MAG_APER_petro_0_3, c=sns.xkcd_rgb['light blue'], alpha=0.9, marker ='o', s=80, zorder=10.0, label='Promising PN')


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

# ax.plot(x_new_s, y_s, color='r', linestyle='--')
# ax.plot(x_new2_s, yy_s , color='r', linestyle='--')


plt.text(0.05, 0.92, 'hPN zone',
         transform=ax.transAxes, fontsize=22)
ax.minorticks_on()

# plt.text(0.56, 0.92, 'SySt Zone',
#          transform=ax.transAxes, color="red", fontsize=22)
# ax.minorticks_on()

#ax1.grid(which='minor')#, lw=0.3)
ax.legend(scatterpoints=1, ncol=2, fontsize=12.3, loc="lower right", **lgd_kws)
#ax.grid()
#sns.despine(bottom=True)
plt.tight_layout()
pltfile = 'Fig1-IDR2-SPLUS-vironen.pdf'
# save_path = '../../../../../Dropbox/paper-pne/Fig/'
# file_save = os.path.join(save_path, pltfile)
plt.savefig(pltfile)

'''
J0515 - J0861 vs J0515 - J0660
'''
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax1 = fig.add_subplot(111)
ax1.set_xlim(xmin=-5.8,xmax=6.4)
ax1.set_ylim(ymin=-4.5,ymax=5.7)
plt.tick_params(axis='x', labelsize=25)
plt.tick_params(axis='y', labelsize=25)
plt.xlabel('$J0515 - J0861$', size = 35)
plt.ylabel('$J0515 - J0660$', size = 35)
ax1.scatter(x1_np_MAG_APER_3_0_0, y1_np_MAG_APER_3_0_0, c=sns.xkcd_rgb['true blue'], alpha=0.5, marker ='o', s=80,  zorder=211.0, label='PN candidate')
ax1.scatter(x1_np_MAG_APER_3_0_1, y1_np_MAG_APER_3_0_1, c=sns.xkcd_rgb['true blue'], alpha=0.5, marker ='o', s=80, zorder=100.0)
ax1.scatter(x1_np_MAG_APER_3_0_2, y1_np_MAG_APER_3_0_2, c=sns.xkcd_rgb['true blue'], alpha=0.5, marker ='o', s=80,  zorder=10.0)#, label='J-PLUS Blue compact galaxy')

ax1.scatter(x1_np_MAG_APER_petro_0_0, y1_np_MAG_APER_petro_0_0, c=sns.xkcd_rgb['true blue'], alpha=0.9, marker ='o', s=80,  zorder=211.0, label='PN candidate')
ax1.scatter(x1_np_MAG_APER_petro_0_1, y1_np_MAG_APER_petro_0_1, c=sns.xkcd_rgb['grey green'], alpha=0.9, marker ='o', s=80, zorder=100.0, label='Known PNe')
ax1.scatter(x1_np_MAG_APER_petro_0_2, y1_np_MAG_APER_petro_0_2, c=sns.xkcd_rgb['grey green'], alpha=0.9, marker ='o', s=80,  zorder=10.0)#, label='J-PLUS Blue compact galaxy')
ax1.scatter(x1_np_MAG_APER_petro_0_3, y1_np_MAG_APER_petro_0_3, c=sns.xkcd_rgb['light blue'], alpha=0.9, marker ='o', s=80, zorder=10.0, label='Promising PN')

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

# source_label(ax1, "", x1_np_MAG_APER_6_0_0, y1_np_MAG_APER_6_0_0, dx=-45)
# source_label(ax1, "LEDA 2790884", x1_np_MAG_APER_6_0_3, y1_np_MAG_APER_6_0_3, dx=8)
# source_label(ax1, "LEDA 101538", x1_np_MAG_APER_6_0_1, y1_np_MAG_APER_6_0_1, dx=-72)
# source_label(ax1, "PN Sp 4-1", x1_np_MAG_APER_6_0_2, y1_np_MAG_APER_6_0_2, dx=-50)
# source_label_hash(ax1, "TK 1", x1_np_hast_MAG_APER_6_0, y1_np_hast_MAG_APER_6_0, 6034, dx=4, dy=-10)
# source_label_hash(ax1, "Kn J1857.7+3931", x1_np_hast_MAG_APER_6_0, y1_np_hast_MAG_APER_6_0, 3014, dx=-50, dy=13)
# source_label_hash(ax1, "KnPa J1848.6+4151", x1_np_hast_MAG_APER_6_0, y1_np_hast_MAG_APER_6_0, 45492, dy=10)
# source_label_hash(ax1, "Jacoby 1", x1_np_hast_MAG_APER_6_0, y1_np_hast_MAG_APER_6_0, 5598, dx=-42, dy=6)
# source_label_hash_s(ax1, "Fr 2-21", x1_np_hast_ISO_GAUSS_s, y1_np_hast_ISO_GAUSS_s, dx=-36, dy=-7)

plt.text(0.05, 0.91, 'hPN zone',
         transform=ax1.transAxes, fontsize=22)
# plt.text(0.56, 0.91, 'SySt Zone',
#          transform=ax1.transAxes, color="red", fontsize=22)
# ax1.minorticks_on()

ax1.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax1.legend(scatterpoints=1, ncol=2, fontsize=12.3, loc="lower right", **lgd_kws)
#ax1.grid()
plt.tight_layout()
pltfile = 'Fig2-IDR2-SPLUS-J0515_J0660.pdf'
#save_path = '../../../../../Dropbox/JPAS/paper-phot/'
#file_save = os.path.join(save_path, pltfile)
plt.savefig(pltfile)

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
ax2.set_ylim(ymin=-5.,ymax=5.0)
plt.tick_params(axis='x', labelsize=25)
plt.tick_params(axis='y', labelsize=25)
plt.xlabel('$z - g$', size =35)
plt.ylabel('$z - J0660$', size =35)
ax2.scatter(x2_np_MAG_APER_3_0_0, y2_np_MAG_APER_3_0_0, c=sns.xkcd_rgb['true blue'], alpha=0.5, marker ='o', s=80,  zorder=211.0, label='PN candidate')
ax2.scatter(x2_np_MAG_APER_3_0_1, y2_np_MAG_APER_3_0_1, c=sns.xkcd_rgb['true blue'], alpha=0.5, marker ='o', s=80, zorder=100.0)
ax2.scatter(x2_np_MAG_APER_3_0_2, y2_np_MAG_APER_3_0_2, c=sns.xkcd_rgb['true blue'], alpha=0.5, marker ='o', s=80,  zorder=10.0)#, label='J-PLUS Blue compact galaxy')

ax2.scatter(x2_np_MAG_APER_petro_0_0, y2_np_MAG_APER_petro_0_0, c=sns.xkcd_rgb['true blue'], alpha=0.9, marker ='o', s=80,  zorder=211.0, label='PN candidate')
ax2.scatter(x2_np_MAG_APER_petro_0_1, y2_np_MAG_APER_petro_0_1, c=sns.xkcd_rgb['grey green'], alpha=0.9, marker ='o', s=80, zorder=100.0, label='Known PNe')
ax2.scatter(x2_np_MAG_APER_petro_0_2, y2_np_MAG_APER_petro_0_2, c=sns.xkcd_rgb['grey green'], alpha=0.9, marker ='o', s=80,  zorder=10.0)#, label='J-PLUS Blue compact galaxy')
ax2.scatter(x2_np_MAG_APER_petro_0_3, y2_np_MAG_APER_petro_0_3, c=sns.xkcd_rgb['light blue'], alpha=0.9, marker ='o', s=80, zorder=10.0, label='Promising PN')

result = findIntersection(0.35, 0.82, -0.8, 1.8, 0.0)
result_y = 0.2319*result + 0.85

x_new = np.linspace(result, 15.5, 200)
x_new2 = np.linspace(-10.0, result, 200)

y = 0.35*x_new + 0.82
yy = -0.8*x_new2 +  1.8
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
# ax2.plot(x_new_s, y_s, color='r', linestyle='--')
# ax2.plot(x_new2_s, yy_s , color='r', linestyle='--')

# source_label(ax2, "", x2_np_MAG_APER_6_0_0, y2_np_MAG_APER_6_0_0, dx=-42)
# source_label(ax2, "LEDA 2790884", x2_np_MAG_APER_6_0_3, y2_np_MAG_APER_6_0_3, dx=-75, dy=7)
# source_label(ax2, "LEDA 101538", x2_np_MAG_APER_6_0_1, y2_np_MAG_APER_6_0_1, dy=-8)
# source_label(ax2, "PN Sp 4-1", x2_np_MAG_APER_6_0_2, y2_np_MAG_APER_6_0_2, dx=7, dy=-5)
# source_label_hash(ax2, "TK 1", x2_np_hast_MAG_APER_6_0, y2_np_hast_MAG_APER_6_0, 6034)
# source_label_hash(ax2, "Kn J1857.7+3931", x2_np_hast_MAG_APER_6_0, y2_np_hast_MAG_APER_6_0, 3014, dx=-85, dy=-5)#, dx=-85, dy=5)
# source_label_hash(ax2, "KnPa J1848.6+4151", x2_np_hast_MAG_APER_6_0, y2_np_hast_MAG_APER_6_0, 45492, dy=-10)
# source_label_hash(ax2, "Jacoby 1", x2_np_hast_MAG_APER_6_0, y2_np_hast_MAG_APER_6_0, 5598, dx=4, dy=-10)#, dx=-45, dy=-5)
# source_label_hash_s(ax2, "Fr 2-21", x2_np_hast_ISO_GAUSS_s, y2_np_hast_ISO_GAUSS_s, dx=-36, dy=7) 

plt.text(0.58, 0.92, 'hPN zone',
         transform=ax2.transAxes, fontsize=22)
# plt.text(0.03, 0.7, 'SySt Zone',
#          transform=ax2.transAxes, color="red", fontsize=22)
# ax2.minorticks_on()

ax2.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
#ax2.legend(scatterpoints=1, ncol=2, fontsize=12.3, loc="lower right", **lgd_kws)
#ax2.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.tight_layout()
pltfile = 'Fig3-IDR2-SPLUS-z.pdf'
#file_save = os.path.join(save_path, pltfile)
plt.savefig(pltfile)
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
plt.tick_params(axis='x', labelsize=25)
plt.tick_params(axis='y', labelsize=25)
plt.xlabel('$J0660 - r$', size =35)
plt.ylabel('$J0660 - gSDSS$', size =35)

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


plt.text(0.05, 0.90, 'hPN zone',
         transform=ax3.transAxes, fontsize=28)

ax3.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax3.legend(scatterpoints=1, ncol=2, fontsize=12.3, **lgd_kws)
#ax3.grid()
#sns.despine(bottom=True)
plt.tight_layout()
#pltfile = 'Fig4-IDR-JPLUS-g_MAG_APER_6_0.pdf'
# file_save = os.path.join(save_path, pltfile)
# plt.savefig(file_save)
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
plt.tick_params(axis='x', labelsize=25)
plt.tick_params(axis='y', labelsize=25)
plt.xlabel('$J0660 - r$', size =35)
plt.ylabel('$g - J0515$', size =35)
ax4.scatter(x4_np_MAG_APER_3_0_0, y4_np_MAG_APER_3_0_0, c=sns.xkcd_rgb['true blue'], alpha=0.5, marker ='o', s=80,  zorder=211.0, label='PN candidate')
ax4.scatter(x4_np_MAG_APER_3_0_1, y4_np_MAG_APER_3_0_1, c=sns.xkcd_rgb['true blue'], alpha=0.5, marker ='o', s=80, zorder=100.0)
ax4.scatter(x4_np_MAG_APER_3_0_2, y4_np_MAG_APER_3_0_2, c=sns.xkcd_rgb['true blue'], alpha=0.5, marker ='o', s=80,  zorder=10.0)#, label='J-PLUS Blue compact galaxy')

ax4.scatter(x4_np_MAG_APER_petro_0_0, y4_np_MAG_APER_petro_0_0, c=sns.xkcd_rgb['true blue'], alpha=0.9, marker ='o', s=80,  zorder=211.0, label='PN candidate')
ax4.scatter(x4_np_MAG_APER_petro_0_1, y4_np_MAG_APER_petro_0_1, c=sns.xkcd_rgb['grey green'], alpha=0.9, marker ='o', s=80, zorder=100.0, label='Known PNe')
ax4.scatter(x4_np_MAG_APER_petro_0_2, y4_np_MAG_APER_petro_0_2, c=sns.xkcd_rgb['grey green'], alpha=0.9, marker ='o', s=80,  zorder=10.0)#, label='J-PLUS Blue compact galaxy')
ax4.scatter(x4_np_MAG_APER_petro_0_3, y4_np_MAG_APER_petro_0_3, c=sns.xkcd_rgb['light blue'], alpha=0.9, marker ='o', s=80, zorder=10.0, label='Promising PN')

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



plt.text(0.05, 0.1, 'hPN zone',
         transform=ax4.transAxes, fontsize=22)
plt.text(0.05, 0.92, 'SySt Zone',
         transform=ax4.transAxes, color="red", fontsize=22)
# ax4.minorticks_on()

ax4.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
#ax4.legend(scatterpoints=1, fontsize=15.0, loc="lower right", **lgd_kws)
#ax4.grid()
#sns.despine(bottom=True)
plt.tight_layout()
pltfile = 'Fig5-IDR2-SPLUS-g.pdf'
#file_save = os.path.join(save_path, pltfile)
plt.savefig(pltfile)
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

plt.tick_params(axis='x', labelsize=25)
plt.tick_params(axis='y', labelsize=25)
plt.xlabel('$g - i$', size=35)
plt.ylabel('$J0410 - J0660$', size =35)
ax5.scatter(x5_np_MAG_APER_3_0_0, y5_np_MAG_APER_3_0_0, c=sns.xkcd_rgb['true blue'], alpha=0.5, marker ='o', s=80,  zorder=211.0, label='PN candidate')
ax5.scatter(x5_np_MAG_APER_3_0_1, y5_np_MAG_APER_3_0_1, c=sns.xkcd_rgb['true blue'], alpha=0.5, marker ='o', s=80, zorder=100.0)
ax5.scatter(x5_np_MAG_APER_3_0_2, y5_np_MAG_APER_3_0_2, c=sns.xkcd_rgb['true blue'], alpha=0.5, marker ='o', s=80,  zorder=10.0)#, label='J-PLUS Blue compact galaxy')

ax5.scatter(x5_np_MAG_APER_petro_0_0, y5_np_MAG_APER_petro_0_0, c=sns.xkcd_rgb['true blue'], alpha=0.9, marker ='o', s=80,  zorder=211.0, label='PN candidate')
ax5.scatter(x5_np_MAG_APER_petro_0_1, y5_np_MAG_APER_petro_0_1, c=sns.xkcd_rgb['grey green'], alpha=0.9, marker ='o', s=80, zorder=100.0, label='Known PNe')
ax5.scatter(x5_np_MAG_APER_petro_0_2, y5_np_MAG_APER_petro_0_2, c=sns.xkcd_rgb['grey green'], alpha=0.9, marker ='o', s=80,  zorder=10.0)#, label='J-PLUS Blue compact galaxy')
ax5.scatter(x5_np_MAG_APER_petro_0_3, y5_np_MAG_APER_petro_0_3, c=sns.xkcd_rgb['light blue'], alpha=0.9, marker ='o', s=80, zorder=10.0, label='Promising PN')


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

# source_label(ax5, "", x5_np_MAG_APER_6_0_0, y5_np_MAG_APER_6_0_0, dy=-4.5)
# source_label(ax5, "LEDA 2790884", x5_np_MAG_APER_6_0_3, y5_np_MAG_APER_6_0_3, dx=10, dy=-4.5)
# source_label(ax5, "LEDA 101538", x5_np_MAG_APER_6_0_1, y5_np_MAG_APER_6_0_1, dx=-65, dy=-4.5)
# source_label(ax5, "PN Sp 4-1", x5_np_MAG_APER_6_0_2, y5_np_MAG_APER_6_0_2, dx= -50, dy=-4.5)
# source_label_hash(ax5, "TK 1", x5_np_hast_MAG_APER_6_0, y5_np_hast_MAG_APER_6_0, 6034, dy=-5)
# source_label_hash(ax5, "Kn J1857.7+3931", x5_np_hast_MAG_APER_6_0, y5_np_hast_MAG_APER_6_0, 3014)#, dx=-85)
# source_label_hash(ax5, "KnPa J1848.6+4151", x5_np_hast_MAG_APER_6_0, y5_np_hast_MAG_APER_6_0, 45492, dy=10)
# source_label_hash(ax5, "Jacoby 1", x5_np_hast_MAG_APER_6_0, y5_np_hast_MAG_APER_6_0, 5598, dx=-46, dy=-5)
# source_label_hash_s(ax5, "Fr 2-21", x5_np_hast_ISO_GAUSS_s, y5_np_hast_ISO_GAUSS_s, dx=-36, dy=8)

plt.text(0.03, 0.90, 'hPN zone',
         transform=ax5.transAxes, fontsize=22)

# plt.text(0.5, 0.93, 'SySt Zone',
#          transform=ax5.transAxes,color="red", fontsize=22)

ax5.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
#ax5.legend(scatterpoints=1, fontsize=15.0, loc='lower right', **lgd_kws)
#ax5.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.tight_layout()
pltfile = 'Fig6-IDR2-SPLUS-gi.pdf'
#file_save = os.path.join(save_path, pltfile)
plt.savefig(pltfile)
