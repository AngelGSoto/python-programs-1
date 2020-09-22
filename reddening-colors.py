# -*- coding: utf-8 -*-
'''
Make color-color diagrams for JPLUS 2017
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from scipy.stats import gaussian_kde
import pandas as pd
from astropy.table import Table
#import StringIO
from sympy import S, symbols
from scipy.optimize import fsolve
import os


#reading the files .json

pattern = "*-spectros/*-JPLUS17-magnitude.json"
file_list = glob.glob(pattern)

# def filter_mag(e, s, f1, f2, f3):
#     '''
#     Calculate the colors using any of set of filters
#     '''
#     col, col0 = [], []
#     if data['id'].endswith(e):
#         if data['id'].startswith(str(s)):
#             filter1 = data[f1]
#             filter2 = data[f2]
#             filter3 = data[f3]
#             diff = filter1 - filter2
#             diff0 = filter1 - filter3
#             col.append(diff)
#             col0.append(diff0)
    
#     return col, col0


def filter_mag(e, s, f1, f2, f3, f4):
    '''
    Calculate the colors using any of set of filters
    '''
    col, col0 = [], []
    if data['id'].endswith(e):
        if data['id'].startswith(str(s)):
            filter1 = data[f1]
            filter2 = data[f2]
            filter3 = data[f3]
            filter4 = data[f4]
            diff = filter1 - filter2
            diff0 = filter3 - filter4
            col.append(diff)
            col0.append(diff0)
    
    return col, col0


def plot_mag(f1, f2, f3, f4):
    x1, y1 = filter_mag("E00_100", "", f1, f2, f3, f4)
    x2, y2 = filter_mag("E01_100", "", f1, f2, f3, f4)
    x3, y3 = filter_mag("E02_100", "", f1, f2, f3, f4)
    x4, y4 = filter_mag("E00_300", "", f1, f2, f3, f4)
    x5, y5 = filter_mag("E01_300", "", f1, f2, f3, f4)
    x6, y6 = filter_mag("E02_300", "", f1, f2, f3, f4)
    x7, y7 = filter_mag("E00_600", "", f1, f2, f3, f4)
    x8, y8 = filter_mag("E01_600", "", f1, f2, f3, f4)
    x9, y9 = filter_mag("E02_600", "", f1, f2, f3, f4)
   
    for a, b in zip(x1, y1):
        A1[0].append(a)
        B1[0].append(b)
    for a, b in zip(x4, y4):
        A1[0].append(a)
        B1[0].append(b)
    for a, b in zip(x7, y7):
        A1[0].append(a)
        B1[0].append(b)
    for a, b in zip(x3, y3):
        A1[1].append(a)
        B1[1].append(b)
    for a, b in zip(x6, y6):
        A1[1].append(a)
        B1[1].append(b)
    for a, b in zip(x9, y9):
        A1[1].append(a)
        B1[1].append(b)

n = 3
A1, B1 = [[] for _ in range(n)], [[] for _ in range(n)]
d_644_jplus, d_768_jplus = [], []
d_644_jplus1, d_768_jplus1 = [], []
label=[]

for file_name in file_list:
    with open(file_name) as f:
        data = json.load(f)
        # if data['id'].endswith("1-HPNe"):
        #     label.append("")
        # elif data['id'].endswith("SLOAN-HPNe-"):
        #     label.append("H4-1")
        # elif data['id'].endswith("1359559-HPNe"):
        #     label.append("PNG 135.9+55.9")
        if data['id'].startswith("ngc"):
            label.append("")
        elif data['id'].startswith("mwc"):
            label.append("")
        #plot_mag("F625_r_sdss", "F660", "F766_i_sdss")
        #plot_mag("F515", "F660", "F861")
        #plot_mag("F911_z_sdss", "F660", "F480_g_sdss")
        #plot_mag("F480_g_sdss", "F515", "F660", "F625_r_sdss")
        plot_mag("F410", "F660", "F480_g_sdss", "F766_i_sdss")

print(np.mean(B1[0]), np.mean(A1[0]))
print(np.mean(B1[1]), np.mean(A1[1]))
