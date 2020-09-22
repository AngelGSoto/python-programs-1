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


tab = Table.read("SPLUS_STRIPE82_Photometry-Datarelease-Junio18.tab", format="ascii.tab")

# shape = (len(tab['Id']), )
# x = np.linspace(-10.0, 15.5, len(tab['Id']))
# X = np.array(x).reshape(shape)

def mk(mask):
    table = Table([tab['Field_ID'][mask], tab['RA'][total_m], tab['Dec'][mask],tab['X'][mask],tab['Y'][mask], tab['Aperture'][mask], tab['s2nDet'][mask], tab['PhotoFlag'][mask],tab['FWHM'][mask],tab['MUMAX'][mask],tab['A'][mask], tab['B'][mask],tab['THETA'][mask], tab['FlRadDet'][mask], tab['KrRadDet'][mask], tab['U_auto'][mask], tab['dU_auto'][mask], tab['s2n_U_auto'][mask], tab['U_petro'][mask], tab['dU_petro'][mask], tab['s2n_U_petro '][mask], tab['U_aper'][mask], tab['DU_aper'][mask], tab['S2n_U_aper'][mask], tab['F0378_auto'][mask],tab['dF0378_auto'][mask], tab['s2n_F0378_auto'][mask], tab['F0378_petro'][mask], tab['dF0378_petro'][mask], tab['s2n_F0378_petro'][mask], tab['F0378_aper'][mask], tab['dF0378_aper'][mask], tab['s2n_F0378_aper'][mask], tab['F0395_auto'][mask], tab['dF0395_auto'][mask], tab['s2n_F0395_auto'][mask], tab['F0395_petro'][mask], tab['dF0395_petro'][mask], tab['s2n_F0395_petro'][mask], tab['F0395_aper'][mask], tab['dF0395_aper'][mask], tab['s2n_F0395_aper'][mask], tab['F0410_auto'][mask], tab['dF0410_auto'][mask], tab['s2n_F0410_auto'][mask], tab['F0410_petro'][mask], tab['dF0410_petro'][mask], tab['s2n_F0410_petro'][mask], tab['F0410_aper'][mask], tab['dF0410_aper'][mask], tab['s2n_F0410_aper'][mask], tab['F0430_auto'][mask], tab['dF0430_auto'][mask], tab['s2n_F0430_auto'][mask], tab['F0430_petro'][mask], tab['dF0430_petro'][mask], tab['s2n_F0430_petro'][mask], tab['F0430_aper'][mask], tab['dF0430_aper'][mask], tab['s2n_F0430_aper'][mask], tab['G_auto'][mask], tab['dG_auto'][mask], tab['s2n_G_auto'][mask], tab['G_petro'][mask], tab['dG_petro'][mask], tab['s2n_G_petro'][mask], tab['G_aper'][mask], tab['dG_aper'][mask], tab['s2n_G_aper'][mask], tab['F0515_auto'][mask], tab['dF0515_auto'][mask], tab['s2n_F0515_auto'][mask], tab['F0515_petro'][mask], tab['dF0515_petro'][mask], tab['s2n_F0515_petro'][mask], tab['F0515_aper'][mask], tab['dF0515_aper'][mask], tab[' s2n_F0515_aper'][mask], tab['R_auto'][mask], tab['dR_auto'][mask], tab['s2n_R_auto'][mask], tab['R_petro'][mask], tab['dR_petro'][mask], tab['s2n_R_petro'][mask], tab['R_aper'][mask], tab['dR_aper'][mask], tab['s2n_R_aper'][mask], tab['F0660_auto'][mask], tab['dF0660_auto'][mask], tab['s2n_F0660_auto'][mask], tab['F0660_petro'][mask], tab['dF0660_petro'][mask], tab['s2n_F0660_petro'][mask], tab['F0660_aper'][mask], tab['dF0660_aper'][mask], tab['s2n_F0660_aper'][mask], tab['I_auto'][mask], tab['dI_auto'][mask], tab['s2n_I_auto'][mask], tab['I_petro'][mask], tab['dI_petro'][mask], tab['s2n_I_petro'][mask],tab['I_aper'][mask],tab['dI_aper'][mask],tab['s2n_I_aper'][mask],tab['F0861_auto'][mask], tab['dF0861_auto'][mask],tab['s2n_F0861_auto'][mask],tab['F0861_petro'][mask], tab['dF0861_petro'][mask], tab['s2n_F0861_petro'][mask], tab['F0861_aper'][mask], tab['dF0861_aper'][mask], tab['s2n_F0861_aper'][mask], tab['Z_auto'][mask], tab['dZ_auto'][mask], tab['s2n_Z_auto'][mask], tab['Z_petro'][mask], tab['dZ_petro'][mask], tab['s2n_Z_petro'][mask], tab['Z_aper'][mask], tab['dZ_aper'][mask], tab['s2n_Z_aper'][mask], tab['zb'][mask], tab['zb_Min'][mask], tab['zb_Max'][mask], tab['Tb'][mask], tab['Odds'][mask], tab['Chi2'][mask], tab['M_B'][mask], tab['Stell_Mass'][mask], tab['CLASS'][mask], tab['PROB_GAL'][mask], tab['PROB_STAR'][mask]],  names=('Field_ID', 'RA', 'Dec', 'X', 'Y', 'Aperture', 's2nDet', 'PhotoFlag', 'FWHM','MUMAX', 'A', 'B','THETA','FlRadDet','KrRadDet','U_auto','dU_auto', 's2n_U_auto', 'U_petro', 'dU_petro', 's2n_U_petro ', 'U_aper', 'DU_aper', 'S2n_U_aper', 'F0378_auto', 'dF0378_auto', 's2n_F0378_auto', 'F0378_petro', 'dF0378_petro', 's2n_F0378_petro', 'F0378_aper', 'dF0378_aper', 's2n_F0378_aper', 'F0395_auto','dF0395_auto', 's2n_F0395_auto', 'F0395_petro', 'dF0395_petro','s2n_F0395_petro', 'F0395_aper','dF0395_aper','s2n_F0395_aper','F0410_auto','dF0410_auto', 's2n_F0410_auto', 'F0410_petro', 'dF0410_petro', 's2n_F0410_petro', 'F0410_aper', 'dF0410_aper', 's2n_F0410_aper', 'F0430_auto', 'dF0430_auto','s2n_F0430_auto','F0430_petro','dF0430_petro', 's2n_F0430_petro', 'F0430_aper', 'dF0430_aper', 's2n_F0430_aper','G_auto','dG_auto','s2n_G_auto', 'G_petro', 'dG_petro', 's2n_G_petro', 'G_aper', 'dG_aper', 's2n_G_aper', 'F0515_auto', 'dF0515_auto', 's2n_F0515_auto', 'F0515_petro','dF0515_petro','s2n_F0515_petro','F0515_aper','dF0515_aper', 's2n_F0515_aper','R_auto','dR_auto','s2n_R_auto','R_petro','dR_petro','s2n_R_petro', 'R_aper', 'dR_aper', 's2n_R_aper', 'F0660_auto', 'dF0660_auto', 's2n_F0660_auto', 'F0660_petro', 'dF0660_petro', 's2n_F0660_petro','F0660_aper', 'dF0660_aper', 's2n_F0660_aper', 'I_auto','dI_auto','s2n_I_auto','I_petro', 'dI_petro','s2n_I_petro','I_aper','dI_aper', 's2n_I_aper', 'F0861_auto', 'dF0861_auto','s2n_F0861_auto', 'F0861_petro', 'dF0861_petro', 's2n_F0861_petro', 'F0861_aper', 'dF0861_aper', 's2n_F0861_aper', 'Z_auto', 'dZ_auto', 's2n_Z_auto', 'Z_petro','dZ_petro', 's2n_Z_petro', 'Z_aper', 'dZ_aper', 's2n_Z_aper', 'zb', 'zb_Min','zb_Max', 'Tb','Odds', 'Chi2', 'M_B', 'Stell_Mass', 'CLASS', 'PROB_GAL', 'PROB_STAR'), meta={'name': 'first table'})
    return table
    

### Aper
#filer deep splus mask
f = tab['U_aper'] <= 21.6
f1 = tab['F0378_aper'] <= 21.5
f2 = tab['F0395_aper'] < 21.4
f3 = tab['F0410_aper'] <= 21.5
f4 = tab['F0430_aper'] < 21.4
f5 = tab['G_aper'] <= 22.2
f6 = tab['F0515_aper'] <= 21.4
f7 = tab['R_aper'] <= 21.9
f8 = tab['F0660_aper'] <= 21.3
f9 = tab['I_aper'] <= 20.8
f10 = tab['F0861_aper'] <= 20.8
f11 = tab['Z_aper'] <= 20.5

mask =  f3 & f5 & f6 & f7 & f8 & f9 & f10 & f11

# # #Mask 1
q = (tab['F0515_aper'] - tab['F0660_aper']) <= 5.0
q1 = (tab['F0515_aper'] - tab['F0861_aper']) >= -3.0
q2 = (tab['R_aper'] - tab['F0660_aper']) <= 4.0
q3 = (tab['R_aper'] - tab['I_aper']) >= -4.0
q4 = (tab['G_aper'] - tab['F0515_aper']) >= -3.2
q5 = (tab['G_aper'] - tab['I_aper']) >= -3.0
q6 = (tab['F0410_aper'] - tab['F0660_aper']) <= 6.0
q7 = (tab['zSDSS_aper'] - tab['G_aper']) <= 4.0

mask1 = q & q1 & q2 & q3 & q4 & q5 & q6 & q7 
#Mask
Y = 5.5*(tab['F0515_aper'] - tab['F0861_aper']) - 6.45
Y1 = 0.98*(tab['F0515_aper'] - tab['F0861_aper']) - 0.16
Y2 = -1.96*(tab['Z_aper'] - tab['G_aper']) - 3.15
Y3 = 0.2*(tab['Z_aper'] - tab['G_aper']) + 0.44 
Y4 = -220*(tab['R_aper'] - tab['I_aper']) + 40.4
Y44 = 0.39*(tab['R_aper'] - tab['I_aper']) + 0.73
Y5 = -4.7*(tab['G_aper'] - tab['I_aper']) + 10.60
Y6 = 2.13*(tab['G_aper'] - tab['I_aper']) - 1.43
Y7 = -0.19*(tab['F0660_aper'] - tab['R_aper']) - 0.05
Y8 = -2.66*(tab['F0660_aper'] - tab['R_aper']) - 2.2

#m = tab['Class star_aper'] < 0.6 
m1 = tab['F0515_aper'] - tab['F0660_aper']<= Y
m2 = tab['F0515_aper'] - tab['F0660_aper']>= Y1
m3 = tab['Z_aper'] - tab['F0660_aper']<= Y2
m4 = tab['Z_aper'] - tab['F0660_aper']>= Y3
m5 = tab['R_aper'] - tab['F0660_aper']>= Y4
m6 = tab['R_aper'] - tab['F0660_aper']>= Y44
m7 = tab['F0410_aper'] - tab['F0660_aper']>= Y5
m8 = tab['F0410_aper'] - tab['F0660_aper']>= Y6
m9 = tab['G_aper'] - tab['F0515_aper']>= Y7
m10 = tab['G_aper'] - tab['F0515_aper']<= Y8
total_m = m1 & m2 & m3 & m4 & m5 & m6 & m7 & m8 & m9 & m10 & mask & mask1

# # #Saving resultated table
table1 = mk(total_m)

####################################################################
### PETRO ##########################################################
###################################################################
#filer deep splus mask
f_petro = tab['U_petro'] <= 21.6
f1_petro = tab['F0378_petro'] <= 21.5
f2_petro = tab['F0395_petro'] < 21.4
f3_petro = tab['F0410_petro'] <= 21.5
f4_petro = tab['F0430_petro'] < 21.4
f5_petro = tab['G_petro'] <= 22.2
f6_petro = tab['F0515_petro'] <= 21.4
f7_petro = tab['R_petro'] <= 21.9
f8_petro = tab['F0660_petro'] <= 21.3
f9_petro = tab['I_petro'] <= 20.8
f10_petro = tab['F0861_petro'] <= 20.8
f11_petro = tab['Z_petro'] <= 20.5

mask_petro =  f3_petro & f5_petro & f6_petro & f7_petro & f8_petro & f9_petro & f10_petro & f11_petro

# # #Mask 1
q_petro = (tab['F0515_petro'] - tab['F0660_petro']) <= 5.0
q1_petro = (tab['F0515_petro'] - tab['F0861_petro']) >= -3.0
q2_petro = (tab['R_petro'] - tab['F0660_petro']) <= 4.0
q3_petro = (tab['R_petro'] - tab['I_petro']) >= -4.0
q4_petro = (tab['G_petro'] - tab['F0515_petro']) >= -3.2
q5_petro = (tab['G_petro'] - tab['I_petro']) >= -3.0
q6_petro = (tab['F0410_petro'] - tab['F0660_petro']) <= 6.0
q7_petro = (tab['zSDSS_petro'] - tab['G_petro']) <= 4.0

mask1_petro = q_petro & q1_petro & q2_petro & q3_petro & q4_petro & q5_petro & q6_petro & q7_petro 
#Mask
Y_petro = 5.5*(tab['F0515_petro'] - tab['F0861_petro']) - 6.45
Y1_petro = 0.98*(tab['F0515_petro'] - tab['F0861_petro']) - 0.16
Y2_petro = -1.96*(tab['Z_petro'] - tab['G_petro']) - 3.15
Y3_petro = 0.2*(tab['Z_petro'] - tab['G_petro']) + 0.44 
Y4_petro = -220*(tab['R_petro'] - tab['I_petro']) + 40.4
Y44_petro = 0.39*(tab['R_petro'] - tab['I_petro']) + 0.73
Y5_petro = -4.7*(tab['G_petro'] - tab['I_petro']) + 10.60
Y6_petro = 2.13*(tab['G_petro'] - tab['I_petro']) - 1.43
Y7_petro = -0.19*(tab['F0660_petro'] - tab['R_petro']) - 0.05
Y8_petro = -2.66*(tab['F0660_petro'] - tab['R_petro']) - 2.2

#m_petro = tab['Class star_petro'] < 0.6 
m1_petro = tab['F0515_petro'] - tab['F0660_petro']<= Y_petro
m2_petro = tab['F0515_petro'] - tab['F0660_petro']>= Y1_petro
m3_petro = tab['Z_petro'] - tab['F0660_petro']<= Y2_petro
m4_petro = tab['Z_petro'] - tab['F0660_petro']>= Y3_petro
m5_petro = tab['R_petro'] - tab['F0660_petro']>= Y4_petro
m6_petro = tab['R_petro'] - tab['F0660_petro']>= Y44_petro
m7_petro = tab['F0410_petro'] - tab['F0660_petro']>= Y5_petro
m8_petro = tab['F0410_petro'] - tab['F0660_petro']>= Y6_petro
m9_petro = tab['G_petro'] - tab['F0515_petro']>= Y7_petro
m10_petro = tab['G_petro'] - tab['F0515_petro']<= Y8_petro
total_m_petro = m1_petro & m2_petro & m3_petro & m4_petro & m5_petro & m6_petro & m7_petro & m8_petro & m9_petro & m10_petro & mask_petro & mask1_petro

table_petro = mk(total_m_petro)

####################################################################
### AUTO ##########################################################
###################################################################
#filer deep splus mask
f_auto = tab['U_auto'] <= 21.6
f1_auto = tab['F0378_auto'] <= 21.5
f2_auto = tab['F0395_auto'] < 21.4
f3_auto = tab['F0410_auto'] <= 21.5
f4_auto = tab['F0430_auto'] < 21.4
f5_auto = tab['G_auto'] <= 22.2
f6_auto = tab['F0515_auto'] <= 21.4
f7_auto = tab['R_auto'] <= 21.9
f8_auto = tab['F0660_auto'] <= 21.3
f9_auto = tab['I_auto'] <= 20.8
f10_auto = tab['F0861_auto'] <= 20.8
f11_auto = tab['Z_auto'] <= 20.5

mask_auto =  f3_auto & f5_auto & f6_auto & f7_auto & f8_auto & f9_auto & f10_auto & f11_auto

# # #Mask 1
q_auto = (tab['F0515_auto'] - tab['F0660_auto']) <= 5.0
q1_auto = (tab['F0515_auto'] - tab['F0861_auto']) >= -3.0
q2_auto = (tab['R_auto'] - tab['F0660_auto']) <= 4.0
q3_auto = (tab['R_auto'] - tab['I_auto']) >= -4.0
q4_auto = (tab['G_auto'] - tab['F0515_auto']) >= -3.2
q5_auto = (tab['G_auto'] - tab['I_auto']) >= -3.0
q6_auto = (tab['F0410_auto'] - tab['F0660_auto']) <= 6.0
q7_auto = (tab['zSDSS_auto'] - tab['G_auto']) <= 4.0

mask1_auto = q_auto & q1_auto & q2_auto & q3_auto & q4_auto & q5_auto & q6_auto & q7_auto 
#Mask
Y_auto = 5.5*(tab['F0515_auto'] - tab['F0861_auto']) - 6.45
Y1_auto = 0.98*(tab['F0515_auto'] - tab['F0861_auto']) - 0.16
Y2_auto = -1.96*(tab['Z_auto'] - tab['G_auto']) - 3.15
Y3_auto = 0.2*(tab['Z_auto'] - tab['G_auto']) + 0.44 
Y4_auto = -220*(tab['R_auto'] - tab['I_auto']) + 40.4
Y44_auto = 0.39*(tab['R_auto'] - tab['I_auto']) + 0.73
Y5_auto = -4.7*(tab['G_auto'] - tab['I_auto']) + 10.60
Y6_auto = 2.13*(tab['G_auto'] - tab['I_auto']) - 1.43
Y7_auto = -0.19*(tab['F0660_auto'] - tab['R_auto']) - 0.05
Y8_auto = -2.66*(tab['F0660_auto'] - tab['R_auto']) - 2.2

#m_auto = tab['Class star_auto'] < 0.6 
m1_auto = tab['F0515_auto'] - tab['F0660_auto']<= Y_auto
m2_auto = tab['F0515_auto'] - tab['F0660_auto']>= Y1_auto
m3_auto = tab['Z_auto'] - tab['F0660_auto']<= Y2_auto
m4_auto = tab['Z_auto'] - tab['F0660_auto']>= Y3_auto
m5_auto = tab['R_auto'] - tab['F0660_auto']>= Y4_auto
m6_auto = tab['R_auto'] - tab['F0660_auto']>= Y44_auto
m7_auto = tab['F0410_auto'] - tab['F0660_auto']>= Y5_auto
m8_auto = tab['F0410_auto'] - tab['F0660_auto']>= Y6_auto
m9_auto = tab['G_auto'] - tab['F0515_auto']>= Y7_auto
m10_auto = tab['G_auto'] - tab['F0515_auto']<= Y8_auto
total_m_auto = m1_auto & m2_auto & m3_auto & m4_auto & m5_auto & m6_auto & m7_auto & m8_auto & m9_auto & m10_auto & mask_auto & mask1_auto

table_auto = mk(total_m_auto)

######
#aper#
######
asciifile = "SySt-SPLUS_STRIPE82_DataRelease-Junio18_aper.tab"
try:
    table1.write(asciifile, format='ascii.tab', overwrite=True)
except TypeError:
    table1.write(asciifile, format='ascii.tab')

#######
#petro#
#######
asciifile_petro = "SySt-SPLUS_STRIPE82_DataRelease-Junio18_petro.tab"
try:
    table_petro.write(asciifile_petro, format='ascii.tab', overwrite=True)
except TypeError:
    table1.write(asciifile_petro, format='ascii.tab')

######
#auto#
######
asciifile_auto = "SySt-SPLUS_STRIPE82_DataRelease-Junio18_auto.tab"
try:
    table_auto.write(asciifile_auto, format='ascii.tab', overwrite=True)
except TypeError:
    table_auto.write(asciifile_auto, format='ascii.tab')

    
