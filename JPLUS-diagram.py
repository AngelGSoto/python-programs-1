'''
Make color-color diagram for SPLUS
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
import seaborn as sns
import sys

pattern = "*-spectros/*-JPLUS13-magnitude.json"
file_list = glob.glob(pattern)

def filter_mag(e, s, f1, f2, f3):
    col, col0 = [], []
    if data['id'].endswith(e):
        if data['id'].startswith(str(s)):
            filter1 = data[f1]
            filter2 = data[f2]
            filter3 = data[f3]
            diff = filter1 - filter2
            diff0 = filter1 - filter3
            col.append(diff)
            col0.append(diff0)
    
    return col, col0

def plot_mag(f1, f2, f3):
    x, y = filter_mag("HPNe", "", f1, f2, f3)
    x1, y1 = filter_mag("CV", "", f1, f2, f3)
    x2, y2 = filter_mag("E00", "DdDm1_L2", f1, f2, f3)
    x3, y3 = filter_mag("E00", "DdDm1_L3", f1, f2, f3)
    x4, y4 = filter_mag("E00", "DdDm1_L4", f1, f2, f3)
    x5, y5 = filter_mag("E00", "DdDm1_L5", f1, f2, f3)
    x6, y6 = filter_mag("E00", "N2242_L2", f1, f2, f3)
    x7, y7 = filter_mag("E00", "N2242_L3", f1, f2, f3)
    x8, y8 = filter_mag("E00", "N2242_L4", f1, f2, f3)
    x9, y9 = filter_mag("E00", "N2242_L5", f1, f2, f3)
    x10, y10 = filter_mag("E00", "K648_L2", f1, f2, f3)
    x11, y11 = filter_mag("E00", "K648_L3", f1, f2, f3)
    x12, y12 = filter_mag("E00", "K648_L4", f1, f2, f3)
    x13, y13 = filter_mag("E00", "K648_L5", f1, f2, f3)
    x14, y14 = filter_mag("E00", "BB1_L2", f1, f2, f3)
    x15, y15 = filter_mag("E00", "BB1_L3", f1, f2, f3)
    x16, y16 = filter_mag("E00", "BB1_L4", f1, f2, f3)
    x17, y17 = filter_mag("E00", "BB1_L5", f1, f2, f3)
    x18, y18 = filter_mag("E00", "Typ_L2", f1, f2, f3)
    x19, y19 = filter_mag("E00", "Typ_L3", f1, f2, f3)
    x20, y20 = filter_mag("E00", "Typ_L4", f1, f2, f3)
    x21, y21 = filter_mag("E00", "Typ_L5", f1, f2, f3)
    x22, y22 = filter_mag("E01", "DdDm1_L2", f1, f2, f3)
    x23, y23 = filter_mag("E01", "DdDm1_L3", f1, f2, f3)
    x24, y24 = filter_mag("E01", "DdDm1_L4", f1, f2, f3)
    x25, y25 = filter_mag("E01", "DdDm1_L5", f1, f2, f3)
    x26, y26 = filter_mag("E01", "N2242_L2", f1, f2, f3)
    x27, y27 = filter_mag("E01", "N2242_L3", f1, f2, f3)
    x28, y28 = filter_mag("E01", "N2242_L4", f1, f2, f3)
    x29, y29 = filter_mag("E01", "N2242_L5", f1, f2, f3)
    x30, y30 = filter_mag("E01", "K648_L2", f1, f2, f3)
    x31, y31 = filter_mag("E01", "K648_L3", f1, f2, f3)
    x32, y32 = filter_mag("E01", "K648_L4", f1, f2, f3)
    x33, y33 = filter_mag("E01", "K648_L5", f1, f2, f3)
    x34, y34 = filter_mag("E01", "BB1_L2", f1, f2, f3)
    x35, y35 = filter_mag("E01", "BB1_L3", f1, f2, f3)
    x36, y36 = filter_mag("E01", "BB1_L4", f1, f2, f3)
    x37, y37 = filter_mag("E01", "BB1_L5", f1, f2, f3)
    x38, y38 = filter_mag("E01", "Typ_L2", f1, f2, f3)
    x39, y39 = filter_mag("E01", "Typ_L3", f1, f2, f3)
    x40, y40 = filter_mag("E01", "Typ_L4", f1, f2, f3)
    x41, y41 = filter_mag("E01", "Typ_L5", f1, f2, f3)
    x42, y42 = filter_mag("E02", "DdDm1_L2", f1, f2, f3)
    x43, y43 = filter_mag("E02", "DdDm1_L3", f1, f2, f3)
    x44, y44 = filter_mag("E02", "DdDm1_L4", f1, f2, f3)
    x45, y45 = filter_mag("E02", "DdDm1_L5", f1, f2, f3)
    x46, y46 = filter_mag("E02", "N2242_L2", f1, f2, f3)
    x47, y47 = filter_mag("E02", "N2242_L3", f1, f2, f3)
    x48, y48 = filter_mag("E02", "N2242_L4", f1, f2, f3)
    x49, y49 = filter_mag("E02", "N2242_L5", f1, f2, f3)
    x50, y50 = filter_mag("E02", "K648_L2", f1, f2, f3)
    x51, y51 = filter_mag("E02", "K648_L3", f1, f2, f3)
    x52, y52 = filter_mag("E02", "K648_L4", f1, f2, f3)
    x53, y53 = filter_mag("E02", "K648_L5", f1, f2, f3)
    x54, y54 = filter_mag("E02", "BB1_L2", f1, f2, f3)
    x55, y55 = filter_mag("E02", "BB1_L3", f1, f2, f3)
    x56, y56 = filter_mag("E02", "BB1_L4", f1, f2, f3)
    x57, y57 = filter_mag("E02", "BB1_L5", f1, f2, f3)
    x58, y58 = filter_mag("E02", "Typ_L2", f1, f2, f3)
    x59, y59 = filter_mag("E02", "Typ_L3", f1, f2, f3)
    x60, y60 = filter_mag("E02", "Typ_L4", f1, f2, f3)
    x61, y61 = filter_mag("E02", "Typ_L5", f1, f2, f3)
    x62, y62 = filter_mag("E00_900", "DdDm1_L2", f1, f2, f3)
    x63, y63 = filter_mag("E00_900", "DdDm1_L3", f1, f2, f3)
    x64, y64 = filter_mag("E00_900", "DdDm1_L4", f1, f2, f3)
    x65, y65 = filter_mag("E00_900", "DdDm1_L5", f1, f2, f3)
    x66, y66 = filter_mag("E00_900", "N2242_L2", f1, f2, f3)
    x67, y67 = filter_mag("E00_900", "N2242_L3", f1, f2, f3)
    x68, y68 = filter_mag("E00_900", "N2242_L4", f1, f2, f3)
    x69, y69 = filter_mag("E00_900", "N2242_L5", f1, f2, f3)
    x70, y70 = filter_mag("E0_900", "K648_L2", f1, f2, f3)
    x71, y71 = filter_mag("E00_900", "K648_L3", f1, f2, f3)
    x72, y72 = filter_mag("E00_900", "K648_L4", f1, f2, f3)
    x73, y73 = filter_mag("E00_900", "K648_L5", f1, f2, f3)
    x74, y74 = filter_mag("E00_900", "BB1_L2", f1, f2, f3)
    x75, y75 = filter_mag("E00_900", "BB1_L3", f1, f2, f3)
    x76, y76 = filter_mag("E00_900", "BB1_L4", f1, f2, f3)
    x77, y77 = filter_mag("E00_900", "BB1_L5", f1, f2, f3)
    x78, y78 = filter_mag("E00_900", "Typ_L2", f1, f2, f3)
    x79, y79 = filter_mag("E00_900", "Typ_L3", f1, f2, f3)
    x80, y80 = filter_mag("E00_900", "Typ_L4", f1, f2, f3)
    x81, y81 = filter_mag("E00_900", "Typ_L5", f1, f2, f3)
    x82, y82 = filter_mag("E01_900", "DdDm1_L2", f1, f2, f3)
    x83, y83 = filter_mag("E01_900", "DdDm1_L3", f1, f2, f3)
    x84, y84 = filter_mag("E01_900", "DdDm1_L4", f1, f2, f3)
    x85, y85 = filter_mag("E01_900", "DdDm1_L5", f1, f2, f3)
    x86, y86 = filter_mag("E01_900", "N2242_L2", f1, f2, f3)
    x87, y87 = filter_mag("E01_900", "N2242_L3", f1, f2, f3)
    x88, y88 = filter_mag("E01_900", "N2242_L4", f1, f2, f3)
    x89, y89 = filter_mag("E01_900", "N2242_L5", f1, f2, f3)
    x90, y90 = filter_mag("E01_900", "K648_L2", f1, f2, f3)
    x91, y91 = filter_mag("E01_900", "K648_L3", f1, f2, f3)
    x92, y92 = filter_mag("E01_900", "K648_L4", f1, f2, f3)
    x93, y93 = filter_mag("E01_900", "K648_L5", f1, f2, f3)
    x94, y94 = filter_mag("E01_900", "BB1_L2", f1, f2, f3)
    x95, y95 = filter_mag("E01_900", "BB1_L3", f1, f2, f3)
    x96, y96 = filter_mag("E01_900", "BB1_L4", f1, f2, f3)
    x97, y97 = filter_mag("E01_900", "BB1_L5", f1, f2, f3)
    x98, y98 = filter_mag("E01_900", "Typ_L2", f1, f2, f3)
    x99, y99 = filter_mag("E01_900", "Typ_L3", f1, f2, f3)
    x100, y100 = filter_mag("E01_900", "Typ_L4", f1, f2, f3)
    x101, y101 = filter_mag("E01_900", "Typ_L5", f1, f2, f3)
    x102, y102 = filter_mag("E02_900", "DdDm1_L2", f1, f2, f3)
    x103, y103 = filter_mag("E02_900", "DdDm1_L3", f1, f2, f3)
    x104, y104 = filter_mag("E02_900", "DdDm1_L4", f1, f2, f3)
    x105, y105 = filter_mag("E02_900", "DdDm1_L5", f1, f2, f3)
    x106, y106 = filter_mag("E02_900", "N2242_L2", f1, f2, f3)
    x107, y107 = filter_mag("E02_900", "N2242_L3", f1, f2, f3)
    x108, y108 = filter_mag("E02_900", "N2242_L4", f1, f2, f3)
    x109, y109 = filter_mag("E02_900", "N2242_L5", f1, f2, f3)
    x110, y110 = filter_mag("E02_900", "K648_L2", f1, f2, f3)
    x111, y111 = filter_mag("E02_900", "K648_L3", f1, f2, f3)
    x112, y112 = filter_mag("E02_900", "K648_L4", f1, f2, f3)
    x113, y113 = filter_mag("E02_900", "K648_L5", f1, f2, f3)
    x114, y114 = filter_mag("E02_900", "BB1_L2", f1, f2, f3)
    x115, y115 = filter_mag("E02_900", "BB1_L3", f1, f2, f3)
    x116, y116 = filter_mag("E02_900", "BB1_L4", f1, f2, f3)
    x117, y117 = filter_mag("E02_900", "BB1_L5", f1, f2, f3)
    x118, y118 = filter_mag("E02_900", "Typ_L2", f1, f2, f3)
    x119, y119 = filter_mag("E02_900", "Typ_L3", f1, f2, f3)
    x120, y120 = filter_mag("E02_900", "Typ_L4", f1, f2, f3)
    x121, y121 = filter_mag("E02_900", "Typ_L5", f1, f2, f3)
    x122, y122= filter_mag("-DPNe", "", f1, f2, f3)
    x123, y123= filter_mag("QSOs-hz", "", f1, f2, f3)
    x124, y124 = filter_mag("QSOs-010", "",  f1, f2, f3)
    x125, y125 = filter_mag("QSOs-101", "", f1, f2, f3)
    x126, y126 = filter_mag("QSOs-201", "", f1, f2, f3)
    x127, y127 = filter_mag("QSOs-301", "", f1, f2, f3)
    x128, y128 = filter_mag("QSOs-401", "", f1, f2, f3)
    x129, y129 = filter_mag("-SFGs", "", f1, f2, f3)
    x130, y130 = filter_mag("-sys", "", f1, f2, f3)
    x131, y131 = filter_mag("-sys-IPHAS", "", f1, f2, f3) 
    x132, y132 = filter_mag("-ExtHII", "", f1, f2, f3)
    x133, y133 = filter_mag("-sys-Ext", '', f1, f2, f3)
    x134, y134 = filter_mag("-survey", '', f1, f2, f3)
    x135, y135 = filter_mag("-SNR", '', f1, f2, f3)
    x136, y136 = filter_mag("extr-SySt-raman", '', f1, f2, f3)
    x137, y137 = filter_mag("-extr-SySt", '', f1, f2, f3)
    x138, y138 = filter_mag("-sys-raman", "", f1, f2, f3)
    x139, y139 = filter_mag("-sys-IPHAS-raman", "", f1, f2, f3)
    x140, y140 = filter_mag("ngc185-raman", "", f1, f2, f3)
    x141, y141 = filter_mag("SySt-ic10", "", f1, f2, f3)
    x142, y142 = filter_mag("LOAN-HPNe-", "", f1, f2, f3)
    x143, y143 = filter_mag("1359559-HPNe-", "", f1, f2, f3)
    for a, b in zip(x, y):
        A1[0].append(a)
        B1[0].append(b)
    for a, b in zip(x1, y1):
        A1[1].append(a)
        B1[1].append(b)
    for a, b in zip(x2, y2):
        A1[2].append(a)
        B1[2].append(b)
    for a, b in zip(x3, y3):
        A1[3].append(a)
        B1[3].append(b)
    for a, b in zip(x4, y4):
        A1[4].append(a)
        B1[4].append(b)
    for a, b in zip(x5, y5):
        A1[5].append(a)
        B1[5].append(b)
    for a, b in zip(x6, y6):
        A1[6].append(a)
        B1[6].append(b)
    for a, b in zip(x7, y7):
        A1[7].append(a)
        B1[7].append(b)
    for a, b in zip(x8, y8):
        A1[8].append(a)
        B1[8].append(b)
    for a, b in zip(x9, y9):
        A1[9].append(a)
        B1[9].append(b)
    for a, b in zip(x10, y10):
        A1[10].append(a)
        B1[10].append(b)
    for a, b in zip(x11, y11):
        A1[11].append(a)
        B1[11].append(b)
    for a, b in zip(x12, y12):
        A1[12].append(a)
        B1[12].append(b)
    for a, b in zip(x13, y13):
        A1[13].append(a)
        B1[13].append(b)
    for a, b in zip(x14, y14):
        A1[14].append(a)
        B1[14].append(b)
    for a, b in zip(x15, y15):
        A1[15].append(a)
        B1[15].append(b)
    for a, b in zip(x16, y16):
        A1[16].append(a)
        B1[16].append(b)
    for a, b in zip(x17, y17):
        A1[17].append(a)
        B1[17].append(b)
    for a, b in zip(x18, y18):
        A1[18].append(a)
        B1[18].append(b)
    for a, b in zip(x19, y19):
        A1[19].append(a)
        B1[19].append(b)
    for a, b in zip(x20, y20):
        A1[20].append(a)
        B1[20].append(b)
    for a, b in zip(x21, y21):
        A1[21].append(a)
        B1[21].append(b)
    for a, b in zip(x22, y22):
        A1[22].append(a)
        B1[22].append(b)
    for a, b in zip(x23, y23):
        A1[23].append(a)
        B1[23].append(b)
    for a, b in zip(x24, y24):
        A1[24].append(a)
        B1[24].append(b)
    for a, b in zip(x25, y25):
        A1[25].append(a)
        B1[25].append(b)
    for a, b in zip(x26, y26):
        A1[26].append(a)
        B1[26].append(b)
    for a, b in zip(x27, y27):
        A1[27].append(a)
        B1[27].append(b)
    for a, b in zip(x28, y28):
        A1[28].append(a)
        B1[28].append(b)
    for a, b in zip(x29, y29):
        A1[29].append(a)
        B1[29].append(b)
    for a, b in zip(x30, y30):
        A1[30].append(a)
        B1[30].append(b)
    for a, b in zip(x31, y31):
        A1[31].append(a)
        B1[31].append(b)
    for a, b in zip(x32, y32):
        A1[32].append(a)
        B1[32].append(b)
    for a, b in zip(x33, y33):
        A1[33].append(a)
        B1[33].append(b)
    for a, b in zip(x34, y34):
        A1[34].append(a)
        B1[34].append(b)
    for a, b in zip(x35, y35):
        A1[35].append(a)
        B1[35].append(b)
    for a, b in zip(x36, y36):
        A1[36].append(a)
        B1[36].append(b)
    for a, b in zip(x37, y37):
        A1[37].append(a)
        B1[37].append(b)
    for a, b in zip(x38, y38):
        A1[38].append(a)
        B1[38].append(b)
    for a, b in zip(x39, y39):
        A1[39].append(a)
        B1[39].append(b)
    for a, b in zip(x40, y40):
        A1[40].append(a)
        B1[40].append(b)
    for a, b in zip(x41, y41):
        A1[41].append(a)
        B1[41].append(b)
    for a, b in zip(x42, y42):
        A1[42].append(a)
        B1[42].append(b)
    for a, b in zip(x43, y43):
        A1[43].append(a)
        B1[43].append(b)
    for a, b in zip(x44, y44):
        A1[44].append(a)
        B1[44].append(b)
    for a, b in zip(x45, y45):
        A1[45].append(a)
        B1[45].append(b)
    for a, b in zip(x46, y46):
        A1[46].append(a)
        B1[46].append(b)
    for a, b in zip(x47, y47):
        A1[47].append(a)
        B1[47].append(b)
    for a, b in zip(x48, y48):
        A1[48].append(a)
        B1[48].append(b)
    for a, b in zip(x49, y49):
        A1[49].append(a)
        B1[49].append(b)
    for a, b in zip(x50, y50):
        A1[50].append(a)
        B1[50].append(b)
    for a, b in zip(x51, y51):
        A1[51].append(a)
        B1[51].append(b)
    for a, b in zip(x52, y52):
        A1[52].append(a)
        B1[52].append(b)
    for a, b in zip(x53, y53):
        A1[53].append(a)
        B1[53].append(b)
    for a, b in zip(x54, y54):
        A1[54].append(a)
        B1[54].append(b)
    for a, b in zip(x55, y55):
        A1[55].append(a)
        B1[55].append(b)
    for a, b in zip(x56, y56):
        A1[56].append(a)
        B1[56].append(b)
    for a, b in zip(x57, y57):
        A1[57].append(a)
        B1[57].append(b)
    for a, b in zip(x58, y58):
        A1[58].append(a)
        B1[58].append(b)
    for a, b in zip(x59, y59):
        A1[59].append(a)
        B1[59].append(b)
    for a, b in zip(x60, y60):
        A1[60].append(a)
        B1[60].append(b)
    for a, b in zip(x61, y61):
        A1[61].append(a)
        B1[61].append(b)
    for a, b in zip(x62, y62):
        A1[62].append(a)
        B1[62].append(b)
    for a, b in zip(x63, y63):
        A1[63].append(a)
        B1[63].append(b)
    for a, b in zip(x64, y64):
        A1[64].append(a)
        B1[64].append(b)
    for a, b in zip(x65, y65):
        A1[65].append(a)
        B1[65].append(b)
    for a, b in zip(x66, y66):
        A1[66].append(a)
        B1[66].append(b)
    for a, b in zip(x67, y67):
        A1[67].append(a)
        B1[67].append(b)
    for a, b in zip(x68, y68):
        A1[68].append(a)
        B1[68].append(b)
    for a, b in zip(x69, y69):
        A1[69].append(a)
        B1[69].append(b)
    for a, b in zip(x70, y70):
        A1[70].append(a)
        B1[70].append(b)
    for a, b in zip(x72, y72):
        A1[72].append(a)
        B1[72].append(b)
    for a, b in zip(x73, y73):
        A1[73].append(a)
        B1[73].append(b)
    for a, b in zip(x74, y74):
        A1[74].append(a)
        B1[74].append(b)
    for a, b in zip(x75, y75):
        A1[75].append(a)
        B1[75].append(b)
    for a, b in zip(x76, y76):
        A1[76].append(a)
        B1[76].append(b)
    for a, b in zip(x77, y77):
        A1[77].append(a)
        B1[77].append(b)
    for a, b in zip(x78, y78):
        A1[78].append(a)
        B1[78].append(b)
    for a, b in zip(x79, y79):
        A1[79].append(a)
        B1[79].append(b)
    for a, b in zip(x80, y80):
        A1[80].append(a)
        B1[80].append(b)
    for a, b in zip(x81, y81):
        A1[81].append(a)
        B1[81].append(b)
    for a, b in zip(x82, y82):
        A1[82].append(a)
        B1[82].append(b)
    for a, b in zip(x83, y83):
        A1[83].append(a)
        B1[83].append(b)
    for a, b in zip(x84, y84):
        A1[84].append(a)
        B1[84].append(b)
    for a, b in zip(x85, y85):
        A1[85].append(a)
        B1[85].append(b)
    for a, b in zip(x86, y86):
        A1[86].append(a)
        B1[86].append(b)
    for a, b in zip(x87, y87):
        A1[87].append(a)
        B1[87].append(b)
    for a, b in zip(x88, y88):
        A1[88].append(a)
        B1[88].append(b)
    for a, b in zip(x89, y89):
        A1[89].append(a)
        B1[89].append(b)
    for a, b in zip(x90, y90):
        A1[90].append(a)
        B1[90].append(b)
    for a, b in zip(x91, y91):
        A1[91].append(a)
        B1[91].append(b)
    for a, b in zip(x92, y92):
        A1[92].append(a)
        B1[92].append(b)
    for a, b in zip(x93, y93):
        A1[93].append(a)
        B1[93].append(b)
    for a, b in zip(x94, y94):
        A1[94].append(a)
        B1[94].append(b)
    for a, b in zip(x95, y95):
        A1[95].append(a)
        B1[95].append(b)
    for a, b in zip(x96, y96):
        A1[96].append(a)
        B1[96].append(b)
    for a, b in zip(x97, y97):
        A1[97].append(a)
        B1[97].append(b)
    for a, b in zip(x98, y98):
        A1[98].append(a)
        B1[98].append(b)
    for a, b in zip(x99, y99):
        A1[99].append(a)
        B1[99].append(b)
    for a, b in zip(x100, y100):
        A1[100].append(a)
        B1[100].append(b)
    for a, b in zip(x101, y101):
        A1[101].append(a)
        B1[101].append(b)
    for a, b in zip(x102, y102):
        A1[102].append(a)
        B1[102].append(b)
    for a, b in zip(x103, y103):
        A1[103].append(a)
        B1[103].append(b)
    for a, b in zip(x104, y104):
        A1[104].append(a)
        B1[104].append(b)
    for a, b in zip(x105, y105):
        A1[105].append(a)
        B1[105].append(b)
    for a, b in zip(x106, y106):
        A1[106].append(a)
        B1[106].append(b)
    for a, b in zip(x107, y107):
        A1[107].append(a)
        B1[107].append(b)
    for a, b in zip(x108, y108):
        A1[108].append(a)
        B1[108].append(b)
    for a, b in zip(x109, y109):
        A1[109].append(a)
        B1[109].append(b)
    for a, b in zip(x110, y110):
        A1[110].append(a)
        B1[110].append(b)
    for a, b in zip(x111, y111):
        A1[111].append(a)
        B1[111].append(b)
    for a, b in zip(x112, y112):
        A1[112].append(a)
        B1[112].append(b)
    for a, b in zip(x113, y113):
        A1[113].append(a)
        B1[113].append(b)
    for a, b in zip(x114, y114):
        A1[114].append(a)
        B1[114].append(b)
    for a, b in zip(x115, y115):
        A1[115].append(a)
        B1[115].append(b)
    for a, b in zip(x116, y116):
        A1[116].append(a)
        B1[116].append(b)
    for a, b in zip(x117, y117):
        A1[117].append(a)
        B1[117].append(b)
    for a, b in zip(x118, y118):
        A1[118].append(a)
        B1[118].append(b)
    for a, b in zip(x119, y119):
        A1[119].append(a)
        B1[119].append(b)
    for a, b in zip(x120, y120):
        A1[120].append(a)
        B1[120].append(b)
    for a, b in zip(x121, y121):
        A1[121].append(a)
        B1[121].append(b)
    for a, b in zip(x122, y122):
        A1[122].append(a)
        B1[122].append(b)
    for a, b in zip(x123, y123): #same list
        A1[123].append(a)
        B1[123].append(b)
    for a, b in zip(x124, y124):
        A1[124].append(a)
        B1[124].append(b)
    for a, b in zip(x125, y125):
        A1[125].append(a)
        B1[125].append(b)
    for a, b in zip(x126, y126):
        A1[126].append(a)
        B1[126].append(b)
    for a, b in zip(x127, y127):  #same list
        A1[123].append(a)
        B1[123].append(b)
    for a, b in zip(x128, y128):
        A1[127].append(a)
        B1[127].append(b)
    for a, b in zip(x129, y129):
        A1[128].append(a)
        B1[128].append(b)
    for a, b in zip(x130, y130):
        A1[129].append(a)
        B1[129].append(b)
    for a, b in zip(x131, y131):
        A1[130].append(a)
        B1[130].append(b)
    for a, b in zip(x132, y132):
        A1[131].append(a)
        B1[131].append(b)
    for a, b in zip(x133, y133):
        A1[132].append(a)
        B1[132].append(b)
    for a, b in zip(x134, y134):
        A1[133].append(a)
        B1[133].append(b)
    for a, b in zip(x135, y135):
        A1[134].append(a)
        B1[134].append(b)
    for a, b in zip(x136, y136):
        A1[135].append(a)
        B1[135].append(b)
    for a, b in zip(x137, y137):
        A1[136].append(a)
        B1[136].append(b)
    for a, b in zip(x138, y138):
        A1[137].append(a)
        B1[137].append(b)
    for a, b in zip(x139, y139):
        A1[138].append(a)
        B1[138].append(b)
    for a, b in zip(x140, y140):
        A1[139].append(a)
        B1[139].append(b)
    for a, b in zip(x141, y141):
        A1[140].append(a)
        B1[140].append(b)
    for a, b in zip(x142, y142):
        A1[141].append(a)
        B1[141].append(b)
    for a, b in zip(x143, y143):
        A1[142].append(a)
        B1[142].append(b)

label = []
label1 = ["H4-1", "PNG 135.9+55.9"]
n = 143
A1, B1 = [[] for _ in range(n)], [[] for _ in range(n)]
d_644_jplus, d_768_jplus = [], []
d_644_jplus1, d_768_jplus1 = [], []

for file_name in file_list:
    with open(file_name) as f:
        data = json.load(f)
        if data['id'].endswith("1-HPNe"):
            label.append("")
        # elif data['id'].endswith("SLOAN-HPNe-"):
        #     label.append("H4-1")
        # elif data['id'].endswith("1359559-HPNe"):
        #     label.append("PNG 135.9+55.9")
        elif data['id'].startswith("ngc"):
            label.append("")
        elif data['id'].startswith("mwc"):
            label.append("")
        plot_mag("F610_r_sdss", "F660", "F760_i_sdss")


#errx, erry = [0.85961154017381602, 0.34603468034288126], [1.9523813664343348, 0.30832288270577646] #comparison between convolved and sloan

#errx, erry = [0.0587, 0.1274], [0.0435, 0.1366 ]
# errx, erry = [1.1, 0.5, 0.5, 0.5], [0.8, 0.5, 0.5, 0.5]
err_zp_h4 = [0.128, 0.020, 0.303, 0.227, 0.235, 0.165, 0.160, 0.138, 0.145, 0.177, 0.193, 0.092] #old error zero point
#err_zp_h4 = [0.05, 0.06, 0.07, 0.06, 0.06, 0.04, 0.04, 0.04, 0.04, 0.04,  0.05, 0.02]
err_zp_pn135 =[0.102, 0.0, 0.314, 0.341, 0.273, 0.261, 0.257, 0.269, 0.309, 0.273, 0.215, 0.100 ] #old error zero point
#err_zp_pn135 =[0.05, 0.06, 0.07, 0.06, 0.06, 0.04, 0.04, 0.04, 0.04, 0.04, 0.05, 0.02]
errx_con, erry_con = [0.86, 0, 0, 0, 0.81], [0.95, 0, 0, 0,0.83]

# err_sloan_h4 = [0.01, 0.00, 0.00, 0.01, 0.02]
# err_sloan_pn135 = [0.01, 0.00, 0.01, 0.01, 0.03]

err_obser_pn135=[0.014, 0.014, 0.03, 0.03, 0.03]

#error computing by Valera
err_zpVale_h4 = [0.061, 0.029, 0.067, 0.036, 0.044, 0.042, 0.043, 0.048, 0.030]
err_zpVale_pn135 = [0.115, 0.103, 0.127, 0.073, 0.073, 0.073, 0.078, 0.071, 0.070]

#Include the magnitudes from JPLUS images
pattern1 = "JPLUS-data/H4-1-phot/*6pix.json"
file_list1 = glob.glob(pattern1)
for file_name1 in file_list1:
    with open(file_name1) as f1:
        data1 = json.load(f1)
        fil1 = data1["J0625_rSDSS"]-25+23.335#-1.12
        fil2 = data1["J0660"]-25+20.859
        fil3 = data1["J0766_iSDSS"]-25+23.122
        diff = fil1 - fil2
        diff0 = fil1 - fil3
        d_644_jplus.append(diff)
        d_768_jplus.append(diff0)
#err_h41x, err_h41y = [], []
#for i in err_zp_h4:
err_h4x = np.sqrt(err_zp_h4[7]**2+err_zp_h4[9]**2)
err_h4y = np.sqrt(err_zp_h4[7]**2+err_zp_h4[8]**2)
    #err_h41x.append(err_h4)
    #err_h41y.append(err_h4_)


pattern2 = "JPLUS-data/PNG135coadded-phot/*6pix.json"
file_list2 = glob.glob(pattern2)
for file_name2 in file_list2:
    with open(file_name2) as f2:
        data2 = json.load(f2)
        fil1 = data2["J0625_rSDSS"]-25+23.565#-1.162
        fil2 = data2["J0660"]-25+21.058
        fil3 = data2["J0766_iSDSS"]-25+23.255
        diff = fil1 - fil2
        diff0 = fil1 - fil3
        d_644_jplus.append(diff)
        d_768_jplus.append(diff0)

    
#error propagation
# err_pn135x, err_pn135y  = [], []
# for i in err_zp_pn135:
err_pn13x = np.sqrt(err_zp_pn135[7]**2+err_zp_pn135[9]**2)
err_pn13y = np.sqrt(err_zp_pn135[7]**2+err_zp_pn135[8]**2)
    # err_pn135x.append(err_pn13)
    # err_pn135y.append(err_pn13_)

#error observationl (Papers)
err_sdss_pn35x=np.sqrt(err_obser_pn135[2]**2+err_obser_pn135[4]**2)
err_sdss_pn35y=np.sqrt(err_obser_pn135[2]**2+err_obser_pn135[3]**2)

#Progation error with Valera's erros
err_Val_h4x= np.sqrt(err_zpVale_h4[5]**2+err_zpVale_h4[7]**2)
err_Val_h4y= np.sqrt(err_zpVale_h4[5]**2+err_zpVale_h4[6]**2)
err_Val_pn135x= np.sqrt(err_zpVale_pn135[5]**2+err_zpVale_pn135[7]**2)
err_Val_pn135y= np.sqrt(err_zpVale_pn135[5]**2+err_zpVale_pn135[6]**2)

# pattern1 = "JPLUS-data/CICgy/*6pix.json"
# file_list1 = glob.glob(pattern1)
# for file_name1 in file_list1:
#     with open(file_name1) as f1:
#         data1 = json.load(f1)
#         fil1 = data1["J0625_rSDSS"]-25+23.736
#         fil2 = data1["J0660"]-25+21.192
#         fil3 = data1["J0766_iSDSS"]-25+23.477
#         diff = fil1 - fil2
#         diff0 = fil1 - fil3
#         d_644_jplus.append(diff)
#         d_768_jplus.append(diff0)

# pattern2 = "JPLUS-data/TXCVn/*6pix.json"
# file_list2 = glob.glob(pattern2)
# for file_name2 in file_list2:
#     with open(file_name2) as f2:
#         data2 = json.load(f2)
#         fil1 = data2["J0625_rSDSS"]-25+23.616
#         fil2 = data2["J0660"]-25+21.072
#         fil3 = data2["J0766_iSDSS"]-25+23.313
#         diff = fil1 - fil2
#         diff0 = fil1 - fil3
#         d_644_jplus.append(diff)
#         d_768_jplus.append(diff0)


lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax1 = fig.add_subplot(111)
ax1.set_xlim(xmin=-3.0,xmax=3.0)
ax1.set_ylim(ymin=-1.0,ymax=3.0)
#ax1.set_xlim(xmin=-2.5,xmax=2.0)
plt.tick_params(axis='x', labelsize=18) 
plt.tick_params(axis='y', labelsize=18)
plt.xlabel(r'$r - i$', fontsize= 22)
plt.ylabel(r'$r - J0660$', fontsize= 22)
ax1.scatter(B1[62], A1[62],  c= "orange", alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral )
ax1.scatter(B1[63], A1[63],  c= "orange", alpha=.8, marker='D', s=7,  lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[64], A1[64],  c= "orange", alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[65], A1[65],  c= "orange", alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[66], A1[66],  c= "green", alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[67], A1[67],  c= "green", alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[68], A1[68],  c= "green", alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[69], A1[69],  c= "green", alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[70], A1[70],  c= "brown", alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[71], A1[71],  c= "brown",  alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[72], A1[72],  c= "brown",  alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[73], A1[73],  c= "brown",  alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[74], A1[74],  c= "cyan",  alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[75], A1[75],  c= "cyan",  alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[76], A1[76],  c= "cyan", alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[77], A1[77],  c= "cyan",  alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[78], A1[78],  c= "magenta",   alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[79], A1[79],  c= "magenta",  alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[80], A1[80],  c= "magenta",   alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[81], A1[81],  c= "magenta",  alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[82], A1[82],  c= "orange",   alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[83], A1[83],  c= "orange",   alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[84], A1[84],  c= "orange",   alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[85], A1[85],  c= "orange",   alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[86], A1[86],  c= "green",  alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[87], A1[87],  c= "green", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[88], A1[88],  c= "green", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[89], A1[89],  c= "green", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[90], A1[90],  c= "brown", alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[91], A1[91],  c= "brown", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[92], A1[92],  c= "brown", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[93], A1[93],  c= "brown", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[94], A1[94],  c= "cyan", alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[95], A1[95],  c= "cyan", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[96], A1[96],  c= "cyan", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[97], A1[97],  c= "cyan", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[98], A1[98],  c= "magenta", alpha=.4, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[99], A1[99],  c= "magenta", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[100], A1[100],  c= "magenta", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[101], A1[101],  c= "magenta", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax1.scatter(B1[102], A1[102],  c= "orange", alpha=.8, s=30,   marker='s', lw=0, cmap=plt.cm.spectral)#, label='BM DdDm1 L2') #
ax1.scatter(B1[103], A1[103],  c= "orange", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral)#, label='BM DdDm1 L3')
ax1.scatter(B1[104], A1[104],  c= "orange", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral)#, label='BM DdDm1 L4')
ax1.scatter(B1[105], A1[105],  c= "orange", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral)#, label='BM DdDm1 L5')
ax1.scatter(B1[106], A1[106],  c= "green", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral)#,  label='BM N2242 L2')
ax1.scatter(B1[107], A1[107],  c= "green", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral)#,  label='BM N2242 L3')
ax1.scatter(B1[108], A1[108],  c= "green", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral)#,  label='BM N2242 L4')
ax1.scatter(B1[109], A1[109],  c= "green", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral)#,  label='BM N2242 L5')
ax1.scatter(B1[110], A1[110],  c= "brown", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral)#, label='BM K648 L2')
ax1.scatter(B1[111], A1[111],  c= "brown", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral)#, label='BM K648 L3')
ax1.scatter(B1[112], A1[112],  c= "brown", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral)#, label='BM K648 L4')
ax1.scatter(B1[113], A1[113],  c= "brown", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral)#, label='BM K648 L5')
ax1.scatter(B1[114], A1[114],  c= "cyan", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral)#, label='BM BB1 L2')
ax1.scatter(B1[115], A1[115],  c= "cyan", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral)#, label='BM BB1 L3')
ax1.scatter(B1[116], A1[116],  c= "cyan", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral)#, label='BM BB1 L4')
ax1.scatter(B1[117], A1[117],  c= "cyan", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral)#, label='BM BB1 L5')
ax1.scatter(B1[118], A1[118],  c= "magenta", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral)#, label='BM Typ L2')
ax1.scatter(B1[119], A1[119],  c= "magenta", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral)#, label='BM Typ L3')
ax1.scatter(B1[120], A1[120],  c= "magenta", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral)#, label='BM Typ L4')
ax1.scatter(B1[121], A1[121],  c= "magenta", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral)#, label='BM Typ L5')
ax1.scatter(B1[2], A1[2], facecolors='none', edgecolors='orange', alpha=0.8, marker='s', s=7)      # c= "orange", alpha=0.8, marker='s', s=7 )
ax1.scatter(B1[3], A1[3], facecolors='none', edgecolors='orange', alpha=0.8, marker='D', s=7)
ax1.scatter(B1[4], A1[4],  facecolors='none', edgecolors='orange', alpha=0.8, marker='^', s=17)
ax1.scatter(B1[5], A1[5], facecolors='none', edgecolors='orange', alpha=0.8, marker='*', s=17)
ax1.scatter(B1[6], A1[6], facecolors='none', edgecolors='green', alpha=0.8, marker='s', s=7)      # c= "green", alpha=0.8, marker='s', s=7)
ax1.scatter(B1[7], A1[7], facecolors='none', edgecolors='green', alpha=0.8, marker='D', s=7)
ax1.scatter(B1[8], A1[8],  facecolors='none', edgecolors='green', alpha=0.8, marker='^', s=17)
ax1.scatter(B1[9], A1[9],  facecolors='none', edgecolors='green', alpha=0.8, marker='*', s=17)
ax1.scatter(B1[10], A1[10],  facecolors='none', edgecolors='brown', alpha=0.8, marker='s', s=7) # c= "brown", alpha=0.8, marker='s', s=7
ax1.scatter(B1[11], A1[11],  facecolors='none', edgecolors='brown',  alpha=0.8, marker='D', s=7)
ax1.scatter(B1[12], A1[12],  facecolors='none', edgecolors='brown',  alpha=0.8, marker='^', s=17)
ax1.scatter(B1[13], A1[13],  facecolors='none', edgecolors='brown',  alpha=0.8, marker='*', s=17)
ax1.scatter(B1[14], A1[14],  facecolors='none', edgecolors='cyan',  alpha=0.8, marker='s', s=7)   #c= "cyan",  alpha=0.8, marker='s', s=7
ax1.scatter(B1[15], A1[15],  facecolors='none', edgecolors='cyan',  alpha=0.8, marker='D', s=7)
ax1.scatter(B1[16], A1[16],  facecolors='none', edgecolors='cyan', alpha=0.8, marker='^', s=17)
ax1.scatter(B1[17], A1[17],  facecolors='none', edgecolors='cyan',  alpha=0.8, marker='*', s=17)
ax1.scatter(B1[18], A1[18],  facecolors='none', edgecolors='magenta',   alpha=0.8, marker='s', s=7)#c= "magenta",alpha=0.8, marker='s', s=7)
ax1.scatter(B1[19], A1[19],  facecolors='none', edgecolors='magenta',  alpha=0.8, marker='D', s=7)
ax1.scatter(B1[20], A1[20],  facecolors='none', edgecolors='magenta',   alpha=0.8, marker='^', s=17)
ax1.scatter(B1[21], A1[21],  facecolors='none', edgecolors='magenta',  alpha=0.8, marker='*', s=17)
ax1.scatter(B1[22], A1[22],  facecolors='none', edgecolors='orange',   alpha=0.8, s=13,  marker='s')#c= "orange",alpha=0.8, s=13, marker='s')
ax1.scatter(B1[23], A1[23],  facecolors='none', edgecolors='orange',   alpha=0.8, s=13,  marker='D')
ax1.scatter(B1[24], A1[24],  facecolors='none', edgecolors='orange',   alpha=0.8, s=23,  marker='^')
ax1.scatter(B1[25], A1[25],  facecolors='none', edgecolors='orange',   alpha=0.8, s=23,  marker='*')
ax1.scatter(B1[26], A1[26],  facecolors='none', edgecolors='green',  alpha=0.8, s=13,  marker='s') # c= "green",alpha=0.8, s=13,  marker='s'
ax1.scatter(B1[27], A1[27],  facecolors='none', edgecolors='green', alpha=0.8, s=13,  marker='D')
ax1.scatter(B1[28], A1[28],  facecolors='none', edgecolors='green', alpha=0.8, s=23,  marker='^')
ax1.scatter(B1[29], A1[29],  facecolors='none', edgecolors='green', alpha=0.8, s=23,  marker='*')
ax1.scatter(B1[30], A1[30],  facecolors='none', edgecolors='brown', alpha=0.8, s=13,  marker='s')  #c= "brown", alpha=0.8, s=13,  marker='s')
ax1.scatter(B1[31], A1[31],  facecolors='none', edgecolors='brown', alpha=0.8, s=13,  marker='D')
ax1.scatter(B1[32], A1[32],  facecolors='none', edgecolors='brown', alpha=0.8, s=23,  marker='^')
ax1.scatter(B1[33], A1[33],  facecolors='none', edgecolors='brown', alpha=0.8, s=23,  marker='*')
ax1.scatter(B1[34], A1[34],  facecolors='none', edgecolors='cyan', alpha=0.8, s=13,  marker='s')  #c= "cyan", alpha=0.8, s=13,  marker='s')
ax1.scatter(B1[35], A1[35],  facecolors='none', edgecolors='cyan', alpha=0.8, s=13,  marker='D')
ax1.scatter(B1[36], A1[36],  facecolors='none', edgecolors='cyan', alpha=0.8, s=23,  marker='^')
ax1.scatter(B1[37], A1[37],  facecolors='none', edgecolors='cyan', alpha=0.8, s=23,  marker='*')
ax1.scatter(B1[38], A1[38],  facecolors='none', edgecolors='magenta', alpha=0.8, s=13,  marker='s') #c= "magenta",alpha=0.8, s=13,marker='s')
ax1.scatter(B1[39], A1[39],  facecolors='none', edgecolors='magenta', alpha=0.8, s=13,  marker='D')
ax1.scatter(B1[40], A1[40],  facecolors='none', edgecolors='magenta', alpha=0.8, s=23,  marker='^')
ax1.scatter(B1[41], A1[41],  facecolors='none', edgecolors='magenta', alpha=0.8, s=23,  marker='*')
ax1.scatter(B1[42], A1[42],  facecolors='none', edgecolors='orange', alpha=0.8, s=30,   marker='s') #c= "orange",alpha=0.8, s=30, marker='s', 
ax1.scatter(B1[43], A1[43],  facecolors='none', edgecolors='orange', alpha=0.8, s=30,  marker='D')
ax1.scatter(B1[44], A1[44],  facecolors='none', edgecolors='orange', alpha=0.8, s=40,  marker='^')
ax1.scatter(B1[45], A1[45],  facecolors='none', edgecolors='orange', alpha=0.8, s=40,  marker='*')
ax1.scatter(B1[46], A1[46],  facecolors='none', edgecolors='green', alpha=0.8, s=30,  marker='s') #c= "green", alpha=0.8, s=30,  marker='s',
ax1.scatter(B1[47], A1[47],  facecolors='none', edgecolors='green', alpha=0.8, s=30,  marker='D')
ax1.scatter(B1[48], A1[48],  facecolors='none', edgecolors='green', alpha=0.8, s=40,  marker='^')
ax1.scatter(B1[49], A1[49],  facecolors='none', edgecolors='green', alpha=0.8, s=40,  marker='*')
ax1.scatter(B1[50], A1[50],  facecolors='none', edgecolors='brown', alpha=0.8, s=30,  marker='s') #c= "brown", alpha=0.8, s=30,  marker='s',
ax1.scatter(B1[51], A1[51],  facecolors='none', edgecolors='brown', alpha=0.8, s=30,  marker='D')
ax1.scatter(B1[52], A1[52],  facecolors='none', edgecolors='brown', alpha=0.8, s=40,  marker='^')
ax1.scatter(B1[53], A1[53],  facecolors='none', edgecolors='brown', alpha=0.8, s=40,  marker='*')
ax1.scatter(B1[54], A1[54],  facecolors='none', edgecolors='cyan', alpha=0.8, s=30,  marker='s') #c= "cyan", alpha=0.8, s=30,  marker='s',
ax1.scatter(B1[55], A1[55],  facecolors='none', edgecolors='cyan', alpha=0.8, s=30,  marker='D')
ax1.scatter(B1[56], A1[56],  facecolors='none', edgecolors='cyan', alpha=0.8, s=40,  marker='^')
ax1.scatter(B1[57], A1[57],  facecolors='none', edgecolors='cyan', alpha=0.8, s=40,  marker='*')
ax1.scatter(B1[58], A1[58],  facecolors='none', edgecolors='magenta', alpha=0.8, s=30,  marker='s') #c= "magenta", alpha=0.8, s=30,  marker='s'
ax1.scatter(B1[59], A1[59],  facecolors='none', edgecolors='magenta', alpha=0.8, s=30,  marker='D')
ax1.scatter(B1[60], A1[60],  facecolors='none', edgecolors='magenta', alpha=0.8, s=40,  marker='^')
ax1.scatter(B1[61], A1[61],  facecolors='none', edgecolors='magenta', alpha=0.8, s=40,  marker='*')

ax1.scatter(B1[0], A1[0], c='black', alpha=0.8, s=40, label='Obs. halo PNe')
(_, caps, _) = ax1.errorbar(B1[0], A1[0], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)


ax1.scatter(B1[141], A1[141], c='black', alpha=0.8, s=40)#, label='Obs. halo PNe')
ax1.errorbar(B1[141], A1[141], yerr=0.2,  lolims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)
ax1.errorbar(B1[141], A1[141], xerr=0.2,  xuplims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)

ax1.scatter(B1[142], A1[142], c='black', alpha=0.8, s=40)
(_, caps, _) = ax1.errorbar(B1[142], A1[142], xerr=err_sdss_pn35x, yerr=err_sdss_pn35y, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)

#ax1.errorbar(B1[141], A1[141], yerr=0.1,  lolims= True)
# (_, caps, _) = ax1.errorbar(B1[0], A1[0], xerr=errx_con, yerr=erry_con, marker='o', fmt='ko', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
# for cap in caps:
#     cap.set_markeredgewidth(1)
#ax1.scatter(B1[62],A1[62],  c= "yellow", alpha=0.8, marker='o', label='Obs. disk PN')
ax1.scatter(B1[1], A1[1], c='purple', alpha=0.8, s=40, label='SDSS CVs')
ax1.scatter(B1[127], A1[127],  c= "mediumaquamarine" , alpha=0.8, marker='s', s=40, label='SDSS QSOs (4.01<z<5.0)')
ax1.scatter(B1[123], A1[123],  c= "royalblue", alpha=0.8, marker='D', s=40, label='SDSS QSOs (3.01<z<4.0)')
ax1.scatter(B1[126], A1[126],  c= "goldenrod", alpha=0.8, s=41, marker='^',  label='SDSS QSOs (2.01<z<3.0)')
ax1.scatter(B1[125], A1[125],  c= "salmon", alpha=0.8, s=40, marker='*',  label='SDSS QSOs (1.01<z<2.0)')
ax1.scatter(B1[124], A1[124],  c= "sage", alpha=0.8, s=40,  marker='o',  label='SDSS QSOs (0.01<z<1.0)')
ax1.scatter(B1[128], A1[128],  c= "white", alpha=0.3, s=41, marker='^', label='SDSS SFGs ')
ax1.scatter(B1[129], A1[129],  facecolors='none', edgecolors='red', alpha=0.8, s=40, marker='s')#, label='Obs. SySts ')
ax1.scatter(B1[137], A1[137],  c= "red", alpha=0.8, s=40, marker='s', label='Obs. SySts ')
#ax1.scatter(B1[72], A1[72],  c= "red", alpha=0.8, marker='D', label='Symbiotics in NGC 55')
ax1.scatter(B1[135], A1[135],  c= "red", alpha=0.8, s=40, marker='D', label=' Obs. SySts in NGC 205')
ax1.scatter(B1[136], A1[136],  facecolors='none', edgecolors='red', alpha=0.8, s=40, marker='D')  #label=' SySts in NGC 205')
ax1.scatter(B1[130], A1[130],  facecolors='none', edgecolors='red', alpha=0.8, s=40, marker='^')#,  label='IPHAS SySts')
ax1.scatter(B1[138], A1[138],  c= "red", alpha=0.8, s=41, marker='^', label='IPHAS SySts')
ax1.scatter(B1[140], A1[140],  facecolors='none', edgecolors='red', alpha=0.8, s=40, marker='o',  label='Obs. SySts in IC10 ')
ax1.scatter(B1[139], A1[139],  c= "red", alpha=0.8, s=41, marker='v', label=' Obs. SySts in NGC 185')
#ax1.scatter(B1[73], A1[73],  c= "red", alpha=0.8, marker='o', label='C. Buil Symbiotics')
ax1.scatter(B1[131], A1[131],  c= "gray", alpha=0.8, s=40, marker='D', label='Obs. HII region in NGC 55')
#ax1.scatter(B1[74], A1[74],  c= "black", alpha=0.8, marker='.', label='SN Remanents')

ax1.scatter(d_768_jplus[0], d_644_jplus[0],  c= "b", alpha=0.8, marker='o', s=70, label='J-PLUS H4-1')
(_, caps, _) = ax1.errorbar(d_768_jplus[0], d_644_jplus[0], xerr=err_Val_h4x, yerr=err_Val_h4y, marker='.', fmt='b.', elinewidth=1.4, markeredgewidth=1.4, markersize=14,)
for cap in caps:
    cap.set_markeredgewidth(1)
ax1.scatter(d_768_jplus[1], d_644_jplus[1],  c= "g", alpha=0.8, marker='o', s=70, label='J-PLUS PNG135.9+55.9 ')
(_, caps, _) = ax1.errorbar(d_768_jplus[1], d_644_jplus[1], xerr=err_Val_pn135x, yerr=err_Val_pn135y, marker='.', fmt='g.', elinewidth=1.4, markeredgewidth=1.4, markersize=14,) #fmt='yo',
for cap in caps:
    cap.set_markeredgewidth(1)

# ax1.scatter(d_768_jplus[2], d_644_jplus[2],  c= "y", alpha=0.8, marker='s', label='J-PLUS CI Cyg')
# (_, caps, _) = ax1.errorbar(d_768_jplus[2], d_644_jplus[2], xerr=errx[2], yerr=erry[2], marker='s', fmt='ys', elinewidth=.8, markeredgewidth=.8, markersize=8,)
# for cap in caps:
#     cap.set_markeredgewidth(1)
# ax1.scatter(d_768_jplus[3], d_644_jplus[3],  c= "m", alpha=0.8, marker='s',  label='J-PLUS TX CVn')
# (_, caps, _) = ax1.errorbar(d_768_jplus[3], d_644_jplus[3], xerr=errx[3], yerr=erry[3], marker='s', fmt='ms', elinewidth=.8, markeredgewidth=.8, markersize=8,) #fmt='yo',
# for cap in caps:
#     cap.set_markeredgewidth(1)

for label_, x, y in zip(label, B1[0], A1[0]):
    ax1.annotate(label_, (x, y), alpha=5, size=8,
                   xytext=(-4.0, 3.6), textcoords='offset points', ha='right', va='bottom',)

ax1.annotate("H4-1", (np.array(B1[141]), np.array(A1[141])), alpha=5, size=8,
                   xytext=(20, -10), textcoords='offset points', ha='right', va='bottom',)
ax1.annotate("PNG 135.9+55.9", (np.array(B1[142]), np.array(A1[142])), alpha=5, size=8,
                   xytext=(-5, -10), textcoords='offset points', ha='right', va='bottom',)

#Obersevado porJPLUS
#for label_, x, y in zip(label1, d_768_jplus[0], d_644_jplus[0]):
# ax1.annotate("H4-1", (d_768_jplus[0], d_644_jplus[0]), alpha=8, size=8,
#                    xytext=(-5, 3), textcoords='offset points', ha='right', va='bottom', color='blue',)

# ax1.annotate("PNG 135.9+55.9", (d_768_jplus[1], d_644_jplus[1]), alpha=8, size=8,
#                    xytext=(68, -10), textcoords='offset points', ha='right', va='bottom', color='green',)

# ax1.annotate("CI Cyg", (d_768_jplus[2], d_644_jplus[2]), alpha=20, size=8,
#                    xytext=(-5, 3), textcoords='offset points', ha='right', va='bottom', color='yellow',)

# ax1.annotate("TX CVn", (d_768_jplus[3], d_644_jplus[3]), alpha=20, size=8,
#                    xytext=(18, -13), textcoords='offset points', ha='right', va='bottom', color='m',)


#for label_, x, y in zip(can_alh, d_768_cAlh, d_644_cAlh):
    #ax1.annotate(label_, (x, y), alpha=0.9, size=8,
                   #xytext=(3,-10), textcoords='offset points', ha='left', va='bottom',)
# plt.annotate(
#     '', xy=(B1[2][0],  A1[2][0]+0.35), xycoords='data',                    #
#     xytext=(B1[42][0]+0.4, A1[42][0]+0.4), textcoords='data', fontsize = 7,# vector extinction
#     arrowprops=dict(edgecolor='black',arrowstyle= '<-'))                   #
# plt.annotate(
#     '', xy=(B1[2][0]+0.35,  A1[2][0]+0.35), xycoords='data',
#     xytext=(5, 0), textcoords='offset points', fontsize='x-small')



#for Z, x, y in zip(z, d_768_Qz, d_644_Qz):
    #ax1.annotate("{:.3f}".format(Z), (x, y), fontsize='x-small',
                       #xytext=(5,-5), textcoords='offset points', ha='left', bbox={"boxstyle": "round", "fc": "white", "ec": "none", "alpha": 0.5}, alpha=0.7)
#ax1.set_title(" ".join([cmd_args.source]))
#ax1.grid(True)
#ax1.annotate('Higher z(3.288)', xy=(0.08749580383300781, 0.181182861328125), xytext=(-0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#ax1.annotate('Lower z(3.065)', xy=(0.3957328796386719, 0.1367034912109375), xytext=(0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
ax1.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
#ax1.legend(scatterpoints=1, ncol=1, fontsize=7.0, loc='lower left', **lgd_kws)
ax1.grid()
#lgd = ax1.legend(loc='center right', bbox_to_anchor=(1.27, 0.5), fontsize=7.5, **lgd_kws)
#ax1.grid(which='minor', lw=0.5)
#sns.despine(bottom=True)
plt.tight_layout()
#plt.savefig('luis-JPLUS-Viironen.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.savefig('Fig1-JPLUS-Viironen-v4.pdf')
plt.clf()


###################################################################################################################################
# F515-F861 vs F515-F660                                                                                                          #
###################################################################################################################################
label = []
n = 143
d_644_jplus, d_768_jplus = [], []
d_644_jplus1, d_768_jplus1 = [], []
A1, B1 = [[] for _ in range(n)], [[] for _ in range(n)]
for file_name in file_list:
    with open(file_name) as f:
        data = json.load(f)
        if data['id'].endswith("1-HPNe"):
            label.append("")
        elif data['id'].endswith("SLOAN-HPNe"):
            label.append("H4-1")
        elif data['id'].endswith("1359559-HPNe"):
            label.append("PNG 135.9+55.9")
        elif data['id'].startswith("ngc"):
            label.append("")
        elif data['id'].startswith("mwc"):
            label.append("")
        plot_mag("F515", "F660", "F861")


#errx, erry = [0.4898979485566356, 0.20976176963403032], [1.817690842800282, 0.20904544960366872]
#errx, erry = [0.1762, 0.2464], [0.13238, 0.1919]
errx, erry = [0.5, 0.5 ], [0.5, 0.5]
errx_con, erry_con = [0.86, 0, 0, 0,0], [0.95, 0, 0, 0,0]
#Include de magnitudes from JPLUS images
pattern1 = "JPLUS-data/H4-1-phot/*6pix.json"
file_list1 = glob.glob(pattern1)
for file_name1 in file_list1:
    with open(file_name1) as f1:
        data1 = json.load(f1)
        fil1 = data1["J0515"]-25+21.193
        fil2 = data1["J0660"]-25+20.859
        fil3 = data1["J0861"]-25+21.410
        diff = fil1 - fil2
        diff0 = fil1 - fil3
        d_644_jplus.append(diff)
        d_768_jplus.append(diff0)

pattern2 = "JPLUS-data/PNG135coadded-phot/*6pix.json"
file_list2 = glob.glob(pattern2)
for file_name2 in file_list2:
    with open(file_name2) as f2:
        data2 = json.load(f2)
        file1 = data2["J0515"]-25+21.468
        file2 = data2["J0660"]-25+21.094
        file3 = data2["J0861"]-25+21.574
        diff = file1 - file2
        diff0 = file1 - file3
        d_644_jplus.append(diff)
        d_768_jplus.append(diff0)

        
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
#fig = plt.figure(figsize=(18, 9)) # doble grafica
ax2 = fig.add_subplot(111)
#ax1.set_xlim(xmin=-1.7,xmax=2.0)
#ax2.set_xlim(xmin=-1.5,xmax=3.8)
ax2.set_ylim(ymin=-1.0,ymax=6.0)
plt.tick_params(axis='x', labelsize=15) 
plt.tick_params(axis='y', labelsize=15)
plt.xlabel(r'J0515 - J0861', size = 18)
plt.ylabel(r'J0515 - J0660', size = 18)
ax2.scatter(B1[62], A1[62],  c= "orange", alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral )
ax2.scatter(B1[63], A1[63],  c= "orange", alpha=.8, marker='D', s=7,  lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[64], A1[64],  c= "orange", alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[65], A1[65],  c= "orange", alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[66], A1[66],  c= "green", alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[67], A1[67],  c= "green", alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[68], A1[68],  c= "green", alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[69], A1[69],  c= "green", alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[70], A1[70],  c= "brown", alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[71], A1[71],  c= "brown",  alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[72], A1[72],  c= "brown",  alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[73], A1[73],  c= "brown",  alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[74], A1[74],  c= "cyan",  alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[75], A1[75],  c= "cyan",  alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[76], A1[76],  c= "cyan", alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[77], A1[77],  c= "cyan",  alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[78], A1[78],  c= "magenta",   alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[79], A1[79],  c= "magenta",  alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[80], A1[80],  c= "magenta",   alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[81], A1[81],  c= "magenta",  alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[82], A1[82],  c= "orange",   alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[83], A1[83],  c= "orange",   alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[84], A1[84],  c= "orange",   alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[85], A1[85],  c= "orange",   alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[86], A1[86],  c= "green",  alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[87], A1[87],  c= "green", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[88], A1[88],  c= "green", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[89], A1[89],  c= "green", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[90], A1[90],  c= "brown", alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[91], A1[91],  c= "brown", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[92], A1[92],  c= "brown", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[93], A1[93],  c= "brown", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[94], A1[94],  c= "cyan", alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[95], A1[95],  c= "cyan", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[96], A1[96],  c= "cyan", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[97], A1[97],  c= "cyan", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[98], A1[98],  c= "magenta", alpha=.4, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[99], A1[99],  c= "magenta", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[100], A1[100],  c= "magenta", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[101], A1[101],  c= "magenta", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax2.scatter(B1[102], A1[102],  c= "orange", alpha=.8, s=30,   marker='s', lw=0, cmap=plt.cm.spectral, label='BM DdDm1 L2') #
ax2.scatter(B1[103], A1[103],  c= "orange", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral, label='BM DdDm1 L3')
ax2.scatter(B1[104], A1[104],  c= "orange", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral, label='BM DdDm1 L4')
ax2.scatter(B1[105], A1[105],  c= "orange", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral, label='BM DdDm1 L5')
ax2.scatter(B1[106], A1[106],  c= "green", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral,  label='BM N2242 L2')
ax2.scatter(B1[107], A1[107],  c= "green", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral,  label='BM N2242 L3')
ax2.scatter(B1[108], A1[108],  c= "green", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral,  label='BM N2242 L4')
ax2.scatter(B1[109], A1[109],  c= "green", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral,  label='BM N2242 L5')
ax2.scatter(B1[110], A1[110],  c= "brown", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral, label='BM K648 L2')
ax2.scatter(B1[111], A1[111],  c= "brown", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral, label='BM K648 L3')
ax2.scatter(B1[112], A1[112],  c= "brown", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral, label='BM K648 L4')
ax2.scatter(B1[113], A1[113],  c= "brown", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral, label='BM K648 L5')
ax2.scatter(B1[114], A1[114],  c= "cyan", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral, label='BM BB1 L2')
ax2.scatter(B1[115], A1[115],  c= "cyan", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral, label='BM BB1 L3')
ax2.scatter(B1[116], A1[116],  c= "cyan", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral, label='BM BB1 L4')
ax2.scatter(B1[117], A1[117],  c= "cyan", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral, label='BM BB1 L5')
ax2.scatter(B1[118], A1[118],  c= "magenta", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral, label='BM Typ L2')
ax2.scatter(B1[119], A1[119],  c= "magenta", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral, label='BM Typ L3')
ax2.scatter(B1[120], A1[120],  c= "magenta", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral, label='BM Typ L4')
ax2.scatter(B1[121], A1[121],  c= "magenta", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral, label='BM Typ L5')
ax2.scatter(B1[2], A1[2], facecolors='none', edgecolors='orange', alpha=0.8, marker='s', s=7)      # c= "orange", alpha=0.8, marker='s', s=7 )
ax2.scatter(B1[3], A1[3], facecolors='none', edgecolors='orange', alpha=0.8, marker='D', s=7)
ax2.scatter(B1[4], A1[4],  facecolors='none', edgecolors='orange', alpha=0.8, marker='^', s=17)
ax2.scatter(B1[5], A1[5], facecolors='none', edgecolors='orange', alpha=0.8, marker='*', s=17)
ax2.scatter(B1[6], A1[6], facecolors='none', edgecolors='green', alpha=0.8, marker='s', s=7)      # c= "green", alpha=0.8, marker='s', s=7)
ax2.scatter(B1[7], A1[7], facecolors='none', edgecolors='green', alpha=0.8, marker='D', s=7)
ax2.scatter(B1[8], A1[8],  facecolors='none', edgecolors='green', alpha=0.8, marker='^', s=17)
ax2.scatter(B1[9], A1[9],  facecolors='none', edgecolors='green', alpha=0.8, marker='*', s=17)
ax2.scatter(B1[10], A1[10],  facecolors='none', edgecolors='brown', alpha=0.8, marker='s', s=7) # c= "brown", alpha=0.8, marker='s', s=7
ax2.scatter(B1[11], A1[11],  facecolors='none', edgecolors='brown',  alpha=0.8, marker='D', s=7)
ax2.scatter(B1[12], A1[12],  facecolors='none', edgecolors='brown',  alpha=0.8, marker='^', s=17)
ax2.scatter(B1[13], A1[13],  facecolors='none', edgecolors='brown',  alpha=0.8, marker='*', s=17)
ax2.scatter(B1[14], A1[14],  facecolors='none', edgecolors='cyan',  alpha=0.8, marker='s', s=7)   #c= "cyan",  alpha=0.8, marker='s', s=7
ax2.scatter(B1[15], A1[15],  facecolors='none', edgecolors='cyan',  alpha=0.8, marker='D', s=7)
ax2.scatter(B1[16], A1[16],  facecolors='none', edgecolors='cyan', alpha=0.8, marker='^', s=17)
ax2.scatter(B1[17], A1[17],  facecolors='none', edgecolors='cyan',  alpha=0.8, marker='*', s=17)
ax2.scatter(B1[18], A1[18],  facecolors='none', edgecolors='magenta',   alpha=0.8, marker='s', s=7)#c= "magenta",alpha=0.8, marker='s', s=7)
ax2.scatter(B1[19], A1[19],  facecolors='none', edgecolors='magenta',  alpha=0.8, marker='D', s=7)
ax2.scatter(B1[20], A1[20],  facecolors='none', edgecolors='magenta',   alpha=0.8, marker='^', s=17)
ax2.scatter(B1[21], A1[21],  facecolors='none', edgecolors='magenta',  alpha=0.8, marker='*', s=17)
ax2.scatter(B1[22], A1[22],  facecolors='none', edgecolors='orange',   alpha=0.8, s=13,  marker='s')#c= "orange",alpha=0.8, s=13, marker='s')
ax2.scatter(B1[23], A1[23],  facecolors='none', edgecolors='orange',   alpha=0.8, s=13,  marker='D')
ax2.scatter(B1[24], A1[24],  facecolors='none', edgecolors='orange',   alpha=0.8, s=23,  marker='^')
ax2.scatter(B1[25], A1[25],  facecolors='none', edgecolors='orange',   alpha=0.8, s=23,  marker='*')
ax2.scatter(B1[26], A1[26],  facecolors='none', edgecolors='green',  alpha=0.8, s=13,  marker='s') # c= "green",alpha=0.8, s=13,  marker='s'
ax2.scatter(B1[27], A1[27],  facecolors='none', edgecolors='green', alpha=0.8, s=13,  marker='D')
ax2.scatter(B1[28], A1[28],  facecolors='none', edgecolors='green', alpha=0.8, s=23,  marker='^')
ax2.scatter(B1[29], A1[29],  facecolors='none', edgecolors='green', alpha=0.8, s=23,  marker='*')
ax2.scatter(B1[30], A1[30],  facecolors='none', edgecolors='brown', alpha=0.8, s=13,  marker='s')  #c= "brown", alpha=0.8, s=13,  marker='s')
ax2.scatter(B1[31], A1[31],  facecolors='none', edgecolors='brown', alpha=0.8, s=13,  marker='D')
ax2.scatter(B1[32], A1[32],  facecolors='none', edgecolors='brown', alpha=0.8, s=23,  marker='^')
ax2.scatter(B1[33], A1[33],  facecolors='none', edgecolors='brown', alpha=0.8, s=23,  marker='*')
ax2.scatter(B1[34], A1[34],  facecolors='none', edgecolors='cyan', alpha=0.8, s=13,  marker='s')  #c= "cyan", alpha=0.8, s=13,  marker='s')
ax2.scatter(B1[35], A1[35],  facecolors='none', edgecolors='cyan', alpha=0.8, s=13,  marker='D')
ax2.scatter(B1[36], A1[36],  facecolors='none', edgecolors='cyan', alpha=0.8, s=23,  marker='^')
ax2.scatter(B1[37], A1[37],  facecolors='none', edgecolors='cyan', alpha=0.8, s=23,  marker='*')
ax2.scatter(B1[38], A1[38],  facecolors='none', edgecolors='magenta', alpha=0.8, s=13,  marker='s') #c= "magenta",alpha=0.8, s=13,marker='s')
ax2.scatter(B1[39], A1[39],  facecolors='none', edgecolors='magenta', alpha=0.8, s=13,  marker='D')
ax2.scatter(B1[40], A1[40],  facecolors='none', edgecolors='magenta', alpha=0.8, s=23,  marker='^')
ax2.scatter(B1[41], A1[41],  facecolors='none', edgecolors='magenta', alpha=0.8, s=23,  marker='*')
ax2.scatter(B1[42], A1[42],  facecolors='none', edgecolors='orange', alpha=0.8, s=30,   marker='s') #c= "orange",alpha=0.8, s=30, marker='s', 
ax2.scatter(B1[43], A1[43],  facecolors='none', edgecolors='orange', alpha=0.8, s=30,  marker='D')
ax2.scatter(B1[44], A1[44],  facecolors='none', edgecolors='orange', alpha=0.8, s=40,  marker='^')
ax2.scatter(B1[45], A1[45],  facecolors='none', edgecolors='orange', alpha=0.8, s=40,  marker='*')
ax2.scatter(B1[46], A1[46],  facecolors='none', edgecolors='green', alpha=0.8, s=30,  marker='s') #c= "green", alpha=0.8, s=30,  marker='s',
ax2.scatter(B1[47], A1[47],  facecolors='none', edgecolors='green', alpha=0.8, s=30,  marker='D')
ax2.scatter(B1[48], A1[48],  facecolors='none', edgecolors='green', alpha=0.8, s=40,  marker='^')
ax2.scatter(B1[49], A1[49],  facecolors='none', edgecolors='green', alpha=0.8, s=40,  marker='*')
ax2.scatter(B1[50], A1[50],  facecolors='none', edgecolors='brown', alpha=0.8, s=30,  marker='s') #c= "brown", alpha=0.8, s=30,  marker='s',
ax2.scatter(B1[51], A1[51],  facecolors='none', edgecolors='brown', alpha=0.8, s=30,  marker='D')
ax2.scatter(B1[52], A1[52],  facecolors='none', edgecolors='brown', alpha=0.8, s=40,  marker='^')
ax2.scatter(B1[53], A1[53],  facecolors='none', edgecolors='brown', alpha=0.8, s=40,  marker='*')
ax2.scatter(B1[54], A1[54],  facecolors='none', edgecolors='cyan', alpha=0.8, s=30,  marker='s') #c= "cyan", alpha=0.8, s=30,  marker='s',
ax2.scatter(B1[55], A1[55],  facecolors='none', edgecolors='cyan', alpha=0.8, s=30,  marker='D')
ax2.scatter(B1[56], A1[56],  facecolors='none', edgecolors='cyan', alpha=0.8, s=40,  marker='^')
ax2.scatter(B1[57], A1[57],  facecolors='none', edgecolors='cyan', alpha=0.8, s=40,  marker='*')
ax2.scatter(B1[58], A1[58],  facecolors='none', edgecolors='magenta', alpha=0.8, s=30,  marker='s') #c= "magenta", alpha=0.8, s=30,  marker='s'
ax2.scatter(B1[59], A1[59],  facecolors='none', edgecolors='magenta', alpha=0.8, s=30,  marker='D')
ax2.scatter(B1[60], A1[60],  facecolors='none', edgecolors='magenta', alpha=0.8, s=40,  marker='^')
ax2.scatter(B1[61], A1[61],  facecolors='none', edgecolors='magenta', alpha=0.8, s=40,  marker='*')

ax2.scatter(B1[0], A1[0], c='black', alpha=0.8, s=40, label='Obs. halo PNe')
#ax2.scatter(B1[62],A1[62],  c= "yellow", alpha=0.8, marker='o', label='Obs. disk PN')
ax2.scatter(B1[1], A1[1], c='purple', alpha=0.8, label='SDSS CVs')
ax2.scatter(B1[127], A1[127],  c= "mediumaquamarine" , alpha=0.8, marker='s',  label='SDSS QSOs (4.01<z<5.0)')
ax2.scatter(B1[123], A1[123],  c= "royalblue", alpha=0.8, marker='D',  label='SDSS QSOs (3.01<z<4.0)')
ax2.scatter(B1[126], A1[126],  c= "goldenrod", alpha=0.8, s=38, marker='^',  label='SDSS QSOs (2.01<z<3.0)')
ax2.scatter(B1[125], A1[125],  c= "salmon", alpha=0.8, s=38, marker='*',  label='SDSS QSOs (1.01<z<2.0)')
ax2.scatter(B1[124], A1[124],  c= "sage", alpha=0.8, marker='o',  label='SDSS QSOs (0.01<z<1.0)')
ax2.scatter(B1[128], A1[128],  c= "white", alpha=0.3, s=38, marker='^', label='SDSS SFGs ')
ax2.scatter(B1[129], A1[129],  c= "red", alpha=0.8, marker='s', label='Obs. SySts ')
#ax2.scatter(B1[72], A1[72],  c= "red", alpha=0.8, marker='D', label='Symbiotics in NGC 55')
ax2.scatter(B1[130], A1[130],  c= "red", alpha=0.8, s=38, marker='^', label='IPHAS SySts')
#ax2.scatter(B1[73], A1[73],  c= "red", alpha=0.8, marker='o', label='C. Buil Symbiotics')
ax2.scatter(B1[131], A1[131],  c= "gray", alpha=0.8, marker='D', label='Obs. HII region in NGC 55')
#ax2.scatter(B1[74], A1[74],  c= "black", alpha=0.8, marker='.', label='SN Remanents')
ax2.scatter(d_768_jplus[0], d_644_jplus[0],  c= "b", alpha=0.8, marker='o', s=35, label='J-PLUS H4-1')
(_, caps, _) = ax2.errorbar(d_768_jplus[0], d_644_jplus[0], xerr=errx[0], yerr=erry[0], marker='o', fmt='bo', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
ax2.scatter(d_768_jplus[1], d_644_jplus[1],  c= "g", alpha=0.8, marker='o', s=35, label='J-PLUS PNG135.9+55.9 ')
(_, caps, _) = ax2.errorbar(d_768_jplus[1], d_644_jplus[1], xerr=errx[1], yerr=erry[1], marker='o', fmt='go', elinewidth=0.8, markeredgewidth=0.8, markersize=8,) #fmt='yo',
for cap in caps:
    cap.set_markeredgewidth(1)
    
for label_, x, y in zip(label, B1[0], A1[0]):
    ax2.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(4, 4), textcoords='offset points', ha='right', va='bottom',)

#Obersevado porJPLUS
#for label_, x, y in zip(label1, d_768_jplus[0], d_644_jplus[0]):
ax2.annotate("H4-1", (d_768_jplus[0], d_644_jplus[0]), alpha=5, size=8,
                   xytext=(-5, -12), textcoords='offset points', ha='right', va='bottom', color='blue',)

ax2.annotate("PNG 135.9+55.9", (d_768_jplus[1], d_644_jplus[1]), alpha=5, size=8,
                   xytext=(64, -10), textcoords='offset points', ha='right', va='bottom', color='green',)


#for label_, x, y in zip(can_alh, d_768_cAlh, d_644_cAlh):
    #ax1.annotate(label_, (x, y), alpha=0.9, size=8,
                   #xytext=(3,-10), textcoords='offset points', ha='left', va='bottom',)
##########################################################
# plt.annotate(                                        
#     '', xy=(B1[2][0]+0.3,  A1[2][0]+0.3), xycoords='data',
#     xytext=(B1[42][0]+0.3, A1[42][0]+0.3), textcoords='data',
#     arrowprops={'arrowstyle': '<-'})                               #vector extinction
# plt.annotate(
#     '', xy=(B1[2][0]+0.35,  A1[2][0]+0.35), xycoords='data',
#     xytext=(5, 0), textcoords='offset points', fontsize='x-small')
#####################################################################
#for Z, x, y in zip(z, d_768_Qz, d_644_Qz):
    #ax1.annotate("{:.3f}".format(Z), (x, y), fontsize='x-small',
                       #xytext=(5,-5), textcoords='offset points', ha='left', bbox={"boxstyle": "round", "fc": "white", "ec": "none", "alpha": 0.5}, alpha=0.7)
#ax1.set_title(" ".join([cmd_args.source]))
#ax1.grid(True)
#ax1.annotate('Higher z(3.288)', xy=(0.08749580383300781, 0.181182861328125), xytext=(-0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#ax1.annotate('Lower z(3.065)', xy=(0.3957328796386719, 0.1367034912109375), xytext=(0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
ax2.minorticks_on()
#ax2.grid(which='minor')#, lw=0.3)
#ax2.legend(scatterpoints=1, ncol=2, fontsize=7.0, **lgd_kws)
ax2.grid()
#lgd = ax2.legend(loc='center right', bbox_to_anchor=(1.27, 0.5), fontsize=7.5, **lgd_kws)
#ax2.grid(which='minor', lw=0.5)
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('luis-JPLUS-F515-F861.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.clf()

###############################################################################################################33
#Halpha-r vs Halpha-g                                                                                          #
################################################################################################################
label = []
n = 143
d_644_jplus, d_768_jplus = [], []
d_644_jplus1, d_768_jplus1 = [], []
A1, B1 = [[] for _ in range(n)], [[] for _ in range(n)]
for file_name in file_list:
    with open(file_name) as f:
        data = json.load(f)
        if data['id'].endswith("1-HPNe"):
            label.append("")
        elif data['id'].endswith("SLOAN-HPNe"):
            label.append("H4-1")
        elif data['id'].endswith("1359559-HPNe"):
            label.append("PNG 135.9+55.9")
        elif data['id'].startswith("ngc"):
            label.append("")
        elif data['id'].startswith("mwc"):
            label.append("")
        plot_mag("F660", "F480_g_sdss", "F610_r_sdss")

#errx, erry = [1.9524, 0.3083], [1.950409, 0.394402]

#errx, erry = [0.0435, 0.1366], [0.04264, 0.1366]

errx, erry = [0.8, 0.5, 0.5, 0.5], [0.8, 0.5, 0.5, 0.5]
errx_con, erry_con = [0.95, 0, 0, 0,0.83], [0.87, 0, 0, 0,0.47]

pattern1 = "JPLUS-data/H4-1-phot/*6pix.json"
file_list1 = glob.glob(pattern1)
for file_name1 in file_list1:
    with open(file_name1) as f1:
        data1 = json.load(f1)
        fil1 = data1["J0660"]-25+20.859
        fil2 = data1["J0480_gSDSS"]-25+23.297#-1.192
        fil3 = data1["J0625_rSDSS"]-25+23.335 #-1.12 
        diff = fil1 - fil2
        diff0 = fil1 - fil3
        d_644_jplus.append(diff)
        d_768_jplus.append(diff0)

err_h4x3 = np.sqrt(err_zp_h4[8]**2+err_zp_h4[7]**2)
err_h4y3 = np.sqrt(err_zp_h4[8]**2+err_zp_h4[5]**2)

pattern1 = "JPLUS-data/PNG135coadded-phot/*6pix.json"
file_list1 = glob.glob(pattern1)
for file_name1 in file_list1:
    with open(file_name1) as f1:
        data1 = json.load(f1)
        fil1 = data1["J0660"]-25+21.058
        fil2 = data1["J0480_gSDSS"]-25+23.425 #-1.367
        fil3 = data1["J0625_rSDSS"]-25+23.565 #-1.162 
        diff = fil1 - fil2
        diff0 = fil1 - fil3
        d_644_jplus.append(diff)
        d_768_jplus.append(diff0)
print(d_644_jplus1, d_768_jplus1)
err_pn13x3 = np.sqrt(err_zp_pn135[8]**2+err_zp_pn135[7]**2)
err_pn13y3 = np.sqrt(err_zp_pn135[8]**2+err_zp_pn135[5]**2)

# pattern1 = "JPLUS-data/CICgy/*6pix.json"
# file_list1 = glob.glob(pattern1)
# for file_name1 in file_list1:
#     with open(file_name1) as f1:
#         data1 = json.load(f1)
#         fil1 = data1["J0660"]-25+21.192
#         fil2 = data1["J0480_gSDSS"]-25+23.436
#         fil3 = data1["J0625_rSDSS"]-25+23.736
#         diff = fil1 - fil2
#         diff0 = fil1 - fil3
#         d_644_jplus.append(diff)
#         d_768_jplus.append(diff0)

# pattern1 = "JPLUS-data/TXCVn/*6pix.json"
# file_list1 = glob.glob(pattern1)
# for file_name1 in file_list1:
#     with open(file_name1) as f1:
#         data1 = json.load(f1)
#         fil1 = data1["J0660"]-25+21.072
#         fil2 = data1["J0480_gSDSS"]-25+23.585
#         fil3 = data1["J0625_rSDSS"]-25+23.616
#         diff = fil1 - fil2
#         diff0 = fil1 - fil3
#         d_644_jplus.append(diff)
#         d_768_jplus.append(diff0) 


lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax3 = fig.add_subplot(111)
#ax1.set_xlim(xmin=-1.7,xmax=2.0)
ax3.set_xlim(xmin=-3.0,xmax=1.1)
ax3.set_ylim(ymin=-5.0,ymax=1.0)
plt.tick_params(axis='x', labelsize=15) 
plt.tick_params(axis='y', labelsize=15)
plt.xlabel(r'J0660 - rSDSS', size = 18)
plt.ylabel(r'J0660 - gSDSS', size = 18)
ax3.scatter(B1[62], A1[62],  c= "orange", alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral )
ax3.scatter(B1[63], A1[63],  c= "orange", alpha=.8, marker='D', s=7,  lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[64], A1[64],  c= "orange", alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[65], A1[65],  c= "orange", alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[66], A1[66],  c= "green", alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[67], A1[67],  c= "green", alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[68], A1[68],  c= "green", alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[69], A1[69],  c= "green", alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[70], A1[70],  c= "brown", alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[71], A1[71],  c= "brown",  alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[72], A1[72],  c= "brown",  alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[73], A1[73],  c= "brown",  alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[74], A1[74],  c= "cyan",  alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[75], A1[75],  c= "cyan",  alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[76], A1[76],  c= "cyan", alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[77], A1[77],  c= "cyan",  alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[78], A1[78],  c= "magenta",   alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[79], A1[79],  c= "magenta",  alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[80], A1[80],  c= "magenta",   alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[81], A1[81],  c= "magenta",  alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[82], A1[82],  c= "orange",   alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[83], A1[83],  c= "orange",   alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[84], A1[84],  c= "orange",   alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[85], A1[85],  c= "orange",   alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[86], A1[86],  c= "green",  alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[87], A1[87],  c= "green", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[88], A1[88],  c= "green", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[89], A1[89],  c= "green", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[90], A1[90],  c= "brown", alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[91], A1[91],  c= "brown", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[92], A1[92],  c= "brown", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[93], A1[93],  c= "brown", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[94], A1[94],  c= "cyan", alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[95], A1[95],  c= "cyan", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[96], A1[96],  c= "cyan", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[97], A1[97],  c= "cyan", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[98], A1[98],  c= "magenta", alpha=.4, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[99], A1[99],  c= "magenta", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[100], A1[100],  c= "magenta", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[101], A1[101],  c= "magenta", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax3.scatter(B1[102], A1[102],  c= "orange", alpha=.8, s=30,   marker='s', lw=0, cmap=plt.cm.spectral, label='BM DdDm1 L2') #
ax3.scatter(B1[103], A1[103],  c= "orange", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral, label='BM DdDm1 L3')
ax3.scatter(B1[104], A1[104],  c= "orange", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral, label='BM DdDm1 L4')
ax3.scatter(B1[105], A1[105],  c= "orange", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral, label='BM DdDm1 L5')
ax3.scatter(B1[106], A1[106],  c= "green", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral,  label='BM N2242 L2')
ax3.scatter(B1[107], A1[107],  c= "green", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral,  label='BM N2242 L3')
ax3.scatter(B1[108], A1[108],  c= "green", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral,  label='BM N2242 L4')
ax3.scatter(B1[109], A1[109],  c= "green", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral,  label='BM N2242 L5')
ax3.scatter(B1[110], A1[110],  c= "brown", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral, label='BM K648 L2')
ax3.scatter(B1[111], A1[111],  c= "brown", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral, label='BM K648 L3')
ax3.scatter(B1[112], A1[112],  c= "brown", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral, label='BM K648 L4')
ax3.scatter(B1[113], A1[113],  c= "brown", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral, label='BM K648 L5')
ax3.scatter(B1[114], A1[114],  c= "cyan", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral, label='BM BB1 L2')
ax3.scatter(B1[115], A1[115],  c= "cyan", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral, label='BM BB1 L3')
ax3.scatter(B1[116], A1[116],  c= "cyan", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral, label='BM BB1 L4')
ax3.scatter(B1[117], A1[117],  c= "cyan", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral, label='BM BB1 L5')
ax3.scatter(B1[118], A1[118],  c= "magenta", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral, label='BM Typ L2')
ax3.scatter(B1[119], A1[119],  c= "magenta", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral, label='BM Typ L3')
ax3.scatter(B1[120], A1[120],  c= "magenta", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral, label='BM Typ L4')
ax3.scatter(B1[121], A1[121],  c= "magenta", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral, label='BM Typ L5')
ax3.scatter(B1[2], A1[2], facecolors='none', edgecolors='orange', alpha=0.8, marker='s', s=7)      # c= "orange", alpha=0.8, marker='s', s=7 )
ax3.scatter(B1[3], A1[3], facecolors='none', edgecolors='orange', alpha=0.8, marker='D', s=7)
ax3.scatter(B1[4], A1[4],  facecolors='none', edgecolors='orange', alpha=0.8, marker='^', s=17)
ax3.scatter(B1[5], A1[5], facecolors='none', edgecolors='orange', alpha=0.8, marker='*', s=17)
ax3.scatter(B1[6], A1[6], facecolors='none', edgecolors='green', alpha=0.8, marker='s', s=7)      # c= "green", alpha=0.8, marker='s', s=7)
ax3.scatter(B1[7], A1[7], facecolors='none', edgecolors='green', alpha=0.8, marker='D', s=7)
ax3.scatter(B1[8], A1[8],  facecolors='none', edgecolors='green', alpha=0.8, marker='^', s=17)
ax3.scatter(B1[9], A1[9],  facecolors='none', edgecolors='green', alpha=0.8, marker='*', s=17)
ax3.scatter(B1[10], A1[10],  facecolors='none', edgecolors='brown', alpha=0.8, marker='s', s=7) # c= "brown", alpha=0.8, marker='s', s=7
ax3.scatter(B1[11], A1[11],  facecolors='none', edgecolors='brown',  alpha=0.8, marker='D', s=7)
ax3.scatter(B1[12], A1[12],  facecolors='none', edgecolors='brown',  alpha=0.8, marker='^', s=17)
ax3.scatter(B1[13], A1[13],  facecolors='none', edgecolors='brown',  alpha=0.8, marker='*', s=17)
ax3.scatter(B1[14], A1[14],  facecolors='none', edgecolors='cyan',  alpha=0.8, marker='s', s=7)   #c= "cyan",  alpha=0.8, marker='s', s=7
ax3.scatter(B1[15], A1[15],  facecolors='none', edgecolors='cyan',  alpha=0.8, marker='D', s=7)
ax3.scatter(B1[16], A1[16],  facecolors='none', edgecolors='cyan', alpha=0.8, marker='^', s=17)
ax3.scatter(B1[17], A1[17],  facecolors='none', edgecolors='cyan',  alpha=0.8, marker='*', s=17)
ax3.scatter(B1[18], A1[18],  facecolors='none', edgecolors='magenta',   alpha=0.8, marker='s', s=7)#c= "magenta",alpha=0.8, marker='s', s=7)
ax3.scatter(B1[19], A1[19],  facecolors='none', edgecolors='magenta',  alpha=0.8, marker='D', s=7)
ax3.scatter(B1[20], A1[20],  facecolors='none', edgecolors='magenta',   alpha=0.8, marker='^', s=17)
ax3.scatter(B1[21], A1[21],  facecolors='none', edgecolors='magenta',  alpha=0.8, marker='*', s=17)
ax3.scatter(B1[22], A1[22],  facecolors='none', edgecolors='orange',   alpha=0.8, s=13,  marker='s')#c= "orange",alpha=0.8, s=13, marker='s')
ax3.scatter(B1[23], A1[23],  facecolors='none', edgecolors='orange',   alpha=0.8, s=13,  marker='D')
ax3.scatter(B1[24], A1[24],  facecolors='none', edgecolors='orange',   alpha=0.8, s=23,  marker='^')
ax3.scatter(B1[25], A1[25],  facecolors='none', edgecolors='orange',   alpha=0.8, s=23,  marker='*')
ax3.scatter(B1[26], A1[26],  facecolors='none', edgecolors='green',  alpha=0.8, s=13,  marker='s') # c= "green",alpha=0.8, s=13,  marker='s'
ax3.scatter(B1[27], A1[27],  facecolors='none', edgecolors='green', alpha=0.8, s=13,  marker='D')
ax3.scatter(B1[28], A1[28],  facecolors='none', edgecolors='green', alpha=0.8, s=23,  marker='^')
ax3.scatter(B1[29], A1[29],  facecolors='none', edgecolors='green', alpha=0.8, s=23,  marker='*')
ax3.scatter(B1[30], A1[30],  facecolors='none', edgecolors='brown', alpha=0.8, s=13,  marker='s')  #c= "brown", alpha=0.8, s=13,  marker='s')
ax3.scatter(B1[31], A1[31],  facecolors='none', edgecolors='brown', alpha=0.8, s=13,  marker='D')
ax3.scatter(B1[32], A1[32],  facecolors='none', edgecolors='brown', alpha=0.8, s=23,  marker='^')
ax3.scatter(B1[33], A1[33],  facecolors='none', edgecolors='brown', alpha=0.8, s=23,  marker='*')
ax3.scatter(B1[34], A1[34],  facecolors='none', edgecolors='cyan', alpha=0.8, s=13,  marker='s')  #c= "cyan", alpha=0.8, s=13,  marker='s')
ax3.scatter(B1[35], A1[35],  facecolors='none', edgecolors='cyan', alpha=0.8, s=13,  marker='D')
ax3.scatter(B1[36], A1[36],  facecolors='none', edgecolors='cyan', alpha=0.8, s=23,  marker='^')
ax3.scatter(B1[37], A1[37],  facecolors='none', edgecolors='cyan', alpha=0.8, s=23,  marker='*')
ax3.scatter(B1[38], A1[38],  facecolors='none', edgecolors='magenta', alpha=0.8, s=13,  marker='s') #c= "magenta",alpha=0.8, s=13,marker='s')
ax3.scatter(B1[39], A1[39],  facecolors='none', edgecolors='magenta', alpha=0.8, s=13,  marker='D')
ax3.scatter(B1[40], A1[40],  facecolors='none', edgecolors='magenta', alpha=0.8, s=23,  marker='^')
ax3.scatter(B1[41], A1[41],  facecolors='none', edgecolors='magenta', alpha=0.8, s=23,  marker='*')
ax3.scatter(B1[42], A1[42],  facecolors='none', edgecolors='orange', alpha=0.8, s=30,   marker='s') #c= "orange",alpha=0.8, s=30, marker='s', 
ax3.scatter(B1[43], A1[43],  facecolors='none', edgecolors='orange', alpha=0.8, s=30,  marker='D')
ax3.scatter(B1[44], A1[44],  facecolors='none', edgecolors='orange', alpha=0.8, s=40,  marker='^')
ax3.scatter(B1[45], A1[45],  facecolors='none', edgecolors='orange', alpha=0.8, s=40,  marker='*')
ax3.scatter(B1[46], A1[46],  facecolors='none', edgecolors='green', alpha=0.8, s=30,  marker='s') #c= "green", alpha=0.8, s=30,  marker='s',
ax3.scatter(B1[47], A1[47],  facecolors='none', edgecolors='green', alpha=0.8, s=30,  marker='D')
ax3.scatter(B1[48], A1[48],  facecolors='none', edgecolors='green', alpha=0.8, s=40,  marker='^')
ax3.scatter(B1[49], A1[49],  facecolors='none', edgecolors='green', alpha=0.8, s=40,  marker='*')
ax3.scatter(B1[50], A1[50],  facecolors='none', edgecolors='brown', alpha=0.8, s=30,  marker='s') #c= "brown", alpha=0.8, s=30,  marker='s',
ax3.scatter(B1[51], A1[51],  facecolors='none', edgecolors='brown', alpha=0.8, s=30,  marker='D')
ax3.scatter(B1[52], A1[52],  facecolors='none', edgecolors='brown', alpha=0.8, s=40,  marker='^')
ax3.scatter(B1[53], A1[53],  facecolors='none', edgecolors='brown', alpha=0.8, s=40,  marker='*')
ax3.scatter(B1[54], A1[54],  facecolors='none', edgecolors='cyan', alpha=0.8, s=30,  marker='s') #c= "cyan", alpha=0.8, s=30,  marker='s',
ax3.scatter(B1[55], A1[55],  facecolors='none', edgecolors='cyan', alpha=0.8, s=30,  marker='D')
ax3.scatter(B1[56], A1[56],  facecolors='none', edgecolors='cyan', alpha=0.8, s=40,  marker='^')
ax3.scatter(B1[57], A1[57],  facecolors='none', edgecolors='cyan', alpha=0.8, s=40,  marker='*')
ax3.scatter(B1[58], A1[58],  facecolors='none', edgecolors='magenta', alpha=0.8, s=30,  marker='s') #c= "magenta", alpha=0.8, s=30,  marker='s'
ax3.scatter(B1[59], A1[59],  facecolors='none', edgecolors='magenta', alpha=0.8, s=30,  marker='D')
ax3.scatter(B1[60], A1[60],  facecolors='none', edgecolors='magenta', alpha=0.8, s=40,  marker='^')
ax3.scatter(B1[61], A1[61],  facecolors='none', edgecolors='magenta', alpha=0.8, s=40,  marker='*')

ax3.scatter(B1[0], A1[0], c='black', alpha=0.8, s=40, label='Obs. halo PNe')
# (_, caps, _) = ax3.errorbar(B1[0], A1[0], xerr=errx_con, yerr=erry_con, marker='o', fmt='ko', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
# for cap in caps:
#     cap.set_markeredgewidth(1)
#ax3.scatter(B1[62],A1[62],  c= "yellow", alpha=0.8, marker='o', label='Obs. disk PN')
ax3.scatter(B1[1], A1[1], c='purple', alpha=0.8, label='SDSS CVs')
ax3.scatter(B1[127], A1[127],  c= "mediumaquamarine" , alpha=0.8, marker='s',  label='SDSS QSOs (4.01<z<5.0)')
ax3.scatter(B1[123], A1[123],  c= "royalblue", alpha=0.8, marker='D',  label='SDSS QSOs (3.01<z<4.0)')
ax3.scatter(B1[126], A1[126],  c= "goldenrod", alpha=0.8, s=38, marker='^',  label='SDSS QSOs (2.01<z<3.0)')
ax3.scatter(B1[125], A1[125],  c= "salmon", alpha=0.8, s=38, marker='*',  label='SDSS QSOs (1.01<z<2.0)')
ax3.scatter(B1[124], A1[124],  c= "sage", alpha=0.8, marker='o',  label='SDSS QSOs (0.01<z<1.0)')
ax3.scatter(B1[128], A1[128],  c= "white", alpha=0.3, s=38, marker='^', label='SDSS SFGs ')
ax3.scatter(B1[129], A1[129],  facecolors='none', edgecolors='red', alpha=0.8, s=38, marker='s')#, label='Obs. SySts ')
ax3.scatter(B1[137], A1[137],  c= "red", alpha=0.8, s=38, marker='s', label='Obs. SySts ')
#ax1.scatter(B1[72], A1[72],  c= "red", alpha=0.8, marker='D', label='Symbiotics in NGC 55')
ax3.scatter(B1[135], A1[135],  c= "red", alpha=0.8, s=38, marker='D', label=' Obs. SySts in NGC 205')
ax3.scatter(B1[136], A1[136],  facecolors='none', edgecolors='red', alpha=0.8, s=38, marker='D')  #label=' SySts in NGC 205')
ax3.scatter(B1[130], A1[130],  facecolors='none', edgecolors='red', alpha=0.8, s=38, marker='^')#,  label='IPHAS SySts')
ax3.scatter(B1[138], A1[138],  c= "red", alpha=0.8, s=38, marker='^', label='IPHAS SySts')
ax3.scatter(B1[140], A1[140],  facecolors='none', edgecolors='red', alpha=0.8, s=38, marker='o',  label='Obs. SySts in IC10 ')
ax3.scatter(B1[139], A1[139],  c= "red", alpha=0.8, s=38, marker='v', label=' Obs. SySts in NGC 185')
#ax1.scatter(B1[73], A1[73],  c= "red", alpha=0.8, marker='o', label='C. Buil Symbiotics')
ax3.scatter(B1[131], A1[131],  c= "gray", alpha=0.8, marker='D', label='Obs. HII region in NGC 55')
#ax3.scatter(B1[74], A1[74],  c= "black", alpha=0.8, marker='.', label='SN Remanents')
ax3.scatter(d_768_jplus[0], d_644_jplus[0],  c= "b", alpha=0.8, marker='o', s=35, label='J-PLUS H4-1')
(_, caps, _) = ax3.errorbar(d_768_jplus[0], d_644_jplus[0], xerr=err_h4x3, yerr=err_h4y3, marker='o', fmt='bo', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
ax3.scatter(d_768_jplus[1], d_644_jplus[1],  c= "g", alpha=0.8, marker='o', s=35, label='J-PLUS PNG135.9+55.9 ')
(_, caps, _) = ax3.errorbar(d_768_jplus[1], d_644_jplus[1], xerr=err_pn13x3, yerr=err_pn13x3, marker='o', fmt='go', elinewidth=0.8, markeredgewidth=0.8, markersize=8,) #fmt='yo',
for cap in caps:
    cap.set_markeredgewidth(1)
# ax3.scatter(d_768_jplus[2], d_644_jplus[2],  c= "y", alpha=0.8, marker='s', label='J-PLUS CI Cyg')
# (_, caps, _) = ax3.errorbar(d_768_jplus[2], d_644_jplus[2], xerr=errx[2], yerr=erry[2], marker='s', fmt='ys', elinewidth=.8, markeredgewidth=.8, markersize=8,)
# for cap in caps:
#     cap.set_markeredgewidth(1)
# ax3.scatter(d_768_jplus[3], d_644_jplus[3],  c= "m", alpha=0.8, marker='s',  label='J-PLUS TX CVn')
# (_, caps, _) = ax3.errorbar(d_768_jplus[3], d_644_jplus[3], xerr=errx[3], yerr=erry[3], marker='s', fmt='ms', elinewidth=.8, markeredgewidth=.8, markersize=8,) #fmt='yo',
# for cap in caps:
#     cap.set_markeredgewidth(1)

for label_, x, y in zip(label, B1[0], A1[0]):
    ax3.annotate(label_, (x, y), alpha=5, size=8,
                   xytext=(-24, 4), textcoords='offset points', ha='left', va='bottom',)
    
#two halo PNe observed by  JPLUS
ax3.annotate("H4-1", (d_768_jplus[0], d_644_jplus[0]), alpha=5, size=8,
                   xytext=(19, 3), textcoords='offset points', ha='right', va='bottom', color='blue',)

ax3.annotate("PNG 135.9+55.9", (d_768_jplus[1], d_644_jplus[1]), alpha=5, size=8,
                   xytext=(25, 4.5), textcoords='offset points', ha='right', va='bottom', color='green',)

# ax3.annotate("CI Cyg", (d_768_jplus[2], d_644_jplus[2]), alpha=20, size=8,
#                    xytext=(-5, 3), textcoords='offset points', ha='right', va='bottom', color='yellow',)

# ax3.annotate("TX CVn", (d_768_jplus[3], d_644_jplus[3]), alpha=20, size=8,
#                    xytext=(18, -13), textcoords='offset points', ha='right', va='bottom', color='m',)


#for label_, x, y in zip(can_alh, d_768_cAlh, d_644_cAlh):
    #ax3.annotate(label_, (x, y), alpha=0.9, size=8,
                   #xytext=(3,-10), textcoords='offset points', ha='left', va='bottom',)
###############################################################
# plt.annotate(
#     '', xy=(B1[2][0]-0.4,  A1[2][0]-0.4), xycoords='data',
#     xytext=(B1[42][0]-0.4, A1[42][0]-0.4), textcoords='data',
#     arrowprops={'arrowstyle': '<-'})                                 #vector extiction 
# plt.annotate(
#     '', xy=(B1[2][0]+0.35,  A1[2][0]+0.35), xycoords='data',
#     xytext=(5, 0), textcoords='offset points', fontsize='x-small')
###################################################################
#for Z, x, y in zip(z, d_768_Qz, d_644_Qz):
    #ax1.annotate("{:.3f}".format(Z), (x, y), fontsize='x-small',
                       #xytext=(5,-5), textcoords='offset points', ha='left', bbox={"boxstyle": "round", "fc": "white", "ec": "none", "alpha": 0.5}, alpha=0.7)
#ax1.set_title(" ".join([cmd_args.source]))
#ax1.grid(True)
#ax1.annotate('Higher z(3.288)', xy=(0.08749580383300781, 0.181182861328125), xytext=(-0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#ax1.annotate('Lower z(3.065)', xy=(0.3957328796386719, 0.1367034912109375), xytext=(0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
ax3.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
#ax1.legend(scatterpoints=1, ncol=2, fontsize=5.8, loc='lower left', **lgd_kws)
ax3.grid()
#lgd = ax3.legend(loc='center right', bbox_to_anchor=(1.27, 0.5), fontsize=7.5, **lgd_kws)
#ax3.grid(which='minor', lw=0.5)
#sns.despine(bottom=True)
plt.tight_layout()
#plt.savefig('luis-JPLUS-H-r.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.savefig('Fig2-JPLUS-H-r_d4.pdf')
#fig.savefig('diagram-SPLUS-paper.pdf')
plt.clf()
#################################################################################################
#  u-Halpha vs u-F861                                                                           #
#################################################################################################
d_644_jplus, d_768_jplus = [], []
d_644_jplus1, d_768_jplus1 = [], []


label = []
n = 143
A1, B1 = [[] for _ in range(n)], [[] for _ in range(n)]
for file_name in file_list:
    with open(file_name) as f:
        data = json.load(f)
        if data['id'].endswith("1-HPNe"):
            label.append(data['id'].split("-H")[0])
        elif data['id'].endswith("SLOAN-HPNe"):
            label.append("H4-1")
        elif data['id'].endswith("1359559-HPNe"):
            label.append("PNG 135.9+55.9")
        elif data['id'].startswith("ngc"):
            label.append("NGC 2242")
        elif data['id'].startswith("mwc"):
            label.append("MWC 574")
        plot_mag("F348", "F861", "F660")

errx, erry = [0.0270, 0.0810], [0.0350, 0.0720]

pattern1 = "JPLUS-data/H4-1-phot/*6pix.json"
file_list1 = glob.glob(pattern1)
for file_name1 in file_list1:
    with open(file_name1) as f1:
        data1 = json.load(f1)
        fil1 = data1["J0348_uJAVA"]-3.05
        fil2 = data1["J0861"]-25+21.410
        fil3 = data1["J0660"]-25+20.859
        diff = fil1 - fil2
        diff0 = fil1 - fil3
        d_644_jplus.append(diff)
        d_768_jplus.append(diff0)

pattern1 = "JPLUS-data/PNG135coadded-phot/*6pix.json"
file_list1 = glob.glob(pattern1)
for file_name1 in file_list1:
    with open(file_name1) as f1:
        data1 = json.load(f1)
        fil1 = data1["J0348_uJAVA"]-3.597
        fil2 = data1["J0861"]-25+21.574
        fil3 = data1["J0660"]-25+21.094
        diff = fil1 - fil2
        diff0 = fil1 - fil3
        d_644_jplus.append(diff)
        d_768_jplus.append(diff0) 
        
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig1 = plt.figure(figsize=(7, 6))
#fig1 = plt.figure(figsize=(18, 9))
ax4 = fig1.add_subplot(111)
#ax1.set_xlim(xmin=-1.7,xmax=2.0)
ax4.set_xlim(xmin=-2.1,xmax=5.5)
ax4.set_ylim(ymin=-2.3,ymax=5.5)
plt.tick_params(axis='x', labelsize=15) 
plt.tick_params(axis='y', labelsize=15)
plt.xlabel(r'uJAVA - J0660', size = 18)
plt.ylabel(r'uJAVA - J0861', size = 18)
ax4.scatter(B1[62], A1[62],  c= "orange", alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral )
ax4.scatter(B1[63], A1[63],  c= "orange", alpha=.8, marker='D', s=7,  lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[64], A1[64],  c= "orange", alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[65], A1[65],  c= "orange", alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[66], A1[66],  c= "green", alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[67], A1[67],  c= "green", alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[68], A1[68],  c= "green", alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[69], A1[69],  c= "green", alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[70], A1[70],  c= "brown", alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[71], A1[71],  c= "brown",  alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[72], A1[72],  c= "brown",  alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[73], A1[73],  c= "brown",  alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[74], A1[74],  c= "cyan",  alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[75], A1[75],  c= "cyan",  alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[76], A1[76],  c= "cyan", alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[77], A1[77],  c= "cyan",  alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[78], A1[78],  c= "magenta",   alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[79], A1[79],  c= "magenta",  alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[80], A1[80],  c= "magenta",   alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[81], A1[81],  c= "magenta",  alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[82], A1[82],  c= "orange",   alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[83], A1[83],  c= "orange",   alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[84], A1[84],  c= "orange",   alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[85], A1[85],  c= "orange",   alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[86], A1[86],  c= "green",  alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[87], A1[87],  c= "green", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[88], A1[88],  c= "green", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[89], A1[89],  c= "green", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[90], A1[90],  c= "brown", alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[91], A1[91],  c= "brown", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[92], A1[92],  c= "brown", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[93], A1[93],  c= "brown", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[94], A1[94],  c= "cyan", alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[95], A1[95],  c= "cyan", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[96], A1[96],  c= "cyan", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[97], A1[97],  c= "cyan", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[98], A1[98],  c= "magenta", alpha=.4, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[99], A1[99],  c= "magenta", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[100], A1[100],  c= "magenta", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[101], A1[101],  c= "magenta", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax4.scatter(B1[102], A1[102],  c= "orange", alpha=.8, s=30,   marker='s', lw=0, cmap=plt.cm.spectral, label='BM DdDm1 L2') #
ax4.scatter(B1[103], A1[103],  c= "orange", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral, label='BM DdDm1 L3')
ax4.scatter(B1[104], A1[104],  c= "orange", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral, label='BM DdDm1 L4')
ax4.scatter(B1[105], A1[105],  c= "orange", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral, label='BM DdDm1 L5')
ax4.scatter(B1[106], A1[106],  c= "green", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral,  label='BM N2242 L2')
ax4.scatter(B1[107], A1[107],  c= "green", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral,  label='BM N2242 L3')
ax4.scatter(B1[108], A1[108],  c= "green", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral,  label='BM N2242 L4')
ax4.scatter(B1[109], A1[109],  c= "green", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral,  label='BM N2242 L5')
ax4.scatter(B1[110], A1[110],  c= "brown", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral, label='BM K648 L2')
ax4.scatter(B1[111], A1[111],  c= "brown", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral, label='BM K648 L3')
ax4.scatter(B1[112], A1[112],  c= "brown", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral, label='BM K648 L4')
ax4.scatter(B1[113], A1[113],  c= "brown", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral, label='BM K648 L5')
ax4.scatter(B1[114], A1[114],  c= "cyan", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral, label='BM BB1 L2')
ax4.scatter(B1[115], A1[115],  c= "cyan", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral, label='BM BB1 L3')
ax4.scatter(B1[116], A1[116],  c= "cyan", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral, label='BM BB1 L4')
ax4.scatter(B1[117], A1[117],  c= "cyan", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral, label='BM BB1 L5')
ax4.scatter(B1[118], A1[118],  c= "magenta", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral, label='BM Typ L2')
ax4.scatter(B1[119], A1[119],  c= "magenta", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral, label='BM Typ L3')
ax4.scatter(B1[120], A1[120],  c= "magenta", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral, label='BM Typ L4')
ax4.scatter(B1[121], A1[121],  c= "magenta", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral, label='BM Typ L5')
ax4.scatter(B1[2], A1[2], facecolors='none', edgecolors='orange', alpha=0.8, marker='s', s=7)      # c= "orange", alpha=0.8, marker='s', s=7 )
ax4.scatter(B1[3], A1[3], facecolors='none', edgecolors='orange', alpha=0.8, marker='D', s=7)
ax4.scatter(B1[4], A1[4],  facecolors='none', edgecolors='orange', alpha=0.8, marker='^', s=17)
ax4.scatter(B1[5], A1[5], facecolors='none', edgecolors='orange', alpha=0.8, marker='*', s=17)
ax4.scatter(B1[6], A1[6], facecolors='none', edgecolors='green', alpha=0.8, marker='s', s=7)      # c= "green", alpha=0.8, marker='s', s=7)
ax4.scatter(B1[7], A1[7], facecolors='none', edgecolors='green', alpha=0.8, marker='D', s=7)
ax4.scatter(B1[8], A1[8],  facecolors='none', edgecolors='green', alpha=0.8, marker='^', s=17)
ax4.scatter(B1[9], A1[9],  facecolors='none', edgecolors='green', alpha=0.8, marker='*', s=17)
ax4.scatter(B1[10], A1[10],  facecolors='none', edgecolors='brown', alpha=0.8, marker='s', s=7) # c= "brown", alpha=0.8, marker='s', s=7
ax4.scatter(B1[11], A1[11],  facecolors='none', edgecolors='brown',  alpha=0.8, marker='D', s=7)
ax4.scatter(B1[12], A1[12],  facecolors='none', edgecolors='brown',  alpha=0.8, marker='^', s=17)
ax4.scatter(B1[13], A1[13],  facecolors='none', edgecolors='brown',  alpha=0.8, marker='*', s=17)
ax4.scatter(B1[14], A1[14],  facecolors='none', edgecolors='cyan',  alpha=0.8, marker='s', s=7)   #c= "cyan",  alpha=0.8, marker='s', s=7
ax4.scatter(B1[15], A1[15],  facecolors='none', edgecolors='cyan',  alpha=0.8, marker='D', s=7)
ax4.scatter(B1[16], A1[16],  facecolors='none', edgecolors='cyan', alpha=0.8, marker='^', s=17)
ax4.scatter(B1[17], A1[17],  facecolors='none', edgecolors='cyan',  alpha=0.8, marker='*', s=17)
ax4.scatter(B1[18], A1[18],  facecolors='none', edgecolors='magenta',   alpha=0.8, marker='s', s=7)#c= "magenta",alpha=0.8, marker='s', s=7)
ax4.scatter(B1[19], A1[19],  facecolors='none', edgecolors='magenta',  alpha=0.8, marker='D', s=7)
ax4.scatter(B1[20], A1[20],  facecolors='none', edgecolors='magenta',   alpha=0.8, marker='^', s=17)
ax4.scatter(B1[21], A1[21],  facecolors='none', edgecolors='magenta',  alpha=0.8, marker='*', s=17)
ax4.scatter(B1[22], A1[22],  facecolors='none', edgecolors='orange',   alpha=0.8, s=13,  marker='s')#c= "orange",alpha=0.8, s=13, marker='s')
ax4.scatter(B1[23], A1[23],  facecolors='none', edgecolors='orange',   alpha=0.8, s=13,  marker='D')
ax4.scatter(B1[24], A1[24],  facecolors='none', edgecolors='orange',   alpha=0.8, s=23,  marker='^')
ax4.scatter(B1[25], A1[25],  facecolors='none', edgecolors='orange',   alpha=0.8, s=23,  marker='*')
ax4.scatter(B1[26], A1[26],  facecolors='none', edgecolors='green',  alpha=0.8, s=13,  marker='s') # c= "green",alpha=0.8, s=13,  marker='s'
ax4.scatter(B1[27], A1[27],  facecolors='none', edgecolors='green', alpha=0.8, s=13,  marker='D')
ax4.scatter(B1[28], A1[28],  facecolors='none', edgecolors='green', alpha=0.8, s=23,  marker='^')
ax4.scatter(B1[29], A1[29],  facecolors='none', edgecolors='green', alpha=0.8, s=23,  marker='*')
ax4.scatter(B1[30], A1[30],  facecolors='none', edgecolors='brown', alpha=0.8, s=13,  marker='s')  #c= "brown", alpha=0.8, s=13,  marker='s')
ax4.scatter(B1[31], A1[31],  facecolors='none', edgecolors='brown', alpha=0.8, s=13,  marker='D')
ax4.scatter(B1[32], A1[32],  facecolors='none', edgecolors='brown', alpha=0.8, s=23,  marker='^')
ax4.scatter(B1[33], A1[33],  facecolors='none', edgecolors='brown', alpha=0.8, s=23,  marker='*')
ax4.scatter(B1[34], A1[34],  facecolors='none', edgecolors='cyan', alpha=0.8, s=13,  marker='s')  #c= "cyan", alpha=0.8, s=13,  marker='s')
ax4.scatter(B1[35], A1[35],  facecolors='none', edgecolors='cyan', alpha=0.8, s=13,  marker='D')
ax4.scatter(B1[36], A1[36],  facecolors='none', edgecolors='cyan', alpha=0.8, s=23,  marker='^')
ax4.scatter(B1[37], A1[37],  facecolors='none', edgecolors='cyan', alpha=0.8, s=23,  marker='*')
ax4.scatter(B1[38], A1[38],  facecolors='none', edgecolors='magenta', alpha=0.8, s=13,  marker='s') #c= "magenta",alpha=0.8, s=13,marker='s')
ax4.scatter(B1[39], A1[39],  facecolors='none', edgecolors='magenta', alpha=0.8, s=13,  marker='D')
ax4.scatter(B1[40], A1[40],  facecolors='none', edgecolors='magenta', alpha=0.8, s=23,  marker='^')
ax4.scatter(B1[41], A1[41],  facecolors='none', edgecolors='magenta', alpha=0.8, s=23,  marker='*')
ax4.scatter(B1[42], A1[42],  facecolors='none', edgecolors='orange', alpha=0.8, s=30,   marker='s') #c= "orange",alpha=0.8, s=30, marker='s', 
ax4.scatter(B1[43], A1[43],  facecolors='none', edgecolors='orange', alpha=0.8, s=30,  marker='D')
ax4.scatter(B1[44], A1[44],  facecolors='none', edgecolors='orange', alpha=0.8, s=40,  marker='^')
ax4.scatter(B1[45], A1[45],  facecolors='none', edgecolors='orange', alpha=0.8, s=40,  marker='*')
ax4.scatter(B1[46], A1[46],  facecolors='none', edgecolors='green', alpha=0.8, s=30,  marker='s') #c= "green", alpha=0.8, s=30,  marker='s',
ax4.scatter(B1[47], A1[47],  facecolors='none', edgecolors='green', alpha=0.8, s=30,  marker='D')
ax4.scatter(B1[48], A1[48],  facecolors='none', edgecolors='green', alpha=0.8, s=40,  marker='^')
ax4.scatter(B1[49], A1[49],  facecolors='none', edgecolors='green', alpha=0.8, s=40,  marker='*')
ax4.scatter(B1[50], A1[50],  facecolors='none', edgecolors='brown', alpha=0.8, s=30,  marker='s') #c= "brown", alpha=0.8, s=30,  marker='s',
ax4.scatter(B1[51], A1[51],  facecolors='none', edgecolors='brown', alpha=0.8, s=30,  marker='D')
ax4.scatter(B1[52], A1[52],  facecolors='none', edgecolors='brown', alpha=0.8, s=40,  marker='^')
ax4.scatter(B1[53], A1[53],  facecolors='none', edgecolors='brown', alpha=0.8, s=40,  marker='*')
ax4.scatter(B1[54], A1[54],  facecolors='none', edgecolors='cyan', alpha=0.8, s=30,  marker='s') #c= "cyan", alpha=0.8, s=30,  marker='s',
ax4.scatter(B1[55], A1[55],  facecolors='none', edgecolors='cyan', alpha=0.8, s=30,  marker='D')
ax4.scatter(B1[56], A1[56],  facecolors='none', edgecolors='cyan', alpha=0.8, s=40,  marker='^')
ax4.scatter(B1[57], A1[57],  facecolors='none', edgecolors='cyan', alpha=0.8, s=40,  marker='*')
ax4.scatter(B1[58], A1[58],  facecolors='none', edgecolors='magenta', alpha=0.8, s=30,  marker='s') #c= "magenta", alpha=0.8, s=30,  marker='s'
ax4.scatter(B1[59], A1[59],  facecolors='none', edgecolors='magenta', alpha=0.8, s=30,  marker='D')
ax4.scatter(B1[60], A1[60],  facecolors='none', edgecolors='magenta', alpha=0.8, s=40,  marker='^')
ax4.scatter(B1[61], A1[61],  facecolors='none', edgecolors='magenta', alpha=0.8, s=40,  marker='*')

ax4.scatter(B1[0], A1[0], c='black', alpha=0.8, s=40, label='Obs. halo PNe')
#ax4.scatter(B1[62],A1[62],  c= "yellow", alpha=0.8, marker='o', label='Obs. disk PN')
ax4.scatter(B1[1], A1[1], c='purple', alpha=0.8, label='SDSS CVs')
ax4.scatter(B1[127], A1[127],  c= "mediumaquamarine" , alpha=0.8, marker='s',  label='SDSS QSOs (4.01<z<5.0)')
ax4.scatter(B1[123], A1[123],  c= "royalblue", alpha=0.8, marker='D',  label='SDSS QSOs (3.01<z<4.0)')
ax4.scatter(B1[126], A1[126],  c= "goldenrod", alpha=0.8, s=38, marker='^',  label='SDSS QSOs (2.01<z<3.0)')
ax4.scatter(B1[125], A1[125],  c= "salmon", alpha=0.8, s=38, marker='*',  label='SDSS QSOs (1.01<z<2.0)')
ax4.scatter(B1[124], A1[124],  c= "sage", alpha=0.8, marker='o',  label='SDSS QSOs (0.01<z<1.0)')
ax4.scatter(B1[128], A1[128],  c= "white", alpha=0.3, s=38, marker='^', label='SDSS SFGs ')
ax4.scatter(B1[129], A1[129],  c= "red", alpha=0.8, marker='s', label='Obs. MW SySts ')
#ax4.scatter(B1[72], A1[72],  c= "red", alpha=0.8, marker='D', label='Symbiotics in NGC 55')
ax4.scatter(B1[130], A1[130],  c= "red", alpha=0.8, s=38, marker='^', label='IPHAS SySts')
#ax4.scatter(B1[73], A1[73],  c= "red", alpha=0.8, marker='o', label='C. Buil Symbiotics')
ax4.scatter(B1[131], A1[131],  c= "gray", alpha=0.8, marker='D', label='Obs. HII region in NGC 55')
#ax4.scatter(B1[74], A1[74],  c= "black", alpha=0.8, marker='.', label='SN Remanents')
ax4.scatter(d_768_jplus, d_644_jplus,  c= "black", alpha=0.8, marker='s', s=35, label='HPNe from JPLUS survey')
(_, caps, _) = ax4.errorbar(d_768_jplus, d_644_jplus, xerr=errx, yerr=erry, marker='s', fmt='ks', markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)

for label_, x, y in zip(label, B1[0], A1[0]):
    ax4.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(-10, -10), textcoords='offset points', ha='center', va='bottom',)

#for label_, x, y in zip(can_alh, d_768_cAlh, d_644_cAlh):
    #ax4.annotate(label_, (x, y), alpha=0.9, size=8,
                   #xytext=(3,-10), textcoords='offset points', ha='left', va='bottom',)
plt.annotate(
    '', xy=(B1[2][0]+1.1,  A1[2][0]+1.1), xycoords='data',
    xytext=(B1[42][0]+1.1, A1[42][0]+1.1), textcoords='data',
    arrowprops={'arrowstyle': '<-'})
plt.annotate(
    '', xy=(B1[2][0]+0.35,  A1[2][0]+0.35), xycoords='data',
    xytext=(5, 0), textcoords='offset points', fontsize='x-small')

#for Z, x, y in zip(z, d_768_Qz, d_644_Qz):
    #ax4.annotate("{:.3f}".format(Z), (x, y), fontsize='x-small',
                       #xytext=(5,-5), textcoords='offset points', ha='left', bbox={"boxstyle": "round", "fc": "white", "ec": "none", "alpha": 0.5}, alpha=0.7)
#ax4.set_title(" ".join([cmd_args.source]))
#ax4.grid(True)
#ax4.annotate('Higher z(3.288)', xy=(0.08749580383300781, 0.181182861328125), xytext=(-0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#ax1.annotate('Lower z(3.065)', xy=(0.3957328796386719, 0.1367034912109375), xytext=(0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
ax4.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax4.legend(scatterpoints=1, ncol=2, fontsize=7.0, loc = 'upper left', **lgd_kws)
ax4.grid()
#lgd = ax4.legend(loc='center right', bbox_to_anchor=(1.27, 0.5), fontsize=7.5, **lgd_kws)
#ax4.grid(which='minor', lw=0.5)
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('luis-JPLUS-u-F861.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
#plt.clf()

#######################################################################################################################################
#  z-i vs z halpha
######################################################################################################################################
d_644_jplus, d_768_jplus = [], []
d_644_jplus1, d_768_jplus1 = [], []

label = []
n = 143
A1, B1 = [[] for _ in range(n)], [[] for _ in range(n)]
for file_name in file_list:
    with open(file_name) as f:
        data = json.load(f)
        if data['id'].endswith("1-HPNe"):
            label.append(data['id'].split("-H")[0])
        elif data['id'].endswith("SLOAN-HPNe"):
            label.append("H4-1")
        elif data['id'].endswith("1359559-HPNe"):
            label.append("PNG 135.9+55.9")
        elif data['id'].startswith("ngc"):
            label.append("NGC 2242")
        elif data['id'].startswith("mwc"):
            label.append("MWC 574")
        plot_mag("F910_z_sdss", "F660", "F760_i_sdss")

errx, erry = [0.22872035327010146, 0.27262656688540271 ], [0.22860008748904714, 0.27615619669259817 ]

pattern1 = "JPLUS-data/H4-1-phot/*6pix.json"
file_list1 = glob.glob(pattern1)
for file_name1 in file_list1:
    with open(file_name1) as f1:
        data1 = json.load(f1)
        fil1 = data1["J0911_zSDSS"]-1.62
        fil2 = data1["J0660"]-25+20.859
        fil3 = data1["J0766_iSDSS"]-25+23.11
        diff = fil1 - fil2
        diff0 = fil1 - fil3
        d_644_jplus.append(diff)
        d_768_jplus.append(diff0)

pattern1 = "JPLUS-data/PNG135coadded-phot/*6pix.json"
file_list1 = glob.glob(pattern1)
for file_name1 in file_list1:
    with open(file_name1) as f1:
        data1 = json.load(f1)
        fil1 = data1["J0911_zSDSS"]-2.097
        fil2 = data1["J0660"]-25+21.094
        fil3 = data1["J0766_iSDSS"]-25+23.260
        diff = fil1 - fil2
        diff0 = fil1 - fil3
        d_644_jplus.append(diff)
        d_768_jplus.append(diff0) 

        
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig5 = plt.figure(figsize=(7, 6))
ax5 = fig5.add_subplot(111)
#ax1.set_xlim(xmin=-1.7,xmax=2.0)
ax5.set_xlim(xmin=-1.8,xmax=1.0)
ax5.set_ylim(ymin=-2.2,ymax=4.8)
plt.tick_params(axis='x', labelsize=15) 
plt.tick_params(axis='y', labelsize=15)
plt.xlabel(r'zSDSS - iSDSS', size = 18)
plt.ylabel(r'zSDSS - J0660', size = 18)
ax5.scatter(B1[62], A1[62],  c= "orange", alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral )
ax5.scatter(B1[63], A1[63],  c= "orange", alpha=.8, marker='D', s=7,  lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[64], A1[64],  c= "orange", alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[65], A1[65],  c= "orange", alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[66], A1[66],  c= "green", alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[67], A1[67],  c= "green", alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[68], A1[68],  c= "green", alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[69], A1[69],  c= "green", alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[70], A1[70],  c= "brown", alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[71], A1[71],  c= "brown",  alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[72], A1[72],  c= "brown",  alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[73], A1[73],  c= "brown",  alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[74], A1[74],  c= "cyan",  alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[75], A1[75],  c= "cyan",  alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[76], A1[76],  c= "cyan", alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[77], A1[77],  c= "cyan",  alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[78], A1[78],  c= "magenta",   alpha=.8, marker='s', s=7, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[79], A1[79],  c= "magenta",  alpha=.8, marker='D', s=7, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[80], A1[80],  c= "magenta",   alpha=.8, marker='^', s=17, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[81], A1[81],  c= "magenta",  alpha=.8, marker='*', s=17, lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[82], A1[82],  c= "orange",   alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[83], A1[83],  c= "orange",   alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[84], A1[84],  c= "orange",   alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[85], A1[85],  c= "orange",   alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[86], A1[86],  c= "green",  alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[87], A1[87],  c= "green", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[88], A1[88],  c= "green", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[89], A1[89],  c= "green", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[90], A1[90],  c= "brown", alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[91], A1[91],  c= "brown", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[92], A1[92],  c= "brown", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[93], A1[93],  c= "brown", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[94], A1[94],  c= "cyan", alpha=.8, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[95], A1[95],  c= "cyan", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[96], A1[96],  c= "cyan", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[97], A1[97],  c= "cyan", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[98], A1[98],  c= "magenta", alpha=.4, s=13,  marker='s', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[99], A1[99],  c= "magenta", alpha=.8, s=13,  marker='D', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[100], A1[100],  c= "magenta", alpha=.8, s=23,  marker='^', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[101], A1[101],  c= "magenta", alpha=.8, s=23,  marker='*', lw=0, cmap=plt.cm.spectral)
ax5.scatter(B1[102], A1[102],  c= "orange", alpha=.8, s=30,   marker='s', lw=0, cmap=plt.cm.spectral, label='BM DdDm1 L2') #
ax5.scatter(B1[103], A1[103],  c= "orange", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral, label='BM DdDm1 L3')
ax5.scatter(B1[104], A1[104],  c= "orange", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral, label='BM DdDm1 L4')
ax5.scatter(B1[105], A1[105],  c= "orange", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral, label='BM DdDm1 L5')
ax5.scatter(B1[106], A1[106],  c= "green", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral,  label='BM N2242 L2')
ax5.scatter(B1[107], A1[107],  c= "green", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral,  label='BM N2242 L3')
ax5.scatter(B1[108], A1[108],  c= "green", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral,  label='BM N2242 L4')
ax5.scatter(B1[109], A1[109],  c= "green", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral,  label='BM N2242 L5')
ax5.scatter(B1[110], A1[110],  c= "brown", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral, label='BM K648 L2')
ax5.scatter(B1[111], A1[111],  c= "brown", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral, label='BM K648 L3')
ax5.scatter(B1[112], A1[112],  c= "brown", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral, label='BM K648 L4')
ax5.scatter(B1[113], A1[113],  c= "brown", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral, label='BM K648 L5')
ax5.scatter(B1[114], A1[114],  c= "cyan", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral, label='BM BB1 L2')
ax5.scatter(B1[115], A1[115],  c= "cyan", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral, label='BM BB1 L3')
ax5.scatter(B1[116], A1[116],  c= "cyan", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral, label='BM BB1 L4')
ax5.scatter(B1[117], A1[117],  c= "cyan", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral, label='BM BB1 L5')
ax5.scatter(B1[118], A1[118],  c= "magenta", alpha=.8, s=30,  marker='s', lw=0, cmap=plt.cm.spectral, label='BM Typ L2')
ax5.scatter(B1[119], A1[119],  c= "magenta", alpha=.8, s=30,  marker='D', lw=0, cmap=plt.cm.spectral, label='BM Typ L3')
ax5.scatter(B1[120], A1[120],  c= "magenta", alpha=.8, s=40,  marker='^', lw=0, cmap=plt.cm.spectral, label='BM Typ L4')
ax5.scatter(B1[121], A1[121],  c= "magenta", alpha=.8, s=40,  marker='*', lw=0, cmap=plt.cm.spectral, label='BM Typ L5')
ax5.scatter(B1[2], A1[2], facecolors='none', edgecolors='orange', alpha=0.8, marker='s', s=7)      # c= "orange", alpha=0.8, marker='s', s=7 )
ax5.scatter(B1[3], A1[3], facecolors='none', edgecolors='orange', alpha=0.8, marker='D', s=7)
ax5.scatter(B1[4], A1[4],  facecolors='none', edgecolors='orange', alpha=0.8, marker='^', s=17)
ax5.scatter(B1[5], A1[5], facecolors='none', edgecolors='orange', alpha=0.8, marker='*', s=17)
ax5.scatter(B1[6], A1[6], facecolors='none', edgecolors='green', alpha=0.8, marker='s', s=7)      # c= "green", alpha=0.8, marker='s', s=7)
ax5.scatter(B1[7], A1[7], facecolors='none', edgecolors='green', alpha=0.8, marker='D', s=7)
ax5.scatter(B1[8], A1[8],  facecolors='none', edgecolors='green', alpha=0.8, marker='^', s=17)
ax5.scatter(B1[9], A1[9],  facecolors='none', edgecolors='green', alpha=0.8, marker='*', s=17)
ax5.scatter(B1[10], A1[10],  facecolors='none', edgecolors='brown', alpha=0.8, marker='s', s=7) # c= "brown", alpha=0.8, marker='s', s=7
ax5.scatter(B1[11], A1[11],  facecolors='none', edgecolors='brown',  alpha=0.8, marker='D', s=7)
ax5.scatter(B1[12], A1[12],  facecolors='none', edgecolors='brown',  alpha=0.8, marker='^', s=17)
ax5.scatter(B1[13], A1[13],  facecolors='none', edgecolors='brown',  alpha=0.8, marker='*', s=17)
ax5.scatter(B1[14], A1[14],  facecolors='none', edgecolors='cyan',  alpha=0.8, marker='s', s=7)   #c= "cyan",  alpha=0.8, marker='s', s=7
ax5.scatter(B1[15], A1[15],  facecolors='none', edgecolors='cyan',  alpha=0.8, marker='D', s=7)
ax5.scatter(B1[16], A1[16],  facecolors='none', edgecolors='cyan', alpha=0.8, marker='^', s=17)
ax5.scatter(B1[17], A1[17],  facecolors='none', edgecolors='cyan',  alpha=0.8, marker='*', s=17)
ax5.scatter(B1[18], A1[18],  facecolors='none', edgecolors='magenta',   alpha=0.8, marker='s', s=7)#c= "magenta",alpha=0.8, marker='s', s=7)
ax5.scatter(B1[19], A1[19],  facecolors='none', edgecolors='magenta',  alpha=0.8, marker='D', s=7)
ax5.scatter(B1[20], A1[20],  facecolors='none', edgecolors='magenta',   alpha=0.8, marker='^', s=17)
ax5.scatter(B1[21], A1[21],  facecolors='none', edgecolors='magenta',  alpha=0.8, marker='*', s=17)
ax5.scatter(B1[22], A1[22],  facecolors='none', edgecolors='orange',   alpha=0.8, s=13,  marker='s')#c= "orange",alpha=0.8, s=13, marker='s')
ax5.scatter(B1[23], A1[23],  facecolors='none', edgecolors='orange',   alpha=0.8, s=13,  marker='D')
ax5.scatter(B1[24], A1[24],  facecolors='none', edgecolors='orange',   alpha=0.8, s=23,  marker='^')
ax5.scatter(B1[25], A1[25],  facecolors='none', edgecolors='orange',   alpha=0.8, s=23,  marker='*')
ax5.scatter(B1[26], A1[26],  facecolors='none', edgecolors='green',  alpha=0.8, s=13,  marker='s') # c= "green",alpha=0.8, s=13,  marker='s'
ax5.scatter(B1[27], A1[27],  facecolors='none', edgecolors='green', alpha=0.8, s=13,  marker='D')
ax5.scatter(B1[28], A1[28],  facecolors='none', edgecolors='green', alpha=0.8, s=23,  marker='^')
ax5.scatter(B1[29], A1[29],  facecolors='none', edgecolors='green', alpha=0.8, s=23,  marker='*')
ax5.scatter(B1[30], A1[30],  facecolors='none', edgecolors='brown', alpha=0.8, s=13,  marker='s')  #c= "brown", alpha=0.8, s=13,  marker='s')
ax5.scatter(B1[31], A1[31],  facecolors='none', edgecolors='brown', alpha=0.8, s=13,  marker='D')
ax5.scatter(B1[32], A1[32],  facecolors='none', edgecolors='brown', alpha=0.8, s=23,  marker='^')
ax5.scatter(B1[33], A1[33],  facecolors='none', edgecolors='brown', alpha=0.8, s=23,  marker='*')
ax5.scatter(B1[34], A1[34],  facecolors='none', edgecolors='cyan', alpha=0.8, s=13,  marker='s')  #c= "cyan", alpha=0.8, s=13,  marker='s')
ax5.scatter(B1[35], A1[35],  facecolors='none', edgecolors='cyan', alpha=0.8, s=13,  marker='D')
ax5.scatter(B1[36], A1[36],  facecolors='none', edgecolors='cyan', alpha=0.8, s=23,  marker='^')
ax5.scatter(B1[37], A1[37],  facecolors='none', edgecolors='cyan', alpha=0.8, s=23,  marker='*')
ax5.scatter(B1[38], A1[38],  facecolors='none', edgecolors='magenta', alpha=0.8, s=13,  marker='s') #c= "magenta",alpha=0.8, s=13,marker='s')
ax5.scatter(B1[39], A1[39],  facecolors='none', edgecolors='magenta', alpha=0.8, s=13,  marker='D')
ax5.scatter(B1[40], A1[40],  facecolors='none', edgecolors='magenta', alpha=0.8, s=23,  marker='^')
ax5.scatter(B1[41], A1[41],  facecolors='none', edgecolors='magenta', alpha=0.8, s=23,  marker='*')
ax5.scatter(B1[42], A1[42],  facecolors='none', edgecolors='orange', alpha=0.8, s=30,   marker='s') #c= "orange",alpha=0.8, s=30, marker='s', 
ax5.scatter(B1[43], A1[43],  facecolors='none', edgecolors='orange', alpha=0.8, s=30,  marker='D')
ax5.scatter(B1[44], A1[44],  facecolors='none', edgecolors='orange', alpha=0.8, s=40,  marker='^')
ax5.scatter(B1[45], A1[45],  facecolors='none', edgecolors='orange', alpha=0.8, s=40,  marker='*')
ax5.scatter(B1[46], A1[46],  facecolors='none', edgecolors='green', alpha=0.8, s=30,  marker='s') #c= "green", alpha=0.8, s=30,  marker='s',
ax5.scatter(B1[47], A1[47],  facecolors='none', edgecolors='green', alpha=0.8, s=30,  marker='D')
ax5.scatter(B1[48], A1[48],  facecolors='none', edgecolors='green', alpha=0.8, s=40,  marker='^')
ax5.scatter(B1[49], A1[49],  facecolors='none', edgecolors='green', alpha=0.8, s=40,  marker='*')
ax5.scatter(B1[50], A1[50],  facecolors='none', edgecolors='brown', alpha=0.8, s=30,  marker='s') #c= "brown", alpha=0.8, s=30,  marker='s',
ax5.scatter(B1[51], A1[51],  facecolors='none', edgecolors='brown', alpha=0.8, s=30,  marker='D')
ax5.scatter(B1[52], A1[52],  facecolors='none', edgecolors='brown', alpha=0.8, s=40,  marker='^')
ax5.scatter(B1[53], A1[53],  facecolors='none', edgecolors='brown', alpha=0.8, s=40,  marker='*')
ax5.scatter(B1[54], A1[54],  facecolors='none', edgecolors='cyan', alpha=0.8, s=30,  marker='s') #c= "cyan", alpha=0.8, s=30,  marker='s',
ax5.scatter(B1[55], A1[55],  facecolors='none', edgecolors='cyan', alpha=0.8, s=30,  marker='D')
ax5.scatter(B1[56], A1[56],  facecolors='none', edgecolors='cyan', alpha=0.8, s=40,  marker='^')
ax5.scatter(B1[57], A1[57],  facecolors='none', edgecolors='cyan', alpha=0.8, s=40,  marker='*')
ax5.scatter(B1[58], A1[58],  facecolors='none', edgecolors='magenta', alpha=0.8, s=30,  marker='s') #c= "magenta", alpha=0.8, s=30,  marker='s'
ax5.scatter(B1[59], A1[59],  facecolors='none', edgecolors='magenta', alpha=0.8, s=30,  marker='D')
ax5.scatter(B1[60], A1[60],  facecolors='none', edgecolors='magenta', alpha=0.8, s=40,  marker='^')
ax5.scatter(B1[61], A1[61],  facecolors='none', edgecolors='magenta', alpha=0.8, s=40,  marker='*')

ax5.scatter(B1[0], A1[0], c='black', alpha=0.8, s=40, label='Obs. halo PNe')
#ax5.scatter(B1[62],A1[62],  c= "yellow", alpha=0.8, marker='o', label='Obs. disk PN')
ax5.scatter(B1[1], A1[1], c='purple', alpha=0.8, label='SDSS CVs')
ax5.scatter(B1[127], A1[127],  c= "mediumaquamarine" , alpha=0.8, marker='s',  label='SDSS QSOs (4.01<z<5.0)')
ax5.scatter(B1[123], A1[123],  c= "royalblue", alpha=0.8, marker='D',  label='SDSS QSOs (3.01<z<4.0)')
ax5.scatter(B1[126], A1[126],  c= "goldenrod", alpha=0.8, s=38, marker='^',  label='SDSS QSOs (2.01<z<3.0)')
ax5.scatter(B1[125], A1[125],  c= "salmon", alpha=0.8, s=38, marker='*',  label='SDSS QSOs (1.01<z<2.0)')
ax5.scatter(B1[124], A1[124],  c= "sage", alpha=0.8, marker='o',  label='SDSS QSOs (0.01<z<1.0)')
ax5.scatter(B1[128], A1[128],  c= "white", alpha=0.3, s=38, marker='^', label='SDSS SFGs ')
ax5.scatter(B1[129], A1[129],  c= "red", alpha=0.8, marker='s', label='Obs. MW SySts ')
#ax5.scatter(B1[72], A1[72],  c= "red", alpha=0.8, marker='D', label='Symbiotics in NGC 55')
ax5.scatter(B1[130], A1[130],  c= "red", alpha=0.8, s=38, marker='^', label='IPHAS SySts')
#ax5.scatter(B1[73], A1[73],  c= "red", alpha=0.8, marker='o', label='C. Buil Symbiotics')
ax5.scatter(B1[131], A1[131],  c= "gray", alpha=0.8, marker='D', label='Obs. HII region in NGC 55')
#ax5.scatter(B1[74], A1[74],  c= "black", alpha=0.8, marker='.', label='SN Remanents')
#ax5.scatter(d_768_jplus, d_644_jplus,  c= "black", alpha=0.8, marker='s', s=35, label='HPNe from JPLUS survey')
(_, caps, _) = ax5.errorbar(d_768_jplus, d_644_jplus, xerr=errx, yerr=erry, marker='s', fmt='ks', markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)

for label_, x, y in zip(label, B1[0], A1[0]):
    ax5.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(-10, -10), textcoords='offset points', ha='center', va='bottom',)

#for label_, x, y in zip(can_alh, d_768_cAlh, d_644_cAlh):
    #ax5.annotate(label_, (x, y), alpha=0.9, size=8,
                   #xytext=(3,-10), textcoords='offset points', ha='left', va='bottom',)
plt.annotate(
    '', xy=(B1[2][0]+0.9,  A1[2][0]+0.9), xycoords='data',
    xytext=(B1[42][0]+0.9, A1[42][0]+0.9), textcoords='data',
    arrowprops={'arrowstyle': '<-'})
plt.annotate(
    '', xy=(B1[2][0]+0.35,  A1[2][0]+0.35), xycoords='data',
    xytext=(5, 0), textcoords='offset points', fontsize='x-small')

#for Z, x, y in zip(z, d_768_Qz, d_644_Qz):
    #ax5.annotate("{:.3f}".format(Z), (x, y), fontsize='x-small',
                       #xytext=(5,-5), textcoords='offset points', ha='left', bbox={"boxstyle": "round", "fc": "white", "ec": "none", "alpha": 0.5}, alpha=0.7)
#ax5.set_title(" ".join([cmd_args.source]))
#ax5.grid(True)
#ax5.annotate('Higher z(3.288)', xy=(0.08749580383300781, 0.181182861328125), xytext=(-0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#ax1.annotate('Lower z(3.065)', xy=(0.3957328796386719, 0.1367034912109375), xytext=(0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
ax5.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
#ax5.legend(scatterpoints=1, ncol=2, fontsize=5.8, loc='lower left', **lgd_kws)
ax5.grid()
#lgd = ax5.legend(loc='center right', bbox_to_anchor=(1.27, 0.5), fontsize=7.5, **lgd_kws)
#ax5.grid(which='minor', lw=0.5)
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('luis-JPLUS-z-H.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
#fig1.savefig('diagram-SPLUS-paper1.pdf')
plt.clf()
