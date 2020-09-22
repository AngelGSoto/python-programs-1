'''
Getting the PN candidtaes in S-PLUS catalog (DR1)
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from astropy.table import Table

#lists
n=134
mag_aper = [[] for _ in range(n)]
mag_petro = [[] for _ in range(n)]
mag_auto = [[] for _ in range(n)]
def select(magg, mag):
    f = data['U_'+magg] <= 21.6
    f1 = data['F0378_'+magg] <= 21.5
    f2 = data['F0395_'+magg] < 21.4
    f3 = data['F0410_'+magg] <= 21.5
    f4 = data['F0430_'+magg] < 21.4
    f5 = data['G_'+magg] <= 22.2
    f6 = data['F0515_'+magg] <= 21.4
    f7 = data['R_'+magg] <= 21.9
    f8 = data['F0660_'+magg] <= 21.3
    f9 = data['I_'+magg] <= 20.8
    f10 = data['F0861_'+magg] <= 20.8
    f11 = data['Z_'+magg] <= 20.5

    mask = f & f1 & f2 & f3 & f5 & f6 & f7 & f8 & f9 & f10 & f11

    #Mask
    #Mask filters
    q = (data['F0515_'+magg] - data['F0660_'+magg]) <= 5.0
    #q1 = (data['J0515'] - data['J0861']) >= -3.0
    q2 = (data['R_'+magg] - data['F0660_'+magg]) <= 4.0
    q3 = (data['R_'+magg] - data['I_'+magg]) >= -4.0
    q4 = (data['G_'+magg] - data['F0515_'+magg]) >= -3.2
    q5 = (data['G_'+magg] - data['I_'+magg]) >= -3.0
    q6 = (data['F0410_'+magg] - data['F0660_'+magg]) <= 6.0
    q7 = (data['Z_'+magg] - data['G_'+magg]) <= 4.0

    mask1 = q  & q2 & q3 & q4 & q5 & q6 & q7
    #Mask
    Y = 2.7*(data['F0515_'+magg] - data['F0861_'+magg]) + 2.15
    Y1 = 0.2319*(data['Z_'+magg] - data['G_'+magg]) + 0.85
    Y2 = -1.3*(data['Z_'+magg] - data['G_'+magg]) + 1.7
    Y3 = 1.559*(data['F0660_'+magg] - data['R_'+magg]) + 0.58
    Y4 = 0.12*(data['F0660_'+magg] - data['R_'+magg]) - 0.01
    Y44 = -1.1*(data['F0660_'+magg] - data['R_'+magg]) - 1.07
    Y5 = 8.0*(data['G_'+magg] - data['I_'+magg]) + 4.5
    Y6 = 0.8*(data['G_'+magg] - data['I_'+magg]) + 0.55
    Y7 = 0.43*(data['R_'+magg] - data['I_'+magg]) + 0.65
    Y8 = -6.8*(data['R_'+magg] - data['I_'+magg]) - 1.3

    m = data['PhotoFlag'] == 0.0
    #m = data['Class star'] > 0.0 
    m1 = data['F0660_'+magg] - data['R_'+magg]<=-1.0 
    m2 = data['F0515_'+magg] - data['F0660_'+magg]>=0.3
    m3 = data['Z_'+magg] - data['F0660_'+magg]>=Y1
    m4 = data['Z_'+magg] - data['F0660_'+magg]>=Y2
    m5 = data['F0515_'+magg] - data['F0660_'+magg]>=Y
    m6 = data['F0660_'+magg] - data['G_'+magg]>=Y3
    m7 = data['G_'+magg] - data['F0515_'+magg]<=Y4
    m8 = data['G_'+magg] - data['F0515_'+magg]<=Y44
    m9 = data['F0410_'+magg] - data['F0660_'+magg]>=Y5
    m10 = data['F0410_'+magg] - data['F0660_'+magg]>=Y6
    m11 = (data['R_'+magg] - data['F0660_'+magg]) >= Y7
    m12 = (data['R_'+magg] - data['F0660_'+magg]) <= Y8
    total_m = m & m1 & m2 & m3 & m4 & m5 & m6 & m7 & m8 & m9 & m10 & m11 & m12 & mask & mask1
    
    for i in data['Field_ID'][total_m]:
        mag[0].append(i)
    for i in data['RA'][total_m]:
        mag[1].append(i)
    for i in data['Dec'][total_m]:
        mag[2].append(i)
    for i in data['X'][total_m]:
        mag[3].append(i)
    for i in data['Y'][total_m]:
        mag[4].append(i)
    for i in data['Aperture'][total_m]:
        mag[5].append(i)
    for i in data['s2nDet'][total_m]:
        mag[6].append(i)
    for i in data['PhotoFlag'][total_m]:
        mag[7].append(i)
    for i in data['FWHM'][total_m]:
        mag[8].append(i)
    for i in data['MUMAX'][total_m]:
        mag[9].append(i)
    for i in data['A'][total_m]:
        mag[10].append(i)
    for i in data['B'][total_m]:
        mag[11].append(i)
    for i in data['THETA'][total_m]:
        mag[12].append(i)
    for i in data['FlRadDet'][total_m]:
        mag[13].append(i)
    for i in data['KrRadDet'][total_m]:
        mag[14].append(i)
    for i in data['U_auto'][total_m]:
        mag[15].append(i)
    for i in data['dU_auto'][total_m]:
        mag[16].append(i)
    for i in data['s2n_U_auto'][total_m]:
        mag[17].append(i)
    for i in data['U_petro'][total_m]:
        mag[18].append(i)
    for i in data['dU_petro'][total_m]:
        mag[19].append(i)
    for i in data['s2n_U_petro'][total_m]:
        mag[20].append(i)
    for i in data['U_aper'][total_m]:
        mag[21].append(i)
    for i in data['DU_aper'][total_m]:
        mag[22].append(i)
    for i in data['S2n_U_aper'][total_m]:
        mag[23].append(i)
    for i in data['F0378_auto'][total_m]:
        mag[24].append(i)
    for i in data['dF0378_auto'][total_m]:
        mag[25].append(i)
    for i in data['s2n_F0378_auto'][total_m]:
        mag[26].append(i)
    for i in data['F0378_petro'][total_m]:
        mag[27].append(i)
    for i in data['dF0378_petro'][total_m]:
        mag[28].append(i)
    for i in data['s2n_F0378_petro'][total_m]:
        mag[29].append(i)
    for i in data['F0378_aper'][total_m]:
        mag[30].append(i)
    for i in data['dF0378_aper'][total_m]:
        mag[31].append(i)
    for i in data['s2n_F0378_aper'][total_m]:
        mag[32].append(i)
    for i in data['F0395_auto'][total_m]:
        mag[33].append(i)
    for i in data['dF0395_auto'][total_m]:
        mag[34].append(i)
    for i in data['s2n_F0395_auto'][total_m]:
        mag[35].append(i)
    for i in data['F0395_petro'][total_m]:
        mag[36].append(i)
    for i in data['dF0395_petro'][total_m]:
        mag[37].append(i)
    for i in data['s2n_F0395_petro'][total_m]:
        mag[38].append(i)
    for i in data['F0395_aper'][total_m]:
        mag[39].append(i)
    for i in data['dF0395_aper'][total_m]:
        mag[40].append(i)
    for i in data['s2n_F0395_aper'][total_m]:
        mag[41].append(i)
    for i in data['F0410_auto'][total_m]:
        mag[42].append(i)
    for i in data['dF0410_auto'][total_m]:
        mag[43].append(i)
    for i in data['s2n_F0410_auto'][total_m]:
        mag[44].append(i)
    for i in data['F0410_petro'][total_m]:
        mag[45].append(i)
    for i in data['dF0410_petro'][total_m]:
        mag[46].append(i)
    for i in data['s2n_F0410_petro'][total_m]:
        mag[47].append(i)
    for i in data['F0410_aper'][total_m]: 
        mag[48].append(i)
    for i in data['dF0410_aper'][total_m]:
        mag[49].append(i)
    for i in data['s2n_F0410_aper'][total_m]:
        mag[50].append(i)
    for i in data['F0430_auto'][total_m]:
        mag[51].append(i)
    for i in data['dF0430_auto'][total_m]:
        mag[52].append(i)
    for i in data['s2n_F0430_auto'][total_m]:
        mag[53].append(i)
    for i in data['F0430_petro'][total_m]:
        mag[54].append(i)
    for i in data['dF0430_petro'][total_m]:
        mag[55].append(i)
    for i in data['s2n_F0430_petro'][total_m]:
        mag[56].append(i)
    for i in data['F0430_aper'][total_m]:
        mag[57].append(i)
    for i in data['dF0430_aper'][total_m]:
        mag[58].append(i)
    for i in data['s2n_F0430_aper'][total_m]:
        mag[59].append(i)
    for i in data['G_auto'][total_m]:
        mag[60].append(i)
    for i in data['dG_auto'][total_m]:
        mag[61].append(i)
    for i in data['s2n_G_auto'][total_m]:
        mag[62].append(i)
    for i in data['G_petro'][total_m]:
        mag[63].append(i)
    for i in data['dG_petro'][total_m]:
        mag[64].append(i)
    for i in data['s2n_G_petro'][total_m]:
        mag[65].append(i)
    for i in data['G_aper'][total_m]:
        mag[66].append(i)
    for i in data['dG_aper'][total_m]:
        mag[67].append(i)
    for i in data['s2n_G_aper'][total_m]:
        mag[68].append(i)
    for i in data['F0515_auto'][total_m]:
        mag[69].append(i)
    for i in data['dF0515_auto'][total_m]:
        mag[70].append(i)
    for i in data['s2n_F0515_auto'][total_m]:
        mag[71].append(i)
    for i in data['F0515_petro'][total_m]:
        mag[72].append(i)
    for i in data['dF0515_petro'][total_m]:
        mag[73].append(i)
    for i in data['s2n_F0515_petro'][total_m]:
        mag[74].append(i)
    for i in data['F0515_aper'][total_m]: 
        mag[75].append(i)
    for i in data['dF0515_aper'][total_m]:
        mag[76].append(i)
    for i in data['s2n_F0515_aper'][total_m]:
        mag[77].append(i)
    for i in data['R_auto'][total_m]:
        mag[78].append(i)
    for i in data['dR_auto'][total_m]:
        mag[79].append(i)
    for i in data['s2n_R_auto'][total_m]:
        mag[80].append(i)
    for i in data['R_petro'][total_m]:
        mag[81].append(i)
    for i in data['dR_petro'][total_m]:
        mag[82].append(i)
    for i in data['s2n_R_petro'][total_m]:
        mag[83].append(i)
    for i in data['R_aper'][total_m]:
        mag[84].append(i)
    for i in data['dR_aper'][total_m]:
        mag[85].append(i)
    for i in data['s2n_R_aper'][total_m]:
        mag[86].append(i)
    for i in data['F0660_auto'][total_m]:
        mag[87].append(i)
    for i in data['dF0660_auto'][total_m]:
        mag[88].append(i)
    for i in data['s2n_F0660_auto'][total_m]:
        mag[89].append(i)
    for i in data['F0660_petro'][total_m]:
        mag[90].append(i)
    for i in data['dF0660_petro'][total_m]:
        mag[91].append(i)
    for i in data['s2n_F0660_petro'][total_m]:
        mag[92].append(i)
    for i in data['F0660_aper'][total_m]:
        mag[93].append(i)
    for i in data['dF0660_aper'][total_m]:
        mag[94].append(i)
    for i in data['s2n_F0660_aper'][total_m]:
        mag[95].append(i)
    for i in data['I_auto'][total_m]:
        mag[96].append(i)
    for i in data['dI_auto'][total_m]:
        mag[97].append(i)
    for i in data['s2n_I_auto'][total_m]:
        mag[98].append(i)
    for i in data['I_petro'][total_m]:
        mag[99].append(i)
    for i in data['dI_petro'][total_m]:
        mag[100].append(i)
    for i in data['s2n_I_petro'][total_m]:
        mag[101].append(i)
    for i in data['I_aper'][total_m]: 
        mag[102].append(i)
    for i in data['dI_aper'][total_m]:
        mag[103].append(i)
    for i in data['s2n_I_aper'][total_m]:
        mag[104].append(i)
    for i in data['F0861_auto'][total_m]:
        mag[105].append(i)
    for i in data['dF0861_auto'][total_m]:
        mag[106].append(i)
    for i in data['s2n_F0861_auto'][total_m]:
        mag[107].append(i)
    for i in data['F0861_petro'][total_m]:
        mag[108].append(i)
    for i in data['dF0861_petro'][total_m]:
        mag[109].append(i)
    for i in data['s2n_F0861_petro'][total_m]:
        mag[110].append(i)
    for i in data['F0861_aper'][total_m]:
        mag[111].append(i)
    for i in data['dF0861_aper'][total_m]:
        mag[112].append(i)
    for i in data['s2n_F0861_aper'][total_m]:
        mag[113].append(i)
    for i in data['Z_auto'][total_m]:
        mag[114].append(i)
    for i in data['dZ_auto'][total_m]:
        mag[115].append(i)
    for i in data['s2n_Z_auto'][total_m]:
        mag[116].append(i)
    for i in data['Z_petro'][total_m]: 
        mag[117].append(i)
    for i in data['dZ_petro'][total_m]:
        mag[118].append(i)
    for i in data['s2n_Z_petro'][total_m]:
        mag[119].append(i)
    for i in data['Z_aper'][total_m]:
        mag[120].append(i)
    for i in data['dZ_aper'][total_m]:
        mag[121].append(i)
    for i in data['s2n_Z_aper'][total_m]:
        mag[122].append(i)
    for i in data['zb'][total_m]:
        mag[123].append(i)
    for i in data['zb_Min'][total_m]:
        mag[124].append(i)
    for i in data['zb_Max'][total_m]:
        mag[125].append(i)
    for i in data['Tb'][total_m]:
        mag[126].append(i)
    for i in data['Odds'][total_m]:
        mag[127].append(i)
    for i in data['Chi2'][total_m]:
        mag[128].append(i)
    for i in data['M_B'][total_m]:
        mag[129].append(i)
    for i in data['Stell_Mass'][total_m]:
        mag[130].append(i)
    for i in data['CLASS'][total_m]:
        mag[131].append(i)
    for i in data['PROB_GAL'][total_m]:
        mag[132].append(i)
    for i in data['PROB_STAR'][total_m]:
        mag[133].append(i)
    table = Table([mag[0], mag[1], mag[2], mag[3], mag[4], mag[5], mag[6], mag[7], mag[8], mag[9], mag[10], mag[11], mag[12], mag[13], mag[14], mag[15], mag[16], mag[17], mag[18], mag[19], mag[20], mag[21], mag[22], mag[23], mag[24], mag[25], mag[26], mag[27], mag[28], mag[29], mag[30], mag[31], mag[32], mag[33], mag[34], mag[35], mag[36], mag[37], mag[38], mag[39], mag[40], mag[41], mag[42], mag[43], mag[44], mag[45], mag[46], mag[47], mag[48], mag[49], mag[50], mag[51], mag[52], mag[53], mag[54], mag[55], mag[56], mag[57], mag[58], mag[59], mag[60], mag[61], mag[62], mag[63], mag[64], mag[65], mag[66], mag[67], mag[68], mag[69], mag[70], mag[71], mag[72], mag[73], mag[74], mag[75], mag[76], mag[77], mag[78], mag[79], mag[80], mag[81], mag[82], mag[83], mag[84], mag[85], mag[86], mag[87], mag[88], mag[89], mag[90], mag[91], mag[92], mag[93], mag[94], mag[95], mag[96], mag[97], mag[98], mag[99], mag[100], mag[101], mag[102], mag[103], mag[104], mag[105], mag[106], mag[107], mag[108], mag[109], mag[110], mag[111], mag[112], mag[113], mag[114], mag[115], mag[116], mag[117], mag[118], mag[119], mag[120], mag[121], mag[122], mag[123], mag[124], mag[125], mag[126], mag[127], mag[128], mag[129], mag[130], mag[131], mag[132], mag[133]],  names=('Field_ID', 'RA', 'Dec', 'X', 'Y', 'Aperture', 's2nDet', 'PhotoFlag', 'FWHM','MUMAX', 'A', 'B','THETA','FlRadDet','KrRadDet','U_auto','dU_auto', 's2n_U_auto', 'U_petro', 'dU_petro', 's2n_U_petro ', 'U_aper', 'DU_aper', 'S2n_U_aper', 'F0378_auto', 'dF0378_auto', 's2n_F0378_auto', 'F0378_petro', 'dF0378_petro', 's2n_F0378_petro', 'F0378_aper', 'dF0378_aper', 's2n_F0378_aper', 'F0395_auto','dF0395_auto', 's2n_F0395_auto', 'F0395_petro', 'dF0395_petro','s2n_F0395_petro', 'F0395_aper','dF0395_aper','s2n_F0395_aper','F0410_auto','dF0410_auto', 's2n_F0410_auto', 'F0410_petro', 'dF0410_petro', 's2n_F0410_petro', 'F0410_aper', 'dF0410_aper', 's2n_F0410_aper', 'F0430_auto', 'dF0430_auto','s2n_F0430_auto','F0430_petro','dF0430_petro', 's2n_F0430_petro', 'F0430_aper', 'dF0430_aper', 's2n_F0430_aper','G_auto','dG_auto','s2n_G_auto', 'G_petro', 'dG_petro', 's2n_G_petro', 'G_aper', 'dG_aper', 's2n_G_aper', 'F0515_auto', 'dF0515_auto', 's2n_F0515_auto', 'F0515_petro','dF0515_petro','s2n_F0515_petro','F0515_aper','dF0515_aper', 's2n_F0515_aper','R_auto','dR_auto','s2n_R_auto','R_petro','dR_petro','s2n_R_petro', 'R_aper', 'dR_aper', 's2n_R_aper', 'F0660_auto', 'dF0660_auto', 's2n_F0660_auto', 'F0660_petro', 'dF0660_petro', 's2n_F0660_petro','F0660_aper', 'dF0660_aper', 's2n_F0660_aper', 'I_auto','dI_auto','s2n_I_auto','I_petro', 'dI_petro','s2n_I_petro','I_aper','dI_aper', 's2n_I_aper', 'F0861_auto', 'dF0861_auto','s2n_F0861_auto', 'F0861_petro', 'dF0861_petro', 's2n_F0861_petro', 'F0861_aper', 'dF0861_aper', 's2n_F0861_aper', 'Z_auto', 'dZ_auto', 's2n_Z_auto', 'Z_petro','dZ_petro', 's2n_Z_petro', 'Z_aper', 'dZ_aper', 's2n_Z_aper', 'zb', 'zb_Min','zb_Max', 'Tb','Odds', 'Chi2', 'M_B', 'Stell_Mass', 'CLASS', 'PROB_GAL', 'PROB_STAR'), meta={'name': 'first table'})
    return table

#Read the files.cat these are the SPLUS-SRTIPE catalog
pattern = "*.cat"
file_list = glob.glob(pattern)

dt = np.dtype([('Field_ID', 'S25'), ('RA', 'f8'), ('Dec', 'f8'),('X', 'f8'),('Y', 'f8'),('Aperture', 'f8'),('s2nDet', 'f4'),('PhotoFlag', 'f4'),('FWHM', 'f4'),('MUMAX', 'f4'),('A', 'f4'),('B', 'f4'),('THETA', 'f4'),('FlRadDet', 'f4'),('KrRadDet', 'f4'),('U_auto', 'f8'),('dU_auto', 'f4'), ('s2n_U_auto', 'f4'), ('U_petro', 'f4'), ('dU_petro', 'f4'), ('s2n_U_petro', 'f4'), ('U_aper', 'f4'), ('DU_aper', 'f4'), ('S2n_U_aper', 'f4'), ('F0378_auto', 'f8'),('dF0378_auto', 'f4'),('s2n_F0378_auto', 'f4'),('F0378_petro', 'f4'),('dF0378_petro', 'f4'),('s2n_F0378_petro', 'f4'),('F0378_aper', 'f4'),('dF0378_aper', 'f4'),('s2n_F0378_aper', 'f4'),('F0395_auto', 'f8'),('dF0395_auto', 'f4'),('s2n_F0395_auto', 'f4'),('F0395_petro', 'f4'),('dF0395_petro', 'f4'),('s2n_F0395_petro', 'f4'),('F0395_aper', 'f4'),('dF0395_aper', 'f4'),('s2n_F0395_aper', 'f4'),('F0410_auto', 'f8'),('dF0410_auto', 'f4'),('s2n_F0410_auto', 'f4'),('F0410_petro', 'f4'),('dF0410_petro', 'f4'),('s2n_F0410_petro', 'f4'),('F0410_aper', 'f4'),('dF0410_aper', 'f4'),('s2n_F0410_aper', 'f4'),('F0430_auto', 'f8'),('dF0430_auto', 'f4'),('s2n_F0430_auto', 'f4'),('F0430_petro', 'f4'),('dF0430_petro', 'f4'),('s2n_F0430_petro', 'f4'),('F0430_aper', 'f4'),('dF0430_aper', 'f4'),('s2n_F0430_aper', 'f4'),('G_auto', 'f8'),('dG_auto', 'f4'),('s2n_G_auto', 'f4'),('G_petro', 'f4'),('dG_petro', 'f4'),('s2n_G_petro', 'f4'),('G_aper', 'f4'),('dG_aper', 'f4'),('s2n_G_aper', 'f4'),('F0515_auto', 'f8'),('dF0515_auto', 'f4'),('s2n_F0515_auto', 'f4'),('F0515_petro', 'f4'),('dF0515_petro', 'f4'),('s2n_F0515_petro', 'f4'),('F0515_aper', 'f4'),('dF0515_aper', 'f4'),('s2n_F0515_aper', 'f4'),('R_auto', 'f8'),('dR_auto', 'f4'),('s2n_R_auto', 'f4'),('R_petro', 'f4'),('dR_petro', 'f4'),('s2n_R_petro', 'f4'),('R_aper', 'f4'),('dR_aper', 'f4'),('s2n_R_aper', 'f4'),('F0660_auto', 'f8'),('dF0660_auto', 'f4'),('s2n_F0660_auto', 'f4'),('F0660_petro', 'f4'),('dF0660_petro', 'f4'),('s2n_F0660_petro', 'f4'),('F0660_aper', 'f4'),('dF0660_aper', 'f4'),('s2n_F0660_aper', 'f4'),('I_auto', 'f8'),('dI_auto', 'f4'),('s2n_I_auto', 'f4'),('I_petro', 'f4'),('dI_petro', 'f4'),('s2n_I_petro', 'f4'),('I_aper', 'f4'),('dI_aper', 'f4'),('s2n_I_aper', 'f4'),('F0861_auto', 'f8'),('dF0861_auto', 'f4'),('s2n_F0861_auto', 'f4'),('F0861_petro', 'f4'),('dF0861_petro', 'f4'),('s2n_F0861_petro', 'f4'),('F0861_aper', 'f4'),('dF0861_aper', 'f4'),('s2n_F0861_aper', 'f4'),('Z_auto', 'f8'),('dZ_auto', 'f4'),('s2n_Z_auto', 'f4'),('Z_petro', 'f4'), ('dZ_petro', 'f4'),('s2n_Z_petro', 'f4'),('Z_aper', 'f4'),('dZ_aper', 'f4'),('s2n_Z_aper', 'f4'),('zb', 'f4'), ('zb_Min', 'f4'), ('zb_Max', 'f4'), ('Tb', 'f4'),('Odds', 'f4'),('Chi2', 'f4'),('M_B', 'f4'),('Stell_Mass', 'f4'),('CLASS', 'f4'), ('PROB_GAL', 'f8'), ('PROB_STAR', 'f8')])
for file_name in file_list:
    data = np.loadtxt(file_name, dtype=dt)
    table_aper = select('aper', mag_aper)
    table_petro = select('petro', mag_petro)
    table_auto = select('auto', mag_auto)

    # # #Saving resultated table
    #######
    #aper#
    #######
    asciifile = "PNe-SPLUS_STRIPE82_DataRelease-Junio18_aper.tab"
    try:
         table_aper.write(asciifile, format='ascii.tab', overwrite=True)
    except TypeError:
         table_aper.write(asciifile, format='ascii.tab')

    #######
    #petro#
    #######
    asciifile_petro = "PNe-SPLUS_STRIPE82_DataRelease-Junio18_petro.tab"
    try:
        table_petro.write(asciifile_petro, format='ascii.tab', overwrite=True)
    except TypeError:
        table_petro.write(asciifile_petro, format='ascii.tab')

    ######
    #auto#
    ######
    asciifile_auto = "PNe-SPLUS_STRIPE82_DataRelease-Junio18_auto.tab"
    try:
        table_auto.write(asciifile_auto, format='ascii.tab', overwrite=True)
    except TypeError:
        table_auto.write(asciifile_auto, format='ascii.tab')
