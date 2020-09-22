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

n=134
mag = [[] for _ in range(n)]

pattern = "*.cat"
file_list = glob.glob(pattern)

dt = np.dtype([('Field_ID', 'S25'), ('RA', 'f8'), ('Dec', 'f8'),('X', 'f8'),('Y', 'f8'),('Aperture', 'f8'),('s2nDet', 'f4'),('PhotoFlag', 'f4'),('FWHM', 'f4'),('MUMAX', 'f4'),('A', 'f4'),('B', 'f4'),('THETA', 'f4'),('FlRadDet', 'f4'),('KrRadDet', 'f4'),('U_auto', 'f8'),('dU_auto', 'f4'), ('s2n_U_auto', 'f4'), ('U_petro', 'f4'), ('dU_petro', 'f4'), ('s2n_U_petro', 'f4'), ('U_aper', 'f4'), ('DU_aper', 'f4'), ('S2n_U_aper', 'f4'), ('F0378_auto', 'f8'),('dF0378_auto', 'f4'),('s2n_F0378_auto', 'f4'),('F0378_petro', 'f4'),('dF0378_petro', 'f4'),('s2n_F0378_petro', 'f4'),('F0378_aper', 'f4'),('dF0378_aper', 'f4'),('s2n_F0378_aper', 'f4'),('F0395_auto', 'f8'),('dF0395_auto', 'f4'),('s2n_F0395_auto', 'f4'),('F0395_petro', 'f4'),('dF0395_petro', 'f4'),('s2n_F0395_petro', 'f4'),('F0395_aper', 'f4'),('dF0395_aper', 'f4'),('s2n_F0395_aper', 'f4'),('F0410_auto', 'f8'),('dF0410_auto', 'f4'),('s2n_F0410_auto', 'f4'),('F0410_petro', 'f4'),('dF0410_petro', 'f4'),('s2n_F0410_petro', 'f4'),('F0410_aper', 'f4'),('dF0410_aper', 'f4'),('s2n_F0410_aper', 'f4'),('F0430_auto', 'f8'),('dF0430_auto', 'f4'),('s2n_F0430_auto', 'f4'),('F0430_petro', 'f4'),('dF0430_petro', 'f4'),('s2n_F0430_petro', 'f4'),('F0430_aper', 'f4'),('dF0430_aper', 'f4'),('s2n_F0430_aper', 'f4'),('G_auto', 'f8'),('dG_auto', 'f4'),('s2n_G_auto', 'f4'),('G_petro', 'f4'),('dG_petro', 'f4'),('s2n_G_petro', 'f4'),('G_aper', 'f4'),('dG_aper', 'f4'),('s2n_G_aper', 'f4'),('F0515_auto', 'f8'),('dF0515_auto', 'f4'),('s2n_F0515_auto', 'f4'),('F0515_petro', 'f4'),('dF0515_petro', 'f4'),('s2n_F0515_petro', 'f4'),('F0515_aper', 'f4'),('dF0515_aper', 'f4'),('s2n_F0515_aper', 'f4'),('R_auto', 'f8'),('dR_auto', 'f4'),('s2n_R_auto', 'f4'),('R_petro', 'f4'),('dR_petro', 'f4'),('s2n_R_petro', 'f4'),('R_aper', 'f4'),('dR_aper', 'f4'),('s2n_R_aper', 'f4'),('F0660_auto', 'f8'),('dF0660_auto', 'f4'),('s2n_F0660_auto', 'f4'),('F0660_petro', 'f4'),('dF0660_petro', 'f4'),('s2n_F0660_petro', 'f4'),('F0660_aper', 'f4'),('dF0660_aper', 'f4'),('s2n_F0660_aper', 'f4'),('I_auto', 'f8'),('dI_auto', 'f4'),('s2n_I_auto', 'f4'),('I_petro', 'f4'),('dI_petro', 'f4'),('s2n_I_petro', 'f4'),('I_aper', 'f4'),('dI_aper', 'f4'),('s2n_I_aper', 'f4'),('F0861_auto', 'f8'),('dF0861_auto', 'f4'),('s2n_F0861_auto', 'f4'),('F0861_petro', 'f4'),('dF0861_petro', 'f4'),('s2n_F0861_petro', 'f4'),('F0861_aper', 'f4'),('dF0861_aper', 'f4'),('s2n_F0861_aper', 'f4'),('Z_auto', 'f8'),('dZ_auto', 'f4'),('s2n_Z_auto', 'f4'),('Z_petro', 'f4'), ('dZ_petro', 'f4'),('s2n_Z_petro', 'f4'),('Z_aper', 'f4'),('dZ_aper', 'f4'),('s2n_Z_aper', 'f4'),('zb', 'f4'), ('zb_Min', 'f4'), ('zb_Max', 'f4'), ('Tb', 'f4'),('Odds', 'f4'),('Chi2', 'f4'),('M_B', 'f4'),('Stell_Mass', 'f4'),('CLASS', 'f4'), ('PROB_GAL', 'f8'), ('PROB_STAR', 'f8')])
for file_name in file_list:
    data = np.loadtxt(file_name, dtype=dt)
    for i in data['Field_ID']:
        mag[0].append(i)
    for i in data['RA']:
        mag[1].append(i)
    for i in data['Dec']:
        mag[2].append(i)
    for i in data['X']:
        mag[3].append(i)
    for i in data['Y']:
        mag[4].append(i)
    for i in data['Aperture']:
        mag[5].append(i)
    for i in data['s2nDet']:
        mag[6].append(i)
    for i in data['PhotoFlag']:
        mag[7].append(i)
    for i in data['FWHM']:
        mag[8].append(i)
    for i in data['MUMAX']:
        mag[9].append(i)
    for i in data['A']:
        mag[10].append(i)
    for i in data['B']:
        mag[11].append(i)
    for i in data['THETA']:
        mag[12].append(i)
    for i in data['FlRadDet']:
        mag[13].append(i)
    for i in data['KrRadDet']:
        mag[14].append(i)
    for i in data['U_auto']:
        mag[15].append(i)
    for i in data['dU_auto']:
        mag[16].append(i)
    for i in data['s2n_U_auto']:
        mag[17].append(i)
    for i in data['U_petro']:
        mag[18].append(i)
    for i in data['dU_petro']:
        mag[19].append(i)
    for i in data['s2n_U_petro']:
        mag[20].append(i)
    for i in data['U_aper']:
        mag[21].append(i)
    for i in data['DU_aper']:
        mag[22].append(i)
    for i in data['S2n_U_aper']:
        mag[23].append(i)
    for i in data['F0378_auto']:
        mag[24].append(i)
    for i in data['dF0378_auto']:
        mag[25].append(i)
    for i in data['s2n_F0378_auto']:
        mag[26].append(i)
    for i in data['F0378_petro']:
        mag[27].append(i)
    for i in data['dF0378_petro']:
        mag[28].append(i)
    for i in data['s2n_F0378_petro']:
        mag[29].append(i)
    for i in data['F0378_aper']:
        mag[30].append(i)
    for i in data['dF0378_aper']:
        mag[31].append(i)
    for i in data['s2n_F0378_aper']:
        mag[32].append(i)
    for i in data['F0395_auto']:
        mag[33].append(i)
    for i in data['dF0395_auto']:
        mag[34].append(i)
    for i in data['s2n_F0395_auto']:
        mag[35].append(i)
    for i in data['F0395_petro']:
        mag[36].append(i)
    for i in data['dF0395_petro']:
        mag[37].append(i)
    for i in data['s2n_F0395_petro']:
        mag[38].append(i)
    for i in data['F0395_aper']:
        mag[39].append(i)
    for i in data['dF0395_aper']:
        mag[40].append(i)
    for i in data['s2n_F0395_aper']:
        mag[41].append(i)
    for i in data['F0410_auto']:
        mag[42].append(i)
    for i in data['dF0410_auto']:
        mag[43].append(i)
    for i in data['s2n_F0410_auto']:
        mag[44].append(i)
    for i in data['F0410_petro']:
        mag[45].append(i)
    for i in data['dF0410_petro']:
        mag[46].append(i)
    for i in data['s2n_F0410_petro']:
        mag[47].append(i)
    for i in data['F0410_aper']: 
        mag[48].append(i)
    for i in data['dF0410_aper']:
        mag[49].append(i)
    for i in data['s2n_F0410_aper']:
        mag[50].append(i)
    for i in data['F0430_auto']:
        mag[51].append(i)
    for i in data['dF0430_auto']:
        mag[52].append(i)
    for i in data['s2n_F0430_auto']:
        mag[53].append(i)
    for i in data['F0430_petro']:
        mag[54].append(i)
    for i in data['dF0430_petro']:
        mag[55].append(i)
    for i in data['s2n_F0430_petro']:
        mag[56].append(i)
    for i in data['F0430_aper']:
        mag[57].append(i)
    for i in data['dF0430_aper']:
        mag[58].append(i)
    for i in data['s2n_F0430_aper']:
        mag[59].append(i)
    for i in data['G_auto']:
        mag[60].append(i)
    for i in data['dG_auto']:
        mag[61].append(i)
    for i in data['s2n_G_auto']:
        mag[62].append(i)
    for i in data['G_petro']:
        mag[63].append(i)
    for i in data['dG_petro']:
        mag[64].append(i)
    for i in data['s2n_G_petro']:
        mag[65].append(i)
    for i in data['G_aper']:
        mag[66].append(i)
    for i in data['dG_aper']:
        mag[67].append(i)
    for i in data['s2n_G_aper']:
        mag[68].append(i)
    for i in data['F0515_auto']:
        mag[69].append(i)
    for i in data['dF0515_auto']:
        mag[70].append(i)
    for i in data['s2n_F0515_auto']:
        mag[71].append(i)
    for i in data['F0515_petro']:
        mag[72].append(i)
    for i in data['dF0515_petro']:
        mag[73].append(i)
    for i in data['s2n_F0515_petro']:
        mag[74].append(i)
    for i in data['F0515_aper']: 
        mag[75].append(i)
    for i in data['dF0515_aper']:
        mag[76].append(i)
    for i in data['s2n_F0515_aper']:
        mag[77].append(i)
    for i in data['R_auto']:
        mag[78].append(i)
    for i in data['dR_auto']:
        mag[79].append(i)
    for i in data['s2n_R_auto']:
        mag[80].append(i)
    for i in data['R_petro']:
        mag[81].append(i)
    for i in data['dR_petro']:
        mag[82].append(i)
    for i in data['s2n_R_petro']:
        mag[83].append(i)
    for i in data['R_aper']:
        mag[84].append(i)
    for i in data['dR_aper']:
        mag[85].append(i)
    for i in data['s2n_R_aper']:
        mag[86].append(i)
    for i in data['F0660_auto']:
        mag[87].append(i)
    for i in data['dF0660_auto']:
        mag[88].append(i)
    for i in data['s2n_F0660_auto']:
        mag[89].append(i)
    for i in data['F0660_petro']:
        mag[90].append(i)
    for i in data['dF0660_petro']:
        mag[91].append(i)
    for i in data['s2n_F0660_petro']:
        mag[92].append(i)
    for i in data['F0660_aper']:
        mag[93].append(i)
    for i in data['dF0660_aper']:
        mag[94].append(i)
    for i in data['s2n_F0660_aper']:
        mag[95].append(i)
    for i in data['I_auto']:
        mag[96].append(i)
    for i in data['dI_auto']:
        mag[97].append(i)
    for i in data['s2n_I_auto']:
        mag[98].append(i)
    for i in data['I_petro']:
        mag[99].append(i)
    for i in data['dI_petro']:
        mag[100].append(i)
    for i in data['s2n_I_petro']:
        mag[101].append(i)
    for i in data['I_aper']: 
        mag[102].append(i)
    for i in data['dI_aper']:
        mag[103].append(i)
    for i in data['s2n_I_aper']:
        mag[104].append(i)
    for i in data['F0861_auto']:
        mag[105].append(i)
    for i in data['dF0861_auto']:
        mag[106].append(i)
    for i in data['s2n_F0861_auto']:
        mag[107].append(i)
    for i in data['F0861_petro']:
        mag[108].append(i)
    for i in data['dF0861_petro']:
        mag[109].append(i)
    for i in data['s2n_F0861_petro']:
        mag[110].append(i)
    for i in data['F0861_aper']:
        mag[111].append(i)
    for i in data['dF0861_aper']:
        mag[112].append(i)
    for i in data['s2n_F0861_aper']:
        mag[113].append(i)
    for i in data['Z_auto']:
        mag[114].append(i)
    for i in data['dZ_auto']:
        mag[115].append(i)
    for i in data['s2n_Z_auto']:
        mag[116].append(i)
    for i in data['Z_petro']: 
        mag[117].append(i)
    for i in data['dZ_petro']:
        mag[118].append(i)
    for i in data['s2n_Z_petro']:
        mag[119].append(i)
    for i in data['Z_aper']:
        mag[120].append(i)
    for i in data['dZ_aper']:
        mag[121].append(i)
    for i in data['s2n_Z_aper']:
        mag[122].append(i)
    for i in data['zb']:
        mag[123].append(i)
    for i in data['zb_Min']:
        mag[124].append(i)
    for i in data['zb_Max']:
        mag[125].append(i)
    for i in data['Tb']:
        mag[126].append(i)
    for i in data['Odds']:
        mag[127].append(i)
    for i in data['Chi2']:
        mag[128].append(i)
    for i in data['M_B']:
        mag[129].append(i)
    for i in data['Stell_Mass']:
        mag[130].append(i)
    for i in data['CLASS']:
        mag[131].append(i)
    for i in data['PROB_GAL']:
        mag[132].append(i)
    for i in data['PROB_STAR']:
        mag[133].append(i)

table = Table([mag[0], mag[1], mag[2], mag[3], mag[4], mag[5], mag[6], mag[7], mag[8], mag[9], mag[10], mag[11], mag[12], mag[13], mag[14], mag[15], mag[16], mag[17], mag[18], mag[19], mag[20], mag[21], mag[22], mag[23], mag[24], mag[25], mag[26], mag[27], mag[28], mag[29], mag[30], mag[31], mag[32], mag[33], mag[34], mag[35], mag[36], mag[37], mag[38], mag[39], mag[40], mag[41], mag[42], mag[43], mag[44], mag[45], mag[46], mag[47], mag[48], mag[49], mag[50], mag[51], mag[52], mag[53], mag[54], mag[55], mag[56], mag[57], mag[58], mag[59], mag[60], mag[61], mag[62], mag[63], mag[64], mag[65], mag[66], mag[67], mag[68], mag[69], mag[70], mag[71], mag[72], mag[73], mag[74], mag[75], mag[76], mag[77], mag[78], mag[79], mag[80], mag[81], mag[82], mag[83], mag[84], mag[85], mag[86], mag[87], mag[88], mag[89], mag[90], mag[91], mag[92], mag[93], mag[94], mag[95], mag[96], mag[97], mag[98], mag[99], mag[100], mag[101], mag[102], mag[103], mag[104], mag[105], mag[106], mag[107], mag[108], mag[109], mag[110], mag[111], mag[112], mag[113], mag[114], mag[115], mag[116], mag[117], mag[118], mag[119], mag[120], mag[121], mag[122], mag[123], mag[124], mag[125], mag[126], mag[127], mag[128], mag[129], mag[130], mag[131], mag[132], mag[133]],  names=('Field_ID', 'RA', 'Dec', 'X', 'Y', 'Aperture', 's2nDet', 'PhotoFlag', 'FWHM','MUMAX', 'A', 'B','THETA','FlRadDet','KrRadDet','U_auto','dU_auto', 's2n_U_auto', 'U_petro', 'dU_petro', 's2n_U_petro ', 'U_aper', 'DU_aper', 'S2n_U_aper', 'F0378_auto', 'dF0378_auto', 's2n_F0378_auto', 'F0378_petro', 'dF0378_petro', 's2n_F0378_petro', 'F0378_aper', 'dF0378_aper', 's2n_F0378_aper', 'F0395_auto','dF0395_auto', 's2n_F0395_auto', 'F0395_petro', 'dF0395_petro','s2n_F0395_petro', 'F0395_aper','dF0395_aper','s2n_F0395_aper','F0410_auto','dF0410_auto', 's2n_F0410_auto', 'F0410_petro', 'dF0410_petro', 's2n_F0410_petro', 'F0410_aper', 'dF0410_aper', 's2n_F0410_aper', 'F0430_auto', 'dF0430_auto','s2n_F0430_auto','F0430_petro','dF0430_petro', 's2n_F0430_petro', 'F0430_aper', 'dF0430_aper', 's2n_F0430_aper','G_auto','dG_auto','s2n_G_auto', 'G_petro', 'dG_petro', 's2n_G_petro', 'G_aper', 'dG_aper', 's2n_G_aper', 'F0515_auto', 'dF0515_auto', 's2n_F0515_auto', 'F0515_petro','dF0515_petro','s2n_F0515_petro','F0515_aper','dF0515_aper', 's2n_F0515_aper','R_auto','dR_auto','s2n_R_auto','R_petro','dR_petro','s2n_R_petro', 'R_aper', 'dR_aper', 's2n_R_aper', 'F0660_auto', 'dF0660_auto', 's2n_F0660_auto', 'F0660_petro', 'dF0660_petro', 's2n_F0660_petro','F0660_aper', 'dF0660_aper', 's2n_F0660_aper', 'I_auto','dI_auto','s2n_I_auto','I_petro', 'dI_petro','s2n_I_petro','I_aper','dI_aper', 's2n_I_aper', 'F0861_auto', 'dF0861_auto','s2n_F0861_auto', 'F0861_petro', 'dF0861_petro', 's2n_F0861_petro', 'F0861_aper', 'dF0861_aper', 's2n_F0861_aper', 'Z_auto', 'dZ_auto', 's2n_Z_auto', 'Z_petro','dZ_petro', 's2n_Z_petro', 'Z_aper', 'dZ_aper', 's2n_Z_aper', 'zb', 'zb_Min','zb_Max', 'Tb','Odds', 'Chi2', 'M_B', 'Stell_Mass', 'CLASS', 'PROB_GAL', 'PROB_STAR'), meta={'name': 'first table'})

print(table)
# # #Saving resultated table
# # #asciifile = "SPLUS_STRIPE82_Photometry-Datarelease-Junio18.tab"
asciifile = "SPLUS_STRIPE82_Photometry-Datarelease-Junio18.tab"
try:
    table.write(asciifile, format='ascii.tab', overwrite=True)
except TypeError:
    table.write(asciifile, format='ascii.tab')

#table.write(asciifile, format="ascii.tab", overwrite=True)

#################################################################################################3############################################
##############################################################################################################################################
##########################################################3##################################################################################
#################################################################################################3#######################################
#table = Table([data['Field_ID'], data['RA'], data['Dec'],data['X'],data['Y'], data['Aperture'], data['s2nDet'], data['PhotoFlag'],data['FWHM'],data['MUMAX'],data['A'], data['B'],data['THETA'], data['FlRadDet'], data['KrRadDet'], data['U_auto'], data['dU_auto'], data['s2n_U_auto'], data['U_petro'], data['dU_petro'], data['s2n_U_petro '], data['U_aper'], data['DU_aper'], data['S2n_U_aper'], data['F0378_auto'],data['dF0378_auto'], data['s2n_F0378_auto'], data['F0378_petro'], data['dF0378_petro'], data['s2n_F0378_petro'], data['F0378_aper'], data['dF0378_aper'], data['s2n_F0378_aper'], data['F0395_auto'], data['dF0395_auto'], data['s2n_F0395_auto'], data['F0395_petro'], data['dF0395_petro'], data['s2n_F0395_petro'], data['F0395_aper'], data['dF0395_aper'], data['s2n_F0395_aper'], data['F0410_auto'], data['dF0410_auto'], data['s2n_F0410_auto'], data['F0410_petro'], data['dF0410_petro'], data['s2n_F0410_petro'], data['F0410_aper'], data['dF0410_aper'], data['s2n_F0410_aper'], data['F0430_auto'], data['dF0430_auto'], data['s2n_F0430_auto'], data['F0430_petro'], data['dF0430_petro'], data['s2n_F0430_petro'], data['F0430_aper'],data['dF0430_aper'], data['s2n_F0430_aper'], data['G_auto'], data['dG_auto'], data['s2n_G_auto'], data['G_petro'], data['dG_petro'], data['s2n_G_petro'], data['G_aper'], data['dG_aper'], data['s2n_G_aper'], data['F0515_auto'], data['dF0515_auto'], data['s2n_F0515_auto'], data['F0515_petro'], data['dF0515_petro'], data['s2n_F0515_petro'], data['F0515_aper'], data['dF0515_aper'], data[' s2n_F0515_aper'], data['R_auto'], data['dR_auto'], data['s2n_R_auto'], data['R_petro'], data['dR_petro'], data['s2n_R_petro'], data['R_aper'], data['dR_aper'], data['s2n_R_aper'], data['F0660_auto'], data['dF0660_auto'], data['s2n_F0660_auto'], data['F0660_petro'], data['dF0660_petro'], data['s2n_F0660_petro'], data['F0660_aper'], data['dF0660_aper'], data['s2n_F0660_aper'], data['I_auto'], data['dI_auto'], data['s2n_I_auto'], data['I_petro'], data['dI_petro'],data['s2n_I_petro'],data['I_aper'],data['dI_aper'],data['s2n_I_aper'],data['F0861_auto'],data['dF0861_auto'],data['s2n_F0861_auto'],data['F0861_petro'], data['dF0861_petro'], data['s2n_F0861_petro'], data['F0861_aper'], data['dF0861_aper'], data['s2n_F0861_aper'], data['Z_auto'], data['dZ_auto'], data['s2n_Z_auto'], data['Z_petro'], data['dZ_petro'], data['s2n_Z_petro'], data['Z_aper'], data['dZ_aper'], data['s2n_Z_aper'], data['zb'], data['zb_Min'], data['zb_Max'], data['Tb'], data['Odds'], data['Chi2'], data['M_B'], data['Stell_Mass'], data['CLASS'], data['PROB_GAL'], data['PROB_STAR']],  names=('Field_ID', 'RA', 'Dec', 'X', 'Y', 'Aperture', 's2nDet', 'PhotoFlag', 'FWHM','MUMAX', 'A', 'B','THETA','FlRadDet','KrRadDet','U_auto','dU_auto', 's2n_U_auto', 'U_petro', 'dU_petro', 's2n_U_petro ', 'U_aper', 'DU_aper', 'S2n_U_aper', 'F0378_auto', 'dF0378_auto', 's2n_F0378_auto', 'F0378_petro', 'dF0378_petro', 's2n_F0378_petro', 'F0378_aper', 'dF0378_aper', 's2n_F0378_aper', 'F0395_auto','dF0395_auto', 's2n_F0395_auto', 'F0395_petro', 'dF0395_petro','s2n_F0395_petro', 'F0395_aper','dF0395_aper','s2n_F0395_aper','F0410_auto','dF0410_auto', 's2n_F0410_auto', 'F0410_petro', 'dF0410_petro', 's2n_F0410_petro', 'F0410_aper', 'dF0410_aper', 's2n_F0410_aper', 'F0430_auto', 'dF0430_auto','s2n_F0430_auto','F0430_petro','dF0430_petro', 's2n_F0430_petro', 'F0430_aper', 'dF0430_aper', 's2n_F0430_aper','G_auto','dG_auto','s2n_G_auto', 'G_petro', 'dG_petro', 's2n_G_petro', 'G_aper', 'dG_aper', 's2n_G_aper', 'F0515_auto', 'dF0515_auto', 's2n_F0515_auto', 'F0515_petro','dF0515_petro','s2n_F0515_petro','F0515_aper','dF0515_aper', 's2n_F0515_aper','R_auto','dR_auto','s2n_R_auto','R_petro','dR_petro','s2n_R_petro', 'R_aper', 'dR_aper', 's2n_R_aper', 'F0660_auto', 'dF0660_auto', 's2n_F0660_auto', 'F0660_petro', 'dF0660_petro', 's2n_F0660_petro','F0660_aper', 'dF0660_aper', 's2n_F0660_aper', 'I_auto','dI_auto','s2n_I_auto','I_petro', 'dI_petro','s2n_I_petro','I_aper','dI_aper', 's2n_I_aper', 'F0861_auto', 'dF0861_auto','s2n_F0861_auto', 'F0861_petro', 'dF0861_petro', 's2n_F0861_petro', 'F0861_aper', 'dF0861_aper', 's2n_F0861_aper', 'Z_auto', 'dZ_auto', 's2n_Z_auto', 'Z_petro','dZ_petro', 's2n_Z_petro', 'Z_aper', 'dZ_aper', 's2n_Z_aper', 'zb', 'zb_Min','zb_Max', 'Tb','Odds', 'Chi2', 'M_B', 'Stell_Mass', 'CLASS', 'PROB_GAL', 'PROB_STAR'), meta={'name': 'first table'})
