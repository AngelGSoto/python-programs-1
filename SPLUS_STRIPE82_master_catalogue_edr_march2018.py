'''
Getting the PN and SyST candidtaes in S-PLUS catalog (DR1)
'''
from __future__ import print_function
import numpy as np
import glob
import json
import os
import matplotlib.pyplot as plt
#import seaborn as sns
import sys
from astropy.table import Table
import argparse

n=18
magnitude = [[] for _ in range(n)]

dt = np.dtype([('Field', 'S13'), ('ID', 'f8'), ('RA', 'f8'), ('Dec', 'f8'),('X', 'f8'),('Y', 'f8'),('Aperture', 'f8'),('s2nDet', 'f4'),('PhotoFlag', 'f4'),('FWHM', 'f4'),('MUMAX', 'f4'),('A', 'f4'),('B', 'f4'),('THETA', 'f4'),('FlRadDet', 'f4'),('KrRadDet', 'f4'),('U_auto', 'f8'),('dU_auto', 'f4'), ('s2n_U_auto', 'f4'), ('U_petro', 'f4'), ('dU_petro', 'f4'), ('s2n_U_petro ', 'f4'), ('U_aper', 'f4'), ('DU_aper', 'f4'), ('S2n_U_aper', 'f4'), ('F0378_auto', 'f8'),('dF0378_auto', 'f4'),('s2n_F0378_auto', 'f4'),('F0378_petro', 'f4'),('dF0378_petro', 'f4'),('s2n_F0378_petro', 'f4'),('F0378_aper', 'f4'),('dF0378_aper', 'f4'),('s2n_F0378_aper', 'f4'),('F0395_auto', 'f8'),('dF0395_auto', 'f4'),('s2n_F0395_auto', 'f4'),('F0395_petro', 'f4'),('dF0395_petro', 'f4'),('s2n_F0395_petro', 'f4'),('F0395_aper', 'f4'),('dF0395_aper', 'f4'),('s2n_F0395_aper', 'f4'),('F0410_auto', 'f8'),('dF0410_auto', 'f4'),('s2n_F0410_auto', 'f4'),('F0410_petro', 'f4'),('dF0410_petro', 'f4'),('s2n_F0410_petro', 'f4'),('F0410_aper', 'f4'),('dF0410_aper', 'f4'),('s2n_F0410_aper', 'f4'),('F0430_auto', 'f8'),('dF0430_auto', 'f4'),('s2n_F0430_auto', 'f4'),('F0430_petro', 'f4'),('dF0430_petro', 'f4'),('s2n_F0430_petro', 'f4'),('F0430_aper', 'f4'),('dF0430_aper', 'f4'),('s2n_F0430_aper', 'f4'),('G_auto', 'f8'),('dG_auto', 'f4'),('s2n_G_auto', 'f4'),('G_petro', 'f4'),('dG_petro', 'f4'),('s2n_G_petro', 'f4'),('G_aper', 'f4'),('dG_aper', 'f4'),('s2n_G_aper', 'f4'),('F0515_auto', 'f8'),('dF0515_auto', 'f4'),('s2n_F0515_auto', 'f4'),('F0515_petro', 'f4'),('dF0515_petro', 'f4'),('s2n_F0515_petro', 'f4'),('F0515_aper', 'f4'),('dF0515_aper', 'f4'),(' s2n_F0515_aper', 'f4'),('R_auto', 'f8'),('dR_auto', 'f4'),('s2n_R_auto', 'f4'),('R_petro', 'f4'),('dR_petro', 'f4'),('s2n_R_petro', 'f4'),('R_aper', 'f4'),('dR_aper', 'f4'),('s2n_R_aper', 'f4'),('F0660_auto', 'f8'),('dF0660_auto', 'f4'),('s2n_F0660_auto', 'f4'),('F0660_petro', 'f4'),('dF0660_petro', 'f4'),('s2n_F0660_petro', 'f4'),('F0660_aper', 'f4'),('dF0660_aper', 'f4'),('s2n_F0660_aper', 'f4'),('I_auto', 'f8'),('dI_auto', 'f4'),('s2n_I_auto', 'f4'),('I_petro', 'f4'),('dI_petro', 'f4'),('s2n_I_petro', 'f4'),('I_aper', 'f4'),('dI_aper', 'f4'),('s2n_I_aper', 'f4'),('F0861_auto', 'f8'),('dF0861_auto', 'f4'),('s2n_F0861_auto', 'f4'),('F0861_petro', 'f4'),('dF0861_petro', 'f4'),('s2n_F0861_petro', 'f4'),('F0861_aper', 'f4'),('dF0861_aper', 'f4'),('s2n_F0861_aper', 'f4'),('Z_auto', 'f8'),('dZ_auto', 'f4'),('s2n_Z_auto', 'f4'),('Z_petro', 'f4'),('dZ_petro', 'f4'),('s2n_Z_petro', 'f4'),('Z_aper', 'f4'),('dZ_aper', 'f4'),('s2n_Z_aper', 'f4'),('zb', 'f4'), ('zb_Min', 'f4'),('zb_Max', 'f4'), ('Tb', 'f4'),('Odds', 'f4'),('Chi2', 'f4'),('M_B', 'f4'),('Stell_Mass', 'f4'),('CLASS', 'f4'), ('PROB_GAL', 'f8'),('PROB_STAR', 'f8')])
data = np.loadtxt("sys-candidate-marz.dat", dtype=dt)

# magnitude[0].append(data['Field']) #Field
# magnitude[1].append(data['ID'])  #id
# magnitude[2].append(data['RA']) #ra
# magnitude[3].append(data['Dec']) #dec
# magnitude[4].append(data['U_auto'])   #u
# magnitude[5].append(data['F0378_auto']) #j0378
# magnitude[6].append(data['F0395_auto']) #j0395
# magnitude[7].append(data['F0410_auto']) #j0410
# magnitude[8].append(data['F0430_auto']) #j0430
# magnitude[9].append(data['G_auto'])     #g
# magnitude[10].append(data['F0515_auto']) #j0515
# magnitude[11].append(data['R_auto'])       #r
# magnitude[12].append(data['F0660_auto'])   #j0660
# magnitude[13].append(data['I_auto'])       #i
# magnitude[14].append(data['F0861_auto'])  #j0861
# magnitude[15].append(data['Z_auto'])      #z
# magnitude[16].append(data['PROB_STAR'])   #clas stars
# #     #field

# print(magnitude[0])
# sys.exit()
#table = Table([magnitude[0], magnitude[1], magnitude[2], magnitude[3], magnitude[4], magnitude[5], magnitude[6], magnitude[7], magnitude[8], magnitude[9], magnitude[10], magnitude[11], magnitude[12], magnitude[13], magnitude[14], magnitude[15], magnitude[16]],  names=('Field', 'Id', 'RA', 'Dec', 'uJAVA', 'J0378', 'J0395', 'J0410', 'J0430', 'gSDSS', 'J0515', 'rSDSS', 'J0660', 'iSDSS', 'J0861', 'zSDSS', "Class star"), meta={'name': 'first table'})
table = Table([data['Field'], data['ID'], data['RA'], data['Dec'], data['Aperture'], data['KrRadDet'], data['U_auto'], data['U_petro'], data['U_aper'], data['F0378_auto'], data['F0378_petro'], data['F0378_aper'], data['F0395_auto'], data['F0395_petro'], data['F0395_aper'], data['F0410_auto'], data['F0410_petro'], data['F0410_aper'], data['F0430_auto'], data['F0430_petro'], data['F0430_aper'], data['G_auto'], data['G_petro'], data['G_aper'], data['F0515_auto'], data['F0515_petro'], data['F0515_aper'],  data['R_auto'], data['R_petro'], data['R_aper'], data['F0660_auto'], data['F0660_petro'], data['F0660_aper'], data['I_auto'], data['I_petro'], data['I_aper'], data['F0861_auto'], data['F0861_petro'], data['F0861_aper'], data['Z_auto'], data['Z_petro'], data['Z_aper'], data['PROB_STAR']],  names=('Field', 'Id', 'RA', 'Dec', 'Aperture', 'KrRadDet', 'uJAVA', 'uJAVA_petro', 'uJAVA_aper', 'J0378', 'J0378_petro', 'J0378_aper', 'J0395', 'J0395_petro', 'J0395_aper', 'J0410', 'J0410_petro', 'J0410_aper', 'J0430', 'J0430_petro', 'J0430_aper', 'gSDSS', 'gSDSS_petro', 'gSDSS_aper', 'J0515', 'J0515_petro', 'J0515_aper', 'rSDSS', 'rSDSS_petro', 'rSDSS_aper', 'J0660', 'J0660_petro', 'J0660_aper', 'iSDSS', 'iSDSS_petro', 'iSDSS_aper', 'J0861', 'J0861_petro', 'J0861_aper', 'zSDSS', 'zSDSS_petro', 'zSDSS_aper', "Class star"), meta={'name': 'first table'})
#Saving resultated table
#asciifile = "SPLUS_STRIPE82-catalogue_edr_march2018.tab"
asciifile = "sys-candidate-march2018.tab"

try:
    table.write(asciifile, format='ascii.tab', overwrite=True)
except TypeError:
    table.write(asciifile, format='ascii.tab')

#table.write(asciifile, format="ascii.tab", overwrite=True)
