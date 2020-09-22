'''
Read the table from SPLUS EDR Juny18 table to find PNe
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


tab = Table.read("SPLUS_STRIPE82-catalogue_edr_march2018.tab", format="ascii.tab")

shape = (len(tab['Id']), )
x = np.linspace(-10.0, 15.5, len(tab['Id']))
X = np.array(x).reshape(shape)

#filer deep splus mask
f = tab['U_petro'] <= 21.6
f1 = tab['F0378_petro'] <= 21.5
f2 = tab['F0395_petro'] < 21.4
f3 = tab['F0410_petro'] <= 21.5
f4 = tab['F0430_petro'] < 21.4
f5 = tab['G_petro'] <= 22.2
f6 = tab['J0515_petro'] <= 21.4
f7 = tab['R_petro'] <= 21.9
f8 = tab['F0660_petro'] <= 21.3
f9 = tab['I_petro'] <= 20.8
f10 = tab['F0861_petro'] <= 20.8
f11 = tab['Z_petro'] <= 20.5

mask = f & f1 & f2 & f3 & f5 & f6 & f7 & f8 & f9 & f10 & f11

#Mask
#Mask filters
q = (tab['F0515_petro'] - tab['F0660_petro']) <= 5.0
#q1 = (tab['J0515'] - tab['J0861']) >= -3.0
q2 = (tab['R_petro'] - tab['F0660_petro']) <= 4.0
q3 = (tab['R_petro'] - tab['I_petro']) >= -4.0
q4 = (tab['G_petro'] - tab['F0515_petro']) >= -3.2
q5 = (tab['G_petro'] - tab['I_petro']) >= -3.0
q6 = (tab['F0410_petro'] - tab['F0660_petro']) <= 6.0
q7 = (tab['Z_petro'] - tab['G_petro']) <= 4.0

mask1 = q  & q2 & q3 & q4 & q5 & q6 & q7
#Mask
Y = 2.7*(tab['F0515_petro'] - tab['F0861_petro']) + 2.15
Y1 = 0.2319*(tab['Z_petro'] - tab['G_petro']) + 0.85
Y2 = -1.3*(tab['Z_petro'] - tab['G_petro']) + 1.7
Y3 = 1.559*(tab['F0660_petro'] - tab['R_petro']) + 0.58
Y4 = 0.12*(tab['F0660_petro'] - tab['R_petro']) - 0.01
Y44 = -1.1*(tab['F0660_petro'] - tab['R_petro']) - 1.07
Y5 = 8.0*(tab['G_petro'] - tab['I_petro']) + 4.5
Y6 = 0.8*(tab['G_petro'] - tab['I_petro']) + 0.55
Y7 = 0.43*(tab['R_petro'] - tab['I_petro']) + 0.65
Y8 = -6.8*(tab['R_petro'] - tab['I_petro']) - 1.3

m = tab['Class star'] > 0.0 
m1 = tab['F0660_petro'] - tab['R_petro']<=-1.0 
m2 = tab['F0515_petro'] - tab['F0660_petro']>=0.3
m3 = tab['Z_petro'] - tab['F0660_petro']>=Y1
m4 = tab['Z_petro'] - tab['F0660_petro']>=Y2
m5 = tab['F0515_petro'] - tab['F0660_petro']>=Y
m6 = tab['F0660_petro'] - tab['G_petro']>=Y3
m7 = tab['G_petro'] - tab['F0515_petro']<=Y4
m8 = tab['G_petro'] - tab['F0515_petro']<=Y44
m9 = tab['F0410_petro'] - tab['F0660_petro']>=Y5
m10 = tab['F0410_petro'] - tab['F0660_petro']>=Y6
m11 = (tab['R_petro'] - tab['F0660_petro']) >= Y7
m12 = (tab['R_petro'] - tab['F0660_petro']) <= Y8
total_m =m & m1 & m2 & m3 & m4 & m5 & m6 & m7 & m8 & m9 & m10 & m11 & m12 & mask & mask1

#Writting the table with the PN cantidates
table = Table([tab['Field_ID'][total_m], tab['RA'][total_m], tab['Dec'][total_m],tab['X'][total_m],tab['Y'][total_m], tab['Aperture'][total_m], tab['s2nDet'][total_m], tab['PhotoFlag'][total_m],tab['FWHM'][total_m],tab['MUMAX'][total_m],tab['A'][total_m], tab['B'][total_m],tab['THETA'][total_m], tab['FlRadDet'][total_m], tab['KrRadDet'][total_m], tab['U_auto'][total_m], tab['dU_auto'][total_m], tab['s2n_U_auto'][total_m], tab['U_petro'][total_m], tab['dU_petro'][total_m], tab['s2n_U_petro '][total_m], tab['U_aper'][total_m], tab['DU_aper'][total_m], tab['S2n_U_aper'][total_m], tab['F0378_auto'][total_m],tab['dF0378_auto'][total_m], tab['s2n_F0378_auto'][total_m], tab['F0378_petro'][total_m], tab['dF0378_petro'][total_m], tab['s2n_F0378_petro'][total_m], tab['F0378_aper'][total_m], tab['dF0378_aper'][total_m], tab['s2n_F0378_aper'][total_m], tab['F0395_auto'][total_m], tab['dF0395_auto'][total_m], tab['s2n_F0395_auto'][total_m], tab['F0395_petro'][total_m], tab['dF0395_petro'][total_m], tab['s2n_F0395_petro'][total_m], tab['F0395_aper'][total_m], tab['dF0395_aper'][total_m], tab['s2n_F0395_aper'][total_m], tab['F0410_auto'][total_m], tab['dF0410_auto'][total_m], tab['s2n_F0410_auto'][total_m], tab['F0410_petro'][total_m], tab['dF0410_petro'][total_m], tab['s2n_F0410_petro'][total_m], tab['F0410_aper'][total_m], tab['dF0410_aper'][total_m], tab['s2n_F0410_aper'][total_m], tab['F0430_auto'][total_m], tab['dF0430_auto'][total_m], tab['s2n_F0430_auto'][total_m], tab['F0430_petro'][total_m], tab['dF0430_petro'][total_m], tab['s2n_F0430_petro'][total_m], tab['F0430_aper'][total_m],tab['dF0430_aper'][total_m], tab['s2n_F0430_aper'][total_m], tab['G_auto'][total_m], tab['dG_auto'][total_m], tab['s2n_G_auto'][total_m], tab['G_petro'][total_m], tab['dG_petro'][total_m], tab['s2n_G_petro'][total_m], tab['G_aper'][total_m], tab['dG_aper'][total_m], tab['s2n_G_aper'][total_m], tab['F0515_auto'][total_m], tab['dF0515_auto'][total_m], tab['s2n_F0515_auto'][total_m], tab['F0515_petro'][total_m], tab['dF0515_petro'][total_m], tab['s2n_F0515_petro'][total_m], tab['F0515_aper'][total_m], tab['dF0515_aper'][total_m], tab[' s2n_F0515_aper'][total_m], tab['R_auto'][total_m], tab['dR_auto'][total_m], tab['s2n_R_auto'][total_m], tab['R_petro'][total_m], tab['dR_petro'][total_m], tab['s2n_R_petro'][total_m], tab['R_aper'][total_m], tab['dR_aper'][total_m], tab['s2n_R_aper'][total_m], tab['F0660_auto'][total_m], tab['dF0660_auto'][total_m], tab['s2n_F0660_auto'][total_m], tab['F0660_petro'][total_m], tab['dF0660_petro'][total_m], tab['s2n_F0660_petro'][total_m], tab['F0660_aper'][total_m], tab['dF0660_aper'][total_m], tab['s2n_F0660_aper'][total_m], tab['I_auto'][total_m], tab['dI_auto'][total_m], tab['s2n_I_auto'][total_m], tab['I_petro'][total_m], tab['dI_petro'][total_m],tab['s2n_I_petro'][total_m],tab['I_aper'][total_m],tab['dI_aper'][total_m],tab['s2n_I_aper'][total_m],tab['F0861_auto'][total_m],tab['dF0861_auto'][total_m],tab['s2n_F0861_auto'][total_m],tab['F0861_petro'][total_m], tab['dF0861_petro'][total_m], tab['s2n_F0861_petro'][total_m], tab['F0861_aper'][total_m], tab['dF0861_aper'][total_m], tab['s2n_F0861_aper'][total_m], tab['Z_auto'][total_m], tab['dZ_auto'][total_m], tab['s2n_Z_auto'][total_m], tab['Z_petro'][total_m], tab['dZ_petro'][total_m], tab['s2n_Z_petro'][total_m], tab['Z_aper'][total_m], tab['dZ_aper'][total_m], tab['s2n_Z_aper'][total_m], tab['zb'][total_m], tab['zb_Min'][total_m], tab['zb_Max'][total_m], tab['Tb'][total_m], tab['Odds'][total_m], tab['Chi2'][total_m], tab['M_B'][total_m], tab['Stell_Mass'][total_m], tab['CLASS'][total_m], tab['PROB_GAL'][total_m], tab['PROB_STAR'][total_m]],  names=('Field_ID', 'RA', 'Dec', 'X', 'Y', 'Aperture', 's2nDet', 'PhotoFlag', 'FWHM','MUMAX', 'A', 'B','THETA','FlRadDet','KrRadDet','U_auto','dU_auto', 's2n_U_auto', 'U_petro', 'dU_petro', 's2n_U_petro ', 'U_aper', 'DU_aper', 'S2n_U_aper', 'F0378_auto', 'dF0378_auto', 's2n_F0378_auto', 'F0378_petro', 'dF0378_petro', 's2n_F0378_petro', 'F0378_aper', 'dF0378_aper', 's2n_F0378_aper', 'F0395_auto','dF0395_auto', 's2n_F0395_auto', 'F0395_petro', 'dF0395_petro','s2n_F0395_petro', 'F0395_aper','dF0395_aper','s2n_F0395_aper','F0410_auto','dF0410_auto', 's2n_F0410_auto', 'F0410_petro', 'dF0410_petro', 's2n_F0410_petro', 'F0410_aper', 'dF0410_aper', 's2n_F0410_aper', 'F0430_auto', 'dF0430_auto','s2n_F0430_auto','F0430_petro','dF0430_petro', 's2n_F0430_petro', 'F0430_aper', 'dF0430_aper', 's2n_F0430_aper','G_auto','dG_auto','s2n_G_auto', 'G_petro', 'dG_petro', 's2n_G_petro', 'G_aper', 'dG_aper', 's2n_G_aper', 'F0515_auto', 'dF0515_auto', 's2n_F0515_auto', 'F0515_petro','dF0515_petro','s2n_F0515_petro','F0515_aper','dF0515_aper', 's2n_F0515_aper','R_auto','dR_auto','s2n_R_auto','R_petro','dR_petro','s2n_R_petro', 'R_aper', 'dR_aper', 's2n_R_aper', 'F0660_auto', 'dF0660_auto', 's2n_F0660_auto', 'F0660_petro', 'dF0660_petro', 's2n_F0660_petro','F0660_aper', 'dF0660_aper', 's2n_F0660_aper', 'I_auto','dI_auto','s2n_I_auto','I_petro', 'dI_petro','s2n_I_petro','I_aper','dI_aper', 's2n_I_aper', 'F0861_auto', 'dF0861_auto','s2n_F0861_auto', 'F0861_petro', 'dF0861_petro', 's2n_F0861_petro', 'F0861_aper', 'dF0861_aper', 's2n_F0861_aper', 'Z_auto', 'dZ_auto', 's2n_Z_auto', 'Z_petro','dZ_petro', 's2n_Z_petro', 'Z_aper', 'dZ_aper', 's2n_Z_aper', 'zb', 'zb_Min','zb_Max', 'Tb','Odds', 'Chi2', 'M_B', 'Stell_Mass', 'CLASS', 'PROB_GAL', 'PROB_STAR'), meta={'name': 'first table'})

# # #Saving resultated table
asciifile = "PN-SPLUS_STRIPE82_DataRelease-Junio18_petro.tab"
try:
    table.write(asciifile, format='ascii.tab', overwrite=True)
except TypeError:
    table.write(asciifile, format='ascii.tab')
