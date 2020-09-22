'''
Superponient the JPAS transmission curve and spectrum of a symbiotic 
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
import seaborn as sns
import os
from astropy.io import ascii

def load_file(filename):
    wll, ress = [], []
    data = ascii.read(filename)
    for i in data:
        wl = i['col1']
        res = i['col2']
        wll.append(wl)
        ress.append(res)
    return wll, ress

pattern = "JPAS_J*.tab"
#pattern = "Jv0915_8100.res"
file_list = glob.glob(pattern)

pattern1 = "JPAS_*SDSS.tab"
file_list1 = glob.glob(pattern1)

fig = plt.figure(figsize=(12, 7))
ax1 = fig.add_subplot(111)
for f in file_list:
    x, y = load_file(f)
    ax1.plot(x,y, c="gray")#, label=f.split('_t')[0])
    #plt.xticks(x, file_list, rotation=90)

for f in file_list1:
    x, y = load_file(f)
    ax1.fill(x,y, alpha=0.5, edgecolor='black', linewidth=2.3)#, label=f.split('_t')[0])
    
# Spectrum
def sys(spectra):
    datadir = "../../Halo-PNe-spectros/"
    #datadir = "../../syst-spectros/"
    #datadir = "../../PN-Tesis-Didactica/"
    file_ = spectra
    x = np.loadtxt(os.path.join(datadir, file_), delimiter = None, skiprows = 0, usecols = None,
                   unpack = False, dtype = np.dtype([('Wl', '|f8'), ('Flux', 'f8')]))
    return x['Wl'], x['Flux']

#x, y = sys("mwc574.dat")
# m = x >=3200
# x = x[m]
x, y = sys("BB1.dat")
#x1, y1 = sys("LHa_115_N_60.txt")
#x, y = sys("PN-NGC6751.dat")

y /=80.0e-15
#y1 /=1.5e-14

#print(x, y)
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
sns.set(style="dark")
#plt.xlim(6e3, 10500)
# plt.xlim(3e3, 10500)
plt.ylim(-0.02, 0.75)
plt.tick_params(axis='x', labelsize=16) 
plt.tick_params(axis='y', labelsize=16)
plt.plot(x, y, linewidth=1.3, color="k")#, label="Lin 358")
#plt.plot(x1, y1, linewidth=1.3, color="red")#, label="LHa 115")
#plt.legend(fontsize='x-small')
plt.xlabel("Wavelength($\AA$)", fontsize= 18)
plt.ylabel("Transmission", fontsize= 18)
plt.tight_layout()
plt.tight_layout()
#plt.legend()

plt.savefig('JPAS2017-filter-BB1.jpg')
