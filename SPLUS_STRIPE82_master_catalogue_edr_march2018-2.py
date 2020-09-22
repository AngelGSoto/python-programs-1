'''
Getting the PN and SyST candidtaes in S-PLUS catalog (DR1)
'''
from __future__ import print_function
import numpy as np
import glob
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from astropy.table import Table
import argparse

n=17
magnitude = [[] for _ in range(n)]

f = open('SPLUS_STRIPE82_master_catalogue_edr_march2018.cat', 'r')
for line in f:
    line = line.strip()
    columns = line.split()
    mag1 = float(columns[3])
    print(mag1)
    # mag2 = float(columns[49])
    # mag3 = float(columns[51])
