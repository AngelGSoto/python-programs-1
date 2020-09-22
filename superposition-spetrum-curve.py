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

def load_file(filename):
    wll, ress = [], []
    data = np.loadtxt(filename, delimiter=None, converters=None, skiprows=0,
                                       usecols=None, unpack=False, ndmin=0)
    for i in data:
        wl = str(i[0])
        res = str(i[1])
        wll.append(wl)
        ress.append(res)
    return wll, ress

#pattern = "Jv*.res"
pattern = "Jv0915_4801"
file_list = glob.glob(pattern)

pattern1 = "*JPAS_0915.res"
file_list1 = glob.glob(pattern1)

fig = plt.figure(figsize=(12, 7))
ax1 = fig.add_subplot(111)
for f in file_list:
    x, y = load_file(f)
    ax1.plot(x,y, c="gray")#, label=f.split('_t')[0])
    #plt.xticks(x, file_list, rotation=90)


for f in file_list1:
    x, y = load_file(f)
    ax1.plot(x,y, linewidth=2.3)#, label=f.split('_t')[0])
    


# Spectrum
def sys(spectra):
    datadir = "../../syst-spectros/"
    file_ = spectra
    x = np.loadtxt(os.path.join(datadir, file_), delimiter = None, skiprows = 0, usecols = None,
                   unpack = False, dtype = np.dtype([('Wl', '|f8'), ('Flux', 'f8')]))
    return x['Wl'], x['Flux']

x, y = sys("SMC1.txt")
#x1, y1 = sys("LHa_115_N_60.txt")


y /=1.5e-14
#y1 /=1.5e-14

#print(x, y)
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
sns.set(style="dark")
#plt.xlim(6e3, 10500)
plt.xlim(4500, 5000)
plt.ylim(0.0, 0.70)
plt.tick_params(axis='x', labelsize=15) 
plt.tick_params(axis='y', labelsize=15)
plt.plot(x, y, linewidth=1.3, color="black", label="Lin 358")
#plt.plot(x1, y1, linewidth=1.3, color="green", label="LHa 115")
#plt.legend(fontsize='x-small')
plt.xlabel("Wavelength($\AA$)", fontsize= 18)
plt.ylabel("Transmission", fontsize= 18)
plt.legend()

plt.savefig('JPAS-filter-systs-heii-filter-Jv0915_4801.pdf')
