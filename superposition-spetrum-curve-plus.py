"""
PLUS transmission curves
"""
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
import seaborn as sns
import os
from astropy.io import fits

def load_file(filename):
    wll, ress = [], []
    data = np.loadtxt(filename, delimiter=None, converters=None, skiprows=0,
                                       usecols=None, unpack=False, ndmin=0)
    for i in data:
        wl = str(i[0]*10)
        res = str(i[1]*100)
        wll.append(wl)
        ress.append(res)
    return wll, ress

filters= [ 'J0378', 'J0395', 'J0410', 'J0430', 'J0515', 'J0660', 'J0861']
filters1= ['uJAVA',   'gSDSS',  'rSDSS',  'iSDSS']

files = [ 'F378_with_ccd_qe.dat', 'F395_with_ccd_qe.dat', 
'F410_with_ccd_qe.dat', 'F430_with_ccd_qe.dat', 
'F515_with_ccd_qe.dat', 'F660_with_ccd_qe.dat',  'F861_with_ccd_qe.dat']

files1 = ['F348_with_ccd_qe.dat', 'g_sdss_with_ccd_qe.dat',  'r_sdss_with_ccd_qe.dat', 
                             'i_sdss_with_ccd_qe.dat']
   
# files = ['F378_transm.txt', 'F395_transm.txt', 'F410_transm.txt', 'F430_transm.txt','F515_transm.txt', 'F660_transm.txt',  
#                 'F861_transm.txt']

# files1 = [ 'uJAVA_transm.txt', 'gSDSS_transm.txt',  'F625_transm.txt',
#           'iSDSS_transm.txt', 'zSDSS_transm.txt']


colors = ["#9900FF", "#6600FF", "#0000FF", "#009999", "#DD8000", "#CC0066", "#660033" ]
colors1 = ["#CC00FF", "#006600", "#FF0000",  "#990033"]
fig = plt.figure(figsize=(12, 7))
ax1 = fig.add_subplot(111)
for f, color, filter_ in zip(files, colors, filters):
    x, y = load_file(f)
    plt.fill(x, y, color=color, label=filter_)

for f, color, filter_ in zip(files1, colors1, filters1):
    x, y = load_file(f)
    plt.plot(x, y,  color=color, linewidth=4.0, label=filter_)

#the scale of the z filter is different
wll, ress = [], []
data = np.loadtxt('z_sdss_with_ccd_qe.dat', delimiter=None, converters=None, skiprows=0,
                                       usecols=None, unpack=False, ndmin=0)
for i in data:
    wl = str(i[0]*10)
    res = str(i[1])
    wll.append(wl)
    ress.append(res)
plt.plot(wll, ress,  color="#330034", linewidth=4.0, label='zSDSS')
# Spectrum
def sys(spectra):
    datadir = "../../Halo-PNe-spectros/"
    file_ = spectra
    x = np.loadtxt(os.path.join(datadir, file_), delimiter = None, skiprows = 0, usecols = None,
                   unpack = False, dtype = np.dtype([('Wl', '|f8'), ('Flux', 'f8')]))
    return x['Wl'], x['Flux']

#x, y = sys("Lin358.txt")
x, y = sys("DdDm-1.dat")

y /=1e-15
#y1 /=1e-16

# spectrum sloan
datadir = "../../Halo-PNe-spectros/"
fitsfile = "spec-0953-52411-0160_PNG_1359559.fits"
hdulist = fits.open(os.path.join(datadir, fitsfile))

wl = (10**hdulist[1].data.field('loglam'))
flux = 1E-17*hdulist[1].data.field('flux')

flux /=0.5e-16

lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
sns.set(style="dark")
# fig = plt.figure(figsize=(12, 7))
# ax1 = fig.add_subplot(111)
plt.ylim(0.0, 100.0)
plt.tick_params(axis='x', labelsize=28) 
plt.tick_params(axis='y', labelsize=28)
plt.xlim(3000, 10000)
#plt.ylim(0.0, 108)
#plt.plot(x, y, linewidth=1.3, color="black")#, label="Lin 358")
#plt.plot(wl, flux, linewidth=1.3, color="black")#, label="Lin 358")
#plt.plot(x1, y1, linewidth=1.3, color="green")#, label="LHa 115")
plt.legend()
plt.xlabel("Wavelength($\mathrm{\AA}$)", fontsize= 28)
plt.ylabel("Transmission", fontsize= 28)
#plt.savefig('jplus-filter-PNe-h4-1.jpg')
#plt.savefig('splus-filter-PNe-png135.jpg')
plt.tight_layout()
plt.savefig('jplus-filter17.pdf')

